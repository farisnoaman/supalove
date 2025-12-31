# Deprecation Notice: Keycloak Authentication

## Status: Deprecated ⚠️

The Keycloak-based authentication system (`/auth` page) has been deprecated in favor of the native GoTrue/Supabase user management system.

---

## Why Deprecated?

1. **Redundancy**: Two authentication systems caused confusion
2. **Complexity**: Keycloak adds unnecessary infrastructure overhead
3. **Native Solution**: GoTrue is Supabase's standard authentication
4. **Better Integration**: Direct database access with role management
5. **Auto-Admin**: New system includes automatic admin user creation

---

## Migration Path

### ✅ Use Instead:

**New Users Page:** `/projects/{id}/users`

**Features:**
- Native Supabase/GoTrue authentication
- Direct `auth.users` table management
- Role-based access control (Admin/Member)
- Auto-admin creation on project setup
- One-time password retrieval
- Full CRUD operations via API

**Documentation:**
- [User Guide](./USER_GUIDE_PROJECT_USERS.md)
- [API Reference](./PROJECT_USER_MANAGEMENT_API.md)

### 📋 What Changed:

| Feature | Old (Keycloak /auth) | New (GoTrue /users) |
|---------|---------------------|---------------------|
| **System** | Keycloak | GoTrue (Supabase native) |
| **Endpoint** | `/api/v1/projects/{id}/auth/users` | `/api/v1/projects/{id}/users` |
| **Auto-Admin** | ❌ No | ✅ Yes |
| **Roles** | Keycloak realms | user_metadata (admin/member) |
| **UI** | `/auth` page | `/users` page |
| **Sidebar** | "Authentication" | "Users" |

---

## Timeline

- **Dec 2024**: New Users page released
- **Jan 2025**: Deprecation notice added to /auth page
- **Q1 2025**: /auth page will be removed (planned)

---

## For Existing Keycloak Users

If you have existing users in Keycloak:

1. **Export** your Keycloak users
2. **Import** them via the new Users API:
   ```bash
   curl -X POST http://localhost:8000/api/v1/projects/{id}/users \
     -H "Authorization: Bearer YOUR_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{
       "email": "user@example.com",
       "password": "temp-password",
       "role": "member"
     }'
   ```
3. **Test** the new system
4. **Switch** your application to use GoTrue endpoints

---

## Questions?

- **Will my existing auth work?** Yes, during the deprecation period
- **Do I need to migrate immediately?** Recommended but not required yet
- **Can I keep using Keycloak?** For dedicated projects, temporarily yes

---

## Contact

Report issues or questions via GitHub Issues.
