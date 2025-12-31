# User Guide: Managing Project Users

## Introduction

This guide explains how to manage users within your Supalove projects. Each project has its own isolated user database, allowing you to control who has access to your project's data and APIs.

---

## Getting Started

### Auto-Generated Admin User

When you create a new project, an admin user is automatically created for you using your organization owner's email address. This user has full administrative access to your project.

**To get your admin credentials:**

1. Navigate to your project in the dashboard
2. Click on **Users** in the sidebar
3. Click **Get Admin Password**
4. Copy the password (⚠️ **One-time only!**)
5. Store it securely

> **Important:** The admin password can only be retrieved once. After you view it, it's permanently deleted from our system for security.

---

## Managing Users via Dashboard

### Viewing Users

1. Go to your project dashboard
2. Click **Users** in the left sidebar
3. See the complete list of users with:
   - Email address
   - Role (Admin/Member)
   - Created date
   - Confirmation status

### Adding a New User

1. Click **Add User** button
2. Fill in the form:
   - **Email:** User's email address
   - **Password:** Secure password (they can change it later)
   - **Role:** Choose Admin or Member
3. Click **Create User**

**Role Definitions:**
- **Admin:** Full access to all project resources
- **Member:** Standard user access (define permissions in your app)

### Deleting a User

1. Find the user in the list
2. Click the trash icon (🗑️)
3. Confirm the deletion
4. User is immediately removed from the project

> **Warning:** User deletion is permanent and cannot be undone.

---

## Managing Users Programmatically

### Using the API

You can manage users programmatically using the REST API. See the [API Documentation](./PROJECT_USER_MANAGEMENT_API.md) for detailed endpoint information.

**Quick Example:**

```bash
# Get admin password
curl -X GET \
  http://localhost:8000/api/v1/projects/YOUR_PROJECT_ID/admin-password \
  -H "Authorization: Bearer YOUR_TOKEN"

# Create a new user
curl -X POST \
  http://localhost:8000/api/v1/projects/YOUR_PROJECT_ID/users \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "SecurePass123!",
    "role": "member"
  }'
```

---

## User Authentication in Your App

Once you've created users, they can authenticate using the Supabase client:

### JavaScript/TypeScript

```typescript
import { createClient } from '@supabase/supabase-js'

const supabase = createClient(
  'YOUR_PROJECT_URL',
  'YOUR_PROJECT_ANON_KEY'
)

// Sign in
const { data, error } = await supabase.auth.signInWithPassword({
  email: 'user@example.com',
  password: 'their-password'
})

if (data.user) {
  console.log('Logged in:', data.user.email)
}
```

### Python

```python
from supabase import create_client

supabase = create_client("YOUR_PROJECT_URL", "YOUR_PROJECT_ANON_KEY")

# Sign in
response = supabase.auth.sign_in_with_password({
    "email": "user@example.com",
    "password": "their-password"
})

print(f"Logged in: {response.user.email}")
```

---

## Best Practices

### Security

1. **Strong Passwords:**
   - Use passwords with at least 16 characters
   - Include uppercase, lowercase, numbers, and symbols
   - Never share passwords via email or chat

2. **Admin Access:**
   - Limit admin users to only those who need full access
   - Use member role for regular users
   - Review user list regularly

3. **Password Storage:**
   - Save the auto-generated admin password in a password manager
   - Don't store passwords in code or configuration files

### User Management

1. **Remove Inactive Users:**
   - Regularly audit your user list
   - Delete users who no longer need access
   - This improves security and quota management

2. **Use Meaningful Email Addresses:**
   - Use real, working email addresses
   - This enables password reset flows (when implemented)

3. **Document Access Levels:**
   - Keep track of who has admin vs member access
   - Document why each user needs access

---

## Common Scenarios

### Scenario 1: New Team Member

**Goal:** Add a new developer to your project

**Steps:**
1. Click **Add User**
2. Enter their email and generate a secure password
3. Choose "Member" role (unless they need admin access)
4. Share the password securely (e.g., via password manager)
5. Ask them to change their password after first login

### Scenario 2: Promote User to Admin

**Current Solution:**
1. Delete the existing member user
2. Re-create them with "Admin" role

**Future Enhancement:** Role update API endpoint (roadmap)

### Scenario 3: Team Member Leaves

**Steps:**
1. Go to Users page
2. Find their account
3. Click delete icon
4. Confirm deletion
5. Their access is immediately revoked

### Scenario 4: Forgot Admin Password

**If you haven't retrieved it yet:**
1. Go to Users page
2. Click "Get Admin Password"
3. Save it in your password manager

**If already retrieved:**
1. Create a new admin user with your email
2. Use that account for admin access

---

## Troubleshooting

### "Admin password not found"

**Cause:** Password was already retrieved  
**Solution:** Create a new admin user if you lost the password

### "User already exists"

**Cause:** Email is already registered in this project  
**Solution:** Use a different email or delete the existing user first

### "Project limit reached"

**Cause:** Your plan allows limited projects  
**Solution:** Delete unused projects or upgrade your plan

### "Could not create user"

**Possible Causes:**
- Invalid email format
- Weak password
- Project provisioning issues

**Solution:** Check the error message for details

---

## Frequently Asked Questions

**Q: Can users have login access to multiple projects?**  
A: Yes, but they need separate accounts in each project since users are isolated per project.

**Q: How many users can I add to a project?**  
A: There's currently no enforced limit, but consider performance at scale.

**Q: Can I import users in bulk?**  
A: Not yet, but this is on the roadmap. For now, use the API to script bulk imports.

**Q: Can users reset their own passwords?**  
A: Password reset flows are on the roadmap. Currently, admins must create new passwords.

**Q: What happens to user data when I delete a user?**  
A: Only the authentication record is removed. Application data remains unless your app implements cascading deletes.

---

## Need Help?

- **API Documentation:** See [API Reference](./PROJECT_USER_MANAGEMENT_API.md)
- **Architecture:** See [Shared Projects Documentation](./SHARED_PROJECTS.md)
- **Issues:** Report bugs or request features on GitHub

---

## Roadmap

Future enhancements planned:

- ✅ Auto-admin creation (Complete)
- ✅ CRUD operations (Complete)  
- ✅ Role management (Complete)
- 🔄 Password reset flows
- 🔄 Email verification
- 🔄 Bulk user import (CSV)
- 🔄 Role update API
- 🔄 Custom roles and permissions
- 🔄 Audit logs
- 🔄 SSO integration
