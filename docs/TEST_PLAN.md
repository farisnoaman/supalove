# Supalove Comprehensive Test Plan

This document outlines the end-to-end (E2E) test scenarios for validating the Supalove platform. It covers critical user journeys across the Dashboard, API, and Data Plane.

## 🧪 Test Environment Setup

**Prerequisites:**
- Detailed in `README.md` under "Quick Start".
- Docker & Docker Compose running.
- Stripe Keys (or Mock Mode).

**Environment Variables:**
Ensure `.env` matches `env.example` but with valid secrets where necessary.

---

## 🟢 1. Authentication Flow

| ID | Scenario | Steps | Expected Result | Priority |
|----|----------|-------|-----------------|----------|
| **A-01** | User Signup | 1. Go to `/login` <br> 2. Click "Sign up" <br> 3. Enter email/password <br> 4. Submit | User created, redirected to Dashboard, "Welcome" toast appears. | P0 |
| **A-02** | User Login | 1. Logout if logged in <br> 2. Enter valid credentials <br> 3. Submit | JWT token stored in localStorage, redirected to `/projects`. | P0 |
| **A-03** | Logout | 1. Click Profile Avatar <br> 2. Click "Log out" | Token cleared, redirected to `/login`. | P1 |

## 🚀 2. Project Lifecycle (Global Shared)

| ID | Scenario | Steps | Expected Result | Priority |
|----|----------|-------|-----------------|----------|
| **P-01** | Create Project | 1. Click "New Project" <br> 2. Enter Name, Org, Region <br> 3. Select **Free Plan** <br> 4. Create | Project card appears. Status: `provisioning` -> `running` (< 5s). | P0 |
| **P-02** | View Overview | 1. Click Project Card | Overview page loads with CPU/RAM/Disk stats (mock or real). | P1 |
| **P-03** | Pause Project | 1. Go to Settings <br> 2. Click "Pause Project" | Status becomes `stopped`. API requests to project fail. | P2 |
| **P-04** | Resume Project | 1. Go to Settings <br> 2. Click "Resume Project" | Status becomes `running`. API requests succeed. | P2 |
| **P-05** | Delete Project | 1. Go to Settings <br> 2. Click "Delete Project" <br> 3. Confirm | Project removed from list. URL 404s. Data purged. | P1 |

## 💳 3. Billing & Plans

| ID | Scenario | Steps | Expected Result | Priority |
|----|----------|-------|-----------------|----------|
| **B-01** | Upgrade to Pro | 1. Go to Org Billing <br> 2. Select **Pro** <br> 3. Complete Checkout (Mock/Stripe) | Plan badge updates to "PRO". Quotas (projects/storage) increase. | P0 |
| **B-02** | Upgrade to Premium | 1. Go to Org Billing <br> 2. Select **Premium** <br> 3. Verify | Plan badge updates to "PREMIUM". "Private Cluster" provisioning starts. | P1 |
| **B-03** | Quota Enforcement | 1. As Free user, create 3rd project (Limit: 2) | Error toast: "Project limit reached for Free plan". | P2 |

## 🗄️ 4. Database & SQL

| ID | Scenario | Steps | Expected Result | Priority |
|----|----------|-------|-----------------|----------|
| **D-01** | Create Table | 1. Go to Database <br> 2. Click "New Table" <br> 3. Name: `todos`, cols: `id`, `task` | Table `todos` appears in sidebar. | P0 |
| **D-02** | Insert Data | 1. Open `todos` table <br> 2. Click "Insert Row" <br> 3. Enter info | New row appears in grid. Row count increases. | P0 |
| **D-03** | Run SQL | 1. Go to SQL Editor <br> 2. Run `SELECT * FROM todos` | Results pane shows the inserted rows. | P1 |
| **D-04** | RLS Policy | 1. Enable RLS on `todos` <br> 2. Add policy "Enable read access for all" | Anonymous requests can read, but not write (without specific policy). | P2 |

## 🔑 5. API & Secrets

| ID | Scenario | Steps | Expected Result | Priority |
|----|----------|-------|-----------------|----------|
| **S-01** | REST API Call | 1. Curl `GET /rest/v1/todos` with Anon Key | Returns JSON array of todos. | P0 |
| **S-02** | Add Secret | 1. Go to Secrets <br> 2. Add `MY_API_KEY` | Secret saved. Restart warning appears. | P2 |
| **S-03** | Verify Secret | 1. Use `Deno.env.get('MY_API_KEY')` in Edge Function | Function accesses the correct value. | P2 |

## 📦 6. Storage

| ID | Scenario | Steps | Expected Result | Priority |
|----|----------|-------|-----------------|----------|
| **ST-01** | Create Bucket | 1. Go to Storage <br> 2. Create public bucket `images` | Bucket appears in list. | P1 |
| **ST-02** | Upload File | 1. Upload `test.jpg` to `images` | File appears. Preview loads. | P1 |
| **ST-03** | Public URL | 1. Copy Public URL <br> 2. Open in Incognito | Image loads (if bucket public). | P2 |

## 🛡️ 7. Premium Features (Private Cluster)

| ID | Scenario | Steps | Expected Result | Priority |
|----|----------|-------|-----------------|----------|
| **PR-01** | Provisioning | 1. Create Project in Premium Org | "Provisioning Dedicated Cluster" status. Takes ~30-60s. | P1 |
| **PR-02** | Isolation Verify | 1. Check Backend Logs | Docker containers `postgres`, `postgrest` spawned *specifically* for this tenant. | P1 |

---

## 🤖 Automated Testing

Run the automated test suite to verify core backend logic.

```bash
# Backend Tests
cd control-plane/api
pytest

# Billing Verification
python scripts/verify_billing_v2.py
```
