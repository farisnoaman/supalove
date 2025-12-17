#!/bin/bash
PROJECT_ID=$1

cp -r data-plane/project-template /tmp/project-$PROJECT_ID
cd /tmp/project-$PROJECT_ID

docker compose up -d