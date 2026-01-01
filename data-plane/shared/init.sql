-- Create roles
CREATE ROLE anon NOLOGIN;
CREATE ROLE authenticated NOLOGIN;
CREATE ROLE service_role NOLOGIN;
CREATE ROLE audit_admin NOLOGIN;
CREATE ROLE supabase_admin NOLOGIN;
CREATE ROLE dashboard_user NOLOGIN;
CREATE ROLE authenticator NOINHERIT LOGIN PASSWORD 'postgres';

-- Grant permissions to roles
GRANT anon TO authenticator;
GRANT authenticated TO authenticator;
GRANT service_role TO authenticator;
GRANT supabase_admin TO authenticator;
GRANT dashboard_user TO authenticator;

-- Create schemas
CREATE SCHEMA IF NOT EXISTS auth;
CREATE SCHEMA IF NOT EXISTS storage;
CREATE SCHEMA IF NOT EXISTS realtime;
CREATE SCHEMA IF NOT EXISTS _realtime;

-- Grant usage on schemas
GRANT USAGE ON SCHEMA public TO anon, authenticated, service_role;
GRANT USAGE ON SCHEMA auth TO anon, authenticated, service_role;
GRANT USAGE ON SCHEMA storage TO anon, authenticated, service_role;
GRANT USAGE ON SCHEMA realtime TO anon, authenticated, service_role;
GRANT USAGE ON SCHEMA _realtime TO anon, authenticated, service_role;

-- Grant all privileges to postgres user (just in case)
GRANT ALL PRIVILEGES ON DATABASE postgres TO postgres;
GRANT ALL PRIVILEGES ON SCHEMA public TO postgres;
GRANT ALL PRIVILEGES ON SCHEMA auth TO postgres;
GRANT ALL PRIVILEGES ON SCHEMA storage TO postgres;
GRANT ALL PRIVILEGES ON SCHEMA realtime TO postgres;
GRANT ALL PRIVILEGES ON SCHEMA _realtime TO postgres;

-- Defaults for PostgREST
ALTER ROLE authenticator SET pgrst.db_schemas = 'public, storage';
ALTER ROLE authenticator SET pgrst.db_anon_role = 'anon';
