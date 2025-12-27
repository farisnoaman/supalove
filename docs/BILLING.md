# Billing System (V2)

Supalove implements a flexible billing system based on **Entitlements** rather than direct plan-based provisioning.

## Core Principle

> **Billing NEVER provisions infrastructure directly.**  
> Billing only defines **entitlements**.  
> Infrastructure reacts to entitlements.

---

## Plan Tiers

| Plan | Price | Projects | Database | Cluster Type | Private Clusters |
|------|-------|----------|----------|--------------|------------------|
| **Free** | $0/mo | 2 | 500MB | Shared Global | 0 |
| **Pro** | $25/mo | 20 | 5GB | Shared Global | 0 |
| **Premium** | $100/mo | 100 | 20GB | Dedicated Private | 1 |

---

## Database Models

### Plans (`plans` table)

Defines available subscription tiers:

```python
class Plan(Base):
    id = Column(String, primary_key=True)  # "free", "pro", "premium"
    name = Column(String)
    monthly_price = Column(Integer)  # cents
    max_projects = Column(Integer)
    max_db_size_mb = Column(Integer)
    max_storage_mb = Column(Integer)
    cluster_strategy = Column(Enum(ClusterStrategy))
    allow_shared_fallback = Column(Boolean)
```

### Organization Entitlements (`organization_entitlements` table)

Links organizations to their plan:

```python
class OrganizationEntitlement(Base):
    org_id = Column(String, ForeignKey("organizations.id"), primary_key=True)
    plan_id = Column(String, ForeignKey("plans.id"))
    projects_used = Column(Integer, default=0)
    private_clusters_used = Column(Integer, default=0)
    expires_at = Column(DateTime, nullable=True)
```

---

## API Endpoints

### Subscription Management

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/billing/orgs/{org_id}/subscription` | GET | Get current subscription status |
| `/api/v1/billing/orgs/{org_id}/checkout` | POST | Create Stripe checkout session |
| `/api/v1/billing/orgs/{org_id}/portal` | POST | Open Stripe billing portal |
| `/api/v1/billing/orgs/{org_id}/usage` | GET | Get usage metrics |
| `/api/v1/billing/orgs/{org_id}/dev-upgrade` | POST | **DEV ONLY** - Upgrade without Stripe |
| `/api/v1/billing/webhook` | POST | Stripe webhook handler |

### Usage Response

```json
{
  "projects": { "used": 2, "limit": 20 },
  "db_size": { "used_mb": 150, "limit_mb": 5120 },
  "storage": { "used_mb": 500, "limit_mb": 51200 }
}
```

---

## Stripe Integration

### Environment Variables

```env
STRIPE_SECRET_KEY=sk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...
STRIPE_PRICE_ID_PRO=price_...
STRIPE_PRICE_ID_PREMIUM=price_...
```

### Webhook Events Handled

- `checkout.session.completed` - New subscription created
- `customer.subscription.updated` - Plan changed
- `customer.subscription.deleted` - Subscription canceled
- `invoice.payment_succeeded` - Invoice recorded

### Mock Mode (Development)

When `STRIPE_SECRET_KEY` is not set, the billing system operates in mock mode:
- Checkout returns a mock URL
- Frontend calls `/dev-upgrade` to directly update the plan
- No real payments processed

---

## Cluster Strategies

### Global Shared (Free/Pro)
- All projects run on a shared PostgreSQL instance
- Lower cost, shared resources
- `cluster_strategy = "global_only"`

### Private Per-Org (Premium)
- Organization gets dedicated Docker stack
- Isolated database and services
- `cluster_strategy = "private_per_org"`
- Provisioned asynchronously via `SchedulerService`

---

## Upgrade/Downgrade Flow

1. User clicks "Upgrade to Pro/Premium" in dashboard
2. Frontend calls `POST /checkout` with `plan_id`
3. If Stripe configured: Redirect to Stripe Checkout
4. If dev mode: Call `POST /dev-upgrade` directly
5. Webhook (or dev endpoint) updates `OrganizationEntitlement`
6. `EntitlementService` enforces new limits
7. For Premium: `ClusterService` provisions private cluster

---

## Services

### EntitlementService
- `get_entitlements(org_id)` - Get current entitlements
- `get_plan(plan_id)` - Get plan details
- `check_can_create_project(org_id)` - Validate quotas

### BillingService
- `create_checkout_session()` - Stripe Checkout
- `handle_webhook()` - Process Stripe events
- Syncs plan changes to `OrganizationEntitlement`

### UsageService
- `get_usage_summary(org_id)` - Current usage vs limits
- `check_limits(org_id, resource)` - Enforce quotas
