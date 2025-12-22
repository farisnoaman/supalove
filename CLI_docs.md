# 🛠️ Supalove CLI Documentation

The **Supalove CLI** is the official command-line tool for managing your Supalove projects. It brings the power of the dashboard to your terminal, allowing for rapid project creation, management, and deployment.

## 🚀 Installation

The CLI is currently distributed as a Python package within the `control-plane` directory.

### Prerequisites
- Python 3.9+
- Access to the Supalove backend (running locally or remotely)

### Setup (Development Mode)
Since the CLI relies on the backend's environment for dependencies (to avoid system package conflicts), we recommend using the provided virtual environment:

```bash
# 1. Navigate to your project root
cd /path/to/supalove

# 2. Install dependencies (if not already done)
./control-plane/api/.venv/bin/pip install typer rich requests

# 3. Create an alias for easy access (add this to your ~/.bashrc or ~/.zshrc)
alias supalove='export PYTHONPATH=$PYTHONPATH:$(pwd)/control-plane/cli/src && ./control-plane/api/.venv/bin/python3 -m supalove.main'
```

Now you can simply run:
```bash
supalove --help
```

---

## 🔑 Authentication

Before managing projects, you must authenticate with your Supalove account.

### Login
```bash
supalove login
```
You will be prompted to enter your **Personal Access Token**. 
*Currently, you can verify your session, but full token generation via CLI is coming in v2.*

### Logout
```bash
supalove logout
```
Removes your credentials from `~/.supalove/config.json`.

---

## 📦 Project Management

### Initialize a Local Project
Sets up a `supalove.toml` file in your current directory.

```bash
supalove init --name my-awesome-project
```

### Create a New Project on Supalove
Creates a new project in your organization directly from the terminal.

```bash
supalove projects create
```
*Prompts:*
- **Project Name**: The display name for your project.
- **Organization ID**: The ID of the organization to create it in.

### List Projects (*Coming Soon*)
Display a table of all your projects.
```bash
supalove projects list
```

---

## 🚀 Deployment

The CLI enables you to deploy Edge Functions and static assets directly to your Supalove project.

### Deploy Functions
Deploys the contents of your `./functions` directory to the platform.

```bash
supalove deploy functions --path ./functions --project-id <PROJECT_ID>
```

---

## 🔮 Roadmap & Improvements

The Supalove CLI is in active development (Phase 6). Here is the roadmap for upcoming features:

### Immediate Improvements (v0.2)
- [ ] **Interactive Project Selection**: Instead of pasting Org/Project IDs, fetch lists from the API and let users select with arrow keys.
- [ ] **`supalove link`**: Link a local directory to a remote project ID to avoid passing `--project-id` on every command.
- [ ] **Better Auth Flow**: Open a browser window to `/settings/tokens` to auto-generate a token instead of manual copy-paste.

### Future Capabilities (v1.0)
- [ ] **Database Migrations**: `supalove db push` to apply local schema changes to remote.
- [ ] **Type Generation**: `supalove gen types` to generate TypeScript types from your Database schema.
- [ ] **Local Development**: `supalove start` to spin up a full local stack (Postgres, Auth, Storage) via Docker Compose for offline dev.

---

## 🐞 Troubleshooting

**"ModuleNotFoundError: No module named 'typer'"**
Ensure you are using the backend's virtual environment or have installed the dependencies in your active environment:
`pip install typer rich requests`

**"Connection Refused"**
Ensure your Supalove backend (Control Plane) is running:
`./start_backend.sh`
