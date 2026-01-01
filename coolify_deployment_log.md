Deployment Log
Hide Debug Logs
Deployment is Finished.


2026-Jan-01 21:36:28.237352
Starting deployment of farisnoaman/supalove:main-mc8cwc4ggsgo8gocw8040gkc to localhost.
2026-Jan-01 21:36:28.916111
Preparing container with helper image: ghcr.io/coollabsio/coolify-helper:1.0.12
2026-Jan-01 21:36:29.296851
[CMD]: docker stop --time=30 l0oso884kogw04wsgscwog0c
2026-Jan-01 21:36:29.296851
Error response from daemon: No such container: l0oso884kogw04wsgscwog0c
2026-Jan-01 21:36:29.560696
[CMD]: docker rm -f l0oso884kogw04wsgscwog0c
2026-Jan-01 21:36:29.560696
Error response from daemon: No such container: l0oso884kogw04wsgscwog0c
2026-Jan-01 21:36:29.921343
[CMD]: docker run -d --network coolify --name l0oso884kogw04wsgscwog0c  --rm -v /var/run/docker.sock:/var/run/docker.sock ghcr.io/coollabsio/coolify-helper:1.0.12
2026-Jan-01 21:36:29.921343
4769563157c793a0c670acdcfe54d3645297e0d64435d328997358743b98f0a5
2026-Jan-01 21:36:32.372803
[CMD]: docker exec l0oso884kogw04wsgscwog0c bash -c 'GIT_SSH_COMMAND="ssh -o ConnectTimeout=30 -p 22 -o Port=22 -o LogLevel=ERROR -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" git ls-remote https://github.com/farisnoaman/supalove refs/heads/main'
2026-Jan-01 21:36:32.372803
38afe497310dc3044746949a4ac89c1fcfb200b7	refs/heads/main
2026-Jan-01 21:36:32.406253
----------------------------------------
2026-Jan-01 21:36:32.426765
Importing farisnoaman/supalove:main (commit sha 38afe497310dc3044746949a4ac89c1fcfb200b7) to /artifacts/l0oso884kogw04wsgscwog0c.
2026-Jan-01 21:36:33.052298
[CMD]: docker exec l0oso884kogw04wsgscwog0c bash -c 'git clone --depth=1 --recurse-submodules --shallow-submodules -b 'main' 'https://github.com/farisnoaman/supalove' '/artifacts/l0oso884kogw04wsgscwog0c' && cd '/artifacts/l0oso884kogw04wsgscwog0c' && if [ -f .gitmodules ]; then sed -i "s#git@\(.*\):#https://\1/#g" '/artifacts/l0oso884kogw04wsgscwog0c'/.gitmodules || true && git submodule sync && GIT_SSH_COMMAND="ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" git submodule update --init --recursive --depth=1; fi && cd '/artifacts/l0oso884kogw04wsgscwog0c' && GIT_SSH_COMMAND="ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" git lfs pull'
2026-Jan-01 21:36:33.052298
Cloning into '/artifacts/l0oso884kogw04wsgscwog0c'...
2026-Jan-01 21:36:35.951407
[CMD]: docker exec l0oso884kogw04wsgscwog0c bash -c 'cd /artifacts/l0oso884kogw04wsgscwog0c && git log -1 38afe497310dc3044746949a4ac89c1fcfb200b7 --pretty=%B'
2026-Jan-01 21:36:35.951407
feat: Initialize PostgreSQL with roles and schemas, import Cluster model in API, and add an API verification script.
2026-Jan-01 21:36:40.069398
[CMD]: docker exec l0oso884kogw04wsgscwog0c bash -c 'test -f /artifacts/l0oso884kogw04wsgscwog0c/control-plane/api/Dockerfile && echo 'exists' || echo 'not found''
2026-Jan-01 21:36:40.069398
exists
2026-Jan-01 21:36:41.362746
[CMD]: docker exec l0oso884kogw04wsgscwog0c bash -c 'cat /artifacts/l0oso884kogw04wsgscwog0c/control-plane/api/Dockerfile'
2026-Jan-01 21:36:41.362746
FROM python:3.12-slim
2026-Jan-01 21:36:41.362746
WORKDIR /app
2026-Jan-01 21:36:41.362746
# Install system dependencies including Docker CLI
2026-Jan-01 21:36:41.362746
RUN apt-get update && apt-get install -y \
2026-Jan-01 21:36:41.362746
curl \
2026-Jan-01 21:36:41.362746
gnupg \
2026-Jan-01 21:36:41.362746
&& mkdir -p /etc/apt/keyrings \
2026-Jan-01 21:36:41.362746
&& curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg \
2026-Jan-01 21:36:41.362746
&& echo \
2026-Jan-01 21:36:41.362746
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
2026-Jan-01 21:36:41.362746
$(. /etc/os-release && echo "$VERSION_CODENAME") stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null \
2026-Jan-01 21:36:41.362746
&& apt-get update && apt-get install -y docker-ce-cli docker-compose-plugin \
2026-Jan-01 21:36:41.362746
&& rm -rf /var/lib/apt/lists/*
2026-Jan-01 21:36:41.362746
2026-Jan-01 21:36:41.362746
COPY control-plane/api/requirements.txt .
2026-Jan-01 21:36:41.362746
RUN pip install -r requirements.txt
2026-Jan-01 21:36:41.362746
2026-Jan-01 21:36:41.362746
# Copy source code to /app/src
2026-Jan-01 21:36:41.362746
COPY control-plane/api/src ./src
2026-Jan-01 21:36:41.362746
2026-Jan-01 21:36:41.362746
# Copy project template to /app/data-plane/project-template
2026-Jan-01 21:36:41.362746
# This bakes it into the image, so it's always available
2026-Jan-01 21:36:41.362746
COPY data-plane/project-template ./data-plane/project-template
2026-Jan-01 21:36:41.362746
2026-Jan-01 21:36:41.362746
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
2026-Jan-01 21:36:42.275678
Added 20 ARG declarations to Dockerfile for service api.
2026-Jan-01 21:36:43.307012
[CMD]: docker exec l0oso884kogw04wsgscwog0c bash -c 'test -f /artifacts/l0oso884kogw04wsgscwog0c/dashboard/Dockerfile && echo 'exists' || echo 'not found''
2026-Jan-01 21:36:43.307012
exists
2026-Jan-01 21:36:44.640931
[CMD]: docker exec l0oso884kogw04wsgscwog0c bash -c 'cat /artifacts/l0oso884kogw04wsgscwog0c/dashboard/Dockerfile'
2026-Jan-01 21:36:44.640931
# Stage 1: Dependencies
2026-Jan-01 21:36:44.640931
FROM node:20-alpine AS deps
2026-Jan-01 21:36:44.640931
WORKDIR /app
2026-Jan-01 21:36:44.640931
COPY dashboard/package*.json ./
2026-Jan-01 21:36:44.640931
RUN npm install
2026-Jan-01 21:36:44.640931
2026-Jan-01 21:36:44.640931
# Stage 2: Builder
2026-Jan-01 21:36:44.640931
FROM node:20-alpine AS builder
2026-Jan-01 21:36:44.640931
WORKDIR /app
2026-Jan-01 21:36:44.640931
COPY --from=deps /app/node_modules ./node_modules
2026-Jan-01 21:36:44.640931
COPY dashboard/ .
2026-Jan-01 21:36:44.640931
COPY docs/ /docs/
2026-Jan-01 21:36:44.640931
# Set environment variables for build if needed (e.g. backend URL)
2026-Jan-01 21:36:44.640931
# For Next.js client-side fetch, it might need to know the URL at build time if pre-rendering,
2026-Jan-01 21:36:44.640931
# but we are using "use client" so it's fine.
2026-Jan-01 21:36:44.640931
ARG NEXT_PUBLIC_API_URL
2026-Jan-01 21:36:44.640931
ENV NEXT_PUBLIC_API_URL=${NEXT_PUBLIC_API_URL}
2026-Jan-01 21:36:44.640931
RUN npm run build
2026-Jan-01 21:36:44.640931
2026-Jan-01 21:36:44.640931
# Stage 3: Runner
2026-Jan-01 21:36:44.640931
FROM node:20-alpine AS runner
2026-Jan-01 21:36:44.640931
WORKDIR /app
2026-Jan-01 21:36:44.640931
ENV NODE_ENV=production
2026-Jan-01 21:36:44.640931
COPY --from=builder /app/public ./public
2026-Jan-01 21:36:44.640931
COPY --from=builder /app/.next ./.next
2026-Jan-01 21:36:44.640931
COPY --from=builder /app/node_modules ./node_modules
2026-Jan-01 21:36:44.640931
COPY --from=builder /app/package.json ./package.json
2026-Jan-01 21:36:44.640931
2026-Jan-01 21:36:44.640931
EXPOSE 3000
2026-Jan-01 21:36:44.640931
CMD ["npm", "start"]
2026-Jan-01 21:36:45.892806
Added 60 ARG declarations to Dockerfile for service dashboard (multi-stage build, added to 3 stages).
2026-Jan-01 21:36:47.420642
[CMD]: docker exec l0oso884kogw04wsgscwog0c bash -c 'test -f /artifacts/l0oso884kogw04wsgscwog0c/data-plane/shared/routing-proxy/Dockerfile && echo 'exists' || echo 'not found''
2026-Jan-01 21:36:47.420642
exists
2026-Jan-01 21:36:48.658360
[CMD]: docker exec l0oso884kogw04wsgscwog0c bash -c 'cat /artifacts/l0oso884kogw04wsgscwog0c/data-plane/shared/routing-proxy/Dockerfile'
2026-Jan-01 21:36:48.658360
FROM python:3.11-slim
2026-Jan-01 21:36:48.658360
2026-Jan-01 21:36:48.658360
WORKDIR /app
2026-Jan-01 21:36:48.658360
2026-Jan-01 21:36:48.658360
COPY requirements.txt .
2026-Jan-01 21:36:48.658360
RUN pip install --no-cache-dir -r requirements.txt
2026-Jan-01 21:36:48.658360
2026-Jan-01 21:36:48.658360
COPY main.py .
2026-Jan-01 21:36:48.658360
2026-Jan-01 21:36:48.658360
EXPOSE 8000
2026-Jan-01 21:36:48.658360
2026-Jan-01 21:36:48.658360
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
2026-Jan-01 21:36:49.869654
Added 20 ARG declarations to Dockerfile for service shared-gateway-v3.
2026-Jan-01 21:36:49.903438
Pulling & building required images.
2026-Jan-01 21:36:50.292538
Creating build-time .env file in /artifacts (outside Docker context).
2026-Jan-01 21:36:51.888516
[CMD]: docker exec l0oso884kogw04wsgscwog0c bash -c 'cat /artifacts/build-time.env'
2026-Jan-01 21:36:51.888516
SOURCE_COMMIT='38afe497310dc3044746949a4ac89c1fcfb200b7'
2026-Jan-01 21:36:51.888516
COOLIFY_URL=''
2026-Jan-01 21:36:51.888516
COOLIFY_FQDN=''
2026-Jan-01 21:36:51.888516
SERVICE_NAME_CONTROL-PLANE-DB='control-plane-db'
2026-Jan-01 21:36:51.888516
SERVICE_NAME_API='api'
2026-Jan-01 21:36:51.888516
SERVICE_NAME_DASHBOARD='dashboard'
2026-Jan-01 21:36:51.888516
SERVICE_NAME_KEYCLOAK='keycloak'
2026-Jan-01 21:36:51.888516
SERVICE_NAME_MINIO='minio'
2026-Jan-01 21:36:51.888516
SERVICE_NAME_SHARED-POSTGRES='shared-postgres'
2026-Jan-01 21:36:51.888516
SERVICE_NAME_SHARED-GATEWAY-V3='shared-gateway-v3'
2026-Jan-01 21:36:51.888516
SERVICE_NAME_SHARED-AUTH='shared-auth'
2026-Jan-01 21:36:51.888516
SERVICE_NAME_SHARED-API='shared-api'
2026-Jan-01 21:36:51.888516
SERVICE_NAME_SHARED-STORAGE='shared-storage'
2026-Jan-01 21:36:51.888516
SERVICE_NAME_SHARED-REALTIME='shared-realtime'
2026-Jan-01 21:36:51.888516
ALLOWED_ORIGINS="http://localhost:3000,http://localhost:8000,https://supalove.hayataxi.online,https://api.hayataxi.online"
2026-Jan-01 21:36:51.888516
KEYCLOAK_ADMIN_PASSWORD="admin"
2026-Jan-01 21:36:51.888516
KEYCLOAK_ADMIN_USER="admin"
2026-Jan-01 21:36:51.888516
MINIO_ROOT_PASSWORD="minioadmin"
2026-Jan-01 21:36:51.888516
MINIO_ROOT_USER="minioadmin"
2026-Jan-01 21:36:51.888516
NEXT_PUBLIC_API_URL="https://api2.hayataxi.online"
2026-Jan-01 21:36:51.888516
POSTGRES_DB="control_plane"
2026-Jan-01 21:36:51.888516
POSTGRES_PASSWORD="platform"
2026-Jan-01 21:36:51.888516
POSTGRES_USER="platform"
2026-Jan-01 21:36:51.888516
SECRET_KEY_BASE="ChangeThisToAVeryLongRandomString"
2026-Jan-01 21:36:51.888516
SHARED_ANON_KEY="placeholder"
2026-Jan-01 21:36:51.888516
SHARED_GATEWAY_URL="http://localhost:8083"
2026-Jan-01 21:36:51.888516
SHARED_JWT_SECRET="your-super-secret-jwt-key-for-shared"
2026-Jan-01 21:36:51.888516
SHARED_POSTGRES_PASSWORD="postgres"
2026-Jan-01 21:36:51.888516
SHARED_SERVICE_ROLE_KEY="placeholder"
2026-Jan-01 21:36:51.888516
SITE_URL="http://localhost:3000"
2026-Jan-01 21:36:51.888516
URL="http://localhost:8000"
2026-Jan-01 21:36:51.903660
Adding build arguments to Docker Compose build command.
2026-Jan-01 21:36:53.395866
[CMD]: docker exec l0oso884kogw04wsgscwog0c bash -c 'SOURCE_COMMIT=38afe497310dc3044746949a4ac89c1fcfb200b7 COOLIFY_BRANCH=main COOLIFY_RESOURCE_UUID=sokwws8k80wcg0gss0k0goww COOLIFY_CONTAINER_NAME=sokwws8k80wcg0gss0k0goww-213626861147  docker compose --env-file /artifacts/build-time.env --project-name sokwws8k80wcg0gss0k0goww --project-directory /artifacts/l0oso884kogw04wsgscwog0c -f /artifacts/l0oso884kogw04wsgscwog0c/docker-compose.coolify.yml build --pull --no-cache --build-arg SOURCE_COMMIT --build-arg COOLIFY_URL --build-arg COOLIFY_FQDN --build-arg ALLOWED_ORIGINS --build-arg KEYCLOAK_ADMIN_PASSWORD --build-arg KEYCLOAK_ADMIN_USER --build-arg MINIO_ROOT_PASSWORD --build-arg MINIO_ROOT_USER --build-arg NEXT_PUBLIC_API_URL --build-arg POSTGRES_DB --build-arg POSTGRES_PASSWORD --build-arg POSTGRES_USER --build-arg SECRET_KEY_BASE --build-arg SHARED_ANON_KEY --build-arg SHARED_GATEWAY_URL --build-arg SHARED_JWT_SECRET --build-arg SHARED_POSTGRES_PASSWORD --build-arg SHARED_SERVICE_ROLE_KEY --build-arg SITE_URL --build-arg URL --build-arg COOLIFY_BUILD_SECRETS_HASH=155662039316dca89a8b1e721ccebfce4f01532d4022e1b429d51511b2c7c6f0'
2026-Jan-01 21:36:53.395866
#1 [internal] load local bake definitions
2026-Jan-01 21:36:53.563459
#1 reading from stdin 4.71kB done
2026-Jan-01 21:36:53.563459
#1 DONE 0.0s
2026-Jan-01 21:36:53.778746
#2 [api internal] load build definition from Dockerfile
2026-Jan-01 21:36:53.778746
#2 transferring dockerfile: 1.52kB 0.0s done
2026-Jan-01 21:36:53.778746
#2 DONE 0.1s
2026-Jan-01 21:36:53.778746
2026-Jan-01 21:36:53.778746
#3 [dashboard internal] load build definition from Dockerfile
2026-Jan-01 21:36:53.778746
#3 transferring dockerfile: 2.13kB 0.0s done
2026-Jan-01 21:36:53.778746
#3 DONE 0.1s
2026-Jan-01 21:36:53.778746
2026-Jan-01 21:36:53.778746
#4 [shared-gateway-v3 internal] load build definition from Dockerfile
2026-Jan-01 21:36:53.778746
#4 transferring dockerfile: 657B 0.0s done
2026-Jan-01 21:36:53.954857
#4 DONE 0.1s
2026-Jan-01 21:36:53.954857
2026-Jan-01 21:36:53.954857
#5 [dashboard internal] load metadata for docker.io/library/node:20-alpine
2026-Jan-01 21:36:54.483777
#5 DONE 0.7s
2026-Jan-01 21:36:54.483777
2026-Jan-01 21:36:54.483777
#6 [shared-gateway-v3 internal] load metadata for docker.io/library/python:3.11-slim
2026-Jan-01 21:36:54.618311
#6 ...
2026-Jan-01 21:36:54.618311
2026-Jan-01 21:36:54.618311
#7 [dashboard internal] load .dockerignore
2026-Jan-01 21:36:54.618311
#7 transferring context: 103B done
2026-Jan-01 21:36:54.618311
#7 DONE 0.0s
2026-Jan-01 21:36:54.618311
2026-Jan-01 21:36:54.618311
#8 [dashboard deps 1/4] FROM docker.io/library/node:20-alpine@sha256:658d0f63e501824d6c23e06d4bb95c71e7d704537c9d9272f488ac03a370d448
2026-Jan-01 21:36:54.618311
#8 DONE 0.0s
2026-Jan-01 21:36:54.618311
2026-Jan-01 21:36:54.618311
#9 [dashboard deps 2/4] WORKDIR /app
2026-Jan-01 21:36:54.618311
#9 CACHED
2026-Jan-01 21:36:54.618311
2026-Jan-01 21:36:54.618311
#10 [api internal] load metadata for docker.io/library/python:3.12-slim
2026-Jan-01 21:36:54.618311
#10 DONE 0.8s
2026-Jan-01 21:36:54.724312
#6 [shared-gateway-v3 internal] load metadata for docker.io/library/python:3.11-slim
2026-Jan-01 21:36:54.724312
#6 DONE 0.8s
2026-Jan-01 21:36:54.724312
2026-Jan-01 21:36:54.724312
#11 [shared-gateway-v3 internal] load .dockerignore
2026-Jan-01 21:36:54.724312
#11 transferring context: 2B 0.0s done
2026-Jan-01 21:36:54.724312
#11 DONE 0.1s
2026-Jan-01 21:36:54.724312
2026-Jan-01 21:36:54.724312
#12 [api internal] load .dockerignore
2026-Jan-01 21:36:54.724312
#12 transferring context: 103B 0.0s done
2026-Jan-01 21:36:54.832658
#12 DONE 0.1s
2026-Jan-01 21:36:54.832658
2026-Jan-01 21:36:54.832658
#13 [shared-gateway-v3 1/5] FROM docker.io/library/python:3.11-slim@sha256:aa9aac8eacc774817e2881238f52d983a5ea13d7f5a1dee479a1a1d466047951
2026-Jan-01 21:36:54.832658
#13 DONE 0.0s
2026-Jan-01 21:36:54.832658
2026-Jan-01 21:36:54.832658
#14 [shared-gateway-v3 2/5] WORKDIR /app
2026-Jan-01 21:36:54.832658
#14 CACHED
2026-Jan-01 21:36:54.832658
2026-Jan-01 21:36:54.832658
#15 [api 1/7] FROM docker.io/library/python:3.12-slim@sha256:8fbd0afc32e6cb14696c2fc47fadcda4c04ca0e766782343464bd716a6dc3f96
2026-Jan-01 21:36:54.832658
#15 DONE 0.0s
2026-Jan-01 21:36:54.832658
2026-Jan-01 21:36:54.832658
#16 [dashboard internal] load build context
2026-Jan-01 21:36:54.832658
#16 transferring context: 1.81MB 0.2s done
2026-Jan-01 21:36:54.832658
#16 DONE 0.3s
2026-Jan-01 21:36:54.832658
2026-Jan-01 21:36:54.832658
#17 [api 2/7] WORKDIR /app
2026-Jan-01 21:36:54.832658
#17 CACHED
2026-Jan-01 21:36:54.832658
2026-Jan-01 21:36:54.832658
#18 [dashboard deps 3/4] COPY dashboard/package*.json ./
2026-Jan-01 21:36:55.063322
#18 ...
2026-Jan-01 21:36:55.063322
2026-Jan-01 21:36:55.063322
#19 [shared-gateway-v3 internal] load build context
2026-Jan-01 21:36:55.063322
#19 transferring context: 12.36kB 0.0s done
2026-Jan-01 21:36:55.063322
#19 DONE 0.1s
2026-Jan-01 21:36:55.157893
#20 [shared-gateway-v3 3/5] COPY requirements.txt .
2026-Jan-01 21:36:55.157893
#20 DONE 0.2s
2026-Jan-01 21:36:55.157893
2026-Jan-01 21:36:55.157893
#18 [dashboard deps 3/4] COPY dashboard/package*.json ./
2026-Jan-01 21:36:55.157893
#18 DONE 0.3s
2026-Jan-01 21:36:55.157893
2026-Jan-01 21:36:55.157893
#21 [api internal] load build context
2026-Jan-01 21:36:55.157893
#21 transferring context: 565.22kB 0.2s done
2026-Jan-01 21:36:55.157893
#21 DONE 0.3s
2026-Jan-01 21:36:55.157893
2026-Jan-01 21:36:55.157893
#22 [dashboard deps 4/4] RUN npm install
2026-Jan-01 21:37:01.160494
#22 ...
2026-Jan-01 21:37:01.160494
2026-Jan-01 21:37:01.160494
#23 [api 3/7] RUN apt-get update && apt-get install -y     curl     gnupg     && mkdir -p /etc/apt/keyrings     && curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg     && echo     "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian     $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null     && apt-get update && apt-get install -y docker-ce-cli docker-compose-plugin     && rm -rf /var/lib/apt/lists/*
2026-Jan-01 21:37:01.160494
#23 1.527 Hit:1 http://deb.debian.org/debian trixie InRelease
2026-Jan-01 21:37:01.160494
#23 1.527 Get:2 http://deb.debian.org/debian trixie-updates InRelease [47.3 kB]
2026-Jan-01 21:37:01.160494
#23 1.527 Get:3 http://deb.debian.org/debian-security trixie-security InRelease [43.4 kB]
2026-Jan-01 21:37:01.160494
#23 1.620 Get:4 http://deb.debian.org/debian trixie/main amd64 Packages [9670 kB]
2026-Jan-01 21:37:01.160494
#23 1.887 Get:5 http://deb.debian.org/debian trixie-updates/main amd64 Packages [5412 B]
2026-Jan-01 21:37:01.160494
#23 1.887 Get:6 http://deb.debian.org/debian-security trixie-security/main amd64 Packages [93.7 kB]
2026-Jan-01 21:37:01.160494
#23 4.396 Fetched 9860 kB in 3s (3334 kB/s)
2026-Jan-01 21:37:01.160494
#23 4.396 Reading package lists...
2026-Jan-01 21:37:02.527734
2026-Jan-01 21:37:02.741611
#23 7.884 Reading package lists...
2026-Jan-01 21:37:05.028255
#23 ...
2026-Jan-01 21:37:05.028255
2026-Jan-01 21:37:05.028255
#24 [shared-gateway-v3 4/5] RUN pip install --no-cache-dir -r requirements.txt
2026-Jan-01 21:37:05.028255
#24 9.259 Collecting fastapi>=0.109.0 (from -r requirements.txt (line 1))
2026-Jan-01 21:37:05.028255
#24 9.325   Downloading fastapi-0.128.0-py3-none-any.whl.metadata (30 kB)
2026-Jan-01 21:37:05.028255
#24 9.586 Collecting uvicorn>=0.27.0 (from -r requirements.txt (line 2))
2026-Jan-01 21:37:05.028255
#24 9.593   Downloading uvicorn-0.40.0-py3-none-any.whl.metadata (6.7 kB)
2026-Jan-01 21:37:05.028255
#24 9.759 Collecting httpx>=0.26.0 (from -r requirements.txt (line 3))
2026-Jan-01 21:37:05.028255
#24 9.772   Downloading httpx-0.28.1-py3-none-any.whl.metadata (7.1 kB)
2026-Jan-01 21:37:05.229129
#24 10.07 Collecting psycopg2-binary>=2.9.9 (from -r requirements.txt (line 4))
2026-Jan-01 21:37:05.340722
#24 10.09   Downloading psycopg2_binary-2.9.11-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (4.9 kB)
2026-Jan-01 21:37:05.517640
#24 10.40 Collecting websockets>=12.0 (from -r requirements.txt (line 5))
2026-Jan-01 21:37:05.767781
#24 10.41   Downloading websockets-15.0.1-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.8 kB)
2026-Jan-01 21:37:05.767781
#24 10.49 Collecting python-dotenv>=1.0.0 (from -r requirements.txt (line 6))
2026-Jan-01 21:37:05.767781
#24 10.50   Downloading python_dotenv-1.2.1-py3-none-any.whl.metadata (25 kB)
2026-Jan-01 21:37:05.849002
#24 10.73 Collecting starlette<0.51.0,>=0.40.0 (from fastapi>=0.109.0->-r requirements.txt (line 1))
2026-Jan-01 21:37:06.044342
#24 10.74   Downloading starlette-0.50.0-py3-none-any.whl.metadata (6.3 kB)
2026-Jan-01 21:37:06.132885
#24 ...
2026-Jan-01 21:37:06.132885
2026-Jan-01 21:37:06.132885
#23 [api 3/7] RUN apt-get update && apt-get install -y     curl     gnupg     && mkdir -p /etc/apt/keyrings     && curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg     && echo     "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian     $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null     && apt-get update && apt-get install -y docker-ce-cli docker-compose-plugin     && rm -rf /var/lib/apt/lists/*
2026-Jan-01 21:37:06.132885
#23 7.884 Reading package lists...
2026-Jan-01 21:37:06.283262
#23 11.30 Building dependency tree...
2026-Jan-01 21:37:07.540563
#23 12.66 Reading state information...
2026-Jan-01 21:37:08.755527
#23 13.94 The following additional packages will be installed:
2026-Jan-01 21:37:08.755527
#23 13.94   bash-completion dirmngr gnupg-l10n gnupg-utils gpg gpg-agent gpg-wks-client
2026-Jan-01 21:37:08.914620
#23 13.94   gpgconf gpgsm gpgv krb5-locales libassuan9 libbrotli1 libcom-err2
2026-Jan-01 21:37:08.914620
#23 13.94   libcurl4t64 libgcrypt20 libgnutls30t64 libgpg-error-l10n libgpg-error0
2026-Jan-01 21:37:08.914620
#23 13.94   libgssapi-krb5-2 libidn2-0 libk5crypto3 libkeyutils1 libkrb5-3
2026-Jan-01 21:37:08.914620
#23 13.94   libkrb5support0 libksba8 libldap-common libldap2 libnghttp2-14 libnghttp3-9
2026-Jan-01 21:37:08.914620
#23 13.95   libnpth0t64 libp11-kit0 libpsl5t64 librtmp1 libsasl2-2 libsasl2-modules
2026-Jan-01 21:37:08.914620
#23 13.95   libsasl2-modules-db libssh2-1t64 libtasn1-6 libunistring5 pinentry-curses
2026-Jan-01 21:37:08.914620
#23 13.95   publicsuffix
2026-Jan-01 21:37:08.914620
#23 13.96 Suggested packages:
2026-Jan-01 21:37:08.914620
#23 13.96   dbus-user-session libpam-systemd pinentry-gnome3 tor gpg-wks-server
2026-Jan-01 21:37:08.914620
#23 13.96   parcimonie xloadimage scdaemon tpm2daemon rng-tools gnutls-bin krb5-doc
2026-Jan-01 21:37:08.914620
#23 13.96   krb5-user libsasl2-modules-gssapi-mit | libsasl2-modules-gssapi-heimdal
2026-Jan-01 21:37:08.914620
#23 13.96   libsasl2-modules-ldap libsasl2-modules-otp libsasl2-modules-sql pinentry-doc
2026-Jan-01 21:37:09.676402
#23 14.87 The following NEW packages will be installed:
2026-Jan-01 21:37:09.795407
#23 14.87   bash-completion curl dirmngr gnupg gnupg-l10n gnupg-utils gpg gpg-agent
2026-Jan-01 21:37:09.795407
#23 14.87   gpg-wks-client gpgconf gpgsm gpgv krb5-locales libassuan9 libbrotli1
2026-Jan-01 21:37:09.795407
#23 14.87   libcom-err2 libcurl4t64 libgcrypt20 libgnutls30t64 libgpg-error-l10n
2026-Jan-01 21:37:09.795407
#23 14.88   libgpg-error0 libgssapi-krb5-2 libidn2-0 libk5crypto3 libkeyutils1 libkrb5-3
2026-Jan-01 21:37:09.795407
#23 14.88   libkrb5support0 libksba8 libldap-common libldap2 libnghttp2-14 libnghttp3-9
2026-Jan-01 21:37:09.795407
#23 14.88   libnpth0t64 libp11-kit0 libpsl5t64 librtmp1 libsasl2-2 libsasl2-modules
2026-Jan-01 21:37:09.795407
#23 14.88   libsasl2-modules-db libssh2-1t64 libtasn1-6 libunistring5 pinentry-curses
2026-Jan-01 21:37:09.795407
#23 14.88   publicsuffix
2026-Jan-01 21:37:09.795407
#23 14.97 0 upgraded, 44 newly installed, 0 to remove and 0 not upgraded.
2026-Jan-01 21:37:09.795407
#23 14.97 Need to get 10.4 MB of archives.
2026-Jan-01 21:37:09.795407
#23 14.97 After this operation, 33.7 MB of additional disk space will be used.
2026-Jan-01 21:37:09.795407
#23 14.97 Get:1 http://deb.debian.org/debian trixie/main amd64 bash-completion all 1:2.16.0-7 [319 kB]
2026-Jan-01 21:37:09.930767
#23 14.98 Get:2 http://deb.debian.org/debian trixie/main amd64 krb5-locales all 1.21.3-5 [101 kB]
2026-Jan-01 21:37:09.930767
#23 15.00 Get:3 http://deb.debian.org/debian trixie/main amd64 libbrotli1 amd64 1.1.0-2+b7 [307 kB]
2026-Jan-01 21:37:09.930767
#23 15.00 Get:4 http://deb.debian.org/debian trixie/main amd64 libkrb5support0 amd64 1.21.3-5 [33.0 kB]
2026-Jan-01 21:37:09.930767
#23 15.00 Get:5 http://deb.debian.org/debian trixie/main amd64 libcom-err2 amd64 1.47.2-3+b3 [25.0 kB]
2026-Jan-01 21:37:09.930767
#23 15.00 Get:6 http://deb.debian.org/debian trixie/main amd64 libk5crypto3 amd64 1.21.3-5 [81.5 kB]
2026-Jan-01 21:37:09.930767
#23 15.00 Get:7 http://deb.debian.org/debian trixie/main amd64 libkeyutils1 amd64 1.6.3-6 [9456 B]
2026-Jan-01 21:37:09.930767
#23 15.01 Get:8 http://deb.debian.org/debian trixie/main amd64 libkrb5-3 amd64 1.21.3-5 [326 kB]
2026-Jan-01 21:37:09.930767
#23 15.01 Get:9 http://deb.debian.org/debian trixie/main amd64 libgssapi-krb5-2 amd64 1.21.3-5 [138 kB]
2026-Jan-01 21:37:09.930767
#23 15.01 Get:10 http://deb.debian.org/debian trixie/main amd64 libunistring5 amd64 1.3-2 [477 kB]
2026-Jan-01 21:37:09.930767
#23 15.02 Get:11 http://deb.debian.org/debian trixie/main amd64 libidn2-0 amd64 2.3.8-2 [109 kB]
2026-Jan-01 21:37:09.930767
#23 15.03 Get:12 http://deb.debian.org/debian trixie/main amd64 libsasl2-modules-db amd64 2.1.28+dfsg1-9 [19.8 kB]
2026-Jan-01 21:37:09.930767
#23 15.03 Get:13 http://deb.debian.org/debian trixie/main amd64 libsasl2-2 amd64 2.1.28+dfsg1-9 [57.5 kB]
2026-Jan-01 21:37:09.930767
#23 15.03 Get:14 http://deb.debian.org/debian trixie/main amd64 libldap2 amd64 2.6.10+dfsg-1 [194 kB]
2026-Jan-01 21:37:09.930767
#23 15.04 Get:15 http://deb.debian.org/debian trixie/main amd64 libnghttp2-14 amd64 1.64.0-1.1 [76.0 kB]
2026-Jan-01 21:37:09.930767
#23 15.05 Get:16 http://deb.debian.org/debian trixie/main amd64 libnghttp3-9 amd64 1.8.0-1 [67.7 kB]
2026-Jan-01 21:37:09.930767
#23 15.05 Get:17 http://deb.debian.org/debian trixie/main amd64 libpsl5t64 amd64 0.21.2-1.1+b1 [57.2 kB]
2026-Jan-01 21:37:09.930767
#23 15.06 Get:18 http://deb.debian.org/debian trixie/main amd64 libp11-kit0 amd64 0.25.5-3 [425 kB]
2026-Jan-01 21:37:09.930767
#23 15.06 Get:19 http://deb.debian.org/debian trixie/main amd64 libtasn1-6 amd64 4.20.0-2 [49.9 kB]
2026-Jan-01 21:37:09.930767
#23 15.07 Get:20 http://deb.debian.org/debian trixie/main amd64 libgnutls30t64 amd64 3.8.9-3 [1465 kB]
2026-Jan-01 21:37:09.930767
#23 15.09 Get:21 http://deb.debian.org/debian trixie/main amd64 librtmp1 amd64 2.4+20151223.gitfa8646d.1-2+b5 [58.8 kB]
2026-Jan-01 21:37:10.000902
#23 15.09 Get:22 http://deb.debian.org/debian trixie/main amd64 libssh2-1t64 amd64 1.11.1-1 [245 kB]
2026-Jan-01 21:37:10.000902
#23 15.10 Get:23 http://deb.debian.org/debian trixie/main amd64 libcurl4t64 amd64 8.14.1-2+deb13u2 [391 kB]
2026-Jan-01 21:37:10.000902
#23 15.10 Get:24 http://deb.debian.org/debian trixie/main amd64 curl amd64 8.14.1-2+deb13u2 [270 kB]
2026-Jan-01 21:37:10.000902
#23 15.11 Get:25 http://deb.debian.org/debian trixie/main amd64 libgpg-error0 amd64 1.51-4 [82.1 kB]
2026-Jan-01 21:37:10.000902
#23 15.12 Get:26 http://deb.debian.org/debian trixie/main amd64 libassuan9 amd64 3.0.2-2 [61.5 kB]
2026-Jan-01 21:37:10.000902
#23 15.12 Get:27 http://deb.debian.org/debian trixie/main amd64 libgcrypt20 amd64 1.11.0-7 [843 kB]
2026-Jan-01 21:37:10.000902
#23 15.13 Get:28 http://deb.debian.org/debian trixie/main amd64 gpgconf amd64 2.4.7-21+b3 [129 kB]
2026-Jan-01 21:37:10.000902
#23 15.14 Get:29 http://deb.debian.org/debian trixie/main amd64 libksba8 amd64 1.6.7-2+b1 [136 kB]
2026-Jan-01 21:37:10.000902
#23 15.14 Get:30 http://deb.debian.org/debian trixie/main amd64 libnpth0t64 amd64 1.8-3 [23.2 kB]
2026-Jan-01 21:37:10.000902
#23 15.14 Get:31 http://deb.debian.org/debian trixie/main amd64 dirmngr amd64 2.4.7-21+b3 [384 kB]
2026-Jan-01 21:37:10.000902
#23 15.16 Get:32 http://deb.debian.org/debian trixie/main amd64 gnupg-l10n all 2.4.7-21 [747 kB]
2026-Jan-01 21:37:10.000902
#23 15.16 Get:33 http://deb.debian.org/debian trixie/main amd64 gpg amd64 2.4.7-21+b3 [634 kB]
2026-Jan-01 21:37:10.000902
#23 15.17 Get:34 http://deb.debian.org/debian trixie/main amd64 pinentry-curses amd64 1.3.1-2 [86.4 kB]
2026-Jan-01 21:37:10.000902
#23 15.17 Get:35 http://deb.debian.org/debian trixie/main amd64 gpg-agent amd64 2.4.7-21+b3 [271 kB]
2026-Jan-01 21:37:10.000902
#23 15.18 Get:36 http://deb.debian.org/debian trixie/main amd64 gpgsm amd64 2.4.7-21+b3 [275 kB]
2026-Jan-01 21:37:10.000902
#23 15.18 Get:37 http://deb.debian.org/debian trixie/main amd64 gnupg all 2.4.7-21 [417 kB]
2026-Jan-01 21:37:10.000902
#23 15.19 Get:38 http://deb.debian.org/debian trixie/main amd64 gpg-wks-client amd64 2.4.7-21+b3 [108 kB]
2026-Jan-01 21:37:10.179220
#23 15.19 Get:39 http://deb.debian.org/debian trixie/main amd64 gpgv amd64 2.4.7-21+b3 [241 kB]
2026-Jan-01 21:37:10.179220
#23 15.20 Get:40 http://deb.debian.org/debian trixie/main amd64 libgpg-error-l10n all 1.51-4 [114 kB]
2026-Jan-01 21:37:10.179220
#23 15.20 Get:41 http://deb.debian.org/debian trixie/main amd64 libldap-common all 2.6.10+dfsg-1 [35.1 kB]
2026-Jan-01 21:37:10.179220
#23 15.20 Get:42 http://deb.debian.org/debian trixie/main amd64 libsasl2-modules amd64 2.1.28+dfsg1-9 [66.7 kB]
2026-Jan-01 21:37:10.179220
#23 15.20 Get:43 http://deb.debian.org/debian trixie/main amd64 publicsuffix all 20250328.1952-0.1 [296 kB]
2026-Jan-01 21:37:10.179220
#23 15.21 Get:44 http://deb.debian.org/debian trixie/main amd64 gnupg-utils amd64 2.4.7-21+b3 [194 kB]
2026-Jan-01 21:37:10.672523
#23 15.86 debconf: unable to initialize frontend: Dialog
2026-Jan-01 21:37:10.672523
#23 15.86 debconf: (TERM is not set, so the dialog frontend is not usable.)
2026-Jan-01 21:37:10.672523
#23 15.86 debconf: falling back to frontend: Readline
2026-Jan-01 21:37:10.882643
#23 15.86 debconf: unable to initialize frontend: Readline
2026-Jan-01 21:37:10.882643
#23 15.86 debconf: (Can't locate Term/ReadLine.pm in @INC (you may need to install the Term::ReadLine module) (@INC entries checked: /etc/perl /usr/local/lib/x86_64-linux-gnu/perl/5.40.1 /usr/local/share/perl/5.40.1 /usr/lib/x86_64-linux-gnu/perl5/5.40 /usr/share/perl5 /usr/lib/x86_64-linux-gnu/perl-base /usr/lib/x86_64-linux-gnu/perl/5.40 /usr/share/perl/5.40 /usr/local/lib/site_perl) at /usr/share/perl5/Debconf/FrontEnd/Readline.pm line 8, <STDIN> line 44.)
2026-Jan-01 21:37:10.882643
#23 15.86 debconf: falling back to frontend: Teletype
2026-Jan-01 21:37:10.882643
#23 15.91 debconf: unable to initialize frontend: Teletype
2026-Jan-01 21:37:10.882643
#23 15.91 debconf: (This frontend requires a controlling tty.)
2026-Jan-01 21:37:10.882643
#23 15.91 debconf: falling back to frontend: Noninteractive
2026-Jan-01 21:37:15.638410
#23 ...
2026-Jan-01 21:37:15.638410
2026-Jan-01 21:37:15.638410
#24 [shared-gateway-v3 4/5] RUN pip install --no-cache-dir -r requirements.txt
2026-Jan-01 21:37:15.638410
#24 11.63 Collecting pydantic>=2.7.0 (from fastapi>=0.109.0->-r requirements.txt (line 1))
2026-Jan-01 21:37:15.638410
#24 11.64   Downloading pydantic-2.12.5-py3-none-any.whl.metadata (90 kB)
2026-Jan-01 21:37:15.638410
#24 11.66      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 90.6/90.6 kB 325.8 MB/s eta 0:00:00
2026-Jan-01 21:37:15.638410
#24 11.78 Collecting typing-extensions>=4.8.0 (from fastapi>=0.109.0->-r requirements.txt (line 1))
2026-Jan-01 21:37:15.638410
#24 11.79   Downloading typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
2026-Jan-01 21:37:15.638410
#24 11.83 Collecting annotated-doc>=0.0.2 (from fastapi>=0.109.0->-r requirements.txt (line 1))
2026-Jan-01 21:37:15.638410
#24 11.84   Downloading annotated_doc-0.0.4-py3-none-any.whl.metadata (6.6 kB)
2026-Jan-01 21:37:15.638410
#24 11.95 Collecting click>=7.0 (from uvicorn>=0.27.0->-r requirements.txt (line 2))
2026-Jan-01 21:37:15.638410
#24 11.97   Downloading click-8.3.1-py3-none-any.whl.metadata (2.6 kB)
2026-Jan-01 21:37:15.638410
#24 12.00 Collecting h11>=0.8 (from uvicorn>=0.27.0->-r requirements.txt (line 2))
2026-Jan-01 21:37:15.638410
#24 12.01   Downloading h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
2026-Jan-01 21:37:15.638410
#24 12.13 Collecting anyio (from httpx>=0.26.0->-r requirements.txt (line 3))
2026-Jan-01 21:37:15.638410
#24 12.14   Downloading anyio-4.12.0-py3-none-any.whl.metadata (4.3 kB)
2026-Jan-01 21:37:15.638410
#24 12.21 Collecting certifi (from httpx>=0.26.0->-r requirements.txt (line 3))
2026-Jan-01 21:37:15.638410
#24 12.23   Downloading certifi-2025.11.12-py3-none-any.whl.metadata (2.5 kB)
2026-Jan-01 21:37:15.638410
#24 12.33 Collecting httpcore==1.* (from httpx>=0.26.0->-r requirements.txt (line 3))
2026-Jan-01 21:37:15.638410
#24 12.34   Downloading httpcore-1.0.9-py3-none-any.whl.metadata (21 kB)
2026-Jan-01 21:37:15.638410
#24 12.41 Collecting idna (from httpx>=0.26.0->-r requirements.txt (line 3))
2026-Jan-01 21:37:15.638410
#24 12.43   Downloading idna-3.11-py3-none-any.whl.metadata (8.4 kB)
2026-Jan-01 21:37:15.638410
#24 12.56 Collecting annotated-types>=0.6.0 (from pydantic>=2.7.0->fastapi>=0.109.0->-r requirements.txt (line 1))
2026-Jan-01 21:37:15.638410
#24 12.57   Downloading annotated_types-0.7.0-py3-none-any.whl.metadata (15 kB)
2026-Jan-01 21:37:15.638410
#24 15.84 Collecting pydantic-core==2.41.5 (from pydantic>=2.7.0->fastapi>=0.109.0->-r requirements.txt (line 1))
2026-Jan-01 21:37:15.638410
#24 15.85   Downloading pydantic_core-2.41.5-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (7.3 kB)
2026-Jan-01 21:37:15.638410
#24 15.89 Collecting typing-inspection>=0.4.2 (from pydantic>=2.7.0->fastapi>=0.109.0->-r requirements.txt (line 1))
2026-Jan-01 21:37:15.638410
#24 15.90   Downloading typing_inspection-0.4.2-py3-none-any.whl.metadata (2.6 kB)
2026-Jan-01 21:37:15.638410
#24 16.04 Downloading fastapi-0.128.0-py3-none-any.whl (103 kB)
2026-Jan-01 21:37:15.638410
#24 16.06    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 103.1/103.1 kB 297.7 MB/s eta 0:00:00
2026-Jan-01 21:37:15.638410
#24 16.08 Downloading uvicorn-0.40.0-py3-none-any.whl (68 kB)
2026-Jan-01 21:37:15.638410
#24 16.09    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 68.5/68.5 kB 247.2 MB/s eta 0:00:00
2026-Jan-01 21:37:15.638410
#24 16.12 Downloading httpx-0.28.1-py3-none-any.whl (73 kB)
2026-Jan-01 21:37:15.638410
#24 16.14    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 73.5/73.5 kB 286.3 MB/s eta 0:00:00
2026-Jan-01 21:37:15.638410
#24 16.16 Downloading httpcore-1.0.9-py3-none-any.whl (78 kB)
2026-Jan-01 21:37:15.638410
#24 16.17    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 78.8/78.8 kB 222.5 MB/s eta 0:00:00
2026-Jan-01 21:37:15.638410
#24 16.19 Downloading psycopg2_binary-2.9.11-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (4.2 MB)
2026-Jan-01 21:37:15.638410
#24 16.28    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.2/4.2 MB 49.5 MB/s eta 0:00:00
2026-Jan-01 21:37:15.638410
#24 16.29 Downloading websockets-15.0.1-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (182 kB)
2026-Jan-01 21:37:15.638410
#24 16.30    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 182.3/182.3 kB 290.6 MB/s eta 0:00:00
2026-Jan-01 21:37:15.638410
#24 16.31 Downloading python_dotenv-1.2.1-py3-none-any.whl (21 kB)
2026-Jan-01 21:37:15.638410
#24 16.31 Downloading annotated_doc-0.0.4-py3-none-any.whl (5.3 kB)
2026-Jan-01 21:37:15.638410
#24 16.32 Downloading click-8.3.1-py3-none-any.whl (108 kB)
2026-Jan-01 21:37:15.638410
#24 16.33    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 108.3/108.3 kB 297.6 MB/s eta 0:00:00
2026-Jan-01 21:37:15.638410
#24 16.34 Downloading h11-0.16.0-py3-none-any.whl (37 kB)
2026-Jan-01 21:37:15.638410
#24 16.35 Downloading pydantic-2.12.5-py3-none-any.whl (463 kB)
2026-Jan-01 21:37:15.638410
#24 16.35    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 463.6/463.6 kB 113.0 MB/s eta 0:00:00
2026-Jan-01 21:37:15.638410
#24 16.37 Downloading pydantic_core-2.41.5-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.1 MB)
2026-Jan-01 21:37:15.638410
#24 16.40    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 95.3 MB/s eta 0:00:00
2026-Jan-01 21:37:15.638410
#24 16.41 Downloading starlette-0.50.0-py3-none-any.whl (74 kB)
2026-Jan-01 21:37:15.638410
#24 16.43    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 74.0/74.0 kB 245.7 MB/s eta 0:00:00
2026-Jan-01 21:37:15.638410
#24 16.44 Downloading anyio-4.12.0-py3-none-any.whl (113 kB)
2026-Jan-01 21:37:15.638410
#24 16.45    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 113.4/113.4 kB 273.9 MB/s eta 0:00:00
2026-Jan-01 21:37:15.638410
#24 16.45 Downloading idna-3.11-py3-none-any.whl (71 kB)
2026-Jan-01 21:37:15.638410
#24 16.46    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 71.0/71.0 kB 76.3 MB/s eta 0:00:00
2026-Jan-01 21:37:15.638410
#24 16.47 Downloading typing_extensions-4.15.0-py3-none-any.whl (44 kB)
2026-Jan-01 21:37:15.638410
#24 16.48    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 44.6/44.6 kB 238.0 MB/s eta 0:00:00
2026-Jan-01 21:37:15.638410
#24 16.49 Downloading certifi-2025.11.12-py3-none-any.whl (159 kB)
2026-Jan-01 21:37:15.638410
#24 16.50    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 159.4/159.4 kB 63.6 MB/s eta 0:00:00
2026-Jan-01 21:37:15.638410
#24 16.50 Downloading annotated_types-0.7.0-py3-none-any.whl (13 kB)
2026-Jan-01 21:37:15.638410
#24 16.52 Downloading typing_inspection-0.4.2-py3-none-any.whl (14 kB)
2026-Jan-01 21:37:15.638410
#24 17.08 Installing collected packages: websockets, typing-extensions, python-dotenv, psycopg2-binary, idna, h11, click, certifi, annotated-types, annotated-doc, uvicorn, typing-inspection, pydantic-core, httpcore, anyio, starlette, pydantic, httpx, fastapi
2026-Jan-01 21:37:17.041451
#24 21.94 WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
2026-Jan-01 21:37:17.041451
#24 21.94 Successfully installed annotated-doc-0.0.4 annotated-types-0.7.0 anyio-4.12.0 certifi-2025.11.12 click-8.3.1 fastapi-0.128.0 h11-0.16.0 httpcore-1.0.9 httpx-0.28.1 idna-3.11 psycopg2-binary-2.9.11 pydantic-2.12.5 pydantic-core-2.41.5 python-dotenv-1.2.1 starlette-0.50.0 typing-extensions-4.15.0 typing-inspection-0.4.2 uvicorn-0.40.0 websockets-15.0.1
2026-Jan-01 21:37:17.292871
#24 22.17
2026-Jan-01 21:37:17.292871
#24 22.17 [notice] A new release of pip is available: 24.0 -> 25.3
2026-Jan-01 21:37:17.292871
#24 22.17 [notice] To update, run: pip install --upgrade pip
2026-Jan-01 21:37:18.151533
#24 ...
2026-Jan-01 21:37:18.151533
2026-Jan-01 21:37:18.151533
#23 [api 3/7] RUN apt-get update && apt-get install -y     curl     gnupg     && mkdir -p /etc/apt/keyrings     && curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg     && echo     "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian     $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null     && apt-get update && apt-get install -y docker-ce-cli docker-compose-plugin     && rm -rf /var/lib/apt/lists/*
2026-Jan-01 21:37:18.151533
#23 23.32 Fetched 10.4 MB in 0s (37.1 MB/s)
2026-Jan-01 21:37:18.243164
#23 23.40 Selecting previously unselected package bash-completion.
2026-Jan-01 21:37:18.243164
#23 23.40 (Reading database ... 
(Reading database ... 5%
(Reading database ... 10%
(Reading database ... 15%
(Reading database ... 20%
(Reading database ... 25%
(Reading database ... 30%
(Reading database ... 35%
(Reading database ... 40%
(Reading database ... 45%
(Reading database ... 50%
(Reading database ... 55%
(Reading database ... 60%
(Reading database ... 65%
(Reading database ... 70%
2026-Jan-01 21:37:18.458792
(Reading database ... 75%
(Reading database ... 80%
(Reading database ... 85%
(Reading database ... 90%
(Reading database ... 95%
(Reading database ... 100%
(Reading database ... 5644 files and directories currently installed.)
2026-Jan-01 21:37:18.458792
#23 23.49 Preparing to unpack .../00-bash-completion_1%3a2.16.0-7_all.deb ...
2026-Jan-01 21:37:18.458792
#23 23.49 Unpacking bash-completion (1:2.16.0-7) ...
2026-Jan-01 21:37:19.395926
#23 24.59 Selecting previously unselected package krb5-locales.
2026-Jan-01 21:37:19.567819
#23 24.59 Preparing to unpack .../01-krb5-locales_1.21.3-5_all.deb ...
2026-Jan-01 21:37:19.567819
#23 24.60 Unpacking krb5-locales (1.21.3-5) ...
2026-Jan-01 21:37:19.590896
#23 24.76 Selecting previously unselected package libbrotli1:amd64.
2026-Jan-01 21:37:19.590896
#23 24.76 Preparing to unpack .../02-libbrotli1_1.1.0-2+b7_amd64.deb ...
2026-Jan-01 21:37:19.731827
#23 24.77 Unpacking libbrotli1:amd64 (1.1.0-2+b7) ...
2026-Jan-01 21:37:19.859485
#23 25.03 Selecting previously unselected package libkrb5support0:amd64.
2026-Jan-01 21:37:19.979487
#23 25.03 Preparing to unpack .../03-libkrb5support0_1.21.3-5_amd64.deb ...
2026-Jan-01 21:37:19.979487
#23 25.05 Unpacking libkrb5support0:amd64 (1.21.3-5) ...
2026-Jan-01 21:37:19.979487
#23 25.18 Selecting previously unselected package libcom-err2:amd64.
2026-Jan-01 21:37:20.122402
#23 25.18 Preparing to unpack .../04-libcom-err2_1.47.2-3+b3_amd64.deb ...
2026-Jan-01 21:37:20.122402
#23 25.18 Unpacking libcom-err2:amd64 (1.47.2-3+b3) ...
2026-Jan-01 21:37:20.122402
#23 25.30 Selecting previously unselected package libk5crypto3:amd64.
2026-Jan-01 21:37:20.286774
#23 25.31 Preparing to unpack .../05-libk5crypto3_1.21.3-5_amd64.deb ...
2026-Jan-01 21:37:20.286774
#23 25.31 Unpacking libk5crypto3:amd64 (1.21.3-5) ...
2026-Jan-01 21:37:20.324713
#23 25.48 Selecting previously unselected package libkeyutils1:amd64.
2026-Jan-01 21:37:20.324713
#23 25.48 Preparing to unpack .../06-libkeyutils1_1.6.3-6_amd64.deb ...
2026-Jan-01 21:37:20.424578
#23 ...
2026-Jan-01 21:37:20.424578
2026-Jan-01 21:37:20.424578
#24 [shared-gateway-v3 4/5] RUN pip install --no-cache-dir -r requirements.txt
2026-Jan-01 21:37:20.424578
#24 DONE 25.3s
2026-Jan-01 21:37:20.424578
2026-Jan-01 21:37:20.424578
#23 [api 3/7] RUN apt-get update && apt-get install -y     curl     gnupg     && mkdir -p /etc/apt/keyrings     && curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg     && echo     "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian     $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null     && apt-get update && apt-get install -y docker-ce-cli docker-compose-plugin     && rm -rf /var/lib/apt/lists/*
2026-Jan-01 21:37:20.424578
#23 25.49 Unpacking libkeyutils1:amd64 (1.6.3-6) ...
2026-Jan-01 21:37:20.618671
#23 ...
2026-Jan-01 21:37:20.618671
2026-Jan-01 21:37:20.618671
#25 [shared-gateway-v3 5/5] COPY main.py .
2026-Jan-01 21:37:20.618671
#25 DONE 0.1s
2026-Jan-01 21:37:20.618671
2026-Jan-01 21:37:20.618671
#23 [api 3/7] RUN apt-get update && apt-get install -y     curl     gnupg     && mkdir -p /etc/apt/keyrings     && curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg     && echo     "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian     $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null     && apt-get update && apt-get install -y docker-ce-cli docker-compose-plugin     && rm -rf /var/lib/apt/lists/*
2026-Jan-01 21:37:20.618671
#23 25.68 Selecting previously unselected package libkrb5-3:amd64.
2026-Jan-01 21:37:20.618671
#23 25.68 Preparing to unpack .../07-libkrb5-3_1.21.3-5_amd64.deb ...
2026-Jan-01 21:37:20.618671
#23 25.69 Unpacking libkrb5-3:amd64 (1.21.3-5) ...
2026-Jan-01 21:37:20.734478
#23 25.93 Selecting previously unselected package libgssapi-krb5-2:amd64.
2026-Jan-01 21:37:20.927921
#23 25.94 Preparing to unpack .../08-libgssapi-krb5-2_1.21.3-5_amd64.deb ...
2026-Jan-01 21:37:20.927921
#23 25.94 Unpacking libgssapi-krb5-2:amd64 (1.21.3-5) ...
2026-Jan-01 21:37:20.927921
#23 26.09 Selecting previously unselected package libunistring5:amd64.
2026-Jan-01 21:37:21.058783
#23 26.09 Preparing to unpack .../09-libunistring5_1.3-2_amd64.deb ...
2026-Jan-01 21:37:21.058783
#23 26.10 Unpacking libunistring5:amd64 (1.3-2) ...
2026-Jan-01 21:37:21.193538
#23 26.38 Selecting previously unselected package libidn2-0:amd64.
2026-Jan-01 21:37:21.367774
#23 26.39 Preparing to unpack .../10-libidn2-0_2.3.8-2_amd64.deb ...
2026-Jan-01 21:37:21.367774
#23 26.39 Unpacking libidn2-0:amd64 (2.3.8-2) ...
2026-Jan-01 21:37:21.367774
#23 26.55 Selecting previously unselected package libsasl2-modules-db:amd64.
2026-Jan-01 21:37:21.367774
#23 26.55 Preparing to unpack .../11-libsasl2-modules-db_2.1.28+dfsg1-9_amd64.deb ...
2026-Jan-01 21:37:21.489008
#23 26.55 Unpacking libsasl2-modules-db:amd64 (2.1.28+dfsg1-9) ...
2026-Jan-01 21:37:21.489008
#23 26.67 Selecting previously unselected package libsasl2-2:amd64.
2026-Jan-01 21:37:21.489008
#23 26.67 Preparing to unpack .../12-libsasl2-2_2.1.28+dfsg1-9_amd64.deb ...
2026-Jan-01 21:37:21.596586
#23 26.68 Unpacking libsasl2-2:amd64 (2.1.28+dfsg1-9) ...
2026-Jan-01 21:37:21.596586
#23 26.78 Selecting previously unselected package libldap2:amd64.
2026-Jan-01 21:37:21.754471
#23 ...
2026-Jan-01 21:37:21.754471
2026-Jan-01 21:37:21.754471
#26 [shared-gateway-v3] exporting to image
2026-Jan-01 21:37:21.754471
#26 exporting layers 1.1s done
2026-Jan-01 21:37:21.754471
#26 writing image sha256:d28993fc88c509b98895b76c5c54bd95fceb8ea1ba36c486493a598f1cc1cd2a done
2026-Jan-01 21:37:21.754471
#26 naming to docker.io/library/sokwws8k80wcg0gss0k0goww-shared-gateway-v3 done
2026-Jan-01 21:37:21.754471
#26 DONE 1.1s
2026-Jan-01 21:37:21.754471
2026-Jan-01 21:37:21.754471
#23 [api 3/7] RUN apt-get update && apt-get install -y     curl     gnupg     && mkdir -p /etc/apt/keyrings     && curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg     && echo     "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian     $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null     && apt-get update && apt-get install -y docker-ce-cli docker-compose-plugin     && rm -rf /var/lib/apt/lists/*
2026-Jan-01 21:37:21.754471
#23 26.78 Preparing to unpack .../13-libldap2_2.6.10+dfsg-1_amd64.deb ...
2026-Jan-01 21:37:21.754471
#23 26.79 Unpacking libldap2:amd64 (2.6.10+dfsg-1) ...
2026-Jan-01 21:37:21.943231
#23 ...
2026-Jan-01 21:37:21.943231
2026-Jan-01 21:37:21.943231
#27 [shared-gateway-v3] resolving provenance for metadata file
2026-Jan-01 21:37:21.943231
#27 DONE 0.0s
2026-Jan-01 21:37:21.943231
2026-Jan-01 21:37:21.943231
#23 [api 3/7] RUN apt-get update && apt-get install -y     curl     gnupg     && mkdir -p /etc/apt/keyrings     && curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg     && echo     "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian     $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null     && apt-get update && apt-get install -y docker-ce-cli docker-compose-plugin     && rm -rf /var/lib/apt/lists/*
2026-Jan-01 21:37:21.943231
#23 26.97 Selecting previously unselected package libnghttp2-14:amd64.
2026-Jan-01 21:37:21.943231
#23 26.98 Preparing to unpack .../14-libnghttp2-14_1.64.0-1.1_amd64.deb ...
2026-Jan-01 21:37:21.943231
#23 26.99 Unpacking libnghttp2-14:amd64 (1.64.0-1.1) ...
2026-Jan-01 21:37:21.990752
#23 27.17 Selecting previously unselected package libnghttp3-9:amd64.
2026-Jan-01 21:37:22.223013
#23 27.18 Preparing to unpack .../15-libnghttp3-9_1.8.0-1_amd64.deb ...
2026-Jan-01 21:37:22.223013
#23 27.18 Unpacking libnghttp3-9:amd64 (1.8.0-1) ...
2026-Jan-01 21:37:22.223013
#23 27.26 Selecting previously unselected package libpsl5t64:amd64.
2026-Jan-01 21:37:22.223013
#23 27.26 Preparing to unpack .../16-libpsl5t64_0.21.2-1.1+b1_amd64.deb ...
2026-Jan-01 21:37:22.223013
#23 27.27 Unpacking libpsl5t64:amd64 (0.21.2-1.1+b1) ...
2026-Jan-01 21:37:22.273019
#23 27.43 Selecting previously unselected package libp11-kit0:amd64.
2026-Jan-01 21:37:22.406269
#23 27.44 Preparing to unpack .../17-libp11-kit0_0.25.5-3_amd64.deb ...
2026-Jan-01 21:37:22.406269
#23 27.45 Unpacking libp11-kit0:amd64 (0.25.5-3) ...
2026-Jan-01 21:37:22.485159
#23 27.68 Selecting previously unselected package libtasn1-6:amd64.
2026-Jan-01 21:37:22.590404
#23 27.68 Preparing to unpack .../18-libtasn1-6_4.20.0-2_amd64.deb ...
2026-Jan-01 21:37:22.590404
#23 27.68 Unpacking libtasn1-6:amd64 (4.20.0-2) ...
2026-Jan-01 21:37:22.590404
#23 27.78 Selecting previously unselected package libgnutls30t64:amd64.
2026-Jan-01 21:37:22.756974
#23 27.79 Preparing to unpack .../19-libgnutls30t64_3.8.9-3_amd64.deb ...
2026-Jan-01 21:37:22.756974
#23 27.79 Unpacking libgnutls30t64:amd64 (3.8.9-3) ...
2026-Jan-01 21:37:22.893949
#23 28.09 Selecting previously unselected package librtmp1:amd64.
2026-Jan-01 21:37:23.016910
#23 28.09 Preparing to unpack .../20-librtmp1_2.4+20151223.gitfa8646d.1-2+b5_amd64.deb ...
2026-Jan-01 21:37:23.016910
#23 28.10 Unpacking librtmp1:amd64 (2.4+20151223.gitfa8646d.1-2+b5) ...
2026-Jan-01 21:37:23.016910
#23 28.21 Selecting previously unselected package libssh2-1t64:amd64.
2026-Jan-01 21:37:23.160637
#23 28.22 Preparing to unpack .../21-libssh2-1t64_1.11.1-1_amd64.deb ...
2026-Jan-01 21:37:23.160637
#23 28.22 Unpacking libssh2-1t64:amd64 (1.11.1-1) ...
2026-Jan-01 21:37:23.160637
#23 28.36 Selecting previously unselected package libcurl4t64:amd64.
2026-Jan-01 21:37:23.326315
#23 28.36 Preparing to unpack .../22-libcurl4t64_8.14.1-2+deb13u2_amd64.deb ...
2026-Jan-01 21:37:23.326315
#23 28.37 Unpacking libcurl4t64:amd64 (8.14.1-2+deb13u2) ...
2026-Jan-01 21:37:23.356555
#23 28.55 Selecting previously unselected package curl.
2026-Jan-01 21:37:23.481771
#23 28.56 Preparing to unpack .../23-curl_8.14.1-2+deb13u2_amd64.deb ...
2026-Jan-01 21:37:23.481771
#23 28.56 Unpacking curl (8.14.1-2+deb13u2) ...
2026-Jan-01 21:37:23.481771
#23 28.68 Selecting previously unselected package libgpg-error0:amd64.
2026-Jan-01 21:37:23.616980
#23 28.69 Preparing to unpack .../24-libgpg-error0_1.51-4_amd64.deb ...
2026-Jan-01 21:37:23.640900
#23 28.70 Unpacking libgpg-error0:amd64 (1.51-4) ...
2026-Jan-01 21:37:23.640900
#23 28.81 Selecting previously unselected package libassuan9:amd64.
2026-Jan-01 21:37:23.720069
#23 28.82 Preparing to unpack .../25-libassuan9_3.0.2-2_amd64.deb ...
2026-Jan-01 21:37:23.731223
#23 28.82 Unpacking libassuan9:amd64 (3.0.2-2) ...
2026-Jan-01 21:37:23.731223
#23 28.91 Selecting previously unselected package libgcrypt20:amd64.
2026-Jan-01 21:37:23.731223
#23 28.92 Preparing to unpack .../26-libgcrypt20_1.11.0-7_amd64.deb ...
2026-Jan-01 21:37:23.854654
#23 28.92 Unpacking libgcrypt20:amd64 (1.11.0-7) ...
2026-Jan-01 21:37:23.854654
#23 29.05 Selecting previously unselected package gpgconf.
2026-Jan-01 21:37:23.974695
#23 29.05 Preparing to unpack .../27-gpgconf_2.4.7-21+b3_amd64.deb ...
2026-Jan-01 21:37:23.989538
#23 29.05 Unpacking gpgconf (2.4.7-21+b3) ...
2026-Jan-01 21:37:23.989538
#23 29.17 Selecting previously unselected package libksba8:amd64.
2026-Jan-01 21:37:24.132600
#23 29.17 Preparing to unpack .../28-libksba8_1.6.7-2+b1_amd64.deb ...
2026-Jan-01 21:37:24.132600
#23 29.18 Unpacking libksba8:amd64 (1.6.7-2+b1) ...
2026-Jan-01 21:37:24.170656
#23 29.36 Selecting previously unselected package libnpth0t64:amd64.
2026-Jan-01 21:37:24.292096
#23 29.37 Preparing to unpack .../29-libnpth0t64_1.8-3_amd64.deb ...
2026-Jan-01 21:37:24.292096
#23 29.37 Unpacking libnpth0t64:amd64 (1.8-3) ...
2026-Jan-01 21:37:24.292096
#23 29.49 Selecting previously unselected package dirmngr.
2026-Jan-01 21:37:24.292096
#23 29.49 Preparing to unpack .../30-dirmngr_2.4.7-21+b3_amd64.deb ...
2026-Jan-01 21:37:24.488194
#23 29.54 Unpacking dirmngr (2.4.7-21+b3) ...
2026-Jan-01 21:37:24.488194
#23 29.68 Selecting previously unselected package gnupg-l10n.
2026-Jan-01 21:37:24.647566
#23 29.69 Preparing to unpack .../31-gnupg-l10n_2.4.7-21_all.deb ...
2026-Jan-01 21:37:24.647566
#23 29.69 Unpacking gnupg-l10n (2.4.7-21) ...
2026-Jan-01 21:37:24.668095
#23 29.86 Selecting previously unselected package gpg.
2026-Jan-01 21:37:24.828523
#23 29.87 Preparing to unpack .../32-gpg_2.4.7-21+b3_amd64.deb ...
2026-Jan-01 21:37:24.828523
#23 29.87 Unpacking gpg (2.4.7-21+b3) ...
2026-Jan-01 21:37:24.858789
#23 30.05 Selecting previously unselected package pinentry-curses.
2026-Jan-01 21:37:24.997607
#23 30.05 Preparing to unpack .../33-pinentry-curses_1.3.1-2_amd64.deb ...
2026-Jan-01 21:37:24.997607
#23 30.06 Unpacking pinentry-curses (1.3.1-2) ...
2026-Jan-01 21:37:24.997607
#23 30.19 Selecting previously unselected package gpg-agent.
2026-Jan-01 21:37:25.096450
#23 30.19 Preparing to unpack .../34-gpg-agent_2.4.7-21+b3_amd64.deb ...
2026-Jan-01 21:37:25.096450
#23 30.19 Unpacking gpg-agent (2.4.7-21+b3) ...
2026-Jan-01 21:37:25.096450
#23 30.29 Selecting previously unselected package gpgsm.
2026-Jan-01 21:37:25.096450
#23 30.29 Preparing to unpack .../35-gpgsm_2.4.7-21+b3_amd64.deb ...
2026-Jan-01 21:37:25.242372
#23 30.30 Unpacking gpgsm (2.4.7-21+b3) ...
2026-Jan-01 21:37:25.242372
#23 30.44 Selecting previously unselected package gnupg.
2026-Jan-01 21:37:25.354172
#23 30.44 Preparing to unpack .../36-gnupg_2.4.7-21_all.deb ...
2026-Jan-01 21:37:25.354172
#23 30.45 Unpacking gnupg (2.4.7-21) ...
2026-Jan-01 21:37:25.354172
#23 30.55 Selecting previously unselected package gpg-wks-client.
2026-Jan-01 21:37:25.474647
#23 30.56 Preparing to unpack .../37-gpg-wks-client_2.4.7-21+b3_amd64.deb ...
2026-Jan-01 21:37:25.474647
#23 30.56 Unpacking gpg-wks-client (2.4.7-21+b3) ...
2026-Jan-01 21:37:25.474647
#23 30.67 Selecting previously unselected package gpgv.
2026-Jan-01 21:37:25.602853
#23 30.68 Preparing to unpack .../38-gpgv_2.4.7-21+b3_amd64.deb ...
2026-Jan-01 21:37:25.602853
#23 30.69 Unpacking gpgv (2.4.7-21+b3) ...
2026-Jan-01 21:37:25.602853
#23 30.80 Selecting previously unselected package libgpg-error-l10n.
2026-Jan-01 21:37:25.740608
#23 30.80 Preparing to unpack .../39-libgpg-error-l10n_1.51-4_all.deb ...
2026-Jan-01 21:37:25.740608
#23 30.81 Unpacking libgpg-error-l10n (1.51-4) ...
2026-Jan-01 21:37:25.740608
#23 30.93 Selecting previously unselected package libldap-common.
2026-Jan-01 21:37:25.872581
#23 30.94 Preparing to unpack .../40-libldap-common_2.6.10+dfsg-1_all.deb ...
2026-Jan-01 21:37:25.872581
#23 30.95 Unpacking libldap-common (2.6.10+dfsg-1) ...
2026-Jan-01 21:37:25.872581
#23 31.06 Selecting previously unselected package libsasl2-modules:amd64.
2026-Jan-01 21:37:25.872581
#23 31.06 Preparing to unpack .../41-libsasl2-modules_2.1.28+dfsg1-9_amd64.deb ...
2026-Jan-01 21:37:25.998645
#23 31.10 Unpacking libsasl2-modules:amd64 (2.1.28+dfsg1-9) ...
2026-Jan-01 21:37:25.998645
#23 31.19 Selecting previously unselected package publicsuffix.
2026-Jan-01 21:37:26.099945
#23 31.20 Preparing to unpack .../42-publicsuffix_20250328.1952-0.1_all.deb ...
2026-Jan-01 21:37:26.107933
#23 31.20 Unpacking publicsuffix (20250328.1952-0.1) ...
2026-Jan-01 21:37:26.107933
#23 31.30 Selecting previously unselected package gnupg-utils.
2026-Jan-01 21:37:26.269833
#23 31.31 Preparing to unpack .../43-gnupg-utils_2.4.7-21+b3_amd64.deb ...
2026-Jan-01 21:37:26.269833
#23 31.31 Unpacking gnupg-utils (2.4.7-21+b3) ...
2026-Jan-01 21:37:26.280366
#23 31.47 Setting up libnpth0t64:amd64 (1.8-3) ...
2026-Jan-01 21:37:26.384334
#23 31.49 Setting up libkeyutils1:amd64 (1.6.3-6) ...
2026-Jan-01 21:37:26.384334
#23 31.50 Setting up libgpg-error0:amd64 (1.51-4) ...
2026-Jan-01 21:37:26.384334
#23 31.51 Setting up libbrotli1:amd64 (1.1.0-2+b7) ...
2026-Jan-01 21:37:26.384334
#23 31.52 Setting up libsasl2-modules:amd64 (2.1.28+dfsg1-9) ...
2026-Jan-01 21:37:26.384334
#23 31.55 Setting up libnghttp2-14:amd64 (1.64.0-1.1) ...
2026-Jan-01 21:37:26.384334
#23 31.57 Setting up libgcrypt20:amd64 (1.11.0-7) ...
2026-Jan-01 21:37:26.384334
#23 31.58 Setting up krb5-locales (1.21.3-5) ...
2026-Jan-01 21:37:26.488452
#23 31.59 Setting up libcom-err2:amd64 (1.47.2-3+b3) ...
2026-Jan-01 21:37:26.488452
#23 31.60 Setting up libldap-common (2.6.10+dfsg-1) ...
2026-Jan-01 21:37:26.488452
#23 31.61 Setting up libkrb5support0:amd64 (1.21.3-5) ...
2026-Jan-01 21:37:26.488452
#23 31.62 Setting up libsasl2-modules-db:amd64 (2.1.28+dfsg1-9) ...
2026-Jan-01 21:37:26.488452
#23 31.63 Setting up gnupg-l10n (2.4.7-21) ...
2026-Jan-01 21:37:26.488452
#23 31.64 Setting up bash-completion (1:2.16.0-7) ...
2026-Jan-01 21:37:26.488452
#23 31.65 Setting up libp11-kit0:amd64 (0.25.5-3) ...
2026-Jan-01 21:37:26.488452
#23 31.66 Setting up libunistring5:amd64 (1.3-2) ...
2026-Jan-01 21:37:26.488452
#23 31.67 Setting up libk5crypto3:amd64 (1.21.3-5) ...
2026-Jan-01 21:37:26.488452
#23 31.68 Setting up libsasl2-2:amd64 (2.1.28+dfsg1-9) ...
2026-Jan-01 21:37:26.488452
#23 31.68 Setting up libnghttp3-9:amd64 (1.8.0-1) ...
2026-Jan-01 21:37:26.601876
#23 31.69 Setting up gpgv (2.4.7-21+b3) ...
2026-Jan-01 21:37:26.601876
#23 31.70 Setting up libassuan9:amd64 (3.0.2-2) ...
2026-Jan-01 21:37:26.601876
#23 31.70 Setting up gpgconf (2.4.7-21+b3) ...
2026-Jan-01 21:37:26.601876
#23 31.71 Setting up libtasn1-6:amd64 (4.20.0-2) ...
2026-Jan-01 21:37:26.601876
#23 31.72 Setting up libkrb5-3:amd64 (1.21.3-5) ...
2026-Jan-01 21:37:26.601876
#23 31.72 Setting up libssh2-1t64:amd64 (1.11.1-1) ...
2026-Jan-01 21:37:26.601876
#23 31.73 Setting up libgpg-error-l10n (1.51-4) ...
2026-Jan-01 21:37:26.601876
#23 31.74 Setting up publicsuffix (20250328.1952-0.1) ...
2026-Jan-01 21:37:26.601876
#23 31.74 Setting up libldap2:amd64 (2.6.10+dfsg-1) ...
2026-Jan-01 21:37:26.601876
#23 31.75 Setting up libksba8:amd64 (1.6.7-2+b1) ...
2026-Jan-01 21:37:26.601876
#23 31.76 Setting up pinentry-curses (1.3.1-2) ...
2026-Jan-01 21:37:26.601876
#23 31.79 Setting up gpg-agent (2.4.7-21+b3) ...
2026-Jan-01 21:37:27.481391
#23 32.68 Setting up gpgsm (2.4.7-21+b3) ...
2026-Jan-01 21:37:27.658457
#23 32.68 Setting up libidn2-0:amd64 (2.3.8-2) ...
2026-Jan-01 21:37:27.658457
#23 32.69 Setting up libgssapi-krb5-2:amd64 (1.21.3-5) ...
2026-Jan-01 21:37:27.658457
#23 32.70 Setting up gpg (2.4.7-21+b3) ...
2026-Jan-01 21:37:27.842371
#23 33.04 Setting up gnupg-utils (2.4.7-21+b3) ...
2026-Jan-01 21:37:28.022901
#23 33.05 Setting up libgnutls30t64:amd64 (3.8.9-3) ...
2026-Jan-01 21:37:28.022901
#23 33.05 Setting up libpsl5t64:amd64 (0.21.2-1.1+b1) ...
2026-Jan-01 21:37:28.022901
#23 33.07 Setting up dirmngr (2.4.7-21+b3) ...
2026-Jan-01 21:37:28.287237
#23 33.48 Setting up librtmp1:amd64 (2.4+20151223.gitfa8646d.1-2+b5) ...
2026-Jan-01 21:37:28.480258
#23 33.49 Setting up gnupg (2.4.7-21) ...
2026-Jan-01 21:37:28.480258
#23 33.50 Setting up gpg-wks-client (2.4.7-21+b3) ...
2026-Jan-01 21:37:28.480258
#23 33.50 Setting up libcurl4t64:amd64 (8.14.1-2+deb13u2) ...
2026-Jan-01 21:37:28.480258
#23 33.51 Setting up curl (8.14.1-2+deb13u2) ...
2026-Jan-01 21:37:28.480258
#23 33.52 Processing triggers for libc-bin (2.41-12) ...
2026-Jan-01 21:37:28.791888
#23 33.99 Hit:1 http://deb.debian.org/debian trixie InRelease
2026-Jan-01 21:37:28.945825
#23 33.99 Hit:2 http://deb.debian.org/debian trixie-updates InRelease
2026-Jan-01 21:37:28.945825
#23 33.99 Hit:3 http://deb.debian.org/debian-security trixie-security InRelease
2026-Jan-01 21:37:28.945825
#23 33.99 Get:4 https://download.docker.com/linux/debian trixie InRelease [32.5 kB]
2026-Jan-01 21:37:28.978930
#23 34.15 Get:5 https://download.docker.com/linux/debian trixie/stable amd64 Packages [23.2 kB]
2026-Jan-01 21:37:29.193331
#23 34.24 Fetched 55.7 kB in 0s (184 kB/s)
2026-Jan-01 21:37:29.193331
#23 34.24 Reading package lists...
2026-Jan-01 21:37:30.778682
2026-Jan-01 21:37:30.988815
#23 36.03 Reading package lists...
2026-Jan-01 21:37:31.966503
2026-Jan-01 21:37:32.135133
#23 37.18 Building dependency tree...
2026-Jan-01 21:37:32.269572
2026-Jan-01 21:37:32.426828
#23 37.47 Reading state information...
2026-Jan-01 21:37:32.643161
#23 37.84 The following additional packages will be installed:
2026-Jan-01 21:37:32.758896
#23 37.84   docker-buildx-plugin
2026-Jan-01 21:37:32.780272
#23 37.85 Suggested packages:
2026-Jan-01 21:37:32.780272
#23 37.85   docker-model-plugin
2026-Jan-01 21:37:32.780272
#23 37.96 The following NEW packages will be installed:
2026-Jan-01 21:37:32.780272
#23 37.96   docker-buildx-plugin docker-ce-cli docker-compose-plugin
2026-Jan-01 21:37:32.868018
#23 38.06 0 upgraded, 3 newly installed, 0 to remove and 0 not upgraded.
2026-Jan-01 21:37:32.868018
#23 38.06 Need to get 40.4 MB of archives.
2026-Jan-01 21:37:32.868018
#23 38.06 After this operation, 157 MB of additional disk space will be used.
2026-Jan-01 21:37:32.868018
#23 38.06 Get:1 https://download.docker.com/linux/debian trixie/stable amd64 docker-buildx-plugin amd64 0.30.1-1~debian.13~trixie [16.4 MB]
2026-Jan-01 21:37:33.186913
#23 38.38 Get:2 https://download.docker.com/linux/debian trixie/stable amd64 docker-ce-cli amd64 5:29.1.3-1~debian.13~trixie [16.3 MB]
2026-Jan-01 21:37:33.531822
#23 38.72 Get:3 https://download.docker.com/linux/debian trixie/stable amd64 docker-compose-plugin amd64 5.0.0-1~debian.13~trixie [7708 kB]
2026-Jan-01 21:37:33.990319
#23 39.18 debconf: unable to initialize frontend: Dialog
2026-Jan-01 21:37:34.169324
#23 39.18 debconf: (TERM is not set, so the dialog frontend is not usable.)
2026-Jan-01 21:37:34.169324
#23 39.18 debconf: falling back to frontend: Readline
2026-Jan-01 21:37:34.169324
#23 39.18 debconf: unable to initialize frontend: Readline
2026-Jan-01 21:37:34.169324
#23 39.18 debconf: (Can't locate Term/ReadLine.pm in @INC (you may need to install the Term::ReadLine module) (@INC entries checked: /etc/perl /usr/local/lib/x86_64-linux-gnu/perl/5.40.1 /usr/local/share/perl/5.40.1 /usr/lib/x86_64-linux-gnu/perl5/5.40 /usr/share/perl5 /usr/lib/x86_64-linux-gnu/perl-base /usr/lib/x86_64-linux-gnu/perl/5.40 /usr/share/perl/5.40 /usr/local/lib/site_perl) at /usr/share/perl5/Debconf/FrontEnd/Readline.pm line 8, <STDIN> line 3.)
2026-Jan-01 21:37:34.169324
#23 39.18 debconf: falling back to frontend: Teletype
2026-Jan-01 21:37:34.169324
#23 39.21 debconf: unable to initialize frontend: Teletype
2026-Jan-01 21:37:34.169324
#23 39.21 debconf: (This frontend requires a controlling tty.)
2026-Jan-01 21:37:34.169324
#23 39.21 debconf: falling back to frontend: Noninteractive
2026-Jan-01 21:37:35.790163
#23 40.99 Fetched 40.4 MB in 1s (45.8 MB/s)
2026-Jan-01 21:37:36.026710
#23 41.04 Selecting previously unselected package docker-buildx-plugin.
2026-Jan-01 21:37:36.026710
#23 41.04 (Reading database ... 
(Reading database ... 5%
(Reading database ... 10%
(Reading database ... 15%
(Reading database ... 20%
(Reading database ... 25%
(Reading database ... 30%
(Reading database ... 35%
(Reading database ... 40%
(Reading database ... 45%
(Reading database ... 50%
(Reading database ... 55%
(Reading database ... 60%
(Reading database ... 65%
(Reading database ... 70%
(Reading database ... 75%
(Reading database ... 80%
(Reading database ... 85%
(Reading database ... 90%
(Reading database ... 95%
(Reading database ... 100%
(Reading database ... 7297 files and directories currently installed.)
2026-Jan-01 21:37:36.026710
#23 41.07 Preparing to unpack .../docker-buildx-plugin_0.30.1-1~debian.13~trixie_amd64.deb ...
2026-Jan-01 21:37:36.026710
#23 41.07 Unpacking docker-buildx-plugin (0.30.1-1~debian.13~trixie) ...
2026-Jan-01 21:37:37.980674
#23 43.18 Selecting previously unselected package docker-ce-cli.
2026-Jan-01 21:37:38.146553
#23 43.19 Preparing to unpack .../docker-ce-cli_5%3a29.1.3-1~debian.13~trixie_amd64.deb ...
2026-Jan-01 21:37:38.146553
#23 43.19 Unpacking docker-ce-cli (5:29.1.3-1~debian.13~trixie) ...
2026-Jan-01 21:37:40.084629
#23 45.27 Selecting previously unselected package docker-compose-plugin.
2026-Jan-01 21:37:40.248626
#23 45.29 Preparing to unpack .../docker-compose-plugin_5.0.0-1~debian.13~trixie_amd64.deb ...
2026-Jan-01 21:37:40.248626
#23 45.29 Unpacking docker-compose-plugin (5.0.0-1~debian.13~trixie) ...
2026-Jan-01 21:37:41.641426
#23 46.84 Setting up docker-buildx-plugin (0.30.1-1~debian.13~trixie) ...
2026-Jan-01 21:37:41.661233
2026-Jan-01 21:37:41.826157
#23 46.85 Setting up docker-compose-plugin (5.0.0-1~debian.13~trixie) ...
2026-Jan-01 21:37:41.826157
#23 46.87 Setting up docker-ce-cli (5:29.1.3-1~debian.13~trixie) ...
2026-Jan-01 21:37:41.877184
#23 DONE 47.1s
2026-Jan-01 21:37:41.877184
2026-Jan-01 21:37:41.877184
#22 [dashboard deps 4/4] RUN npm install
2026-Jan-01 21:37:41.981339
#22 ...
2026-Jan-01 21:37:41.981339
2026-Jan-01 21:37:41.981339
#28 [api 4/7] COPY control-plane/api/requirements.txt .
2026-Jan-01 21:37:41.981339
#28 DONE 0.1s
2026-Jan-01 21:37:42.142830
2026-Jan-01 21:37:42.163953
#29 [api 5/7] RUN pip install -r requirements.txt
2026-Jan-01 21:37:45.596891
#29 3.599 Collecting fastapi (from -r requirements.txt (line 1))
2026-Jan-01 21:37:45.808710
#29 3.661   Downloading fastapi-0.128.0-py3-none-any.whl.metadata (30 kB)
2026-Jan-01 21:37:46.032233
#29 4.039 Collecting sqlalchemy (from -r requirements.txt (line 3))
2026-Jan-01 21:37:46.177302
#29 4.045   Downloading sqlalchemy-2.0.45-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (9.5 kB)
2026-Jan-01 21:37:46.191884
#29 4.185 Collecting psycopg2-binary (from -r requirements.txt (line 4))
2026-Jan-01 21:37:46.326315
#29 4.196   Downloading psycopg2_binary-2.9.11-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (4.9 kB)
2026-Jan-01 21:37:46.326315
#29 4.226 Collecting httpx (from -r requirements.txt (line 5))
2026-Jan-01 21:37:46.341066
#29 4.231   Downloading httpx-0.28.1-py3-none-any.whl.metadata (7.1 kB)
2026-Jan-01 21:37:46.341066
#29 4.272 Collecting python-keycloak (from -r requirements.txt (line 6))
2026-Jan-01 21:37:46.341066
#29 4.280   Downloading python_keycloak-6.0.0-py3-none-any.whl.metadata (6.1 kB)
2026-Jan-01 21:37:46.341066
#29 4.334 Collecting minio (from -r requirements.txt (line 7))
2026-Jan-01 21:37:46.460125
#29 4.340   Downloading minio-7.2.20-py3-none-any.whl.metadata (6.5 kB)
2026-Jan-01 21:37:46.460125
#29 4.404 Collecting requests (from -r requirements.txt (line 8))
2026-Jan-01 21:37:46.460125
#29 4.418   Downloading requests-2.32.5-py3-none-any.whl.metadata (4.9 kB)
2026-Jan-01 21:37:46.460125
#29 4.464 Collecting python-dotenv (from -r requirements.txt (line 9))
2026-Jan-01 21:37:46.559015
#29 4.468   Downloading python_dotenv-1.2.1-py3-none-any.whl.metadata (25 kB)
2026-Jan-01 21:37:46.559015
#29 4.566 Collecting bcrypt<4.1.0 (from -r requirements.txt (line 11))
2026-Jan-01 21:37:46.698626
#29 4.572   Downloading bcrypt-4.0.1-cp36-abi3-manylinux_2_28_x86_64.whl.metadata (9.0 kB)
2026-Jan-01 21:37:46.698626
#29 4.599 Collecting python-multipart (from -r requirements.txt (line 13))
2026-Jan-01 21:37:46.698626
#29 4.606   Downloading python_multipart-0.0.21-py3-none-any.whl.metadata (1.8 kB)
2026-Jan-01 21:37:46.698626
#29 4.699 Collecting stripe (from -r requirements.txt (line 14))
2026-Jan-01 21:37:46.852417
#29 4.707   Downloading stripe-14.1.0-py3-none-any.whl.metadata (18 kB)
2026-Jan-01 21:37:46.852417
#29 4.743 Collecting prometheus_client (from -r requirements.txt (line 15))
2026-Jan-01 21:37:46.852417
#29 4.750   Downloading prometheus_client-0.23.1-py3-none-any.whl.metadata (1.9 kB)
2026-Jan-01 21:37:46.852417
#29 4.789 Collecting APScheduler (from -r requirements.txt (line 16))
2026-Jan-01 21:37:46.852417
#29 4.794   Downloading apscheduler-3.11.2-py3-none-any.whl.metadata (6.4 kB)
2026-Jan-01 21:37:46.852417
#29 4.860 Collecting uvicorn[standard] (from -r requirements.txt (line 2))
2026-Jan-01 21:37:46.990682
#29 4.868   Downloading uvicorn-0.40.0-py3-none-any.whl.metadata (6.7 kB)
2026-Jan-01 21:37:47.010005
#29 4.896 Collecting passlib[bcrypt] (from -r requirements.txt (line 10))
2026-Jan-01 21:37:47.010005
#29 4.905   Downloading passlib-1.7.4-py2.py3-none-any.whl.metadata (1.7 kB)
2026-Jan-01 21:37:47.010005
#29 4.940 Collecting python-jose[cryptography] (from -r requirements.txt (line 12))
2026-Jan-01 21:37:47.010005
#29 4.948   Downloading python_jose-3.5.0-py2.py3-none-any.whl.metadata (5.5 kB)
2026-Jan-01 21:37:47.010005
#29 4.997 Collecting starlette<0.51.0,>=0.40.0 (from fastapi->-r requirements.txt (line 1))
2026-Jan-01 21:37:47.114295
#29 5.005   Downloading starlette-0.50.0-py3-none-any.whl.metadata (6.3 kB)
2026-Jan-01 21:37:47.114295
#29 5.122 Collecting pydantic>=2.7.0 (from fastapi->-r requirements.txt (line 1))
2026-Jan-01 21:37:47.241379
#29 5.132   Downloading pydantic-2.12.5-py3-none-any.whl.metadata (90 kB)
2026-Jan-01 21:37:47.241379
#29 5.164 Collecting typing-extensions>=4.8.0 (from fastapi->-r requirements.txt (line 1))
2026-Jan-01 21:37:47.241379
#29 5.171   Downloading typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
2026-Jan-01 21:37:47.241379
#29 5.193 Collecting annotated-doc>=0.0.2 (from fastapi->-r requirements.txt (line 1))
2026-Jan-01 21:37:47.241379
#29 5.202   Downloading annotated_doc-0.0.4-py3-none-any.whl.metadata (6.6 kB)
2026-Jan-01 21:37:47.241379
#29 5.245 Collecting click>=7.0 (from uvicorn[standard]->-r requirements.txt (line 2))
2026-Jan-01 21:37:47.345483
#29 5.250   Downloading click-8.3.1-py3-none-any.whl.metadata (2.6 kB)
2026-Jan-01 21:37:47.345483
#29 5.282 Collecting h11>=0.8 (from uvicorn[standard]->-r requirements.txt (line 2))
2026-Jan-01 21:37:47.345483
#29 5.294   Downloading h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
2026-Jan-01 21:37:47.345483
#29 5.343 Collecting httptools>=0.6.3 (from uvicorn[standard]->-r requirements.txt (line 2))
2026-Jan-01 21:37:47.345483
#29 5.352   Downloading httptools-0.7.1-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (3.5 kB)
2026-Jan-01 21:37:47.539637
#29 5.439 Collecting pyyaml>=5.1 (from uvicorn[standard]->-r requirements.txt (line 2))
2026-Jan-01 21:37:47.539637
#29 5.451   Downloading pyyaml-6.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.4 kB)
2026-Jan-01 21:37:47.539637
#29 5.547 Collecting uvloop>=0.15.1 (from uvicorn[standard]->-r requirements.txt (line 2))
2026-Jan-01 21:37:47.686176
#29 5.555   Downloading uvloop-0.22.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (4.9 kB)
2026-Jan-01 21:37:47.686176
#29 5.692 Collecting watchfiles>=0.13 (from uvicorn[standard]->-r requirements.txt (line 2))
2026-Jan-01 21:37:47.842968
#29 5.697   Downloading watchfiles-1.1.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.9 kB)
2026-Jan-01 21:37:47.878572
#29 5.881 Collecting websockets>=10.4 (from uvicorn[standard]->-r requirements.txt (line 2))
2026-Jan-01 21:37:48.029038
#29 5.886   Downloading websockets-15.0.1-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.8 kB)
2026-Jan-01 21:37:48.066304
#29 6.073 Collecting greenlet>=1 (from sqlalchemy->-r requirements.txt (line 3))
2026-Jan-01 21:37:48.207858
#29 6.079   Downloading greenlet-3.3.0-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (4.1 kB)
2026-Jan-01 21:37:48.207858
#29 6.144 Collecting anyio (from httpx->-r requirements.txt (line 5))
2026-Jan-01 21:37:48.207858
#29 6.158   Downloading anyio-4.12.0-py3-none-any.whl.metadata (4.3 kB)
2026-Jan-01 21:37:48.207858
#29 6.214 Collecting certifi (from httpx->-r requirements.txt (line 5))
2026-Jan-01 21:37:48.324606
#29 6.221   Downloading certifi-2025.11.12-py3-none-any.whl.metadata (2.5 kB)
2026-Jan-01 21:37:48.324606
#29 6.279 Collecting httpcore==1.* (from httpx->-r requirements.txt (line 5))
2026-Jan-01 21:37:48.324606
#29 6.286   Downloading httpcore-1.0.9-py3-none-any.whl.metadata (21 kB)
2026-Jan-01 21:37:48.324606
#29 6.332 Collecting idna (from httpx->-r requirements.txt (line 5))
2026-Jan-01 21:37:48.440727
#29 6.335   Downloading idna-3.11-py3-none-any.whl.metadata (8.4 kB)
2026-Jan-01 21:37:48.440727
#29 6.379 Collecting aiofiles>=24.1.0 (from python-keycloak->-r requirements.txt (line 6))
2026-Jan-01 21:37:48.440727
#29 6.386   Downloading aiofiles-25.1.0-py3-none-any.whl.metadata (6.3 kB)
2026-Jan-01 21:37:48.440727
#29 6.415 Collecting async-property>=0.2.2 (from python-keycloak->-r requirements.txt (line 6))
2026-Jan-01 21:37:48.440727
#29 6.422   Downloading async_property-0.2.2-py2.py3-none-any.whl.metadata (5.3 kB)
2026-Jan-01 21:37:48.440727
#29 6.445 Collecting deprecation>=2.1.0 (from python-keycloak->-r requirements.txt (line 6))
2026-Jan-01 21:37:48.580917
#29 6.452   Downloading deprecation-2.1.0-py2.py3-none-any.whl.metadata (4.6 kB)
2026-Jan-01 21:37:48.580917
#29 6.588 Collecting jwcrypto>=1.5.4 (from python-keycloak->-r requirements.txt (line 6))
2026-Jan-01 21:37:48.685856
#29 6.602   Downloading jwcrypto-1.5.6-py3-none-any.whl.metadata (3.1 kB)
2026-Jan-01 21:37:48.685856
#29 6.643 Collecting requests-toolbelt>=0.6.0 (from python-keycloak->-r requirements.txt (line 6))
2026-Jan-01 21:37:48.685856
#29 6.648   Downloading requests_toolbelt-1.0.0-py2.py3-none-any.whl.metadata (14 kB)
2026-Jan-01 21:37:48.685856
#29 6.690 Collecting argon2-cffi (from minio->-r requirements.txt (line 7))
2026-Jan-01 21:37:48.830322
#29 6.700   Downloading argon2_cffi-25.1.0-py3-none-any.whl.metadata (4.1 kB)
2026-Jan-01 21:37:48.830322
#29 6.838 Collecting pycryptodome (from minio->-r requirements.txt (line 7))
2026-Jan-01 21:37:49.050215
#29 6.851   Downloading pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (3.4 kB)
2026-Jan-01 21:37:49.050215
#29 6.900 Collecting urllib3 (from minio->-r requirements.txt (line 7))
2026-Jan-01 21:37:49.050215
#29 6.907   Downloading urllib3-2.6.2-py3-none-any.whl.metadata (6.6 kB)
2026-Jan-01 21:37:49.073365
#29 7.082 Collecting charset_normalizer<4,>=2 (from requests->-r requirements.txt (line 8))
2026-Jan-01 21:37:49.214452
#29 7.091   Downloading charset_normalizer-3.4.4-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (37 kB)
2026-Jan-01 21:37:49.214452
#29 7.172 Collecting ecdsa!=0.15 (from python-jose[cryptography]->-r requirements.txt (line 12))
2026-Jan-01 21:37:49.214452
#29 7.180   Downloading ecdsa-0.19.1-py2.py3-none-any.whl.metadata (29 kB)
2026-Jan-01 21:37:49.214452
#29 7.221 Collecting rsa!=4.1.1,!=4.4,<5.0,>=4.0 (from python-jose[cryptography]->-r requirements.txt (line 12))
2026-Jan-01 21:37:49.422509
#29 7.227   Downloading rsa-4.9.1-py3-none-any.whl.metadata (5.6 kB)
2026-Jan-01 21:37:49.422509
#29 7.273 Collecting pyasn1>=0.5.0 (from python-jose[cryptography]->-r requirements.txt (line 12))
2026-Jan-01 21:37:49.422509
#29 7.276   Downloading pyasn1-0.6.1-py3-none-any.whl.metadata (8.4 kB)
2026-Jan-01 21:37:49.467088
#29 7.474 Collecting cryptography>=3.4.0 (from python-jose[cryptography]->-r requirements.txt (line 12))
2026-Jan-01 21:37:49.676192
#29 7.481   Downloading cryptography-46.0.3-cp311-abi3-manylinux_2_34_x86_64.whl.metadata (5.7 kB)
2026-Jan-01 21:37:49.676192
#29 7.525 Collecting tzlocal>=3.0 (from APScheduler->-r requirements.txt (line 16))
2026-Jan-01 21:37:49.676192
#29 7.531   Downloading tzlocal-5.3.1-py3-none-any.whl.metadata (7.6 kB)
2026-Jan-01 21:37:49.858584
#29 7.862 Collecting cffi>=2.0.0 (from cryptography>=3.4.0->python-jose[cryptography]->-r requirements.txt (line 12))
2026-Jan-01 21:37:50.008801
#29 7.876   Downloading cffi-2.0.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (2.6 kB)
2026-Jan-01 21:37:50.008801
#29 7.929 Collecting packaging (from deprecation>=2.1.0->python-keycloak->-r requirements.txt (line 6))
2026-Jan-01 21:37:50.008801
#29 7.938   Downloading packaging-25.0-py3-none-any.whl.metadata (3.3 kB)
2026-Jan-01 21:37:50.008801
#29 8.012 Collecting six>=1.9.0 (from ecdsa!=0.15->python-jose[cryptography]->-r requirements.txt (line 12))
2026-Jan-01 21:37:50.218810
#29 8.024   Downloading six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
2026-Jan-01 21:37:50.218810
#29 8.069 Collecting annotated-types>=0.6.0 (from pydantic>=2.7.0->fastapi->-r requirements.txt (line 1))
2026-Jan-01 21:37:50.218810
#29 8.075   Downloading annotated_types-0.7.0-py3-none-any.whl.metadata (15 kB)
2026-Jan-01 21:37:51.078581
#29 9.086 Collecting pydantic-core==2.41.5 (from pydantic>=2.7.0->fastapi->-r requirements.txt (line 1))
2026-Jan-01 21:37:51.091120
2026-Jan-01 21:37:51.203507
#29 9.095   Downloading pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (7.3 kB)
2026-Jan-01 21:37:51.203507
#29 9.122 Collecting typing-inspection>=0.4.2 (from pydantic>=2.7.0->fastapi->-r requirements.txt (line 1))
2026-Jan-01 21:37:51.220541
#29 9.127   Downloading typing_inspection-0.4.2-py3-none-any.whl.metadata (2.6 kB)
2026-Jan-01 21:37:51.220541
#29 9.209 Collecting argon2-cffi-bindings (from argon2-cffi->minio->-r requirements.txt (line 7))
2026-Jan-01 21:37:51.308574
#29 9.215   Downloading argon2_cffi_bindings-25.1.0-cp39-abi3-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl.metadata (7.4 kB)
2026-Jan-01 21:37:51.327843
#29 9.261 Collecting pycparser (from cffi>=2.0.0->cryptography>=3.4.0->python-jose[cryptography]->-r requirements.txt (line 12))
2026-Jan-01 21:37:51.327843
#29 9.270   Downloading pycparser-2.23-py3-none-any.whl.metadata (993 bytes)
2026-Jan-01 21:37:51.327843
#29 9.314 Downloading fastapi-0.128.0-py3-none-any.whl (103 kB)
2026-Jan-01 21:37:51.423327
#29 9.334 Downloading sqlalchemy-2.0.45-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (3.3 MB)
2026-Jan-01 21:37:51.423327
#29 9.410    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.3/3.3 MB 49.3 MB/s eta 0:00:00
2026-Jan-01 21:37:51.423327
#29 9.428 Downloading psycopg2_binary-2.9.11-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (4.2 MB)
2026-Jan-01 21:37:51.526156
#29 9.518    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.2/4.2 MB 51.1 MB/s eta 0:00:00
2026-Jan-01 21:37:51.526156
#29 9.524 Downloading httpx-0.28.1-py3-none-any.whl (73 kB)
2026-Jan-01 21:37:51.526156
#29 9.534 Downloading httpcore-1.0.9-py3-none-any.whl (78 kB)
2026-Jan-01 21:37:51.649306
#29 9.587 Downloading python_keycloak-6.0.0-py3-none-any.whl (80 kB)
2026-Jan-01 21:37:51.649306
#29 9.601 Downloading minio-7.2.20-py3-none-any.whl (93 kB)
2026-Jan-01 21:37:51.649306
#29 9.615 Downloading requests-2.32.5-py3-none-any.whl (64 kB)
2026-Jan-01 21:37:51.649306
#29 9.631 Downloading python_dotenv-1.2.1-py3-none-any.whl (21 kB)
2026-Jan-01 21:37:51.649306
#29 9.654 Downloading bcrypt-4.0.1-cp36-abi3-manylinux_2_28_x86_64.whl (593 kB)
2026-Jan-01 21:37:51.761642
#29 9.684    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 593.7/593.7 kB 23.1 MB/s eta 0:00:00
2026-Jan-01 21:37:51.761642
#29 9.691 Downloading python_multipart-0.0.21-py3-none-any.whl (24 kB)
2026-Jan-01 21:37:51.761642
#29 9.705 Downloading stripe-14.1.0-py3-none-any.whl (2.1 MB)
2026-Jan-01 21:37:51.761642
#29 9.748    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 59.7 MB/s eta 0:00:00
2026-Jan-01 21:37:51.761642
#29 9.751 Downloading prometheus_client-0.23.1-py3-none-any.whl (61 kB)
2026-Jan-01 21:37:51.761642
#29 9.769 Downloading apscheduler-3.11.2-py3-none-any.whl (64 kB)
2026-Jan-01 21:37:51.866099
#29 9.782 Downloading aiofiles-25.1.0-py3-none-any.whl (14 kB)
2026-Jan-01 21:37:51.886518
#29 9.802 Downloading annotated_doc-0.0.4-py3-none-any.whl (5.3 kB)
2026-Jan-01 21:37:51.886518
#29 9.815 Downloading async_property-0.2.2-py2.py3-none-any.whl (9.5 kB)
2026-Jan-01 21:37:51.886518
#29 9.829 Downloading certifi-2025.11.12-py3-none-any.whl (159 kB)
2026-Jan-01 21:37:51.886518
#29 9.842 Downloading charset_normalizer-3.4.4-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (153 kB)
2026-Jan-01 21:37:51.886518
#29 9.859 Downloading click-8.3.1-py3-none-any.whl (108 kB)
2026-Jan-01 21:37:51.886518
#29 9.873 Downloading cryptography-46.0.3-cp311-abi3-manylinux_2_34_x86_64.whl (4.5 MB)
2026-Jan-01 21:37:51.993487
#29 10.00    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.5/4.5 MB 36.7 MB/s eta 0:00:00
2026-Jan-01 21:37:52.114778
#29 10.01 Downloading deprecation-2.1.0-py2.py3-none-any.whl (11 kB)
2026-Jan-01 21:37:52.144858
#29 10.03 Downloading ecdsa-0.19.1-py2.py3-none-any.whl (150 kB)
2026-Jan-01 21:37:52.144858
#29 10.05 Downloading greenlet-3.3.0-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (609 kB)
2026-Jan-01 21:37:52.144858
#29 10.07    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 609.9/609.9 kB 29.8 MB/s eta 0:00:00
2026-Jan-01 21:37:52.144858
#29 10.09 Downloading h11-0.16.0-py3-none-any.whl (37 kB)
2026-Jan-01 21:37:52.144858
#29 10.12 Downloading httptools-0.7.1-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (517 kB)
2026-Jan-01 21:37:52.213939
#29 10.14 Downloading idna-3.11-py3-none-any.whl (71 kB)
2026-Jan-01 21:37:52.213939
#29 10.16 Downloading jwcrypto-1.5.6-py3-none-any.whl (92 kB)
2026-Jan-01 21:37:52.213939
#29 10.18 Downloading pyasn1-0.6.1-py3-none-any.whl (83 kB)
2026-Jan-01 21:37:52.213939
#29 10.19 Downloading pydantic-2.12.5-py3-none-any.whl (463 kB)
2026-Jan-01 21:37:52.213939
#29 10.22 Downloading pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.1 MB)
2026-Jan-01 21:37:52.317450
#29 10.26    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 60.4 MB/s eta 0:00:00
2026-Jan-01 21:37:52.331707
#29 10.27 Downloading pyyaml-6.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (807 kB)
2026-Jan-01 21:37:52.331707
#29 10.29    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 807.9/807.9 kB 37.1 MB/s eta 0:00:00
2026-Jan-01 21:37:52.331707
#29 10.29 Downloading requests_toolbelt-1.0.0-py2.py3-none-any.whl (54 kB)
2026-Jan-01 21:37:52.331707
#29 10.30 Downloading rsa-4.9.1-py3-none-any.whl (34 kB)
2026-Jan-01 21:37:52.331707
#29 10.31 Downloading starlette-0.50.0-py3-none-any.whl (74 kB)
2026-Jan-01 21:37:52.331707
#29 10.32 Downloading anyio-4.12.0-py3-none-any.whl (113 kB)
2026-Jan-01 21:37:52.467255
#29 10.34 Downloading typing_extensions-4.15.0-py3-none-any.whl (44 kB)
2026-Jan-01 21:37:52.467255
#29 10.35 Downloading tzlocal-5.3.1-py3-none-any.whl (18 kB)
2026-Jan-01 21:37:52.467255
#29 10.36 Downloading urllib3-2.6.2-py3-none-any.whl (131 kB)
2026-Jan-01 21:37:52.467255
#29 10.38 Downloading uvloop-0.22.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (4.4 MB)
2026-Jan-01 21:37:52.467255
#29 10.47    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.4/4.4 MB 48.4 MB/s eta 0:00:00
2026-Jan-01 21:37:52.623831
#29 10.49 Downloading watchfiles-1.1.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (456 kB)
2026-Jan-01 21:37:52.623831
#29 10.51 Downloading websockets-15.0.1-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (182 kB)
2026-Jan-01 21:37:52.623831
#29 10.52 Downloading argon2_cffi-25.1.0-py3-none-any.whl (14 kB)
2026-Jan-01 21:37:52.623831
#29 10.53 Downloading passlib-1.7.4-py2.py3-none-any.whl (525 kB)
2026-Jan-01 21:37:52.623831
#29 10.54    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 525.6/525.6 kB 44.8 MB/s eta 0:00:00
2026-Jan-01 21:37:52.623831
#29 10.56 Downloading pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.3 MB)
2026-Jan-01 21:37:52.623831
#29 10.63    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.3/2.3 MB 32.8 MB/s eta 0:00:00
2026-Jan-01 21:37:52.743921
#29 10.65 Downloading python_jose-3.5.0-py2.py3-none-any.whl (34 kB)
2026-Jan-01 21:37:52.743921
#29 10.66 Downloading uvicorn-0.40.0-py3-none-any.whl (68 kB)
2026-Jan-01 21:37:52.743921
#29 10.67 Downloading annotated_types-0.7.0-py3-none-any.whl (13 kB)
2026-Jan-01 21:37:52.743921
#29 10.69 Downloading cffi-2.0.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (219 kB)
2026-Jan-01 21:37:52.743921
#29 10.70 Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
2026-Jan-01 21:37:52.743921
#29 10.73 Downloading typing_inspection-0.4.2-py3-none-any.whl (14 kB)
2026-Jan-01 21:37:52.743921
#29 10.75 Downloading argon2_cffi_bindings-25.1.0-cp39-abi3-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl (87 kB)
2026-Jan-01 21:37:52.923870
#29 10.77 Downloading packaging-25.0-py3-none-any.whl (66 kB)
2026-Jan-01 21:37:52.923870
#29 10.78 Downloading pycparser-2.23-py3-none-any.whl (118 kB)
2026-Jan-01 21:37:53.193139
#29 11.20 Installing collected packages: passlib, async-property, websockets, uvloop, urllib3, tzlocal, typing-extensions, six, pyyaml, python-multipart, python-dotenv, pycryptodome, pycparser, pyasn1, psycopg2-binary, prometheus_client, packaging, idna, httptools, h11, greenlet, click, charset_normalizer, certifi, bcrypt, annotated-types, annotated-doc, aiofiles, uvicorn, typing-inspection, sqlalchemy, rsa, requests, pydantic-core, httpcore, ecdsa, deprecation, cffi, APScheduler, anyio, watchfiles, stripe, starlette, requests-toolbelt, python-jose, pydantic, httpx, cryptography, argon2-cffi-bindings, jwcrypto, fastapi, argon2-cffi, python-keycloak, minio
2026-Jan-01 21:38:05.202213
#29 23.21 Successfully installed APScheduler-3.11.2 aiofiles-25.1.0 annotated-doc-0.0.4 annotated-types-0.7.0 anyio-4.12.0 argon2-cffi-25.1.0 argon2-cffi-bindings-25.1.0 async-property-0.2.2 bcrypt-4.0.1 certifi-2025.11.12 cffi-2.0.0 charset_normalizer-3.4.4 click-8.3.1 cryptography-46.0.3 deprecation-2.1.0 ecdsa-0.19.1 fastapi-0.128.0 greenlet-3.3.0 h11-0.16.0 httpcore-1.0.9 httptools-0.7.1 httpx-0.28.1 idna-3.11 jwcrypto-1.5.6 minio-7.2.20 packaging-25.0 passlib-1.7.4 prometheus_client-0.23.1 psycopg2-binary-2.9.11 pyasn1-0.6.1 pycparser-2.23 pycryptodome-3.23.0 pydantic-2.12.5 pydantic-core-2.41.5 python-dotenv-1.2.1 python-jose-3.5.0 python-keycloak-6.0.0 python-multipart-0.0.21 pyyaml-6.0.3 requests-2.32.5 requests-toolbelt-1.0.0 rsa-4.9.1 six-1.17.0 sqlalchemy-2.0.45 starlette-0.50.0 stripe-14.1.0 typing-extensions-4.15.0 typing-inspection-0.4.2 tzlocal-5.3.1 urllib3-2.6.2 uvicorn-0.40.0 uvloop-0.22.1 watchfiles-1.1.1 websockets-15.0.1
2026-Jan-01 21:38:05.355514
#29 23.21 WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager, possibly rendering your system unusable. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv. Use the --root-user-action option if you know what you are doing and want to suppress this warning.
2026-Jan-01 21:38:05.382939
#29 23.39
2026-Jan-01 21:38:05.382939
#29 23.39 [notice] A new release of pip is available: 25.0.1 -> 25.3
2026-Jan-01 21:38:05.382939
#29 23.39 [notice] To update, run: pip install --upgrade pip
2026-Jan-01 21:38:06.243258
#29 DONE 24.2s
2026-Jan-01 21:38:06.243258
2026-Jan-01 21:38:06.243258
#22 [dashboard deps 4/4] RUN npm install
2026-Jan-01 21:38:06.382673
#22 ...
2026-Jan-01 21:38:06.382673
2026-Jan-01 21:38:06.382673
#30 [api 6/7] COPY control-plane/api/src ./src
2026-Jan-01 21:38:06.382673
#30 DONE 0.1s
2026-Jan-01 21:38:06.625640
#31 [api 7/7] COPY data-plane/project-template ./data-plane/project-template
2026-Jan-01 21:38:06.625640
#31 DONE 0.1s
2026-Jan-01 21:38:06.625640
2026-Jan-01 21:38:06.625640
#32 [api] exporting to image
2026-Jan-01 21:38:06.625640
#32 exporting layers
2026-Jan-01 21:38:08.260722
#32 ...
2026-Jan-01 21:38:08.260722
2026-Jan-01 21:38:08.260722
#22 [dashboard deps 4/4] RUN npm install
2026-Jan-01 21:38:08.260722
#22 72.52
2026-Jan-01 21:38:08.260722
#22 72.52 added 574 packages, and audited 575 packages in 1m
2026-Jan-01 21:38:08.260722
#22 72.52
2026-Jan-01 21:38:08.260722
#22 72.52 238 packages are looking for funding
2026-Jan-01 21:38:08.260722
#22 72.52   run `npm fund` for details
2026-Jan-01 21:38:08.260722
#22 72.52
2026-Jan-01 21:38:08.260722
#22 72.52 found 0 vulnerabilities
2026-Jan-01 21:38:08.260722
#22 72.52 npm notice
2026-Jan-01 21:38:08.260722
#22 72.52 npm notice New major version of npm available! 10.8.2 -> 11.7.0
2026-Jan-01 21:38:08.260722
#22 72.52 npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.7.0
2026-Jan-01 21:38:08.260722
#22 72.52 npm notice To update run: npm install -g npm@11.7.0
2026-Jan-01 21:38:08.260722
#22 72.52 npm notice
2026-Jan-01 21:38:08.260722
#22 DONE 73.1s
2026-Jan-01 21:38:08.421534
#32 [api] exporting to image
2026-Jan-01 21:38:10.479731
#32 exporting layers 4.0s done
2026-Jan-01 21:38:10.479731
#32 writing image sha256:843fb580d6ead6849a8e9c741d72dd251f0f9a47ac071c389e49ab1b95c3e92c
2026-Jan-01 21:38:10.596906
#32 writing image sha256:843fb580d6ead6849a8e9c741d72dd251f0f9a47ac071c389e49ab1b95c3e92c done
2026-Jan-01 21:38:10.596906
#32 naming to docker.io/library/sokwws8k80wcg0gss0k0goww-api done
2026-Jan-01 21:38:10.596906
#32 DONE 4.0s
2026-Jan-01 21:38:10.596906
2026-Jan-01 21:38:10.596906
#33 [api] resolving provenance for metadata file
2026-Jan-01 21:38:10.761184
#33 DONE 0.0s
2026-Jan-01 21:38:18.469731
#34 [dashboard builder 3/6] COPY --from=deps /app/node_modules ./node_modules
2026-Jan-01 21:38:33.331321
#34 DONE 14.9s
2026-Jan-01 21:38:33.498855
#35 [dashboard builder 4/6] COPY dashboard/ .
2026-Jan-01 21:38:33.755096
#35 DONE 0.4s
2026-Jan-01 21:38:34.004795
#36 [dashboard builder 5/6] COPY docs/ /docs/
2026-Jan-01 21:38:34.004795
#36 DONE 0.1s
2026-Jan-01 21:38:34.004795
2026-Jan-01 21:38:34.004795
#37 [dashboard builder 6/6] RUN npm run build
2026-Jan-01 21:38:35.178676
#37 1.326
2026-Jan-01 21:38:35.178676
#37 1.326 > dashboard@0.1.0 build
2026-Jan-01 21:38:35.178676
#37 1.326 > next build
2026-Jan-01 21:38:35.178676
#37 1.326
2026-Jan-01 21:38:36.240399
#37 2.390 Attention: Next.js now collects completely anonymous telemetry regarding usage.
2026-Jan-01 21:38:36.260005
2026-Jan-01 21:38:36.400526
#37 2.392 This information is used to shape Next.js' roadmap and prioritize features.
2026-Jan-01 21:38:36.400526
#37 2.392 You can learn more, including how to opt-out if you'd not like to participate in this anonymous program, by visiting the following URL:
2026-Jan-01 21:38:36.400526
#37 2.392 https://nextjs.org/telemetry
2026-Jan-01 21:38:36.400526
#37 2.392
2026-Jan-01 21:38:36.400526
#37 2.419 ▲ Next.js 16.1.0 (Turbopack)
2026-Jan-01 21:38:36.400526
#37 2.419
2026-Jan-01 21:38:36.400526
#37 2.549   Creating an optimized production build ...
2026-Jan-01 21:39:05.623732
#37 31.77 ✓ Compiled successfully in 28.5s
2026-Jan-01 21:39:05.798569
#37 31.80   Running TypeScript ...
2026-Jan-01 21:39:20.075941
#37 46.22   Collecting page data using 1 worker ...
2026-Jan-01 21:39:20.810245
#37 46.96   Generating static pages using 1 worker (0/12) ...
2026-Jan-01 21:39:21.171629
#37 47.32   Generating static pages using 1 worker (3/12)
2026-Jan-01 21:39:21.171629
#37 47.32   Generating static pages using 1 worker (6/12)
2026-Jan-01 21:39:21.272358
#37 47.41   Generating static pages using 1 worker (9/12)
2026-Jan-01 21:39:21.272358
#37 47.41 ✓ Generating static pages using 1 worker (12/12) in 454.7ms
2026-Jan-01 21:39:21.272358
#37 47.42   Finalizing page optimization ...
2026-Jan-01 21:39:21.436940
#37 47.43
2026-Jan-01 21:39:21.436940
#37 47.44 Route (app)
2026-Jan-01 21:39:21.436940
#37 47.44 ┌ ○ /
2026-Jan-01 21:39:21.436940
#37 47.44 ├ ○ /_not-found
2026-Jan-01 21:39:21.436940
#37 47.44 ├ ○ /docs
2026-Jan-01 21:39:21.436940
#37 47.44 ├ ƒ /docs/[slug]
2026-Jan-01 21:39:21.436940
#37 47.44 ├ ○ /login
2026-Jan-01 21:39:21.436940
#37 47.44 ├ ○ /org
2026-Jan-01 21:39:21.436940
#37 47.44 ├ ƒ /org/[orgId]/billing
2026-Jan-01 21:39:21.436940
#37 47.44 ├ ƒ /org/[orgId]/projects
2026-Jan-01 21:39:21.436940
#37 47.44 ├ ƒ /org/[orgId]/projects/new
2026-Jan-01 21:39:21.436940
#37 47.44 ├ ƒ /org/[orgId]/settings
2026-Jan-01 21:39:21.436940
#37 47.44 ├ ƒ /org/[orgId]/team
2026-Jan-01 21:39:21.436940
#37 47.44 ├ ○ /projects
2026-Jan-01 21:39:21.436940
#37 47.44 ├ ƒ /projects/[id]
2026-Jan-01 21:39:21.436940
#37 47.44 ├ ƒ /projects/[id]/auth
2026-Jan-01 21:39:21.436940
#37 47.44 ├ ƒ /projects/[id]/backups
2026-Jan-01 21:39:21.436940
#37 47.44 ├ ƒ /projects/[id]/database
2026-Jan-01 21:39:21.436940
#37 47.44 ├ ƒ /projects/[id]/database/[table]
2026-Jan-01 21:39:21.436940
#37 47.44 ├ ƒ /projects/[id]/edge-functions
2026-Jan-01 21:39:21.436940
#37 47.44 ├ ƒ /projects/[id]/logs
2026-Jan-01 21:39:21.436940
#37 47.44 ├ ƒ /projects/[id]/realtime
2026-Jan-01 21:39:21.436940
#37 47.44 ├ ƒ /projects/[id]/secrets
2026-Jan-01 21:39:21.436940
#37 47.44 ├ ƒ /projects/[id]/settings
2026-Jan-01 21:39:21.436940
#37 47.44 ├ ƒ /projects/[id]/settings/deployment
2026-Jan-01 21:39:21.436940
#37 47.44 ├ ƒ /projects/[id]/sql
2026-Jan-01 21:39:21.436940
#37 47.44 ├ ƒ /projects/[id]/storage
2026-Jan-01 21:39:21.436940
#37 47.44 ├ ƒ /projects/[id]/users
2026-Jan-01 21:39:21.436940
#37 47.44 ├ ○ /projects/new
2026-Jan-01 21:39:21.436940
#37 47.44 ├ ○ /settings/organization
2026-Jan-01 21:39:21.436940
#37 47.44 ├ ƒ /settings/organization/[id]
2026-Jan-01 21:39:21.436940
#37 47.44 ├ ○ /settings/profile
2026-Jan-01 21:39:21.436940
#37 47.44 └ ○ /signup
2026-Jan-01 21:39:21.436940
#37 47.44
2026-Jan-01 21:39:21.436940
#37 47.44
2026-Jan-01 21:39:21.436940
#37 47.44 ○  (Static)   prerendered as static content
2026-Jan-01 21:39:21.436940
#37 47.44 ƒ  (Dynamic)  server-rendered on demand
2026-Jan-01 21:39:21.436940
#37 47.44
2026-Jan-01 21:39:21.486463
#37 47.63 npm notice
2026-Jan-01 21:39:21.486463
#37 47.63 npm notice New major version of npm available! 10.8.2 -> 11.7.0
2026-Jan-01 21:39:21.486463
#37 47.63 npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.7.0
2026-Jan-01 21:39:21.486463
#37 47.63 npm notice To update run: npm install -g npm@11.7.0
2026-Jan-01 21:39:21.486463
#37 47.63 npm notice
2026-Jan-01 21:39:21.705817
#37 DONE 47.7s
2026-Jan-01 21:39:27.843745
#38 [dashboard runner 3/6] COPY --from=builder /app/public ./public
2026-Jan-01 21:39:28.022801
#38 DONE 0.0s
2026-Jan-01 21:39:28.030851
#39 [dashboard runner 4/6] COPY --from=builder /app/.next ./.next
2026-Jan-01 21:39:28.030851
#39 DONE 0.2s
2026-Jan-01 21:39:28.186573
#40 [dashboard runner 5/6] COPY --from=builder /app/node_modules ./node_modules
2026-Jan-01 21:39:35.524820
#40 DONE 7.5s
2026-Jan-01 21:39:35.721898
#41 [dashboard runner 6/6] COPY --from=builder /app/package.json ./package.json
2026-Jan-01 21:39:35.721898
#41 DONE 0.0s
2026-Jan-01 21:39:35.721898
2026-Jan-01 21:39:35.721898
#42 [dashboard] exporting to image
2026-Jan-01 21:39:35.721898
#42 exporting layers
2026-Jan-01 21:39:45.562685
#42 exporting layers 10.0s done
2026-Jan-01 21:39:45.677034
#42 writing image sha256:b18690147e5d2f457248459c51840dc6485ff04a214217c6d0fea90c16252b37 done
2026-Jan-01 21:39:45.677034
#42 naming to docker.io/library/sokwws8k80wcg0gss0k0goww-dashboard done
2026-Jan-01 21:39:45.677034
#42 DONE 10.0s
2026-Jan-01 21:39:45.700743
#43 [dashboard] resolving provenance for metadata file
2026-Jan-01 21:39:45.700743
#43 DONE 0.0s
2026-Jan-01 21:39:45.708774
shared-gateway-v3  Built
2026-Jan-01 21:39:45.708774
dashboard  Built
2026-Jan-01 21:39:45.708774
api  Built
2026-Jan-01 21:39:45.761244
Creating .env file with runtime variables for build phase.
2026-Jan-01 21:39:46.127497
[CMD]: docker exec l0oso884kogw04wsgscwog0c bash -c 'cat /artifacts/l0oso884kogw04wsgscwog0c/.env'
2026-Jan-01 21:39:46.127497
SOURCE_COMMIT=38afe497310dc3044746949a4ac89c1fcfb200b7
2026-Jan-01 21:39:46.127497
COOLIFY_URL=
2026-Jan-01 21:39:46.127497
COOLIFY_FQDN=
2026-Jan-01 21:39:46.127497
SERVICE_NAME_CONTROL-PLANE-DB=control-plane-db
2026-Jan-01 21:39:46.127497
SERVICE_NAME_API=api
2026-Jan-01 21:39:46.127497
SERVICE_NAME_DASHBOARD=dashboard
2026-Jan-01 21:39:46.127497
SERVICE_NAME_KEYCLOAK=keycloak
2026-Jan-01 21:39:46.127497
SERVICE_NAME_MINIO=minio
2026-Jan-01 21:39:46.127497
SERVICE_NAME_SHARED-POSTGRES=shared-postgres
2026-Jan-01 21:39:46.127497
SERVICE_NAME_SHARED-GATEWAY-V3=shared-gateway-v3
2026-Jan-01 21:39:46.127497
SERVICE_NAME_SHARED-AUTH=shared-auth
2026-Jan-01 21:39:46.127497
SERVICE_NAME_SHARED-API=shared-api
2026-Jan-01 21:39:46.127497
SERVICE_NAME_SHARED-STORAGE=shared-storage
2026-Jan-01 21:39:46.127497
SERVICE_NAME_SHARED-REALTIME=shared-realtime
2026-Jan-01 21:39:46.127497
POSTGRES_USER=platform
2026-Jan-01 21:39:46.127497
POSTGRES_PASSWORD=platform
2026-Jan-01 21:39:46.127497
POSTGRES_DB=control_plane
2026-Jan-01 21:39:46.127497
KEYCLOAK_ADMIN_USER=admin
2026-Jan-01 21:39:46.127497
KEYCLOAK_ADMIN_PASSWORD=admin
2026-Jan-01 21:39:46.127497
MINIO_ROOT_PASSWORD=minioadmin
2026-Jan-01 21:39:46.127497
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8000,https://supalove.hayataxi.online,https://api.hayataxi.online
2026-Jan-01 21:39:46.127497
URL=http://localhost:8000
2026-Jan-01 21:39:46.127497
SHARED_POSTGRES_PASSWORD=postgres
2026-Jan-01 21:39:46.127497
NEXT_PUBLIC_API_URL=https://api2.hayataxi.online
2026-Jan-01 21:39:46.127497
MINIO_ROOT_USER=minioadmin
2026-Jan-01 21:39:46.127497
SHARED_GATEWAY_URL=http://localhost:8083
2026-Jan-01 21:39:46.127497
SITE_URL=http://localhost:3000
2026-Jan-01 21:39:46.127497
SHARED_JWT_SECRET=your-super-secret-jwt-key-for-shared
2026-Jan-01 21:39:46.127497
SHARED_ANON_KEY=placeholder
2026-Jan-01 21:39:46.127497
SHARED_SERVICE_ROLE_KEY=placeholder
2026-Jan-01 21:39:46.127497
SECRET_KEY_BASE=ChangeThisToAVeryLongRandomString
2026-Jan-01 21:39:46.127497
HOST=0.0.0.0
2026-Jan-01 21:39:46.251947
Removing old containers.
2026-Jan-01 21:39:46.754634
[CMD]: docker stop --time=30 dashboard-sokwws8k80wcg0gss0k0goww-213010245397
2026-Jan-01 21:39:46.754634
dashboard-sokwws8k80wcg0gss0k0goww-213010245397
2026-Jan-01 21:39:46.998369
[CMD]: docker rm -f dashboard-sokwws8k80wcg0gss0k0goww-213010245397
2026-Jan-01 21:39:46.998369
dashboard-sokwws8k80wcg0gss0k0goww-213010245397
2026-Jan-01 21:39:48.714049
[CMD]: docker stop --time=30 shared-storage-sokwws8k80wcg0gss0k0goww-213010357330
2026-Jan-01 21:39:48.714049
shared-storage-sokwws8k80wcg0gss0k0goww-213010357330
2026-Jan-01 21:39:48.884611
[CMD]: docker rm -f shared-storage-sokwws8k80wcg0gss0k0goww-213010357330
2026-Jan-01 21:39:48.884611
shared-storage-sokwws8k80wcg0gss0k0goww-213010357330
2026-Jan-01 21:39:49.005054
[CMD]: docker stop --time=30 api-sokwws8k80wcg0gss0k0goww-213010168800
2026-Jan-01 21:39:49.005054
api-sokwws8k80wcg0gss0k0goww-213010168800
2026-Jan-01 21:39:49.133252
[CMD]: docker rm -f api-sokwws8k80wcg0gss0k0goww-213010168800
2026-Jan-01 21:39:49.133252
api-sokwws8k80wcg0gss0k0goww-213010168800
2026-Jan-01 21:39:49.256248
[CMD]: docker stop --time=30 shared-api-sokwws8k80wcg0gss0k0goww-213010349397
2026-Jan-01 21:39:49.256248
shared-api-sokwws8k80wcg0gss0k0goww-213010349397
2026-Jan-01 21:39:49.414529
[CMD]: docker rm -f shared-api-sokwws8k80wcg0gss0k0goww-213010349397
2026-Jan-01 21:39:49.414529
shared-api-sokwws8k80wcg0gss0k0goww-213010349397
2026-Jan-01 21:39:49.925696
[CMD]: docker stop --time=30 shared-gateway-v3-sokwws8k80wcg0gss0k0goww-213010325174
2026-Jan-01 21:39:49.925696
shared-gateway-v3-sokwws8k80wcg0gss0k0goww-213010325174
2026-Jan-01 21:39:50.077564
[CMD]: docker rm -f shared-gateway-v3-sokwws8k80wcg0gss0k0goww-213010325174
2026-Jan-01 21:39:50.077564
shared-gateway-v3-sokwws8k80wcg0gss0k0goww-213010325174
2026-Jan-01 21:39:50.222924
[CMD]: docker stop --time=30 shared-realtime-sokwws8k80wcg0gss0k0goww-213010403376
2026-Jan-01 21:39:50.222924
shared-realtime-sokwws8k80wcg0gss0k0goww-213010403376
2026-Jan-01 21:39:50.354935
[CMD]: docker rm -f shared-realtime-sokwws8k80wcg0gss0k0goww-213010403376
2026-Jan-01 21:39:50.354935
shared-realtime-sokwws8k80wcg0gss0k0goww-213010403376
2026-Jan-01 21:39:50.472997
[CMD]: docker stop --time=30 shared-auth-sokwws8k80wcg0gss0k0goww-213010332634
2026-Jan-01 21:39:50.472997
shared-auth-sokwws8k80wcg0gss0k0goww-213010332634
2026-Jan-01 21:39:50.609761
[CMD]: docker rm -f shared-auth-sokwws8k80wcg0gss0k0goww-213010332634
2026-Jan-01 21:39:50.609761
shared-auth-sokwws8k80wcg0gss0k0goww-213010332634
2026-Jan-01 21:39:50.975087
[CMD]: docker stop --time=30 keycloak-sokwws8k80wcg0gss0k0goww-213010261304
2026-Jan-01 21:39:50.975087
keycloak-sokwws8k80wcg0gss0k0goww-213010261304
2026-Jan-01 21:39:51.173684
[CMD]: docker rm -f keycloak-sokwws8k80wcg0gss0k0goww-213010261304
2026-Jan-01 21:39:51.173684
keycloak-sokwws8k80wcg0gss0k0goww-213010261304
2026-Jan-01 21:39:51.508787
[CMD]: docker stop --time=30 shared-postgres-sokwws8k80wcg0gss0k0goww-213010286951
2026-Jan-01 21:39:51.508787
shared-postgres-sokwws8k80wcg0gss0k0goww-213010286951
2026-Jan-01 21:39:51.675554
[CMD]: docker rm -f shared-postgres-sokwws8k80wcg0gss0k0goww-213010286951
2026-Jan-01 21:39:51.675554
shared-postgres-sokwws8k80wcg0gss0k0goww-213010286951
2026-Jan-01 21:39:51.968821
[CMD]: docker stop --time=30 minio-sokwws8k80wcg0gss0k0goww-213010271254
2026-Jan-01 21:39:51.968821
minio-sokwws8k80wcg0gss0k0goww-213010271254
2026-Jan-01 21:39:52.099055
[CMD]: docker rm -f minio-sokwws8k80wcg0gss0k0goww-213010271254
2026-Jan-01 21:39:52.099055
minio-sokwws8k80wcg0gss0k0goww-213010271254
2026-Jan-01 21:39:52.337932
[CMD]: docker stop --time=30 control-plane-db-sokwws8k80wcg0gss0k0goww-213010131432
2026-Jan-01 21:39:52.337932
control-plane-db-sokwws8k80wcg0gss0k0goww-213010131432
2026-Jan-01 21:39:52.468573
[CMD]: docker rm -f control-plane-db-sokwws8k80wcg0gss0k0goww-213010131432
2026-Jan-01 21:39:52.468573
control-plane-db-sokwws8k80wcg0gss0k0goww-213010131432
2026-Jan-01 21:39:52.482232
Starting new application.
2026-Jan-01 21:39:53.084856
[CMD]: docker exec l0oso884kogw04wsgscwog0c bash -c 'SOURCE_COMMIT=38afe497310dc3044746949a4ac89c1fcfb200b7 COOLIFY_BRANCH=main COOLIFY_RESOURCE_UUID=sokwws8k80wcg0gss0k0goww COOLIFY_CONTAINER_NAME=sokwws8k80wcg0gss0k0goww-213626861147  docker compose --env-file /artifacts/l0oso884kogw04wsgscwog0c/.env --project-name sokwws8k80wcg0gss0k0goww --project-directory /artifacts/l0oso884kogw04wsgscwog0c -f /artifacts/l0oso884kogw04wsgscwog0c/docker-compose.coolify.yml up -d'
2026-Jan-01 21:39:53.084856
Container control-plane-db-sokwws8k80wcg0gss0k0goww-213638743919  Creating
2026-Jan-01 21:39:53.084856
Container minio-sokwws8k80wcg0gss0k0goww-213638979785  Creating
2026-Jan-01 21:39:53.096436
Container shared-postgres-sokwws8k80wcg0gss0k0goww-213639019566  Creating
2026-Jan-01 21:39:53.147938
Container minio-sokwws8k80wcg0gss0k0goww-213638979785  Created
2026-Jan-01 21:39:53.157458
Container control-plane-db-sokwws8k80wcg0gss0k0goww-213638743919  Created
2026-Jan-01 21:39:53.157458
Container keycloak-sokwws8k80wcg0gss0k0goww-213638957377  Creating
2026-Jan-01 21:39:53.166711
Container shared-postgres-sokwws8k80wcg0gss0k0goww-213639019566  Created
2026-Jan-01 21:39:53.166711
Container shared-gateway-v3-sokwws8k80wcg0gss0k0goww-213639054885  Creating
2026-Jan-01 21:39:53.166711
Container shared-realtime-sokwws8k80wcg0gss0k0goww-213639093972  Creating
2026-Jan-01 21:39:53.166711
Container shared-api-sokwws8k80wcg0gss0k0goww-213639074522  Creating
2026-Jan-01 21:39:53.166711
Container shared-auth-sokwws8k80wcg0gss0k0goww-213639057511  Creating
2026-Jan-01 21:39:53.210028
Container shared-gateway-v3-sokwws8k80wcg0gss0k0goww-213639054885  Created
2026-Jan-01 21:39:53.219842
Container shared-realtime-sokwws8k80wcg0gss0k0goww-213639093972  Created
2026-Jan-01 21:39:53.219842
Container shared-api-sokwws8k80wcg0gss0k0goww-213639074522  Created
2026-Jan-01 21:39:53.219842
Container shared-storage-sokwws8k80wcg0gss0k0goww-213639080629  Creating
2026-Jan-01 21:39:53.228234
Container keycloak-sokwws8k80wcg0gss0k0goww-213638957377  Created
2026-Jan-01 21:39:53.228234
Container api-sokwws8k80wcg0gss0k0goww-213638827176  Creating
2026-Jan-01 21:39:53.228234
Container shared-auth-sokwws8k80wcg0gss0k0goww-213639057511  Created
2026-Jan-01 21:39:53.267019
Container api-sokwws8k80wcg0gss0k0goww-213638827176  Created
2026-Jan-01 21:39:53.267019
Container dashboard-sokwws8k80wcg0gss0k0goww-213638937756  Creating
2026-Jan-01 21:39:53.281465
Container shared-storage-sokwws8k80wcg0gss0k0goww-213639080629  Created
2026-Jan-01 21:39:53.294456
Container dashboard-sokwws8k80wcg0gss0k0goww-213638937756  Created
2026-Jan-01 21:39:53.306707
Container shared-postgres-sokwws8k80wcg0gss0k0goww-213639019566  Starting
2026-Jan-01 21:39:53.306707
Container minio-sokwws8k80wcg0gss0k0goww-213638979785  Starting
2026-Jan-01 21:39:53.306707
Container control-plane-db-sokwws8k80wcg0gss0k0goww-213638743919  Starting
2026-Jan-01 21:39:53.829844
Container control-plane-db-sokwws8k80wcg0gss0k0goww-213638743919  Started
2026-Jan-01 21:39:53.829844
Container control-plane-db-sokwws8k80wcg0gss0k0goww-213638743919  Waiting
2026-Jan-01 21:39:53.931922
Container shared-postgres-sokwws8k80wcg0gss0k0goww-213639019566  Started
2026-Jan-01 21:39:53.931922
Container shared-postgres-sokwws8k80wcg0gss0k0goww-213639019566  Waiting
2026-Jan-01 21:39:53.931922
Container shared-postgres-sokwws8k80wcg0gss0k0goww-213639019566  Waiting
2026-Jan-01 21:39:53.952811
Container shared-postgres-sokwws8k80wcg0gss0k0goww-213639019566  Waiting
2026-Jan-01 21:39:53.952811
Container shared-postgres-sokwws8k80wcg0gss0k0goww-213639019566  Waiting
2026-Jan-01 21:39:54.029465
Container minio-sokwws8k80wcg0gss0k0goww-213638979785  Started
2026-Jan-01 21:39:59.333154
Container control-plane-db-sokwws8k80wcg0gss0k0goww-213638743919  Healthy
2026-Jan-01 21:39:59.333154
Container keycloak-sokwws8k80wcg0gss0k0goww-213638957377  Starting
2026-Jan-01 21:39:59.437331
Container shared-postgres-sokwws8k80wcg0gss0k0goww-213639019566  Healthy
2026-Jan-01 21:39:59.437331
Container shared-realtime-sokwws8k80wcg0gss0k0goww-213639093972  Starting
2026-Jan-01 21:39:59.473262
Container shared-postgres-sokwws8k80wcg0gss0k0goww-213639019566  Healthy
2026-Jan-01 21:39:59.473262
Container shared-auth-sokwws8k80wcg0gss0k0goww-213639057511  Starting
2026-Jan-01 21:39:59.473262
Container shared-postgres-sokwws8k80wcg0gss0k0goww-213639019566  Healthy
2026-Jan-01 21:39:59.473262
Container shared-gateway-v3-sokwws8k80wcg0gss0k0goww-213639054885  Starting
2026-Jan-01 21:39:59.473262
Container shared-postgres-sokwws8k80wcg0gss0k0goww-213639019566  Healthy
2026-Jan-01 21:39:59.473262
Container shared-api-sokwws8k80wcg0gss0k0goww-213639074522  Starting
2026-Jan-01 21:39:59.843325
Container keycloak-sokwws8k80wcg0gss0k0goww-213638957377  Started
2026-Jan-01 21:39:59.843325
Container control-plane-db-sokwws8k80wcg0gss0k0goww-213638743919  Waiting
2026-Jan-01 21:39:59.843325
Container shared-postgres-sokwws8k80wcg0gss0k0goww-213639019566  Waiting
2026-Jan-01 21:40:00.194479
Container shared-realtime-sokwws8k80wcg0gss0k0goww-213639093972  Started
2026-Jan-01 21:40:00.374065
Container shared-api-sokwws8k80wcg0gss0k0goww-213639074522  Started
2026-Jan-01 21:40:00.374065
Container shared-postgres-sokwws8k80wcg0gss0k0goww-213639019566  Waiting
2026-Jan-01 21:40:00.374065
Container control-plane-db-sokwws8k80wcg0gss0k0goww-213638743919  Healthy
2026-Jan-01 21:40:00.452908
Container shared-postgres-sokwws8k80wcg0gss0k0goww-213639019566  Healthy
2026-Jan-01 21:40:00.452908
Container api-sokwws8k80wcg0gss0k0goww-213638827176  Starting
2026-Jan-01 21:40:00.564564
Container shared-gateway-v3-sokwws8k80wcg0gss0k0goww-213639054885  Started
2026-Jan-01 21:40:00.865023
Container shared-auth-sokwws8k80wcg0gss0k0goww-213639057511  Started
2026-Jan-01 21:40:00.934896
Container shared-postgres-sokwws8k80wcg0gss0k0goww-213639019566  Healthy
2026-Jan-01 21:40:00.934896
Container shared-storage-sokwws8k80wcg0gss0k0goww-213639080629  Starting
2026-Jan-01 21:40:03.369925
Container api-sokwws8k80wcg0gss0k0goww-213638827176  Started
2026-Jan-01 21:40:03.369925
Container dashboard-sokwws8k80wcg0gss0k0goww-213638937756  Starting
2026-Jan-01 21:40:03.953668
Container shared-storage-sokwws8k80wcg0gss0k0goww-213639080629  Started
2026-Jan-01 21:40:05.852158
Container dashboard-sokwws8k80wcg0gss0k0goww-213638937756  Started
2026-Jan-01 21:40:08.933973
New container started.
2026-Jan-01 21:40:14.997389
Gracefully shutting down build container: l0oso884kogw04wsgscwog0c
2026-Jan-01 21:40:17.192728
[CMD]: docker stop --time=30 l0oso884kogw04wsgscwog0c
2026-Jan-01 21:40:17.192728
l0oso884kogw04wsgscwog0c
2026-Jan-01 21:40:19.053712
[CMD]: docker rm -f l0oso884kogw04wsgscwog0c
2026-Jan-01 21:40:19.053712
Error response from daemon: No such container: l0oso884kogw04wsgscwog0c