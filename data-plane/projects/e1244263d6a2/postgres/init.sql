-- Postgres init script for SupaLove project
-- This script runs when the PostgreSQL container starts

-- Create the app user with the specified password
-- Note: The password will be set via environment variable during container startup

-- Enable necessary extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- Create a sample table for testing
CREATE TABLE IF NOT EXISTS test_table (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Insert some sample data
INSERT INTO test_table (name) VALUES ('Hello from SupaLove!') ON CONFLICT DO NOTHING;