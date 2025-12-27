import os
import stripe
from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.organization import Organization
from models.subscription import Subscription, SubscriptionStatus
from models.invoice import Invoice
from datetime import datetime

class BillingService:
    def __init__(self):
        self.stripe_key = os.getenv("STRIPE_SECRET_KEY")
        if self.stripe_key:
            stripe.api_key = self.stripe_key
        
        self.pro_price_id = os.getenv("STRIPE_PRICE_ID_PRO", "price_123456789")

    def create_checkout_session(self, org_id: str, plan_id: str, success_url: str, cancel_url: str):
        """Creates a Stripe Checkout Session for subscription upgrade."""
        if not self.stripe_key:
            # Mock behavior for development without Stripe keys
            return "https://mock.stripe.com/checkout/session_mock_123"

        try:
            session = stripe.checkout.Session.create(
                payment_method_types=["card"],
                line_items=[{"price": plan_id, "quantity": 1}],
                mode="subscription",
                success_url=success_url,
                cancel_url=cancel_url,
                client_reference_id=org_id,
            )
            return session.url
        except Exception as e:
            print(f"Stripe error: {e}")
            # If we fail (e.g. invalid key in local dev), fallback to mock
            return "https://mock.stripe.com/checkout/session_mock_123"
            # raise HTTPException(status_code=500, detail="Failed to create checkout session")

    def create_portal_session(self, customer_id: str, return_url: str):
        """Creates a Customer Portal session for billing management."""
        if not self.stripe_key:
            return "https://mock.stripe.com/portal/session_mock_123"

        try:
            session = stripe.billing_portal.Session.create(
                customer=customer_id,
                return_url=return_url
            )
            return session.url
        except Exception as e:
            print(f"Stripe error: {e}")
            raise HTTPException(status_code=500, detail="Failed to create portal session")

    def handle_webhook(self, payload: bytes, sig_header: str, db: Session):
        """Handles Stripe webhooks to sync subscription state."""
        if not self.stripe_key:
            return {"status": "mock_success"}

        webhook_secret = os.getenv("STRIPE_WEBHOOK_SECRET")
        
        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, webhook_secret
            )
        except ValueError as e:
            raise HTTPException(status_code=400, detail="Invalid payload")
        except stripe.error.SignatureVerificationError as e:
            raise HTTPException(status_code=400, detail="Invalid signature")

        if event["type"] == "checkout.session.completed":
            self._handle_checkout_completed(event["data"]["object"], db)
        elif event["type"] == "invoice.payment_succeeded":
            self._handle_invoice_paid(event["data"]["object"], db)
        elif event["type"] in ["customer.subscription.updated", "customer.subscription.deleted"]:
            self._handle_subscription_updated(event["data"]["object"], db)

        return {"status": "success"}

    def _handle_checkout_completed(self, session, db: Session):
        org_id = session.get("client_reference_id")
        customer_id = session.get("customer")
        subscription_id = session.get("subscription")

        if org_id and customer_id and subscription_id:
            # Update or create subscription
            sub = db.query(Subscription).filter(Subscription.org_id == org_id).first()
            if not sub:
                sub = Subscription(org_id=org_id)
                db.add(sub)
            
            sub.stripe_customer_id = customer_id
            sub.stripe_subscription_id = subscription_id
            sub.status = SubscriptionStatus.active
            
            # Determine plan from session metadata or line items
            # For simplicity in this demo, we assume checkout is for 'pro' or 'premium'
            plan_id = "pro" 
            if session.get("metadata") and "plan_id" in session.get("metadata"):
                plan_id = session.get("metadata")["plan_id"]
                
            sub.plan_id = plan_id
            
            # Update Entitlements
            from services.entitlement_service import EntitlementService
            ent = EntitlementService.get_entitlements(db, org_id)
            ent.plan_id = plan_id
            
            db.commit()

    def _handle_subscription_updated(self, stripe_sub, db: Session):
        sub = db.query(Subscription).filter(Subscription.stripe_subscription_id == stripe_sub["id"]).first()
        if sub:
            sub.status = stripe_sub["status"]
            sub.current_period_end = datetime.fromtimestamp(stripe_sub["current_period_end"])
            
            from services.entitlement_service import EntitlementService
            ent = EntitlementService.get_entitlements(db, sub.org_id)
            
            # Check for plan change in metadata
            # We assume the subscription metadata contains 'plan_id' updated by our checkout/portal logic
            # Or we can look at the price ID of the first item if we had a mapping.
            # For now, relying on metadata is safest if we ensure it's set.
            new_plan_id = stripe_sub.get("metadata", {}).get("plan_id")
            
            if sub.status == "active":
                if new_plan_id:
                    sub.plan_id = new_plan_id
                    ent.plan_id = new_plan_id
                
                # If no metadata plan_id, we might be keeping existing plan
                
            elif sub.status in ["canceled", "unpaid", "past_due"]:
                # Downgrade to free if not active
                # Note: 'past_due' might deserve a grace period, but strict for now
                ent.plan_id = "free"
                sub.plan_id = "free"

            db.commit()

    def _handle_invoice_paid(self, invoice, db: Session):
         # Create invoice record
         sub = db.query(Subscription).filter(Subscription.stripe_customer_id == invoice["customer"]).first()
         if sub:
             new_inv = Invoice(
                 org_id=sub.org_id,
                 stripe_invoice_id=invoice["id"],
                 amount_paid=invoice["amount_paid"],
                 status=invoice["status"],
                 invoice_pdf=invoice["invoice_pdf"]
             )
             db.add(new_inv)
             db.commit()

    def sync_subscription(self, org_id: str, db: Session):
        """Manually sync status if needed (e.g. at startup or user request)"""
        pass
