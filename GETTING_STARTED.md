# Getting Started with Supalove Multi-Tenancy

Welcome to the new version of Supalove! We have introduced User Accounts and Organizations. Follow the steps below to sign up and create your first project.

## 1. Sign Up
1.  Navigate to [Signup Page](http://localhost:3000/signup).
2.  Enter your **Full Name**, **Email**, and **Password**.
3.  Click **Sign Up**.
4.  Upon success, an organization named `[Name]'s Org` is automatically created for you.
5.  You will be redirected to the **Projects Dashboard**.

## 2. Create a Project
1.  From the dashboard, click **+ New Project**.
2.  Enter a unique **Project Name** (e.g., `my-startup-app`).
3.  Click **Create Project**.
    *   *Note: This process provisions a dedicated Docker environment for your project. It may take 10-20 seconds.*
4.  Once complete, you will see your **API URL** and **Database URL**.
5.  Click **Return to Project List** to see your running project.

## 3. Manage Your Project
*   Click **Manage** on the project card to view database tables, storage buckets, and logs.
*   The project is now securely isolated within your Organization.

## Troubleshooting
*   **401 Unauthorized**: If you see this, ensure you logged in via the `/login` or `/signup` page so your session token is saved.
*   **Provisioning Stuck**: Check the terminal running `./start_backend.sh` for any Docker errors.

Enjoy building! 🚀
