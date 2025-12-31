# Supalove Documentation

Welcome to the Supalove documentation! This directory contains comprehensive guides and references for managing and developing with Supalove.

---

## Quick Links

### 🏗️ Architecture & Infrastructure

- **[Shared Projects Architecture](./SHARED_PROJECTS.md)**  
  Complete guide to how shared projects work, including database isolation, request routing, and multi-tenancy. Essential reading for understanding the system architecture.

### 👥 User Management

- **[Project User Management API](./PROJECT_USER_MANAGEMENT_API.md)**  
  Complete API reference for managing users within projects, including endpoints, request/response formats, and code examples.

- **[User Guide: Managing Project Users](./USER_GUIDE_PROJECT_USERS.md)**  
  Step-by-step guide for project owners on how to manage users via the dashboard and API, including best practices and common scenarios.

---

## Getting Started

### For Platform Owners

1. Read [Shared Projects Architecture](./SHARED_PROJECTS.md) to understand the system
2. Learn about [User Management](./USER_GUIDE_PROJECT_USERS.md) to manage access

### For Developers

1. Check [API Documentation](./PROJECT_USER_MANAGEMENT_API.md) for integration
2. Review [Shared Projects Architecture](./SHARED_PROJECTS.md) for database access patterns

---

## Features Documentation

### ✅ Implemented Features

- **Multi-Tenant Database Isolation** - Each project gets its own database
- **Automatic Admin Creation** - Admin users auto-created on project setup
- **User Management API** - Full CRUD operations for project users
- **Dashboard UI** - Web interface for managing users
- **Per-Project JWT Secrets** - Cryptographic isolation between projects
- **Shared Infrastructure** - Cost-efficient resource sharing

### 🔄 Roadmap

- Password reset flows
- Email verification
- Bulk user import (CSV)
- Custom roles and permissions
- Audit logs
- SSO integration

---

## File Structure

```
docs/
├── README.md                           # This file
├── SHARED_PROJECTS.md                  # Architecture documentation
├── PROJECT_USER_MANAGEMENT_API.md      # API reference
└── USER_GUIDE_PROJECT_USERS.md         # User guide
```

---

## Need Help?

- **Issues:** Report bugs on GitHub
- **Questions:** Check the guides in this directory
- **Contributing:** See main repository README

---

## Version

Documentation Version: 1.0.0  
Last Updated: 2024-01-01
