-- Migration: Add shared plan support columns to projects table
-- Run this migration after existing data is backed up

-- Create enum types for plan and backend_type
DO $$ BEGIN
    CREATE TYPE project_plan AS ENUM ('shared', 'dedicated');
EXCEPTION
    WHEN duplicate_object THEN null;
END $$;

DO $$ BEGIN
    CREATE TYPE backend_type AS ENUM ('local_docker', 'shared_cluster', 'coolify');
EXCEPTION
    WHEN duplicate_object THEN null;
END $$;

-- Add new columns to projects table
ALTER TABLE projects ADD COLUMN IF NOT EXISTS plan project_plan DEFAULT 'shared';
ALTER TABLE projects ADD COLUMN IF NOT EXISTS backend_type backend_type DEFAULT 'shared_cluster';
ALTER TABLE projects ADD COLUMN IF NOT EXISTS db_name VARCHAR(255);

-- Update existing projects to be dedicated (preserve current behavior for existing projects)
UPDATE projects SET plan = 'dedicated', backend_type = 'local_docker' WHERE plan IS NULL;
