-- SQL dump: 10 tables with RLS policies

-- Enable required extension for UUIDs if not present
CREATE EXTENSION IF NOT EXISTS pgcrypto;

-- 1) users
CREATE TABLE IF NOT EXISTS public.users (
  id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  email text UNIQUE,
  created_at timestamptz DEFAULT now()
);
ALTER TABLE public.users ENABLE ROW LEVEL SECURITY;

-- Owner-only: users can manage their own row; admin can do anything
CREATE POLICY users_select_owner ON public.users
  FOR SELECT TO authenticated
  USING ((SELECT auth.uid()) = id OR (auth.jwt() ->> 'role') = 'admin');
CREATE POLICY users_insert_owner ON public.users
  FOR INSERT TO authenticated
  WITH CHECK ((SELECT auth.uid()) = id);
CREATE POLICY users_update_owner ON public.users
  FOR UPDATE TO authenticated
  USING ((SELECT auth.uid()) = id OR (auth.jwt() ->> 'role') = 'admin')
  WITH CHECK ((SELECT auth.uid()) = id OR (auth.jwt() ->> 'role') = 'admin');
CREATE POLICY users_delete_owner ON public.users
  FOR DELETE TO authenticated
  USING ((SELECT auth.uid()) = id OR (auth.jwt() ->> 'role') = 'admin');

-- 2) user_profiles
CREATE TABLE IF NOT EXISTS public.user_profiles (
  id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  auth_user_id uuid,
  full_name text,
  metadata jsonb,
  created_at timestamptz DEFAULT now()
);
ALTER TABLE public.user_profiles ENABLE ROW LEVEL SECURITY;

CREATE POLICY user_profiles_select_owner ON public.user_profiles
  FOR SELECT TO authenticated
  USING ((SELECT auth.uid()) = auth_user_id OR (auth.jwt() ->> 'role') = 'admin');
CREATE POLICY user_profiles_insert_owner ON public.user_profiles
  FOR INSERT TO authenticated
  WITH CHECK ((SELECT auth.uid()) = auth_user_id);
CREATE POLICY user_profiles_update_owner ON public.user_profiles
  FOR UPDATE TO authenticated
  USING ((SELECT auth.uid()) = auth_user_id OR (auth.jwt() ->> 'role') = 'admin')
  WITH CHECK ((SELECT auth.uid()) = auth_user_id OR (auth.jwt() ->> 'role') = 'admin');
CREATE POLICY user_profiles_delete_owner ON public.user_profiles
  FOR DELETE TO authenticated
  USING ((SELECT auth.uid()) = auth_user_id OR (auth.jwt() ->> 'role') = 'admin');

-- 3) vehicles
CREATE TABLE IF NOT EXISTS public.vehicles (
  id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  driver_id uuid,
  make text,
  model text,
  created_at timestamptz DEFAULT now()
);
ALTER TABLE public.vehicles ENABLE ROW LEVEL SECURITY;

-- Drivers can select/insert/update their vehicles; admins can do anything
CREATE POLICY vehicles_select_driver ON public.vehicles
  FOR SELECT TO authenticated
  USING (driver_id = (SELECT auth.uid()) OR (auth.jwt() ->> 'role') = 'admin');
CREATE POLICY vehicles_insert_driver ON public.vehicles
  FOR INSERT TO authenticated
  WITH CHECK (driver_id = (SELECT auth.uid()));
CREATE POLICY vehicles_update_driver ON public.vehicles
  FOR UPDATE TO authenticated
  USING (driver_id = (SELECT auth.uid()) OR (auth.jwt() ->> 'role') = 'admin')
  WITH CHECK (driver_id = (SELECT auth.uid()) OR (auth.jwt() ->> 'role') = 'admin');
CREATE POLICY vehicles_delete_admin ON public.vehicles
  FOR DELETE TO authenticated
  USING ((auth.jwt() ->> 'role') = 'admin');

-- 4) trips
CREATE TABLE IF NOT EXISTS public.trips (
  id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  rider_id uuid,
  driver_id uuid,
  origin jsonb,
  destination jsonb,
  status text,
  created_at timestamptz DEFAULT now()
);
ALTER TABLE public.trips ENABLE ROW LEVEL SECURITY;

-- Riders and drivers can access rows related to them; admins can access all
CREATE POLICY trips_select_participants ON public.trips
  FOR SELECT TO authenticated
  USING ((SELECT auth.uid()) = rider_id OR (SELECT auth.uid()) = driver_id OR (auth.jwt() ->> 'role') = 'admin');
CREATE POLICY trips_insert_rider ON public.trips
  FOR INSERT TO authenticated
  WITH CHECK ((SELECT auth.uid()) = rider_id);
CREATE POLICY trips_update_participants ON public.trips
  FOR UPDATE TO authenticated
  USING ((SELECT auth.uid()) = rider_id OR (SELECT auth.uid()) = driver_id OR (auth.jwt() ->> 'role') = 'admin')
  WITH CHECK ((SELECT auth.uid()) = rider_id OR (SELECT auth.uid()) = driver_id OR (auth.jwt() ->> 'role') = 'admin');
CREATE POLICY trips_delete_admin ON public.trips
  FOR DELETE TO authenticated
  USING ((auth.jwt() ->> 'role') = 'admin');

-- 5) trip_payments
CREATE TABLE IF NOT EXISTS public.trip_payments (
  id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  trip_id uuid,
  user_id uuid,
  amount numeric,
  status text,
  created_at timestamptz DEFAULT now()
);
ALTER TABLE public.trip_payments ENABLE ROW LEVEL SECURITY;

CREATE POLICY trip_payments_select_owner ON public.trip_payments
  FOR SELECT TO authenticated
  USING ((SELECT auth.uid()) = user_id OR (auth.jwt() ->> 'role') = 'admin');
CREATE POLICY trip_payments_insert_owner ON public.trip_payments
  FOR INSERT TO authenticated
  WITH CHECK ((SELECT auth.uid()) = user_id);
CREATE POLICY trip_payments_update_admin ON public.trip_payments
  FOR UPDATE TO authenticated
  USING ((auth.jwt() ->> 'role') = 'admin')
  WITH CHECK ((auth.jwt() ->> 'role') = 'admin');
CREATE POLICY trip_payments_delete_admin ON public.trip_payments
  FOR DELETE TO authenticated
  USING ((auth.jwt() ->> 'role') = 'admin');

-- 6) user_notifications
CREATE TABLE IF NOT EXISTS public.user_notifications (
  id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  user_id uuid,
  type text,
  payload jsonb,
  read boolean DEFAULT false,
  created_at timestamptz DEFAULT now()
);
ALTER TABLE public.user_notifications ENABLE ROW LEVEL SECURITY;

CREATE POLICY user_notifications_select_owner ON public.user_notifications
  FOR SELECT TO authenticated
  USING ((SELECT auth.uid()) = user_id);
CREATE POLICY user_notifications_insert_system ON public.user_notifications
  FOR INSERT TO authenticated
  WITH CHECK ((SELECT auth.uid()) = user_id OR (auth.jwt() ->> 'role') = 'admin');
CREATE POLICY user_notifications_update_owner ON public.user_notifications
  FOR UPDATE TO authenticated
  USING ((SELECT auth.uid()) = user_id)
  WITH CHECK ((SELECT auth.uid()) = user_id);
CREATE POLICY user_notifications_delete_admin ON public.user_notifications
  FOR DELETE TO authenticated
  USING ((auth.jwt() ->> 'role') = 'admin');

-- 7) user_payment_methods
CREATE TABLE IF NOT EXISTS public.user_payment_methods (
  id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  user_id uuid,
  type text,
  provider text,
  last_four text,
  created_at timestamptz DEFAULT now()
);
ALTER TABLE public.user_payment_methods ENABLE ROW LEVEL SECURITY;

CREATE POLICY user_payment_methods_select_owner ON public.user_payment_methods
  FOR SELECT TO authenticated
  USING ((SELECT auth.uid()) = user_id OR (auth.jwt() ->> 'role') = 'admin');
CREATE POLICY user_payment_methods_insert_owner ON public.user_payment_methods
  FOR INSERT TO authenticated
  WITH CHECK ((SELECT auth.uid()) = user_id);
CREATE POLICY user_payment_methods_update_owner ON public.user_payment_methods
  FOR UPDATE TO authenticated
  USING ((SELECT auth.uid()) = user_id OR (auth.jwt() ->> 'role') = 'admin')
  WITH CHECK ((SELECT auth.uid()) = user_id OR (auth.jwt() ->> 'role') = 'admin');
CREATE POLICY user_payment_methods_delete_owner ON public.user_payment_methods
  FOR DELETE TO authenticated
  USING ((SELECT auth.uid()) = user_id OR (auth.jwt() ->> 'role') = 'admin');

-- 8) support_tickets
CREATE TABLE IF NOT EXISTS public.support_tickets (
  id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  user_id uuid,
  subject text,
  description text,
  status text DEFAULT 'open',
  created_at timestamptz DEFAULT now()
);
ALTER TABLE public.support_tickets ENABLE ROW LEVEL SECURITY;

CREATE POLICY support_tickets_select_owner ON public.support_tickets
  FOR SELECT TO authenticated
  USING ((SELECT auth.uid()) = user_id OR (auth.jwt() ->> 'role') = 'admin');
CREATE POLICY support_tickets_insert_owner ON public.support_tickets
  FOR INSERT TO authenticated
  WITH CHECK ((SELECT auth.uid()) = user_id);
CREATE POLICY support_tickets_update_admin_or_owner ON public.support_tickets
  FOR UPDATE TO authenticated
  USING ((SELECT auth.uid()) = user_id OR (auth.jwt() ->> 'role') = 'admin')
  WITH CHECK ((SELECT auth.uid()) = user_id OR (auth.jwt() ->> 'role') = 'admin');
CREATE POLICY support_tickets_delete_admin ON public.support_tickets
  FOR DELETE TO authenticated
  USING ((auth.jwt() ->> 'role') = 'admin');

-- 9) subscriptions
CREATE TABLE IF NOT EXISTS public.subscriptions (
  id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  user_id uuid,
  plan_id uuid,
  status text DEFAULT 'active',
  started_at timestamptz DEFAULT now()
);
ALTER TABLE public.subscriptions ENABLE ROW LEVEL SECURITY;

CREATE POLICY subscriptions_select_owner ON public.subscriptions
  FOR SELECT TO authenticated
  USING ((SELECT auth.uid()) = user_id OR (auth.jwt() ->> 'role') = 'admin');
CREATE POLICY subscriptions_insert_owner ON public.subscriptions
  FOR INSERT TO authenticated
  WITH CHECK ((SELECT auth.uid()) = user_id);
CREATE POLICY subscriptions_update_admin_or_owner ON public.subscriptions
  FOR UPDATE TO authenticated
  USING ((SELECT auth.uid()) = user_id OR (auth.jwt() ->> 'role') = 'admin')
  WITH CHECK ((SELECT auth.uid()) = user_id OR (auth.jwt() ->> 'role') = 'admin');
CREATE POLICY subscriptions_delete_admin ON public.subscriptions
  FOR DELETE TO authenticated
  USING ((auth.jwt() ->> 'role') = 'admin');

-- 10) webhooks
CREATE TABLE IF NOT EXISTS public.webhooks (
  id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  event text,
  url text,
  secret text,
  is_active boolean DEFAULT true,
  created_at timestamptz DEFAULT now()
);
ALTER TABLE public.webhooks ENABLE ROW LEVEL SECURITY;

-- Only admins can manage webhooks
CREATE POLICY webhooks_select_admin ON public.webhooks
  FOR SELECT TO authenticated
  USING ((auth.jwt() ->> 'role') = 'admin');
CREATE POLICY webhooks_insert_admin ON public.webhooks
  FOR INSERT TO authenticated
  WITH CHECK ((auth.jwt() ->> 'role') = 'admin');
CREATE POLICY webhooks_update_admin ON public.webhooks
  FOR UPDATE TO authenticated
  USING ((auth.jwt() ->> 'role') = 'admin')
  WITH CHECK ((auth.jwt() ->> 'role') = 'admin');
CREATE POLICY webhooks_delete_admin ON public.webhooks
  FOR DELETE TO authenticated
  USING ((auth.jwt() ->> 'role') = 'admin');

-- End of dump
