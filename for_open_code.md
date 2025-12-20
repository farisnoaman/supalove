
---

# 1️⃣ Exact V1 → V2 Refactor Steps (File by File)

## 🎯 Goal of V2 (Very Important)

**V1** = “Works locally, one host, manual recovery”
**V2** = “Deterministic, recoverable, auditable, safe to automate”

👉 V2 does **NOT** change architecture.
👉 V2 **adds discipline**.

---

## 🔁 Step 1 — Normalize API Structure (Mandatory)

### ✅ Current (Problematic)

You still have **two patterns** in history:

* `routes/`
* `api/v1/`

### ✅ V2 Target (Single Source of Truth)

```
control-plane/api/src/
├── api/
│   └── v1/
│       ├── projects.py
│       ├── auth.py
│       ├── storage.py
│       └── health.py
```

### 🔧 Actions

**DELETE**

```
src/routes/
```

**EDIT**
`main.py`

```python
from api.v1.projects import router as projects_router

app.include_router(projects_router, prefix="/api/v1")
```

📌 **Why**

* Versioning becomes enforceable
* You can deploy v2 alongside v1 later

---

## 🔁 Step 2 — Introduce Project Lifecycle State Machine

### ✅ Files to Change

#### `models/project.py`

```python
class ProjectStatus(enum.Enum):
    pending = "pending"
    provisioning = "provisioning"
    running = "running"
    failed = "failed"
    deleting = "deleting"
    deleted = "deleted"
```

```python
status = Column(Enum(ProjectStatus), default=ProjectStatus.pending)
last_error = Column(Text, nullable=True)
```

---

#### `services/project_service.py`

**Before**

```python
project.status = "running"
```

**After**

```python
project.status = ProjectStatus.provisioning
db.commit()

try:
    provision_project(project_id, secrets)
    project.status = ProjectStatus.running
except Exception as e:
    project.status = ProjectStatus.failed
    project.last_error = str(e)

db.commit()
```

📌 **Why**

* Makes provisioning **recoverable**
* Enables retries
* Enables UI error display

---

## 🔁 Step 3 — Make Provisioning Explicitly Typed

### ✅ Current (Implicit, fragile)

```python
provision_project(project_id, secrets)
```

### ✅ V2 Target

#### `services/provisioning_interface.py`

```python
class Provisioner(ABC):
    @abstractmethod
    def provision(self, project_id: str, secrets: dict): ...
    
    @abstractmethod
    def destroy(self, project_id: str): ...
```

---

#### `services/provisioning_local.py`

```python
class LocalProvisioner(Provisioner):
    def provision(self, project_id, secrets): ...
    def destroy(self, project_id): ...
```

---

#### `services/provisioning_service.py`

```python
def get_provisioner() -> Provisioner:
    return LocalProvisioner()
```

📌 **Why**

* You already support Coolify
* This lets you switch infra **without touching business logic**

---

## 🔁 Step 4 — Secrets Become a First-Class Domain

### ✅ Current (V1)

Secrets are:

* Generated
* Stored
* Used once

### ✅ V2 Target

#### `services/secrets_service.py`

Add:

```python
def get_project_secrets(db, project_id) -> dict:
    return {
        s.key: s.value
        for s in db.query(ProjectSecret)
                .filter(ProjectSecret.project_id == project_id)
    }
```

Now provisioning **never regenerates secrets**.

📌 **Why**

* Enables rotation
* Enables recovery
* Prevents accidental mismatch

---

## 🔁 Step 5 — Filesystem Isolation Contract

### ✅ Current

```
data-plane/projects/{project_id}
```

### ✅ V2 Rule (Hard)

> Control plane NEVER infers project existence from filesystem

#### Add:

`services/database_service.py`

```python
def project_exists(db, project_id):
    return db.query(Project).filter(Project.id == project_id).first()
```

📌 **Why**

* Prevents ghost projects
* Prevents privilege escalation

---

# 2️⃣ Project State Machine (Formal Definition)

This is **non-negotiable** if you want to scale.

---

## 🧠 State Diagram

```
[pending]
    |
    v
[provisioning]
    | success
    v
[running]
    |
    | delete
    v
[deleting]
    |
    v
[deleted]

(provisioning error)
        |
        v
      [failed]
        |
        | retry
        v
   [provisioning]
```

---

## 🧾 State Rules (Enforced in Code)

| From                   | To        | Allowed? |
| ---------------------- | --------- | -------- |
| pending → provisioning | ✅         |          |
| provisioning → running | ✅         |          |
| provisioning → failed  | ✅         |          |
| failed → provisioning  | ✅ (retry) |          |
| running → deleting     | ✅         |          |
| deleting → deleted     | ✅         |          |
| deleted → anything     | ❌         |          |

---

## 🛑 What This Enables

* Retry without data loss
* UI can show progress
* CLI automation
* Safe crash recovery

This is **production-grade behavior**.

---

# 3️⃣ Security Boundary Review (Critical)

I’ll be blunt here.

---

## ✅ What You Did RIGHT

### ✔ Physical Isolation

Each project has:

* Its own containers
* Its own volumes
* Its own secrets

This is **stronger than schema isolation**.

---

### ✔ Control Plane Separation

Control plane:

* Never connects to project DB directly
* Only provisions

This is **excellent design**.

---

## ⚠️ Current Weak Points (Must Fix in V2)

---

### 🔴 1. Secrets Stored in Plaintext

**Current**

```
project_secrets.value = "raw_secret"
```

### ✅ V2 Fix (Simple)

* Encrypt at rest (Fernet / KMS later)
* Or restrict DB access strictly

📌 Acceptable for early V2 if DB is private.

---

### 🔴 2. No Auth Boundary Between Projects

Right now:

* Any request can theoretically target any project

### ✅ V2 Minimum Fix

Every API must require:

```python
project_id
```

And validate:

```python
project.owner_id == current_user.id
```

---

### 🔴 3. Docker Socket Access Risk

If provisioning uses:

```
docker compose up
```

And control-plane has docker access:

🚨 **This is root-level power**

### ✅ V2 Rule

* Provisioning runs in **isolated worker**
* Control-plane never exposes docker socket to API layer

---

## 🔐 Security Model Summary

| Layer             | Isolation  | Status                 |
| ----------------- | ---------- | ---------------------- |
| Control Plane API | Logical    | ⚠️ Needs auth          |
| Secrets           | DB-level   | ⚠️ Encrypt later       |
| Data Plane        | Container  | ✅ Strong               |
| Storage           | Volume     | ✅ Good                 |
| Network           | Local only | ⚠️ Needs ingress rules |

-