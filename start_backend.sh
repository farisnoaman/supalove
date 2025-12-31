#!/bin/bash

# Navigate to the script's directory (root)
cd "$(dirname "$0")"

echo "🚀 Starting Infrastructure (PostgreSQL, MinIO, Keycloak)..."
docker compose up -d control-plane-db keycloak minio
echo "🌐 Starting Shared Infrastructure..."
docker compose -f data-plane/shared/docker-compose.yml up -d

# Give the database a moment to initialize
echo "⏳ Waiting for infrastructure to warm up..."
sleep 5

echo "🐍 Starting Backend in Virtual Environment..."
# Change directory to backend source
cd control-plane/api/src

# Run uvicorn from the virtual environment
../.venv/bin/uvicorn main:app --reload --host 0.0.0.0 --port 8000
