Deployment is Failed.


2026-Jan-01 14:50:25.795483
Starting deployment of farisnoaman/supalove:main-mc8cwc4ggsgo8gocw8040gkc to localhost.
2026-Jan-01 14:50:26.412708
Preparing container with helper image: ghcr.io/coollabsio/coolify-helper:1.0.12
2026-Jan-01 14:50:26.739046
[CMD]: docker stop --time=30 fcsows88cs0gosg8os084wgc
2026-Jan-01 14:50:26.739046
Error response from daemon: No such container: fcsows88cs0gosg8os084wgc
2026-Jan-01 14:50:27.065762
[CMD]: docker rm -f fcsows88cs0gosg8os084wgc
2026-Jan-01 14:50:27.065762
Error response from daemon: No such container: fcsows88cs0gosg8os084wgc
2026-Jan-01 14:50:27.434619
[CMD]: docker run -d --network coolify --name fcsows88cs0gosg8os084wgc  --rm -v /var/run/docker.sock:/var/run/docker.sock ghcr.io/coollabsio/coolify-helper:1.0.12
2026-Jan-01 14:50:27.434619
7bd627a00bfd625997e6710ea62a33134942cc843bb6040fb3ed406496c3ddf1
2026-Jan-01 14:50:28.868933
[CMD]: docker exec fcsows88cs0gosg8os084wgc bash -c 'GIT_SSH_COMMAND="ssh -o ConnectTimeout=30 -p 22 -o Port=22 -o LogLevel=ERROR -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" git ls-remote https://github.com/farisnoaman/supalove refs/heads/main'
2026-Jan-01 14:50:28.868933
a2b9a9934409606028f42bb30ee7fc8743dd3c44	refs/heads/main
2026-Jan-01 14:50:28.885589
----------------------------------------
2026-Jan-01 14:50:28.892524
Importing farisnoaman/supalove:main (commit sha a2b9a9934409606028f42bb30ee7fc8743dd3c44) to /artifacts/fcsows88cs0gosg8os084wgc.
2026-Jan-01 14:50:29.269045
[CMD]: docker exec fcsows88cs0gosg8os084wgc bash -c 'git clone --depth=1 --recurse-submodules --shallow-submodules -b 'main' 'https://github.com/farisnoaman/supalove' '/artifacts/fcsows88cs0gosg8os084wgc' && cd '/artifacts/fcsows88cs0gosg8os084wgc' && if [ -f .gitmodules ]; then sed -i "s#git@\(.*\):#https://\1/#g" '/artifacts/fcsows88cs0gosg8os084wgc'/.gitmodules || true && git submodule sync && GIT_SSH_COMMAND="ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" git submodule update --init --recursive --depth=1; fi && cd '/artifacts/fcsows88cs0gosg8os084wgc' && GIT_SSH_COMMAND="ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" git lfs pull'
2026-Jan-01 14:50:29.269045
Cloning into '/artifacts/fcsows88cs0gosg8os084wgc'...
2026-Jan-01 14:50:31.247791
[CMD]: docker exec fcsows88cs0gosg8os084wgc bash -c 'cd /artifacts/fcsows88cs0gosg8os084wgc && git log -1 a2b9a9934409606028f42bb30ee7fc8743dd3c44 --pretty=%B'
2026-Jan-01 14:50:31.247791
feat: implement shared multi-tenant infrastructure services (Postgres, Gateway, Auth, API, Storage, Realtime) and update Coolify deployment guide.
2026-Jan-01 14:50:34.993538
[CMD]: docker exec fcsows88cs0gosg8os084wgc bash -c 'test -f /artifacts/fcsows88cs0gosg8os084wgc/control-plane/api/Dockerfile && echo 'exists' || echo 'not found''
2026-Jan-01 14:50:34.993538
exists
2026-Jan-01 14:50:35.437048
[CMD]: docker exec fcsows88cs0gosg8os084wgc bash -c 'cat /artifacts/fcsows88cs0gosg8os084wgc/control-plane/api/Dockerfile'
2026-Jan-01 14:50:35.437048
FROM python:3.12-slim
2026-Jan-01 14:50:35.437048
WORKDIR /app
2026-Jan-01 14:50:35.437048
# Install system dependencies including Docker CLI
2026-Jan-01 14:50:35.437048
RUN apt-get update && apt-get install -y \
2026-Jan-01 14:50:35.437048
curl \
2026-Jan-01 14:50:35.437048
gnupg \
2026-Jan-01 14:50:35.437048
&& mkdir -p /etc/apt/keyrings \
2026-Jan-01 14:50:35.437048
&& curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg \
2026-Jan-01 14:50:35.437048
&& echo \
2026-Jan-01 14:50:35.437048
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
2026-Jan-01 14:50:35.437048
$(. /etc/os-release && echo "$VERSION_CODENAME") stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null \
2026-Jan-01 14:50:35.437048
&& apt-get update && apt-get install -y docker-ce-cli docker-compose-plugin \
2026-Jan-01 14:50:35.437048
&& rm -rf /var/lib/apt/lists/*
2026-Jan-01 14:50:35.437048
2026-Jan-01 14:50:35.437048
COPY control-plane/api/requirements.txt .
2026-Jan-01 14:50:35.437048
RUN pip install -r requirements.txt
2026-Jan-01 14:50:35.437048
2026-Jan-01 14:50:35.437048
# Copy source code to /app/src
2026-Jan-01 14:50:35.437048
COPY control-plane/api/src ./src
2026-Jan-01 14:50:35.437048
2026-Jan-01 14:50:35.437048
# Copy project template to /app/data-plane/project-template
2026-Jan-01 14:50:35.437048
# This bakes it into the image, so it's always available
2026-Jan-01 14:50:35.437048
COPY data-plane/project-template ./data-plane/project-template
2026-Jan-01 14:50:35.437048
2026-Jan-01 14:50:35.437048
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
2026-Jan-01 14:50:35.903994
Added 20 ARG declarations to Dockerfile for service api.
2026-Jan-01 14:50:36.414790
[CMD]: docker exec fcsows88cs0gosg8os084wgc bash -c 'test -f /artifacts/fcsows88cs0gosg8os084wgc/dashboard/Dockerfile && echo 'exists' || echo 'not found''
2026-Jan-01 14:50:36.414790
exists
2026-Jan-01 14:50:37.029185
[CMD]: docker exec fcsows88cs0gosg8os084wgc bash -c 'cat /artifacts/fcsows88cs0gosg8os084wgc/dashboard/Dockerfile'
2026-Jan-01 14:50:37.029185
# Stage 1: Dependencies
2026-Jan-01 14:50:37.029185
FROM node:20-alpine AS deps
2026-Jan-01 14:50:37.029185
WORKDIR /app
2026-Jan-01 14:50:37.029185
COPY package*.json ./
2026-Jan-01 14:50:37.029185
RUN npm install
2026-Jan-01 14:50:37.029185
2026-Jan-01 14:50:37.029185
# Stage 2: Builder
2026-Jan-01 14:50:37.029185
FROM node:20-alpine AS builder
2026-Jan-01 14:50:37.029185
WORKDIR /app
2026-Jan-01 14:50:37.029185
COPY --from=deps /app/node_modules ./node_modules
2026-Jan-01 14:50:37.029185
COPY . .
2026-Jan-01 14:50:37.029185
# Set environment variables for build if needed (e.g. backend URL)
2026-Jan-01 14:50:37.029185
# For Next.js client-side fetch, it might need to know the URL at build time if pre-rendering,
2026-Jan-01 14:50:37.029185
# but we are using "use client" so it's fine.
2026-Jan-01 14:50:37.029185
ARG NEXT_PUBLIC_API_URL
2026-Jan-01 14:50:37.029185
ENV NEXT_PUBLIC_API_URL=${NEXT_PUBLIC_API_URL}
2026-Jan-01 14:50:37.029185
RUN npm run build
2026-Jan-01 14:50:37.029185
2026-Jan-01 14:50:37.029185
# Stage 3: Runner
2026-Jan-01 14:50:37.029185
FROM node:20-alpine AS runner
2026-Jan-01 14:50:37.029185
WORKDIR /app
2026-Jan-01 14:50:37.029185
ENV NODE_ENV=production
2026-Jan-01 14:50:37.029185
COPY --from=builder /app/public ./public
2026-Jan-01 14:50:37.029185
COPY --from=builder /app/.next ./.next
2026-Jan-01 14:50:37.029185
COPY --from=builder /app/node_modules ./node_modules
2026-Jan-01 14:50:37.029185
COPY --from=builder /app/package.json ./package.json
2026-Jan-01 14:50:37.029185
2026-Jan-01 14:50:37.029185
EXPOSE 3000
2026-Jan-01 14:50:37.029185
CMD ["npm", "start"]
2026-Jan-01 14:50:37.787422
Added 60 ARG declarations to Dockerfile for service dashboard (multi-stage build, added to 3 stages).
2026-Jan-01 14:50:38.522280
[CMD]: docker exec fcsows88cs0gosg8os084wgc bash -c 'test -f /artifacts/fcsows88cs0gosg8os084wgc/data-plane/shared/routing-proxy/Dockerfile && echo 'exists' || echo 'not found''
2026-Jan-01 14:50:38.522280
exists
2026-Jan-01 14:50:39.164213
[CMD]: docker exec fcsows88cs0gosg8os084wgc bash -c 'cat /artifacts/fcsows88cs0gosg8os084wgc/data-plane/shared/routing-proxy/Dockerfile'
2026-Jan-01 14:50:39.164213
FROM python:3.11-slim
2026-Jan-01 14:50:39.164213
2026-Jan-01 14:50:39.164213
WORKDIR /app
2026-Jan-01 14:50:39.164213
2026-Jan-01 14:50:39.164213
COPY requirements.txt .
2026-Jan-01 14:50:39.164213
RUN pip install --no-cache-dir -r requirements.txt
2026-Jan-01 14:50:39.164213
2026-Jan-01 14:50:39.164213
COPY main.py .
2026-Jan-01 14:50:39.164213
2026-Jan-01 14:50:39.164213
EXPOSE 8000
2026-Jan-01 14:50:39.164213
2026-Jan-01 14:50:39.164213
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
2026-Jan-01 14:50:39.583888
Added 20 ARG declarations to Dockerfile for service shared-gateway-v3.
2026-Jan-01 14:50:39.591220
Pulling & building required images.
2026-Jan-01 14:50:39.639333
Creating build-time .env file in /artifacts (outside Docker context).
2026-Jan-01 14:50:40.403791
[CMD]: docker exec fcsows88cs0gosg8os084wgc bash -c 'cat /artifacts/build-time.env'
2026-Jan-01 14:50:40.403791
SOURCE_COMMIT='a2b9a9934409606028f42bb30ee7fc8743dd3c44'
2026-Jan-01 14:50:40.403791
COOLIFY_URL=''
2026-Jan-01 14:50:40.403791
COOLIFY_FQDN=''
2026-Jan-01 14:50:40.403791
SERVICE_NAME_CONTROL-PLANE-DB='control-plane-db'
2026-Jan-01 14:50:40.403791
SERVICE_NAME_API='api'
2026-Jan-01 14:50:40.403791
SERVICE_NAME_DASHBOARD='dashboard'
2026-Jan-01 14:50:40.403791
SERVICE_NAME_KEYCLOAK='keycloak'
2026-Jan-01 14:50:40.403791
SERVICE_NAME_MINIO='minio'
2026-Jan-01 14:50:40.403791
SERVICE_NAME_SHARED-POSTGRES='shared-postgres'
2026-Jan-01 14:50:40.403791
SERVICE_NAME_SHARED-GATEWAY-V3='shared-gateway-v3'
2026-Jan-01 14:50:40.403791
SERVICE_NAME_SHARED-AUTH='shared-auth'
2026-Jan-01 14:50:40.403791
SERVICE_NAME_SHARED-API='shared-api'
2026-Jan-01 14:50:40.403791
SERVICE_NAME_SHARED-STORAGE='shared-storage'
2026-Jan-01 14:50:40.403791
SERVICE_NAME_SHARED-REALTIME='shared-realtime'
2026-Jan-01 14:50:40.403791
ALLOWED_ORIGINS="http://localhost:3000,http://localhost:8000,https://supalove.hayataxi.online,https://api.hayataxi.online"
2026-Jan-01 14:50:40.403791
KEYCLOAK_ADMIN_PASSWORD="admin"
2026-Jan-01 14:50:40.403791
KEYCLOAK_ADMIN_USER="admin"
2026-Jan-01 14:50:40.403791
MINIO_ROOT_PASSWORD="minioadmin"
2026-Jan-01 14:50:40.403791
MINIO_ROOT_USER="minioadmin"
2026-Jan-01 14:50:40.403791
NEXT_PUBLIC_API_URL="https://api2.hayataxi.online"
2026-Jan-01 14:50:40.403791
POSTGRES_DB="control_plane"
2026-Jan-01 14:50:40.403791
POSTGRES_PASSWORD="platform"
2026-Jan-01 14:50:40.403791
POSTGRES_USER="platform"
2026-Jan-01 14:50:40.403791
SECRET_KEY_BASE="ChangeThisToAVeryLongRandomString"
2026-Jan-01 14:50:40.403791
SHARED_ANON_KEY="placeholder"
2026-Jan-01 14:50:40.403791
SHARED_GATEWAY_URL="http://localhost:8083"
2026-Jan-01 14:50:40.403791
SHARED_JWT_SECRET="your-super-secret-jwt-key-for-shared"
2026-Jan-01 14:50:40.403791
SHARED_POSTGRES_PASSWORD="postgres"
2026-Jan-01 14:50:40.403791
SHARED_SERVICE_ROLE_KEY="placeholder"
2026-Jan-01 14:50:40.403791
SITE_URL="http://localhost:3000"
2026-Jan-01 14:50:40.403791
URL="http://localhost:8000"
2026-Jan-01 14:50:40.413302
Adding build arguments to Docker Compose build command.
2026-Jan-01 14:50:40.980999
[CMD]: docker exec fcsows88cs0gosg8os084wgc bash -c 'SOURCE_COMMIT=a2b9a9934409606028f42bb30ee7fc8743dd3c44 COOLIFY_BRANCH=main COOLIFY_RESOURCE_UUID=sokwws8k80wcg0gss0k0goww COOLIFY_CONTAINER_NAME=sokwws8k80wcg0gss0k0goww-145022980310  docker compose --env-file /artifacts/build-time.env --project-name sokwws8k80wcg0gss0k0goww --project-directory /artifacts/fcsows88cs0gosg8os084wgc -f /artifacts/fcsows88cs0gosg8os084wgc/docker-compose.coolify.yml build --pull --no-cache --build-arg SOURCE_COMMIT --build-arg COOLIFY_URL --build-arg COOLIFY_FQDN --build-arg ALLOWED_ORIGINS --build-arg KEYCLOAK_ADMIN_PASSWORD --build-arg KEYCLOAK_ADMIN_USER --build-arg MINIO_ROOT_PASSWORD --build-arg MINIO_ROOT_USER --build-arg NEXT_PUBLIC_API_URL --build-arg POSTGRES_DB --build-arg POSTGRES_PASSWORD --build-arg POSTGRES_USER --build-arg SECRET_KEY_BASE --build-arg SHARED_ANON_KEY --build-arg SHARED_GATEWAY_URL --build-arg SHARED_JWT_SECRET --build-arg SHARED_POSTGRES_PASSWORD --build-arg SHARED_SERVICE_ROLE_KEY --build-arg SITE_URL --build-arg URL --build-arg COOLIFY_BUILD_SECRETS_HASH=710e97bb14002606f0bf9c53295cda5b349808592a7fb90c84510e3e7e94faf9'
2026-Jan-01 14:50:40.980999
#1 [internal] load local bake definitions
2026-Jan-01 14:50:41.092774
#1 reading from stdin 4.72kB done
2026-Jan-01 14:50:41.092774
#1 DONE 0.0s
2026-Jan-01 14:50:41.092774
2026-Jan-01 14:50:41.092774
#2 [dashboard internal] load build definition from Dockerfile
2026-Jan-01 14:50:41.092774
#2 transferring dockerfile: 2.10kB done
2026-Jan-01 14:50:41.288175
#2 DONE 0.0s
2026-Jan-01 14:50:41.288175
2026-Jan-01 14:50:41.288175
#3 [shared-gateway-v3 internal] load build definition from Dockerfile
2026-Jan-01 14:50:41.288175
#3 transferring dockerfile: 657B done
2026-Jan-01 14:50:41.288175
#3 DONE 0.0s
2026-Jan-01 14:50:41.288175
2026-Jan-01 14:50:41.288175
#4 [api internal] load build definition from Dockerfile
2026-Jan-01 14:50:41.288175
#4 transferring dockerfile: 1.52kB done
2026-Jan-01 14:50:41.288175
#4 DONE 0.1s
2026-Jan-01 14:50:41.288175
2026-Jan-01 14:50:41.288175
#5 [dashboard internal] load metadata for docker.io/library/node:20-alpine
2026-Jan-01 14:50:41.763728
#5 DONE 0.6s
2026-Jan-01 14:50:41.763728
2026-Jan-01 14:50:41.763728
#6 [api internal] load metadata for docker.io/library/python:3.12-slim
2026-Jan-01 14:50:41.887124
#6 DONE 0.7s
2026-Jan-01 14:50:41.887124
2026-Jan-01 14:50:41.887124
#7 [dashboard internal] load .dockerignore
2026-Jan-01 14:50:41.887124
#7 transferring context: 2B done
2026-Jan-01 14:50:41.887124
#7 DONE 0.0s
2026-Jan-01 14:50:41.887124
2026-Jan-01 14:50:41.887124
#8 [dashboard deps 1/4] FROM docker.io/library/node:20-alpine@sha256:658d0f63e501824d6c23e06d4bb95c71e7d704537c9d9272f488ac03a370d448
2026-Jan-01 14:50:41.887124
#8 DONE 0.0s
2026-Jan-01 14:50:41.887124
2026-Jan-01 14:50:41.887124
#9 [dashboard deps 2/4] WORKDIR /app
2026-Jan-01 14:50:41.887124
#9 CACHED
2026-Jan-01 14:50:41.887124
2026-Jan-01 14:50:41.887124
#10 [dashboard internal] load build context
2026-Jan-01 14:50:41.887124
#10 transferring context: 1.11MB 0.0s done
2026-Jan-01 14:50:41.887124
#10 DONE 0.0s
2026-Jan-01 14:50:41.887124
2026-Jan-01 14:50:41.887124
#11 [shared-gateway-v3 internal] load metadata for docker.io/library/python:3.11-slim
2026-Jan-01 14:50:41.986158
#11 DONE 0.8s
2026-Jan-01 14:50:41.986158
2026-Jan-01 14:50:41.986158
#12 [dashboard deps 3/4] COPY package*.json ./
2026-Jan-01 14:50:41.986158
#12 DONE 0.1s
2026-Jan-01 14:50:41.986158
2026-Jan-01 14:50:41.986158
#13 [shared-gateway-v3 internal] load .dockerignore
2026-Jan-01 14:50:41.986158
#13 transferring context: 2B done
2026-Jan-01 14:50:41.986158
#13 DONE 0.0s
2026-Jan-01 14:50:41.986158
2026-Jan-01 14:50:41.986158
#14 [shared-gateway-v3 1/5] FROM docker.io/library/python:3.11-slim@sha256:aa9aac8eacc774817e2881238f52d983a5ea13d7f5a1dee479a1a1d466047951
2026-Jan-01 14:50:41.986158
#14 DONE 0.0s
2026-Jan-01 14:50:41.986158
2026-Jan-01 14:50:41.986158
#15 [api internal] load .dockerignore
2026-Jan-01 14:50:41.986158
#15 transferring context: 103B done
2026-Jan-01 14:50:41.986158
#15 DONE 0.1s
2026-Jan-01 14:50:41.986158
2026-Jan-01 14:50:41.986158
#16 [shared-gateway-v3 2/5] WORKDIR /app
2026-Jan-01 14:50:41.986158
#16 CACHED
2026-Jan-01 14:50:41.986158
2026-Jan-01 14:50:41.986158
#17 [api 1/7] FROM docker.io/library/python:3.12-slim@sha256:8fbd0afc32e6cb14696c2fc47fadcda4c04ca0e766782343464bd716a6dc3f96
2026-Jan-01 14:50:41.986158
#17 DONE 0.0s
2026-Jan-01 14:50:41.986158
2026-Jan-01 14:50:41.986158
#18 [api internal] load build context
2026-Jan-01 14:50:42.112207
#18 ...
2026-Jan-01 14:50:42.112207
2026-Jan-01 14:50:42.112207
#19 [api 2/7] WORKDIR /app
2026-Jan-01 14:50:42.112207
#19 CACHED
2026-Jan-01 14:50:42.112207
2026-Jan-01 14:50:42.112207
#20 [shared-gateway-v3 internal] load build context
2026-Jan-01 14:50:42.112207
#20 transferring context: 12.36kB 0.0s done
2026-Jan-01 14:50:42.112207
#20 DONE 0.1s
2026-Jan-01 14:50:42.112207
2026-Jan-01 14:50:42.112207
#18 [api internal] load build context
2026-Jan-01 14:50:42.249717
#18 transferring context: 565.15kB 0.1s done
2026-Jan-01 14:50:42.249717
#18 DONE 0.2s
2026-Jan-01 14:50:42.249717
2026-Jan-01 14:50:42.249717
#21 [shared-gateway-v3 3/5] COPY requirements.txt .
2026-Jan-01 14:50:42.249717
#21 DONE 0.2s
2026-Jan-01 14:50:42.249717
2026-Jan-01 14:50:42.249717
#22 [api 3/7] RUN apt-get update && apt-get install -y     curl     gnupg     && mkdir -p /etc/apt/keyrings     && curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg     && echo     "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian     $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null     && apt-get update && apt-get install -y docker-ce-cli docker-compose-plugin     && rm -rf /var/lib/apt/lists/*
2026-Jan-01 14:50:42.645102
#22 0.660 Hit:1 http://deb.debian.org/debian trixie InRelease
2026-Jan-01 14:50:42.828617
#22 0.664 Get:2 http://deb.debian.org/debian trixie-updates InRelease [47.3 kB]
2026-Jan-01 14:50:42.828617
#22 0.664 Get:3 http://deb.debian.org/debian-security trixie-security InRelease [43.4 kB]
2026-Jan-01 14:50:42.828617
#22 0.694 Get:4 http://deb.debian.org/debian trixie/main amd64 Packages [9670 kB]
2026-Jan-01 14:50:42.859535
#22 0.875 Get:5 http://deb.debian.org/debian trixie-updates/main amd64 Packages [5412 B]
2026-Jan-01 14:50:42.859535
#22 0.875 Get:6 http://deb.debian.org/debian-security trixie-security/main amd64 Packages [93.7 kB]
2026-Jan-01 14:50:43.805557
#22 1.823 Fetched 9860 kB in 1s (7281 kB/s)
2026-Jan-01 14:50:43.805557
#22 1.823 Reading package lists...
2026-Jan-01 14:50:44.594368
2026-Jan-01 14:50:44.782559
#22 2.645 Reading package lists...
2026-Jan-01 14:50:45.597471
#22 3.566 Building dependency tree...
2026-Jan-01 14:50:45.847128
#22 3.863 Reading state information...
2026-Jan-01 14:50:46.334507
#22 4.353 The following additional packages will be installed:
2026-Jan-01 14:50:46.462451
#22 4.353   bash-completion dirmngr gnupg-l10n gnupg-utils gpg gpg-agent gpg-wks-client
2026-Jan-01 14:50:46.462451
#22 4.357   gpgconf gpgsm gpgv krb5-locales libassuan9 libbrotli1 libcom-err2
2026-Jan-01 14:50:46.462451
#22 4.358   libcurl4t64 libgcrypt20 libgnutls30t64 libgpg-error-l10n libgpg-error0
2026-Jan-01 14:50:46.462451
#22 4.358   libgssapi-krb5-2 libidn2-0 libk5crypto3 libkeyutils1 libkrb5-3
2026-Jan-01 14:50:46.462451
#22 4.358   libkrb5support0 libksba8 libldap-common libldap2 libnghttp2-14 libnghttp3-9
2026-Jan-01 14:50:46.462451
#22 4.358   libnpth0t64 libp11-kit0 libpsl5t64 librtmp1 libsasl2-2 libsasl2-modules
2026-Jan-01 14:50:46.462451
#22 4.358   libsasl2-modules-db libssh2-1t64 libtasn1-6 libunistring5 pinentry-curses
2026-Jan-01 14:50:46.462451
#22 4.358   publicsuffix
2026-Jan-01 14:50:46.462451
#22 4.364 Suggested packages:
2026-Jan-01 14:50:46.462451
#22 4.364   dbus-user-session libpam-systemd pinentry-gnome3 tor gpg-wks-server
2026-Jan-01 14:50:46.462451
#22 4.364   parcimonie xloadimage scdaemon tpm2daemon rng-tools gnutls-bin krb5-doc
2026-Jan-01 14:50:46.462451
#22 4.364   krb5-user libsasl2-modules-gssapi-mit | libsasl2-modules-gssapi-heimdal
2026-Jan-01 14:50:46.462451
#22 4.364   libsasl2-modules-ldap libsasl2-modules-otp libsasl2-modules-sql pinentry-doc
2026-Jan-01 14:50:46.700424
#22 4.718 The following NEW packages will be installed:
2026-Jan-01 14:50:46.801890
#22 4.719   bash-completion curl dirmngr gnupg gnupg-l10n gnupg-utils gpg gpg-agent
2026-Jan-01 14:50:46.801890
#22 4.719   gpg-wks-client gpgconf gpgsm gpgv krb5-locales libassuan9 libbrotli1
2026-Jan-01 14:50:46.801890
#22 4.719   libcom-err2 libcurl4t64 libgcrypt20 libgnutls30t64 libgpg-error-l10n
2026-Jan-01 14:50:46.801890
#22 4.719   libgpg-error0 libgssapi-krb5-2 libidn2-0 libk5crypto3 libkeyutils1 libkrb5-3
2026-Jan-01 14:50:46.801890
#22 4.721   libkrb5support0 libksba8 libldap-common libldap2 libnghttp2-14 libnghttp3-9
2026-Jan-01 14:50:46.801890
#22 4.724   libnpth0t64 libp11-kit0 libpsl5t64 librtmp1 libsasl2-2 libsasl2-modules
2026-Jan-01 14:50:46.801890
#22 4.724   libsasl2-modules-db libssh2-1t64 libtasn1-6 libunistring5 pinentry-curses
2026-Jan-01 14:50:46.801890
#22 4.724   publicsuffix
2026-Jan-01 14:50:46.801890
#22 4.767 0 upgraded, 44 newly installed, 0 to remove and 0 not upgraded.
2026-Jan-01 14:50:46.801890
#22 4.767 Need to get 10.4 MB of archives.
2026-Jan-01 14:50:46.801890
#22 4.767 After this operation, 33.7 MB of additional disk space will be used.
2026-Jan-01 14:50:46.801890
#22 4.767 Get:1 http://deb.debian.org/debian trixie/main amd64 bash-completion all 1:2.16.0-7 [319 kB]
2026-Jan-01 14:50:46.801890
#22 4.776 Get:2 http://deb.debian.org/debian trixie/main amd64 krb5-locales all 1.21.3-5 [101 kB]
2026-Jan-01 14:50:46.801890
#22 4.783 Get:3 http://deb.debian.org/debian trixie/main amd64 libbrotli1 amd64 1.1.0-2+b7 [307 kB]
2026-Jan-01 14:50:46.801890
#22 4.790 Get:4 http://deb.debian.org/debian trixie/main amd64 libkrb5support0 amd64 1.21.3-5 [33.0 kB]
2026-Jan-01 14:50:46.801890
#22 4.790 Get:5 http://deb.debian.org/debian trixie/main amd64 libcom-err2 amd64 1.47.2-3+b3 [25.0 kB]
2026-Jan-01 14:50:46.801890
#22 4.793 Get:6 http://deb.debian.org/debian trixie/main amd64 libk5crypto3 amd64 1.21.3-5 [81.5 kB]
2026-Jan-01 14:50:46.801890
#22 4.794 Get:7 http://deb.debian.org/debian trixie/main amd64 libkeyutils1 amd64 1.6.3-6 [9456 B]
2026-Jan-01 14:50:46.801890
#22 4.794 Get:8 http://deb.debian.org/debian trixie/main amd64 libkrb5-3 amd64 1.21.3-5 [326 kB]
2026-Jan-01 14:50:46.801890
#22 4.800 Get:9 http://deb.debian.org/debian trixie/main amd64 libgssapi-krb5-2 amd64 1.21.3-5 [138 kB]
2026-Jan-01 14:50:46.801890
#22 4.808 Get:10 http://deb.debian.org/debian trixie/main amd64 libunistring5 amd64 1.3-2 [477 kB]
2026-Jan-01 14:50:46.801890
#22 4.810 Get:11 http://deb.debian.org/debian trixie/main amd64 libidn2-0 amd64 2.3.8-2 [109 kB]
2026-Jan-01 14:50:46.801890
#22 4.812 Get:12 http://deb.debian.org/debian trixie/main amd64 libsasl2-modules-db amd64 2.1.28+dfsg1-9 [19.8 kB]
2026-Jan-01 14:50:46.801890
#22 4.818 Get:13 http://deb.debian.org/debian trixie/main amd64 libsasl2-2 amd64 2.1.28+dfsg1-9 [57.5 kB]
2026-Jan-01 14:50:46.801890
#22 4.818 Get:14 http://deb.debian.org/debian trixie/main amd64 libldap2 amd64 2.6.10+dfsg-1 [194 kB]
2026-Jan-01 14:50:46.801890
#22 4.820 Get:15 http://deb.debian.org/debian trixie/main amd64 libnghttp2-14 amd64 1.64.0-1.1 [76.0 kB]
2026-Jan-01 14:50:46.907454
#22 4.822 Get:16 http://deb.debian.org/debian trixie/main amd64 libnghttp3-9 amd64 1.8.0-1 [67.7 kB]
2026-Jan-01 14:50:46.907454
#22 4.827 Get:17 http://deb.debian.org/debian trixie/main amd64 libpsl5t64 amd64 0.21.2-1.1+b1 [57.2 kB]
2026-Jan-01 14:50:46.907454
#22 4.830 Get:18 http://deb.debian.org/debian trixie/main amd64 libp11-kit0 amd64 0.25.5-3 [425 kB]
2026-Jan-01 14:50:46.907454
#22 4.837 Get:19 http://deb.debian.org/debian trixie/main amd64 libtasn1-6 amd64 4.20.0-2 [49.9 kB]
2026-Jan-01 14:50:46.907454
#22 4.837 Get:20 http://deb.debian.org/debian trixie/main amd64 libgnutls30t64 amd64 3.8.9-3 [1465 kB]
2026-Jan-01 14:50:46.907454
#22 4.857 Get:21 http://deb.debian.org/debian trixie/main amd64 librtmp1 amd64 2.4+20151223.gitfa8646d.1-2+b5 [58.8 kB]
2026-Jan-01 14:50:46.907454
#22 4.858 Get:22 http://deb.debian.org/debian trixie/main amd64 libssh2-1t64 amd64 1.11.1-1 [245 kB]
2026-Jan-01 14:50:46.907454
#22 4.863 Get:23 http://deb.debian.org/debian trixie/main amd64 libcurl4t64 amd64 8.14.1-2+deb13u2 [391 kB]
2026-Jan-01 14:50:46.907454
#22 4.866 Get:24 http://deb.debian.org/debian trixie/main amd64 curl amd64 8.14.1-2+deb13u2 [270 kB]
2026-Jan-01 14:50:46.907454
#22 4.869 Get:25 http://deb.debian.org/debian trixie/main amd64 libgpg-error0 amd64 1.51-4 [82.1 kB]
2026-Jan-01 14:50:46.907454
#22 4.873 Get:26 http://deb.debian.org/debian trixie/main amd64 libassuan9 amd64 3.0.2-2 [61.5 kB]
2026-Jan-01 14:50:46.907454
#22 4.874 Get:27 http://deb.debian.org/debian trixie/main amd64 libgcrypt20 amd64 1.11.0-7 [843 kB]
2026-Jan-01 14:50:46.907454
#22 4.882 Get:28 http://deb.debian.org/debian trixie/main amd64 gpgconf amd64 2.4.7-21+b3 [129 kB]
2026-Jan-01 14:50:46.907454
#22 4.883 Get:29 http://deb.debian.org/debian trixie/main amd64 libksba8 amd64 1.6.7-2+b1 [136 kB]
2026-Jan-01 14:50:46.907454
#22 4.886 Get:30 http://deb.debian.org/debian trixie/main amd64 libnpth0t64 amd64 1.8-3 [23.2 kB]
2026-Jan-01 14:50:46.907454
#22 4.889 Get:31 http://deb.debian.org/debian trixie/main amd64 dirmngr amd64 2.4.7-21+b3 [384 kB]
2026-Jan-01 14:50:46.907454
#22 4.893 Get:32 http://deb.debian.org/debian trixie/main amd64 gnupg-l10n all 2.4.7-21 [747 kB]
2026-Jan-01 14:50:46.907454
#22 4.898 Get:33 http://deb.debian.org/debian trixie/main amd64 gpg amd64 2.4.7-21+b3 [634 kB]
2026-Jan-01 14:50:46.907454
#22 4.904 Get:34 http://deb.debian.org/debian trixie/main amd64 pinentry-curses amd64 1.3.1-2 [86.4 kB]
2026-Jan-01 14:50:46.907454
#22 4.904 Get:35 http://deb.debian.org/debian trixie/main amd64 gpg-agent amd64 2.4.7-21+b3 [271 kB]
2026-Jan-01 14:50:46.907454
#22 4.906 Get:36 http://deb.debian.org/debian trixie/main amd64 gpgsm amd64 2.4.7-21+b3 [275 kB]
2026-Jan-01 14:50:46.907454
#22 4.910 Get:37 http://deb.debian.org/debian trixie/main amd64 gnupg all 2.4.7-21 [417 kB]
2026-Jan-01 14:50:46.907454
#22 4.912 Get:38 http://deb.debian.org/debian trixie/main amd64 gpg-wks-client amd64 2.4.7-21+b3 [108 kB]
2026-Jan-01 14:50:46.907454
#22 4.913 Get:39 http://deb.debian.org/debian trixie/main amd64 gpgv amd64 2.4.7-21+b3 [241 kB]
2026-Jan-01 14:50:46.907454
#22 4.916 Get:40 http://deb.debian.org/debian trixie/main amd64 libgpg-error-l10n all 1.51-4 [114 kB]
2026-Jan-01 14:50:46.907454
#22 4.916 Get:41 http://deb.debian.org/debian trixie/main amd64 libldap-common all 2.6.10+dfsg-1 [35.1 kB]
2026-Jan-01 14:50:46.907454
#22 4.918 Get:42 http://deb.debian.org/debian trixie/main amd64 libsasl2-modules amd64 2.1.28+dfsg1-9 [66.7 kB]
2026-Jan-01 14:50:46.919181
#22 4.918 Get:43 http://deb.debian.org/debian trixie/main amd64 publicsuffix all 20250328.1952-0.1 [296 kB]
2026-Jan-01 14:50:46.919181
#22 4.919 Get:44 http://deb.debian.org/debian trixie/main amd64 gnupg-utils amd64 2.4.7-21+b3 [194 kB]
2026-Jan-01 14:50:47.147528
#22 5.165 debconf: unable to initialize frontend: Dialog
2026-Jan-01 14:50:47.310339
#22 5.166 debconf: (TERM is not set, so the dialog frontend is not usable.)
2026-Jan-01 14:50:47.310339
#22 5.166 debconf: falling back to frontend: Readline
2026-Jan-01 14:50:47.310339
#22 5.170 debconf: unable to initialize frontend: Readline
2026-Jan-01 14:50:47.310339
#22 5.170 debconf: (Can't locate Term/ReadLine.pm in @INC (you may need to install the Term::ReadLine module) (@INC entries checked: /etc/perl /usr/local/lib/x86_64-linux-gnu/perl/5.40.1 /usr/local/share/perl/5.40.1 /usr/lib/x86_64-linux-gnu/perl5/5.40 /usr/share/perl5 /usr/lib/x86_64-linux-gnu/perl-base /usr/lib/x86_64-linux-gnu/perl/5.40 /usr/share/perl/5.40 /usr/local/lib/site_perl) at /usr/share/perl5/Debconf/FrontEnd/Readline.pm line 8, <STDIN> line 44.)
2026-Jan-01 14:50:47.310339
#22 5.170 debconf: falling back to frontend: Teletype
2026-Jan-01 14:50:47.310339
#22 5.178 debconf: unable to initialize frontend: Teletype
2026-Jan-01 14:50:47.310339
#22 5.178 debconf: (This frontend requires a controlling tty.)
2026-Jan-01 14:50:47.310339
#22 5.178 debconf: falling back to frontend: Noninteractive
2026-Jan-01 14:50:49.255496
#22 7.274 Fetched 10.4 MB in 0s (60.3 MB/s)
2026-Jan-01 14:50:49.359795
#22 7.337 Selecting previously unselected package bash-completion.
2026-Jan-01 14:50:49.359795
#22 7.337 (Reading database ... 
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
(Reading database ... 5644 files and directories currently installed.)
2026-Jan-01 14:50:49.359795
#22 7.369 Preparing to unpack .../00-bash-completion_1%3a2.16.0-7_all.deb ...
2026-Jan-01 14:50:49.359795
#22 7.377 Unpacking bash-completion (1:2.16.0-7) ...
2026-Jan-01 14:50:49.747781
#22 7.766 Selecting previously unselected package krb5-locales.
2026-Jan-01 14:50:49.921292
#22 7.772 Preparing to unpack .../01-krb5-locales_1.21.3-5_all.deb ...
2026-Jan-01 14:50:49.921292
#22 7.778 Unpacking krb5-locales (1.21.3-5) ...
2026-Jan-01 14:50:49.921292
#22 7.845 Selecting previously unselected package libbrotli1:amd64.
2026-Jan-01 14:50:49.921292
#22 7.847 Preparing to unpack .../02-libbrotli1_1.1.0-2+b7_amd64.deb ...
2026-Jan-01 14:50:49.921292
#22 7.852 Unpacking libbrotli1:amd64 (1.1.0-2+b7) ...
2026-Jan-01 14:50:49.921292
#22 7.939 Selecting previously unselected package libkrb5support0:amd64.
2026-Jan-01 14:50:50.083691
#22 7.942 Preparing to unpack .../03-libkrb5support0_1.21.3-5_amd64.deb ...
2026-Jan-01 14:50:50.083691
#22 7.946 Unpacking libkrb5support0:amd64 (1.21.3-5) ...
2026-Jan-01 14:50:50.083691
#22 8.024 Selecting previously unselected package libcom-err2:amd64.
2026-Jan-01 14:50:50.083691
#22 8.029 Preparing to unpack .../04-libcom-err2_1.47.2-3+b3_amd64.deb ...
2026-Jan-01 14:50:50.083691
#22 8.037 Unpacking libcom-err2:amd64 (1.47.2-3+b3) ...
2026-Jan-01 14:50:50.083691
#22 8.101 Selecting previously unselected package libk5crypto3:amd64.
2026-Jan-01 14:50:50.202520
#22 8.105 Preparing to unpack .../05-libk5crypto3_1.21.3-5_amd64.deb ...
2026-Jan-01 14:50:50.207998
#22 8.109 Unpacking libk5crypto3:amd64 (1.21.3-5) ...
2026-Jan-01 14:50:50.207998
#22 8.166 Selecting previously unselected package libkeyutils1:amd64.
2026-Jan-01 14:50:50.207998
#22 8.170 Preparing to unpack .../06-libkeyutils1_1.6.3-6_amd64.deb ...
2026-Jan-01 14:50:50.207998
#22 8.174 Unpacking libkeyutils1:amd64 (1.6.3-6) ...
2026-Jan-01 14:50:50.207998
#22 8.221 Selecting previously unselected package libkrb5-3:amd64.
2026-Jan-01 14:50:50.304467
#22 8.225 Preparing to unpack .../07-libkrb5-3_1.21.3-5_amd64.deb ...
2026-Jan-01 14:50:50.304467
#22 8.227 Unpacking libkrb5-3:amd64 (1.21.3-5) ...
2026-Jan-01 14:50:50.304467
#22 8.320 Selecting previously unselected package libgssapi-krb5-2:amd64.
2026-Jan-01 14:50:50.404449
#22 8.325 Preparing to unpack .../08-libgssapi-krb5-2_1.21.3-5_amd64.deb ...
2026-Jan-01 14:50:50.404449
#22 8.329 Unpacking libgssapi-krb5-2:amd64 (1.21.3-5) ...
2026-Jan-01 14:50:50.404449
#22 8.418 Selecting previously unselected package libunistring5:amd64.
2026-Jan-01 14:50:50.404449
#22 8.422 Preparing to unpack .../09-libunistring5_1.3-2_amd64.deb ...
2026-Jan-01 14:50:50.555647
#22 8.427 Unpacking libunistring5:amd64 (1.3-2) ...
2026-Jan-01 14:50:50.555647
#22 8.573 Selecting previously unselected package libidn2-0:amd64.
2026-Jan-01 14:50:50.555647
#22 8.573 Preparing to unpack .../10-libidn2-0_2.3.8-2_amd64.deb ...
2026-Jan-01 14:50:50.693377
#22 8.577 Unpacking libidn2-0:amd64 (2.3.8-2) ...
2026-Jan-01 14:50:50.693377
#22 8.656 Selecting previously unselected package libsasl2-modules-db:amd64.
2026-Jan-01 14:50:50.693377
#22 8.658 Preparing to unpack .../11-libsasl2-modules-db_2.1.28+dfsg1-9_amd64.deb ...
2026-Jan-01 14:50:50.693377
#22 8.663 Unpacking libsasl2-modules-db:amd64 (2.1.28+dfsg1-9) ...
2026-Jan-01 14:50:50.693377
#22 8.712 Selecting previously unselected package libsasl2-2:amd64.
2026-Jan-01 14:50:50.809943
#22 8.718 Preparing to unpack .../12-libsasl2-2_2.1.28+dfsg1-9_amd64.deb ...
2026-Jan-01 14:50:50.809943
#22 8.722 Unpacking libsasl2-2:amd64 (2.1.28+dfsg1-9) ...
2026-Jan-01 14:50:50.809943
#22 8.779 Selecting previously unselected package libldap2:amd64.
2026-Jan-01 14:50:50.809943
#22 8.782 Preparing to unpack .../13-libldap2_2.6.10+dfsg-1_amd64.deb ...
2026-Jan-01 14:50:50.809943
#22 8.787 Unpacking libldap2:amd64 (2.6.10+dfsg-1) ...
2026-Jan-01 14:50:50.928490
#22 8.865 Selecting previously unselected package libnghttp2-14:amd64.
2026-Jan-01 14:50:50.938046
#22 8.870 Preparing to unpack .../14-libnghttp2-14_1.64.0-1.1_amd64.deb ...
2026-Jan-01 14:50:50.938046
#22 8.873 Unpacking libnghttp2-14:amd64 (1.64.0-1.1) ...
2026-Jan-01 14:50:50.938046
#22 8.946 Selecting previously unselected package libnghttp3-9:amd64.
2026-Jan-01 14:50:51.096174
#22 8.953 Preparing to unpack .../15-libnghttp3-9_1.8.0-1_amd64.deb ...
2026-Jan-01 14:50:51.096174
#22 8.957 Unpacking libnghttp3-9:amd64 (1.8.0-1) ...
2026-Jan-01 14:50:51.096174
#22 9.032 Selecting previously unselected package libpsl5t64:amd64.
2026-Jan-01 14:50:51.096174
#22 9.038 Preparing to unpack .../16-libpsl5t64_0.21.2-1.1+b1_amd64.deb ...
2026-Jan-01 14:50:51.096174
#22 9.041 Unpacking libpsl5t64:amd64 (0.21.2-1.1+b1) ...
2026-Jan-01 14:50:51.096174
#22 9.113 Selecting previously unselected package libp11-kit0:amd64.
2026-Jan-01 14:50:51.228349
#22 9.115 Preparing to unpack .../17-libp11-kit0_0.25.5-3_amd64.deb ...
2026-Jan-01 14:50:51.228349
#22 9.121 Unpacking libp11-kit0:amd64 (0.25.5-3) ...
2026-Jan-01 14:50:51.228349
#22 9.243 Selecting previously unselected package libtasn1-6:amd64.
2026-Jan-01 14:50:51.470509
#22 9.247 Preparing to unpack .../18-libtasn1-6_4.20.0-2_amd64.deb ...
2026-Jan-01 14:50:51.484171
#22 9.247 Unpacking libtasn1-6:amd64 (4.20.0-2) ...
2026-Jan-01 14:50:51.484171
#22 9.332 Selecting previously unselected package libgnutls30t64:amd64.
2026-Jan-01 14:50:51.484171
#22 9.333 Preparing to unpack .../19-libgnutls30t64_3.8.9-3_amd64.deb ...
2026-Jan-01 14:50:51.484171
#22 9.338 Unpacking libgnutls30t64:amd64 (3.8.9-3) ...
2026-Jan-01 14:50:51.628524
#22 9.644 Selecting previously unselected package librtmp1:amd64.
2026-Jan-01 14:50:51.769704
#22 ...
2026-Jan-01 14:50:51.769704
2026-Jan-01 14:50:51.769704
#23 [shared-gateway-v3 4/5] RUN pip install --no-cache-dir -r requirements.txt
2026-Jan-01 14:50:51.769704
#23 3.198 Collecting fastapi>=0.109.0 (from -r requirements.txt (line 1))
2026-Jan-01 14:50:51.769704
#23 3.228   Downloading fastapi-0.128.0-py3-none-any.whl.metadata (30 kB)
2026-Jan-01 14:50:51.769704
#23 3.288 Collecting uvicorn>=0.27.0 (from -r requirements.txt (line 2))
2026-Jan-01 14:50:51.769704
#23 3.297   Downloading uvicorn-0.40.0-py3-none-any.whl.metadata (6.7 kB)
2026-Jan-01 14:50:51.769704
#23 3.344 Collecting httpx>=0.26.0 (from -r requirements.txt (line 3))
2026-Jan-01 14:50:51.769704
#23 3.349   Downloading httpx-0.28.1-py3-none-any.whl.metadata (7.1 kB)
2026-Jan-01 14:50:51.776061
#23 3.443 Collecting psycopg2-binary>=2.9.9 (from -r requirements.txt (line 4))
2026-Jan-01 14:50:51.776061
#23 3.450   Downloading psycopg2_binary-2.9.11-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (4.9 kB)
2026-Jan-01 14:50:51.776061
#23 3.700 Collecting websockets>=12.0 (from -r requirements.txt (line 5))
2026-Jan-01 14:50:51.776061
#23 3.707   Downloading websockets-15.0.1-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.8 kB)
2026-Jan-01 14:50:51.776061
#23 3.746 Collecting python-dotenv>=1.0.0 (from -r requirements.txt (line 6))
2026-Jan-01 14:50:51.776061
#23 3.752   Downloading python_dotenv-1.2.1-py3-none-any.whl.metadata (25 kB)
2026-Jan-01 14:50:51.776061
#23 3.855 Collecting starlette<0.51.0,>=0.40.0 (from fastapi>=0.109.0->-r requirements.txt (line 1))
2026-Jan-01 14:50:51.776061
#23 3.860   Downloading starlette-0.50.0-py3-none-any.whl.metadata (6.3 kB)
2026-Jan-01 14:50:51.776061
#23 4.208 Collecting pydantic>=2.7.0 (from fastapi>=0.109.0->-r requirements.txt (line 1))
2026-Jan-01 14:50:51.776061
#23 4.215   Downloading pydantic-2.12.5-py3-none-any.whl.metadata (90 kB)
2026-Jan-01 14:50:51.776061
#23 4.228      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 90.6/90.6 kB 278.3 MB/s eta 0:00:00
2026-Jan-01 14:50:51.776061
#23 4.295 Collecting typing-extensions>=4.8.0 (from fastapi>=0.109.0->-r requirements.txt (line 1))
2026-Jan-01 14:50:51.776061
#23 4.301   Downloading typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
2026-Jan-01 14:50:51.776061
#23 4.335 Collecting annotated-doc>=0.0.2 (from fastapi>=0.109.0->-r requirements.txt (line 1))
2026-Jan-01 14:50:51.776061
#23 4.342   Downloading annotated_doc-0.0.4-py3-none-any.whl.metadata (6.6 kB)
2026-Jan-01 14:50:51.776061
#23 4.388 Collecting click>=7.0 (from uvicorn>=0.27.0->-r requirements.txt (line 2))
2026-Jan-01 14:50:51.776061
#23 4.394   Downloading click-8.3.1-py3-none-any.whl.metadata (2.6 kB)
2026-Jan-01 14:50:51.776061
#23 4.414 Collecting h11>=0.8 (from uvicorn>=0.27.0->-r requirements.txt (line 2))
2026-Jan-01 14:50:51.776061
#23 4.422   Downloading h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
2026-Jan-01 14:50:51.776061
#23 4.476 Collecting anyio (from httpx>=0.26.0->-r requirements.txt (line 3))
2026-Jan-01 14:50:51.776061
#23 4.484   Downloading anyio-4.12.0-py3-none-any.whl.metadata (4.3 kB)
2026-Jan-01 14:50:51.776061
#23 4.513 Collecting certifi (from httpx>=0.26.0->-r requirements.txt (line 3))
2026-Jan-01 14:50:51.776061
#23 4.530   Downloading certifi-2025.11.12-py3-none-any.whl.metadata (2.5 kB)
2026-Jan-01 14:50:51.776061
#23 4.600 Collecting httpcore==1.* (from httpx>=0.26.0->-r requirements.txt (line 3))
2026-Jan-01 14:50:51.776061
#23 4.618   Downloading httpcore-1.0.9-py3-none-any.whl.metadata (21 kB)
2026-Jan-01 14:50:51.776061
#23 4.646 Collecting idna (from httpx>=0.26.0->-r requirements.txt (line 3))
2026-Jan-01 14:50:51.776061
#23 4.654   Downloading idna-3.11-py3-none-any.whl.metadata (8.4 kB)
2026-Jan-01 14:50:51.776061
#23 4.710 Collecting annotated-types>=0.6.0 (from pydantic>=2.7.0->fastapi>=0.109.0->-r requirements.txt (line 1))
2026-Jan-01 14:50:51.776061
#23 4.717   Downloading annotated_types-0.7.0-py3-none-any.whl.metadata (15 kB)
2026-Jan-01 14:50:51.776061
#23 6.013 Collecting pydantic-core==2.41.5 (from pydantic>=2.7.0->fastapi>=0.109.0->-r requirements.txt (line 1))
2026-Jan-01 14:50:51.776061
#23 6.021   Downloading pydantic_core-2.41.5-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (7.3 kB)
2026-Jan-01 14:50:51.776061
#23 6.046 Collecting typing-inspection>=0.4.2 (from pydantic>=2.7.0->fastapi>=0.109.0->-r requirements.txt (line 1))
2026-Jan-01 14:50:51.776061
#23 6.050   Downloading typing_inspection-0.4.2-py3-none-any.whl.metadata (2.6 kB)
2026-Jan-01 14:50:51.776061
#23 6.152 Downloading fastapi-0.128.0-py3-none-any.whl (103 kB)
2026-Jan-01 14:50:51.776061
#23 6.157    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 103.1/103.1 kB 379.6 MB/s eta 0:00:00
2026-Jan-01 14:50:51.776061
#23 6.161 Downloading uvicorn-0.40.0-py3-none-any.whl (68 kB)
2026-Jan-01 14:50:51.776061
#23 6.163    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 68.5/68.5 kB 359.0 MB/s eta 0:00:00
2026-Jan-01 14:50:51.776061
#23 6.170 Downloading httpx-0.28.1-py3-none-any.whl (73 kB)
2026-Jan-01 14:50:51.776061
#23 6.175    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 73.5/73.5 kB 345.7 MB/s eta 0:00:00
2026-Jan-01 14:50:51.776061
#23 6.181 Downloading httpcore-1.0.9-py3-none-any.whl (78 kB)
2026-Jan-01 14:50:51.776061
#23 6.187    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 78.8/78.8 kB 33.4 MB/s eta 0:00:00
2026-Jan-01 14:50:51.776061
#23 6.193 Downloading psycopg2_binary-2.9.11-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (4.2 MB)
2026-Jan-01 14:50:51.776061
#23 6.251    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.2/4.2 MB 80.0 MB/s eta 0:00:00
2026-Jan-01 14:50:51.776061
#23 6.268 Downloading websockets-15.0.1-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (182 kB)
2026-Jan-01 14:50:51.776061
#23 6.273    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 182.3/182.3 kB 293.4 MB/s eta 0:00:00
2026-Jan-01 14:50:51.776061
#23 6.275 Downloading python_dotenv-1.2.1-py3-none-any.whl (21 kB)
2026-Jan-01 14:50:51.776061
#23 6.285 Downloading annotated_doc-0.0.4-py3-none-any.whl (5.3 kB)
2026-Jan-01 14:50:51.776061
#23 6.291 Downloading click-8.3.1-py3-none-any.whl (108 kB)
2026-Jan-01 14:50:51.776061
#23 6.293    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 108.3/108.3 kB 259.1 MB/s eta 0:00:00
2026-Jan-01 14:50:51.776061
#23 6.299 Downloading h11-0.16.0-py3-none-any.whl (37 kB)
2026-Jan-01 14:50:51.776061
#23 6.304 Downloading pydantic-2.12.5-py3-none-any.whl (463 kB)
2026-Jan-01 14:50:51.776061
#23 6.311    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 463.6/463.6 kB 164.4 MB/s eta 0:00:00
2026-Jan-01 14:50:51.776061
#23 6.322 Downloading pydantic_core-2.41.5-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.1 MB)
2026-Jan-01 14:50:51.776061
#23 6.348    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 85.2 MB/s eta 0:00:00
2026-Jan-01 14:50:51.776061
#23 6.355 Downloading starlette-0.50.0-py3-none-any.whl (74 kB)
2026-Jan-01 14:50:51.776061
#23 6.359    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 74.0/74.0 kB 359.6 MB/s eta 0:00:00
2026-Jan-01 14:50:51.776061
#23 6.363 Downloading anyio-4.12.0-py3-none-any.whl (113 kB)
2026-Jan-01 14:50:51.776061
#23 6.366    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 113.4/113.4 kB 426.7 MB/s eta 0:00:00
2026-Jan-01 14:50:51.776061
#23 6.370 Downloading idna-3.11-py3-none-any.whl (71 kB)
2026-Jan-01 14:50:51.776061
#23 6.371    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 71.0/71.0 kB 372.9 MB/s eta 0:00:00
2026-Jan-01 14:50:51.776061
#23 6.376 Downloading typing_extensions-4.15.0-py3-none-any.whl (44 kB)
2026-Jan-01 14:50:51.776061
#23 6.379    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 44.6/44.6 kB 333.3 MB/s eta 0:00:00
2026-Jan-01 14:50:51.776061
#23 6.384 Downloading certifi-2025.11.12-py3-none-any.whl (159 kB)
2026-Jan-01 14:50:51.776061
#23 6.387    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 159.4/159.4 kB 371.7 MB/s eta 0:00:00
2026-Jan-01 14:50:51.776061
#23 6.394 Downloading annotated_types-0.7.0-py3-none-any.whl (13 kB)
2026-Jan-01 14:50:51.776061
#23 6.400 Downloading typing_inspection-0.4.2-py3-none-any.whl (14 kB)
2026-Jan-01 14:50:51.776061
#23 6.567 Installing collected packages: websockets, typing-extensions, python-dotenv, psycopg2-binary, idna, h11, click, certifi, annotated-types, annotated-doc, uvicorn, typing-inspection, pydantic-core, httpcore, anyio, starlette, pydantic, httpx, fastapi
2026-Jan-01 14:50:51.776061
#23 8.473 Successfully installed annotated-doc-0.0.4 annotated-types-0.7.0 anyio-4.12.0 certifi-2025.11.12 click-8.3.1 fastapi-0.128.0 h11-0.16.0 httpcore-1.0.9 httpx-0.28.1 idna-3.11 psycopg2-binary-2.9.11 pydantic-2.12.5 pydantic-core-2.41.5 python-dotenv-1.2.1 starlette-0.50.0 typing-extensions-4.15.0 typing-inspection-0.4.2 uvicorn-0.40.0 websockets-15.0.1
2026-Jan-01 14:50:51.776061
#23 8.474 WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
2026-Jan-01 14:50:51.776061
#23 8.557
2026-Jan-01 14:50:51.776061
#23 8.557 [notice] A new release of pip is available: 24.0 -> 25.3
2026-Jan-01 14:50:51.776061
#23 8.557 [notice] To update, run: pip install --upgrade pip
2026-Jan-01 14:50:51.776061
#23 DONE 9.4s
2026-Jan-01 14:50:51.776061
2026-Jan-01 14:50:51.776061
#24 [shared-gateway-v3 5/5] COPY main.py .
2026-Jan-01 14:50:51.776061
#24 DONE 0.0s
2026-Jan-01 14:50:51.776061
2026-Jan-01 14:50:51.776061
#22 [api 3/7] RUN apt-get update && apt-get install -y     curl     gnupg     && mkdir -p /etc/apt/keyrings     && curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg     && echo     "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian     $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null     && apt-get update && apt-get install -y docker-ce-cli docker-compose-plugin     && rm -rf /var/lib/apt/lists/*
2026-Jan-01 14:50:51.776061
#22 9.647 Preparing to unpack .../20-librtmp1_2.4+20151223.gitfa8646d.1-2+b5_amd64.deb ...
2026-Jan-01 14:50:51.776061
#22 9.657 Unpacking librtmp1:amd64 (2.4+20151223.gitfa8646d.1-2+b5) ...
2026-Jan-01 14:50:51.776061
#22 9.699 Selecting previously unselected package libssh2-1t64:amd64.
2026-Jan-01 14:50:51.776061
#22 9.701 Preparing to unpack .../21-libssh2-1t64_1.11.1-1_amd64.deb ...
2026-Jan-01 14:50:51.776061
#22 9.706 Unpacking libssh2-1t64:amd64 (1.11.1-1) ...
2026-Jan-01 14:50:51.776061
#22 9.786 Selecting previously unselected package libcurl4t64:amd64.
2026-Jan-01 14:50:51.776061
#22 9.786 Preparing to unpack .../22-libcurl4t64_8.14.1-2+deb13u2_amd64.deb ...
2026-Jan-01 14:50:51.776061
#22 ...
2026-Jan-01 14:50:51.776061
2026-Jan-01 14:50:51.776061
#25 [shared-gateway-v3] exporting to image
2026-Jan-01 14:50:51.776061
#25 exporting layers
2026-Jan-01 14:50:51.995222
#25 ...
2026-Jan-01 14:50:51.995222
2026-Jan-01 14:50:51.995222
#26 [dashboard deps 4/4] RUN npm install
2026-Jan-01 14:50:52.105703
#26 ...
2026-Jan-01 14:50:52.112993
#22 [api 3/7] RUN apt-get update && apt-get install -y     curl     gnupg     && mkdir -p /etc/apt/keyrings     && curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg     && echo     "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian     $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null     && apt-get update && apt-get install -y docker-ce-cli docker-compose-plugin     && rm -rf /var/lib/apt/lists/*
2026-Jan-01 14:50:52.112993
#22 9.788 Unpacking libcurl4t64:amd64 (8.14.1-2+deb13u2) ...
2026-Jan-01 14:50:52.112993
#22 9.908 Selecting previously unselected package curl.
2026-Jan-01 14:50:52.112993
#22 9.910 Preparing to unpack .../23-curl_8.14.1-2+deb13u2_amd64.deb ...
2026-Jan-01 14:50:52.112993
#22 9.917 Unpacking curl (8.14.1-2+deb13u2) ...
2026-Jan-01 14:50:52.112993
#22 10.00 Selecting previously unselected package libgpg-error0:amd64.
2026-Jan-01 14:50:52.112993
#22 10.00 Preparing to unpack .../24-libgpg-error0_1.51-4_amd64.deb ...
2026-Jan-01 14:50:52.112993
#22 10.01 Unpacking libgpg-error0:amd64 (1.51-4) ...
2026-Jan-01 14:50:52.112993
#22 10.07 Selecting previously unselected package libassuan9:amd64.
2026-Jan-01 14:50:52.112993
#22 10.07 Preparing to unpack .../25-libassuan9_3.0.2-2_amd64.deb ...
2026-Jan-01 14:50:52.112993
#22 10.07 Unpacking libassuan9:amd64 (3.0.2-2) ...
2026-Jan-01 14:50:52.112993
#22 10.12 Selecting previously unselected package libgcrypt20:amd64.
2026-Jan-01 14:50:52.226953
#22 ...
2026-Jan-01 14:50:52.226953
2026-Jan-01 14:50:52.226953
#25 [shared-gateway-v3] exporting to image
2026-Jan-01 14:50:52.226953
#25 exporting layers 0.5s done
2026-Jan-01 14:50:52.226953
#25 writing image sha256:b5de6adc6627f03cc97aa4c2c6d5e8613fb2e2304768b2289374925fdfe58236 done
2026-Jan-01 14:50:52.226953
#25 naming to docker.io/library/sokwws8k80wcg0gss0k0goww-shared-gateway-v3 done
2026-Jan-01 14:50:52.226953
#25 DONE 0.5s
2026-Jan-01 14:50:52.226953
2026-Jan-01 14:50:52.226953
#22 [api 3/7] RUN apt-get update && apt-get install -y     curl     gnupg     && mkdir -p /etc/apt/keyrings     && curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg     && echo     "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian     $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null     && apt-get update && apt-get install -y docker-ce-cli docker-compose-plugin     && rm -rf /var/lib/apt/lists/*
2026-Jan-01 14:50:52.226953
#22 10.13 Preparing to unpack .../26-libgcrypt20_1.11.0-7_amd64.deb ...
2026-Jan-01 14:50:52.226953
#22 10.13 Unpacking libgcrypt20:amd64 (1.11.0-7) ...
2026-Jan-01 14:50:52.372618
#22 ...
2026-Jan-01 14:50:52.372618
2026-Jan-01 14:50:52.372618
#27 [shared-gateway-v3] resolving provenance for metadata file
2026-Jan-01 14:50:52.372618
#27 DONE 0.0s
2026-Jan-01 14:50:52.372618
2026-Jan-01 14:50:52.372618
#22 [api 3/7] RUN apt-get update && apt-get install -y     curl     gnupg     && mkdir -p /etc/apt/keyrings     && curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg     && echo     "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian     $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null     && apt-get update && apt-get install -y docker-ce-cli docker-compose-plugin     && rm -rf /var/lib/apt/lists/*
2026-Jan-01 14:50:52.372618
#22 10.24 Selecting previously unselected package gpgconf.
2026-Jan-01 14:50:52.372618
#22 10.24 Preparing to unpack .../27-gpgconf_2.4.7-21+b3_amd64.deb ...
2026-Jan-01 14:50:52.372618
#22 10.25 Unpacking gpgconf (2.4.7-21+b3) ...
2026-Jan-01 14:50:52.372618
#22 10.32 Selecting previously unselected package libksba8:amd64.
2026-Jan-01 14:50:52.372618
#22 10.32 Preparing to unpack .../28-libksba8_1.6.7-2+b1_amd64.deb ...
2026-Jan-01 14:50:52.372618
#22 10.33 Unpacking libksba8:amd64 (1.6.7-2+b1) ...
2026-Jan-01 14:50:52.372618
#22 10.39 Selecting previously unselected package libnpth0t64:amd64.
2026-Jan-01 14:50:52.372618
#22 10.39 Preparing to unpack .../29-libnpth0t64_1.8-3_amd64.deb ...
2026-Jan-01 14:50:52.506802
#22 10.40 Unpacking libnpth0t64:amd64 (1.8-3) ...
2026-Jan-01 14:50:52.506802
#22 10.44 Selecting previously unselected package dirmngr.
2026-Jan-01 14:50:52.506802
#22 10.44 Preparing to unpack .../30-dirmngr_2.4.7-21+b3_amd64.deb ...
2026-Jan-01 14:50:52.506802
#22 10.47 Unpacking dirmngr (2.4.7-21+b3) ...
2026-Jan-01 14:50:52.506802
#22 10.52 Selecting previously unselected package gnupg-l10n.
2026-Jan-01 14:50:52.611247
#22 10.53 Preparing to unpack .../31-gnupg-l10n_2.4.7-21_all.deb ...
2026-Jan-01 14:50:52.611247
#22 10.53 Unpacking gnupg-l10n (2.4.7-21) ...
2026-Jan-01 14:50:52.611247
#22 10.63 Selecting previously unselected package gpg.
2026-Jan-01 14:50:52.725448
#22 10.63 Preparing to unpack .../32-gpg_2.4.7-21+b3_amd64.deb ...
2026-Jan-01 14:50:52.725448
#22 10.64 Unpacking gpg (2.4.7-21+b3) ...
2026-Jan-01 14:50:52.725448
#22 10.74 Selecting previously unselected package pinentry-curses.
2026-Jan-01 14:50:52.854909
#22 10.74 Preparing to unpack .../33-pinentry-curses_1.3.1-2_amd64.deb ...
2026-Jan-01 14:50:52.854909
#22 10.74 Unpacking pinentry-curses (1.3.1-2) ...
2026-Jan-01 14:50:52.854909
#22 10.80 Selecting previously unselected package gpg-agent.
2026-Jan-01 14:50:52.854909
#22 10.81 Preparing to unpack .../34-gpg-agent_2.4.7-21+b3_amd64.deb ...
2026-Jan-01 14:50:52.854909
#22 10.81 Unpacking gpg-agent (2.4.7-21+b3) ...
2026-Jan-01 14:50:52.854909
#22 10.87 Selecting previously unselected package gpgsm.
2026-Jan-01 14:50:52.854909
#22 10.87 Preparing to unpack .../35-gpgsm_2.4.7-21+b3_amd64.deb ...
2026-Jan-01 14:50:52.965774
#22 10.88 Unpacking gpgsm (2.4.7-21+b3) ...
2026-Jan-01 14:50:52.965774
#22 10.93 Selecting previously unselected package gnupg.
2026-Jan-01 14:50:52.965774
#22 10.94 Preparing to unpack .../36-gnupg_2.4.7-21_all.deb ...
2026-Jan-01 14:50:52.965774
#22 10.94 Unpacking gnupg (2.4.7-21) ...
2026-Jan-01 14:50:52.965774
#22 10.98 Selecting previously unselected package gpg-wks-client.
2026-Jan-01 14:50:53.093919
#22 10.98 Preparing to unpack .../37-gpg-wks-client_2.4.7-21+b3_amd64.deb ...
2026-Jan-01 14:50:53.093919
#22 10.99 Unpacking gpg-wks-client (2.4.7-21+b3) ...
2026-Jan-01 14:50:53.093919
#22 11.03 Selecting previously unselected package gpgv.
2026-Jan-01 14:50:53.093919
#22 11.04 Preparing to unpack .../38-gpgv_2.4.7-21+b3_amd64.deb ...
2026-Jan-01 14:50:53.093919
#22 11.04 Unpacking gpgv (2.4.7-21+b3) ...
2026-Jan-01 14:50:53.093919
#22 11.11 Selecting previously unselected package libgpg-error-l10n.
2026-Jan-01 14:50:53.203598
#22 11.12 Preparing to unpack .../39-libgpg-error-l10n_1.51-4_all.deb ...
2026-Jan-01 14:50:53.213803
#22 11.13 Unpacking libgpg-error-l10n (1.51-4) ...
2026-Jan-01 14:50:53.213803
#22 11.17 Selecting previously unselected package libldap-common.
2026-Jan-01 14:50:53.213803
#22 11.17 Preparing to unpack .../40-libldap-common_2.6.10+dfsg-1_all.deb ...
2026-Jan-01 14:50:53.213803
#22 11.17 Unpacking libldap-common (2.6.10+dfsg-1) ...
2026-Jan-01 14:50:53.213803
#22 11.21 Selecting previously unselected package libsasl2-modules:amd64.
2026-Jan-01 14:50:53.213803
#22 11.21 Preparing to unpack .../41-libsasl2-modules_2.1.28+dfsg1-9_amd64.deb ...
2026-Jan-01 14:50:53.213803
#22 11.22 Unpacking libsasl2-modules:amd64 (2.1.28+dfsg1-9) ...
2026-Jan-01 14:50:53.350907
#22 11.26 Selecting previously unselected package publicsuffix.
2026-Jan-01 14:50:53.350907
#22 11.27 Preparing to unpack .../42-publicsuffix_20250328.1952-0.1_all.deb ...
2026-Jan-01 14:50:53.350907
#22 11.27 Unpacking publicsuffix (20250328.1952-0.1) ...
2026-Jan-01 14:50:53.350907
#22 11.36 Selecting previously unselected package gnupg-utils.
2026-Jan-01 14:50:53.448894
#22 11.37 Preparing to unpack .../43-gnupg-utils_2.4.7-21+b3_amd64.deb ...
2026-Jan-01 14:50:53.448894
#22 11.37 Unpacking gnupg-utils (2.4.7-21+b3) ...
2026-Jan-01 14:50:53.448894
#22 11.46 Setting up libnpth0t64:amd64 (1.8-3) ...
2026-Jan-01 14:50:53.448894
#22 11.47 Setting up libkeyutils1:amd64 (1.6.3-6) ...
2026-Jan-01 14:50:53.554442
#22 11.47 Setting up libgpg-error0:amd64 (1.51-4) ...
2026-Jan-01 14:50:53.554442
#22 11.48 Setting up libbrotli1:amd64 (1.1.0-2+b7) ...
2026-Jan-01 14:50:53.554442
#22 11.48 Setting up libsasl2-modules:amd64 (2.1.28+dfsg1-9) ...
2026-Jan-01 14:50:53.554442
#22 11.50 Setting up libnghttp2-14:amd64 (1.64.0-1.1) ...
2026-Jan-01 14:50:53.554442
#22 11.51 Setting up libgcrypt20:amd64 (1.11.0-7) ...
2026-Jan-01 14:50:53.554442
#22 11.52 Setting up krb5-locales (1.21.3-5) ...
2026-Jan-01 14:50:53.554442
#22 11.52 Setting up libcom-err2:amd64 (1.47.2-3+b3) ...
2026-Jan-01 14:50:53.554442
#22 11.53 Setting up libldap-common (2.6.10+dfsg-1) ...
2026-Jan-01 14:50:53.554442
#22 11.54 Setting up libkrb5support0:amd64 (1.21.3-5) ...
2026-Jan-01 14:50:53.554442
#22 11.55 Setting up libsasl2-modules-db:amd64 (2.1.28+dfsg1-9) ...
2026-Jan-01 14:50:53.554442
#22 11.57 Setting up gnupg-l10n (2.4.7-21) ...
2026-Jan-01 14:50:53.656520
#22 11.58 Setting up bash-completion (1:2.16.0-7) ...
2026-Jan-01 14:50:53.656520
#22 11.60 Setting up libp11-kit0:amd64 (0.25.5-3) ...
2026-Jan-01 14:50:53.656520
#22 11.61 Setting up libunistring5:amd64 (1.3-2) ...
2026-Jan-01 14:50:53.656520
#22 11.61 Setting up libk5crypto3:amd64 (1.21.3-5) ...
2026-Jan-01 14:50:53.656520
#22 11.62 Setting up libsasl2-2:amd64 (2.1.28+dfsg1-9) ...
2026-Jan-01 14:50:53.656520
#22 11.63 Setting up libnghttp3-9:amd64 (1.8.0-1) ...
2026-Jan-01 14:50:53.656520
#22 11.63 Setting up gpgv (2.4.7-21+b3) ...
2026-Jan-01 14:50:53.656520
#22 11.64 Setting up libassuan9:amd64 (3.0.2-2) ...
2026-Jan-01 14:50:53.656520
#22 11.65 Setting up gpgconf (2.4.7-21+b3) ...
2026-Jan-01 14:50:53.656520
#22 11.66 Setting up libtasn1-6:amd64 (4.20.0-2) ...
2026-Jan-01 14:50:53.656520
#22 11.67 Setting up libkrb5-3:amd64 (1.21.3-5) ...
2026-Jan-01 14:50:53.656520
#22 11.67 Setting up libssh2-1t64:amd64 (1.11.1-1) ...
2026-Jan-01 14:50:53.851526
2026-Jan-01 14:50:53.860902
#22 11.68 Setting up libgpg-error-l10n (1.51-4) ...
2026-Jan-01 14:50:53.860902
#22 11.69 Setting up publicsuffix (20250328.1952-0.1) ...
2026-Jan-01 14:50:53.860902
#22 11.70 Setting up libldap2:amd64 (2.6.10+dfsg-1) ...
2026-Jan-01 14:50:53.860902
#22 11.70 Setting up libksba8:amd64 (1.6.7-2+b1) ...
2026-Jan-01 14:50:53.860902
#22 11.71 Setting up pinentry-curses (1.3.1-2) ...
2026-Jan-01 14:50:53.860902
#22 11.72 Setting up gpg-agent (2.4.7-21+b3) ...
2026-Jan-01 14:50:54.204496
#22 12.22 Setting up gpgsm (2.4.7-21+b3) ...
2026-Jan-01 14:50:54.211249
2026-Jan-01 14:50:54.337068
#22 12.23 Setting up libidn2-0:amd64 (2.3.8-2) ...
2026-Jan-01 14:50:54.337068
#22 12.24 Setting up libgssapi-krb5-2:amd64 (1.21.3-5) ...
2026-Jan-01 14:50:54.337068
#22 12.25 Setting up gpg (2.4.7-21+b3) ...
2026-Jan-01 14:50:54.337068
#22 12.35 Setting up gnupg-utils (2.4.7-21+b3) ...
2026-Jan-01 14:50:54.509986
#22 12.36 Setting up libgnutls30t64:amd64 (3.8.9-3) ...
2026-Jan-01 14:50:54.509986
#22 12.37 Setting up libpsl5t64:amd64 (0.21.2-1.1+b1) ...
2026-Jan-01 14:50:54.509986
#22 12.38 Setting up dirmngr (2.4.7-21+b3) ...
2026-Jan-01 14:50:54.518792
#22 12.53 Setting up librtmp1:amd64 (2.4+20151223.gitfa8646d.1-2+b5) ...
2026-Jan-01 14:50:54.710223
#22 12.54 Setting up gnupg (2.4.7-21) ...
2026-Jan-01 14:50:54.710223
#22 12.55 Setting up gpg-wks-client (2.4.7-21+b3) ...
2026-Jan-01 14:50:54.710223
#22 12.56 Setting up libcurl4t64:amd64 (8.14.1-2+deb13u2) ...
2026-Jan-01 14:50:54.710223
#22 12.57 Setting up curl (8.14.1-2+deb13u2) ...
2026-Jan-01 14:50:54.710223
#22 12.58 Processing triggers for libc-bin (2.41-12) ...
2026-Jan-01 14:50:54.781887
#22 12.80 Hit:1 http://deb.debian.org/debian trixie InRelease
2026-Jan-01 14:50:54.781887
#22 12.80 Hit:2 http://deb.debian.org/debian trixie-updates InRelease
2026-Jan-01 14:50:54.905312
#22 12.81 Hit:3 http://deb.debian.org/debian-security trixie-security InRelease
2026-Jan-01 14:50:54.905312
#22 12.82 Get:4 https://download.docker.com/linux/debian trixie InRelease [32.5 kB]
2026-Jan-01 14:50:54.905312
#22 12.86 Get:5 https://download.docker.com/linux/debian trixie/stable amd64 Packages [23.2 kB]
2026-Jan-01 14:50:54.905312
#22 12.92 Fetched 55.7 kB in 0s (325 kB/s)
2026-Jan-01 14:50:54.905312
#22 12.92 Reading package lists...
2026-Jan-01 14:50:55.799884
2026-Jan-01 14:50:56.001221
#22 13.87 Reading package lists...
2026-Jan-01 14:50:56.600778
2026-Jan-01 14:50:56.773598
#22 14.64 Building dependency tree...
2026-Jan-01 14:50:56.813667
#22 14.82 Reading state information...
2026-Jan-01 14:50:56.955122
2026-Jan-01 14:50:57.181993
#22 15.20 The following additional packages will be installed:
2026-Jan-01 14:50:57.315942
#22 15.20   docker-buildx-plugin
2026-Jan-01 14:50:57.315942
#22 15.21 Suggested packages:
2026-Jan-01 14:50:57.315942
#22 15.21   docker-model-plugin
2026-Jan-01 14:50:57.315942
#22 15.23 The following NEW packages will be installed:
2026-Jan-01 14:50:57.315942
#22 15.24   docker-buildx-plugin docker-ce-cli docker-compose-plugin
2026-Jan-01 14:50:57.315942
#22 15.33 0 upgraded, 3 newly installed, 0 to remove and 0 not upgraded.
2026-Jan-01 14:50:57.315942
#22 15.33 Need to get 40.4 MB of archives.
2026-Jan-01 14:50:57.315942
#22 15.33 After this operation, 157 MB of additional disk space will be used.
2026-Jan-01 14:50:57.315942
#22 15.33 Get:1 https://download.docker.com/linux/debian trixie/stable amd64 docker-buildx-plugin amd64 0.30.1-1~debian.13~trixie [16.4 MB]
2026-Jan-01 14:50:57.597695
#22 15.61 Get:2 https://download.docker.com/linux/debian trixie/stable amd64 docker-ce-cli amd64 5:29.1.3-1~debian.13~trixie [16.3 MB]
2026-Jan-01 14:50:58.096195
#22 16.11 Get:3 https://download.docker.com/linux/debian trixie/stable amd64 docker-compose-plugin amd64 5.0.0-1~debian.13~trixie [7708 kB]
2026-Jan-01 14:50:58.107598
2026-Jan-01 14:50:58.352031
#22 16.37 debconf: unable to initialize frontend: Dialog
2026-Jan-01 14:50:58.352031
#22 16.37 debconf: (TERM is not set, so the dialog frontend is not usable.)
2026-Jan-01 14:50:58.352031
#22 16.37 debconf: falling back to frontend: Readline
2026-Jan-01 14:50:58.352031
#22 16.37 debconf: unable to initialize frontend: Readline
2026-Jan-01 14:50:58.352031
#22 16.37 debconf: (Can't locate Term/ReadLine.pm in @INC (you may need to install the Term::ReadLine module) (@INC entries checked: /etc/perl /usr/local/lib/x86_64-linux-gnu/perl/5.40.1 /usr/local/share/perl/5.40.1 /usr/lib/x86_64-linux-gnu/perl5/5.40 /usr/share/perl5 /usr/lib/x86_64-linux-gnu/perl-base /usr/lib/x86_64-linux-gnu/perl/5.40 /usr/share/perl/5.40 /usr/local/lib/site_perl) at /usr/share/perl5/Debconf/FrontEnd/Readline.pm line 8, <STDIN> line 3.)
2026-Jan-01 14:50:58.352031
#22 16.37 debconf: falling back to frontend: Teletype
2026-Jan-01 14:50:58.526551
#22 16.39 debconf: unable to initialize frontend: Teletype
2026-Jan-01 14:50:58.526551
#22 16.39 debconf: (This frontend requires a controlling tty.)
2026-Jan-01 14:50:58.526551
#22 16.39 debconf: falling back to frontend: Noninteractive
2026-Jan-01 14:50:59.598570
#22 17.62 Fetched 40.4 MB in 1s (42.0 MB/s)
2026-Jan-01 14:50:59.820370
#22 17.65 Selecting previously unselected package docker-buildx-plugin.
2026-Jan-01 14:50:59.820370
#22 17.65 (Reading database ... 
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
2026-Jan-01 14:50:59.820370
#22 17.68 Preparing to unpack .../docker-buildx-plugin_0.30.1-1~debian.13~trixie_amd64.deb ...
2026-Jan-01 14:50:59.834177
#22 17.69 Unpacking docker-buildx-plugin (0.30.1-1~debian.13~trixie) ...
2026-Jan-01 14:51:01.439209
#22 19.46 Selecting previously unselected package docker-ce-cli.
2026-Jan-01 14:51:01.439209
#22 19.46 Preparing to unpack .../docker-ce-cli_5%3a29.1.3-1~debian.13~trixie_amd64.deb ...
2026-Jan-01 14:51:01.595290
#22 19.46 Unpacking docker-ce-cli (5:29.1.3-1~debian.13~trixie) ...
2026-Jan-01 14:51:02.121685
#22 20.14 Selecting previously unselected package docker-compose-plugin.
2026-Jan-01 14:51:02.284367
#22 20.14 Preparing to unpack .../docker-compose-plugin_5.0.0-1~debian.13~trixie_amd64.deb ...
2026-Jan-01 14:51:02.284367
#22 20.15 Unpacking docker-compose-plugin (5.0.0-1~debian.13~trixie) ...
2026-Jan-01 14:51:02.843654
#22 20.86 Setting up docker-buildx-plugin (0.30.1-1~debian.13~trixie) ...
2026-Jan-01 14:51:03.013008
#22 20.87 Setting up docker-compose-plugin (5.0.0-1~debian.13~trixie) ...
2026-Jan-01 14:51:03.013008
#22 20.88 Setting up docker-ce-cli (5:29.1.3-1~debian.13~trixie) ...
2026-Jan-01 14:51:03.310036
#22 DONE 21.3s
2026-Jan-01 14:51:03.310036
2026-Jan-01 14:51:03.310036
#26 [dashboard deps 4/4] RUN npm install
2026-Jan-01 14:51:03.484161
#26 ...
2026-Jan-01 14:51:03.484161
2026-Jan-01 14:51:03.484161
#28 [api 4/7] COPY control-plane/api/requirements.txt .
2026-Jan-01 14:51:03.521334
#28 DONE 0.2s
2026-Jan-01 14:51:03.521334
2026-Jan-01 14:51:03.521334
#26 [dashboard deps 4/4] RUN npm install
2026-Jan-01 14:51:03.664677
#26 ...
2026-Jan-01 14:51:03.664677
2026-Jan-01 14:51:03.664677
#29 [api 5/7] RUN pip install -r requirements.txt
2026-Jan-01 14:51:06.004862
#29 2.515 Collecting fastapi (from -r requirements.txt (line 1))
2026-Jan-01 14:51:06.182653
#29 2.543   Downloading fastapi-0.128.0-py3-none-any.whl.metadata (30 kB)
2026-Jan-01 14:51:06.296651
#29 2.806 Collecting sqlalchemy (from -r requirements.txt (line 3))
2026-Jan-01 14:51:06.305994
2026-Jan-01 14:51:06.426600
#29 2.814   Downloading sqlalchemy-2.0.45-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (9.5 kB)
2026-Jan-01 14:51:06.426600
#29 2.897 Collecting psycopg2-binary (from -r requirements.txt (line 4))
2026-Jan-01 14:51:06.426600
#29 2.904   Downloading psycopg2_binary-2.9.11-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (4.9 kB)
2026-Jan-01 14:51:06.426600
#29 2.935 Collecting httpx (from -r requirements.txt (line 5))
2026-Jan-01 14:51:06.551434
#29 2.936   Downloading httpx-0.28.1-py3-none-any.whl.metadata (7.1 kB)
2026-Jan-01 14:51:06.551434
#29 2.994 Collecting python-keycloak (from -r requirements.txt (line 6))
2026-Jan-01 14:51:06.551434
#29 3.001   Downloading python_keycloak-6.0.0-py3-none-any.whl.metadata (6.1 kB)
2026-Jan-01 14:51:06.551434
#29 3.061 Collecting minio (from -r requirements.txt (line 7))
2026-Jan-01 14:51:06.681025
#29 3.068   Downloading minio-7.2.20-py3-none-any.whl.metadata (6.5 kB)
2026-Jan-01 14:51:06.681025
#29 3.128 Collecting requests (from -r requirements.txt (line 8))
2026-Jan-01 14:51:06.681025
#29 3.140   Downloading requests-2.32.5-py3-none-any.whl.metadata (4.9 kB)
2026-Jan-01 14:51:06.681025
#29 3.183 Collecting python-dotenv (from -r requirements.txt (line 9))
2026-Jan-01 14:51:06.867531
#29 3.186   Downloading python_dotenv-1.2.1-py3-none-any.whl.metadata (25 kB)
2026-Jan-01 14:51:06.867531
#29 3.243 Collecting bcrypt<4.1.0 (from -r requirements.txt (line 11))
2026-Jan-01 14:51:06.867531
#29 3.249   Downloading bcrypt-4.0.1-cp36-abi3-manylinux_2_28_x86_64.whl.metadata (9.0 kB)
2026-Jan-01 14:51:06.867531
#29 3.269 Collecting python-multipart (from -r requirements.txt (line 13))
2026-Jan-01 14:51:06.867531
#29 3.274   Downloading python_multipart-0.0.21-py3-none-any.whl.metadata (1.8 kB)
2026-Jan-01 14:51:06.867531
#29 3.377 Collecting stripe (from -r requirements.txt (line 14))
2026-Jan-01 14:51:06.985969
#29 3.385   Downloading stripe-14.1.0-py3-none-any.whl.metadata (18 kB)
2026-Jan-01 14:51:06.985969
#29 3.413 Collecting prometheus_client (from -r requirements.txt (line 15))
2026-Jan-01 14:51:06.985969
#29 3.417   Downloading prometheus_client-0.23.1-py3-none-any.whl.metadata (1.9 kB)
2026-Jan-01 14:51:06.985969
#29 3.444 Collecting APScheduler (from -r requirements.txt (line 16))
2026-Jan-01 14:51:06.985969
#29 3.450   Downloading apscheduler-3.11.2-py3-none-any.whl.metadata (6.4 kB)
2026-Jan-01 14:51:06.985969
#29 3.496 Collecting uvicorn[standard] (from -r requirements.txt (line 2))
2026-Jan-01 14:51:07.099716
#29 3.503   Downloading uvicorn-0.40.0-py3-none-any.whl.metadata (6.7 kB)
2026-Jan-01 14:51:07.109145
#29 3.529 Collecting passlib[bcrypt] (from -r requirements.txt (line 10))
2026-Jan-01 14:51:07.109145
#29 3.536   Downloading passlib-1.7.4-py2.py3-none-any.whl.metadata (1.7 kB)
2026-Jan-01 14:51:07.109145
#29 3.563 Collecting python-jose[cryptography] (from -r requirements.txt (line 12))
2026-Jan-01 14:51:07.109145
#29 3.568   Downloading python_jose-3.5.0-py2.py3-none-any.whl.metadata (5.5 kB)
2026-Jan-01 14:51:07.109145
#29 3.611 Collecting starlette<0.51.0,>=0.40.0 (from fastapi->-r requirements.txt (line 1))
2026-Jan-01 14:51:07.204173
#29 3.618   Downloading starlette-0.50.0-py3-none-any.whl.metadata (6.3 kB)
2026-Jan-01 14:51:07.204173
#29 3.714 Collecting pydantic>=2.7.0 (from fastapi->-r requirements.txt (line 1))
2026-Jan-01 14:51:07.306273
#29 3.722   Downloading pydantic-2.12.5-py3-none-any.whl.metadata (90 kB)
2026-Jan-01 14:51:07.314487
#29 3.747 Collecting typing-extensions>=4.8.0 (from fastapi->-r requirements.txt (line 1))
2026-Jan-01 14:51:07.314487
#29 3.750   Downloading typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
2026-Jan-01 14:51:07.314487
#29 3.767 Collecting annotated-doc>=0.0.2 (from fastapi->-r requirements.txt (line 1))
2026-Jan-01 14:51:07.314487
#29 3.772   Downloading annotated_doc-0.0.4-py3-none-any.whl.metadata (6.6 kB)
2026-Jan-01 14:51:07.314487
#29 3.793 Collecting click>=7.0 (from uvicorn[standard]->-r requirements.txt (line 2))
2026-Jan-01 14:51:07.314487
#29 3.796   Downloading click-8.3.1-py3-none-any.whl.metadata (2.6 kB)
2026-Jan-01 14:51:07.314487
#29 3.816 Collecting h11>=0.8 (from uvicorn[standard]->-r requirements.txt (line 2))
2026-Jan-01 14:51:07.445345
#29 3.823   Downloading h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
2026-Jan-01 14:51:07.445345
#29 3.858 Collecting httptools>=0.6.3 (from uvicorn[standard]->-r requirements.txt (line 2))
2026-Jan-01 14:51:07.445345
#29 3.866   Downloading httptools-0.7.1-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (3.5 kB)
2026-Jan-01 14:51:07.445345
#29 3.909 Collecting pyyaml>=5.1 (from uvicorn[standard]->-r requirements.txt (line 2))
2026-Jan-01 14:51:07.445345
#29 3.915   Downloading pyyaml-6.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.4 kB)
2026-Jan-01 14:51:07.445345
#29 3.955 Collecting uvloop>=0.15.1 (from uvicorn[standard]->-r requirements.txt (line 2))
2026-Jan-01 14:51:07.548878
#29 3.965   Downloading uvloop-0.22.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (4.9 kB)
2026-Jan-01 14:51:07.558180
#29 4.052 Collecting watchfiles>=0.13 (from uvicorn[standard]->-r requirements.txt (line 2))
2026-Jan-01 14:51:07.558180
#29 4.059   Downloading watchfiles-1.1.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.9 kB)
2026-Jan-01 14:51:07.739440
#29 4.131 Collecting websockets>=10.4 (from uvicorn[standard]->-r requirements.txt (line 2))
2026-Jan-01 14:51:07.747769
#29 4.142   Downloading websockets-15.0.1-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.8 kB)
2026-Jan-01 14:51:07.747769
#29 4.249 Collecting greenlet>=1 (from sqlalchemy->-r requirements.txt (line 3))
2026-Jan-01 14:51:07.867359
#29 4.270   Downloading greenlet-3.3.0-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (4.1 kB)
2026-Jan-01 14:51:07.867359
#29 4.299 Collecting anyio (from httpx->-r requirements.txt (line 5))
2026-Jan-01 14:51:07.867359
#29 4.301   Downloading anyio-4.12.0-py3-none-any.whl.metadata (4.3 kB)
2026-Jan-01 14:51:07.867359
#29 4.325 Collecting certifi (from httpx->-r requirements.txt (line 5))
2026-Jan-01 14:51:07.867359
#29 4.331   Downloading certifi-2025.11.12-py3-none-any.whl.metadata (2.5 kB)
2026-Jan-01 14:51:07.867359
#29 4.371 Collecting httpcore==1.* (from httpx->-r requirements.txt (line 5))
2026-Jan-01 14:51:07.975676
#29 4.378   Downloading httpcore-1.0.9-py3-none-any.whl.metadata (21 kB)
2026-Jan-01 14:51:07.975676
#29 4.416 Collecting idna (from httpx->-r requirements.txt (line 5))
2026-Jan-01 14:51:07.975676
#29 4.423   Downloading idna-3.11-py3-none-any.whl.metadata (8.4 kB)
2026-Jan-01 14:51:07.975676
#29 4.465 Collecting aiofiles>=24.1.0 (from python-keycloak->-r requirements.txt (line 6))
2026-Jan-01 14:51:07.975676
#29 4.468   Downloading aiofiles-25.1.0-py3-none-any.whl.metadata (6.3 kB)
2026-Jan-01 14:51:07.975676
#29 4.487 Collecting async-property>=0.2.2 (from python-keycloak->-r requirements.txt (line 6))
2026-Jan-01 14:51:08.095754
#29 4.494   Downloading async_property-0.2.2-py2.py3-none-any.whl.metadata (5.3 kB)
2026-Jan-01 14:51:08.095754
#29 4.524 Collecting deprecation>=2.1.0 (from python-keycloak->-r requirements.txt (line 6))
2026-Jan-01 14:51:08.095754
#29 4.528   Downloading deprecation-2.1.0-py2.py3-none-any.whl.metadata (4.6 kB)
2026-Jan-01 14:51:08.095754
#29 4.565 Collecting jwcrypto>=1.5.4 (from python-keycloak->-r requirements.txt (line 6))
2026-Jan-01 14:51:08.095754
#29 4.571   Downloading jwcrypto-1.5.6-py3-none-any.whl.metadata (3.1 kB)
2026-Jan-01 14:51:08.095754
#29 4.606 Collecting requests-toolbelt>=0.6.0 (from python-keycloak->-r requirements.txt (line 6))
2026-Jan-01 14:51:08.232413
#29 4.615   Downloading requests_toolbelt-1.0.0-py2.py3-none-any.whl.metadata (14 kB)
2026-Jan-01 14:51:08.232413
#29 4.650 Collecting argon2-cffi (from minio->-r requirements.txt (line 7))
2026-Jan-01 14:51:08.232413
#29 4.654   Downloading argon2_cffi-25.1.0-py3-none-any.whl.metadata (4.1 kB)
2026-Jan-01 14:51:08.232413
#29 4.743 Collecting pycryptodome (from minio->-r requirements.txt (line 7))
2026-Jan-01 14:51:08.392148
#29 4.747   Downloading pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (3.4 kB)
2026-Jan-01 14:51:08.392148
#29 4.775 Collecting urllib3 (from minio->-r requirements.txt (line 7))
2026-Jan-01 14:51:08.392148
#29 4.781   Downloading urllib3-2.6.2-py3-none-any.whl.metadata (6.6 kB)
2026-Jan-01 14:51:08.392148
#29 4.902 Collecting charset_normalizer<4,>=2 (from requests->-r requirements.txt (line 8))
2026-Jan-01 14:51:08.507170
#29 4.908   Downloading charset_normalizer-3.4.4-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (37 kB)
2026-Jan-01 14:51:08.507170
#29 4.976 Collecting ecdsa!=0.15 (from python-jose[cryptography]->-r requirements.txt (line 12))
2026-Jan-01 14:51:08.507170
#29 4.980   Downloading ecdsa-0.19.1-py2.py3-none-any.whl.metadata (29 kB)
2026-Jan-01 14:51:08.507170
#29 5.017 Collecting rsa!=4.1.1,!=4.4,<5.0,>=4.0 (from python-jose[cryptography]->-r requirements.txt (line 12))
2026-Jan-01 14:51:08.702732
#29 5.022   Downloading rsa-4.9.1-py3-none-any.whl.metadata (5.6 kB)
2026-Jan-01 14:51:08.702732
#29 5.058 Collecting pyasn1>=0.5.0 (from python-jose[cryptography]->-r requirements.txt (line 12))
2026-Jan-01 14:51:08.702732
#29 5.063   Downloading pyasn1-0.6.1-py3-none-any.whl.metadata (8.4 kB)
2026-Jan-01 14:51:08.778506
#29 5.289 Collecting cryptography>=3.4.0 (from python-jose[cryptography]->-r requirements.txt (line 12))
2026-Jan-01 14:51:08.883056
#29 5.294   Downloading cryptography-46.0.3-cp311-abi3-manylinux_2_34_x86_64.whl.metadata (5.7 kB)
2026-Jan-01 14:51:08.883056
#29 5.385 Collecting tzlocal>=3.0 (from APScheduler->-r requirements.txt (line 16))
2026-Jan-01 14:51:08.883056
#29 5.391   Downloading tzlocal-5.3.1-py3-none-any.whl.metadata (7.6 kB)
2026-Jan-01 14:51:09.069540
#29 5.580 Collecting cffi>=2.0.0 (from cryptography>=3.4.0->python-jose[cryptography]->-r requirements.txt (line 12))
2026-Jan-01 14:51:09.174066
#29 5.589   Downloading cffi-2.0.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (2.6 kB)
2026-Jan-01 14:51:09.174066
#29 5.624 Collecting packaging (from deprecation>=2.1.0->python-keycloak->-r requirements.txt (line 6))
2026-Jan-01 14:51:09.174066
#29 5.634   Downloading packaging-25.0-py3-none-any.whl.metadata (3.3 kB)
2026-Jan-01 14:51:09.174066
#29 5.675 Collecting six>=1.9.0 (from ecdsa!=0.15->python-jose[cryptography]->-r requirements.txt (line 12))
2026-Jan-01 14:51:09.174066
#29 5.683   Downloading six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
2026-Jan-01 14:51:09.395985
#29 5.746 Collecting annotated-types>=0.6.0 (from pydantic>=2.7.0->fastapi->-r requirements.txt (line 1))
2026-Jan-01 14:51:09.395985
#29 5.754   Downloading annotated_types-0.7.0-py3-none-any.whl.metadata (15 kB)
2026-Jan-01 14:51:10.195956
#29 6.707 Collecting pydantic-core==2.41.5 (from pydantic>=2.7.0->fastapi->-r requirements.txt (line 1))
2026-Jan-01 14:51:10.414267
#29 6.712   Downloading pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (7.3 kB)
2026-Jan-01 14:51:10.414267
#29 6.782 Collecting typing-inspection>=0.4.2 (from pydantic>=2.7.0->fastapi->-r requirements.txt (line 1))
2026-Jan-01 14:51:10.414267
#29 6.792   Downloading typing_inspection-0.4.2-py3-none-any.whl.metadata (2.6 kB)
2026-Jan-01 14:51:10.414267
#29 6.925 Collecting argon2-cffi-bindings (from argon2-cffi->minio->-r requirements.txt (line 7))
2026-Jan-01 14:51:10.518222
#29 6.933   Downloading argon2_cffi_bindings-25.1.0-cp39-abi3-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl.metadata (7.4 kB)
2026-Jan-01 14:51:10.518222
#29 6.975 Collecting pycparser (from cffi>=2.0.0->cryptography>=3.4.0->python-jose[cryptography]->-r requirements.txt (line 12))
2026-Jan-01 14:51:10.518222
#29 6.981   Downloading pycparser-2.23-py3-none-any.whl.metadata (993 bytes)
2026-Jan-01 14:51:10.518222
#29 7.028 Downloading fastapi-0.128.0-py3-none-any.whl (103 kB)
2026-Jan-01 14:51:10.629754
#29 7.044 Downloading sqlalchemy-2.0.45-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (3.3 MB)
2026-Jan-01 14:51:10.629754
#29 7.140    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.3/3.3 MB 35.3 MB/s eta 0:00:00
2026-Jan-01 14:51:10.733956
2026-Jan-01 14:51:10.743759
#29 7.156 Downloading psycopg2_binary-2.9.11-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (4.2 MB)
2026-Jan-01 14:51:10.743759
#29 7.223    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.2/4.2 MB 66.7 MB/s eta 0:00:00
2026-Jan-01 14:51:10.743759
#29 7.233 Downloading httpx-0.28.1-py3-none-any.whl (73 kB)
2026-Jan-01 14:51:10.743759
#29 7.244 Downloading httpcore-1.0.9-py3-none-any.whl (78 kB)
2026-Jan-01 14:51:10.860158
#29 7.263 Downloading python_keycloak-6.0.0-py3-none-any.whl (80 kB)
2026-Jan-01 14:51:10.860158
#29 7.272 Downloading minio-7.2.20-py3-none-any.whl (93 kB)
2026-Jan-01 14:51:10.860158
#29 7.282 Downloading requests-2.32.5-py3-none-any.whl (64 kB)
2026-Jan-01 14:51:10.860158
#29 7.290 Downloading python_dotenv-1.2.1-py3-none-any.whl (21 kB)
2026-Jan-01 14:51:10.860158
#29 7.313 Downloading bcrypt-4.0.1-cp36-abi3-manylinux_2_28_x86_64.whl (593 kB)
2026-Jan-01 14:51:10.860158
#29 7.333    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 593.7/593.7 kB 27.6 MB/s eta 0:00:00
2026-Jan-01 14:51:10.860158
#29 7.343 Downloading python_multipart-0.0.21-py3-none-any.whl (24 kB)
2026-Jan-01 14:51:10.860158
#29 7.361 Downloading stripe-14.1.0-py3-none-any.whl (2.1 MB)
2026-Jan-01 14:51:10.957039
#29 7.402    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 81.1 MB/s eta 0:00:00
2026-Jan-01 14:51:10.957039
#29 7.409 Downloading prometheus_client-0.23.1-py3-none-any.whl (61 kB)
2026-Jan-01 14:51:10.957039
#29 7.422 Downloading apscheduler-3.11.2-py3-none-any.whl (64 kB)
2026-Jan-01 14:51:10.957039
#29 7.434 Downloading aiofiles-25.1.0-py3-none-any.whl (14 kB)
2026-Jan-01 14:51:10.957039
#29 7.444 Downloading annotated_doc-0.0.4-py3-none-any.whl (5.3 kB)
2026-Jan-01 14:51:10.957039
#29 7.458 Downloading async_property-0.2.2-py2.py3-none-any.whl (9.5 kB)
2026-Jan-01 14:51:10.957039
#29 7.467 Downloading certifi-2025.11.12-py3-none-any.whl (159 kB)
2026-Jan-01 14:51:11.147660
#29 7.479 Downloading charset_normalizer-3.4.4-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (153 kB)
2026-Jan-01 14:51:11.147660
#29 7.490 Downloading click-8.3.1-py3-none-any.whl (108 kB)
2026-Jan-01 14:51:11.147660
#29 7.503 Downloading cryptography-46.0.3-cp311-abi3-manylinux_2_34_x86_64.whl (4.5 MB)
2026-Jan-01 14:51:11.289907
#29 7.800    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.5/4.5 MB 44.2 MB/s eta 0:00:00
2026-Jan-01 14:51:11.395033
#29 7.813 Downloading deprecation-2.1.0-py2.py3-none-any.whl (11 kB)
2026-Jan-01 14:51:11.395033
#29 7.828 Downloading ecdsa-0.19.1-py2.py3-none-any.whl (150 kB)
2026-Jan-01 14:51:11.395033
#29 7.841 Downloading greenlet-3.3.0-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (609 kB)
2026-Jan-01 14:51:11.395033
#29 7.853    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 609.9/609.9 kB 56.2 MB/s eta 0:00:00
2026-Jan-01 14:51:11.395033
#29 7.859 Downloading h11-0.16.0-py3-none-any.whl (37 kB)
2026-Jan-01 14:51:11.395033
#29 7.869 Downloading httptools-0.7.1-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (517 kB)
2026-Jan-01 14:51:11.395033
#29 7.884 Downloading idna-3.11-py3-none-any.whl (71 kB)
2026-Jan-01 14:51:11.395033
#29 7.895 Downloading jwcrypto-1.5.6-py3-none-any.whl (92 kB)
2026-Jan-01 14:51:11.395033
#29 7.905 Downloading pyasn1-0.6.1-py3-none-any.whl (83 kB)
2026-Jan-01 14:51:11.509525
#29 7.920 Downloading pydantic-2.12.5-py3-none-any.whl (463 kB)
2026-Jan-01 14:51:11.509525
#29 7.930 Downloading pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.1 MB)
2026-Jan-01 14:51:11.509525
#29 7.961    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 71.7 MB/s eta 0:00:00
2026-Jan-01 14:51:11.509525
#29 7.971 Downloading pyyaml-6.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (807 kB)
2026-Jan-01 14:51:11.509525
#29 7.988    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 807.9/807.9 kB 58.8 MB/s eta 0:00:00
2026-Jan-01 14:51:11.509525
#29 7.993 Downloading requests_toolbelt-1.0.0-py2.py3-none-any.whl (54 kB)
2026-Jan-01 14:51:11.509525
#29 8.004 Downloading rsa-4.9.1-py3-none-any.whl (34 kB)
2026-Jan-01 14:51:11.509525
#29 8.019 Downloading starlette-0.50.0-py3-none-any.whl (74 kB)
2026-Jan-01 14:51:11.735108
#29 8.030 Downloading anyio-4.12.0-py3-none-any.whl (113 kB)
2026-Jan-01 14:51:11.735108
#29 8.060 Downloading typing_extensions-4.15.0-py3-none-any.whl (44 kB)
2026-Jan-01 14:51:11.735108
#29 8.071 Downloading tzlocal-5.3.1-py3-none-any.whl (18 kB)
2026-Jan-01 14:51:11.735108
#29 8.084 Downloading urllib3-2.6.2-py3-none-any.whl (131 kB)
2026-Jan-01 14:51:11.735108
#29 8.111 Downloading uvloop-0.22.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (4.4 MB)
2026-Jan-01 14:51:11.735108
#29 8.243    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.4/4.4 MB 40.1 MB/s eta 0:00:00
2026-Jan-01 14:51:11.856800
#29 8.254 Downloading watchfiles-1.1.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (456 kB)
2026-Jan-01 14:51:11.856800
#29 8.331 Downloading websockets-15.0.1-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (182 kB)
2026-Jan-01 14:51:11.856800
#29 8.367 Downloading argon2_cffi-25.1.0-py3-none-any.whl (14 kB)
2026-Jan-01 14:51:11.983039
#29 8.385 Downloading passlib-1.7.4-py2.py3-none-any.whl (525 kB)
2026-Jan-01 14:51:11.983039
#29 8.412    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 525.6/525.6 kB 24.9 MB/s eta 0:00:00
2026-Jan-01 14:51:11.983039
#29 8.421 Downloading pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.3 MB)
2026-Jan-01 14:51:11.983039
#29 8.493    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.3/2.3 MB 31.5 MB/s eta 0:00:00
2026-Jan-01 14:51:12.083491
#29 8.497 Downloading python_jose-3.5.0-py2.py3-none-any.whl (34 kB)
2026-Jan-01 14:51:12.083491
#29 8.507 Downloading uvicorn-0.40.0-py3-none-any.whl (68 kB)
2026-Jan-01 14:51:12.083491
#29 8.518 Downloading annotated_types-0.7.0-py3-none-any.whl (13 kB)
2026-Jan-01 14:51:12.083491
#29 8.530 Downloading cffi-2.0.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (219 kB)
2026-Jan-01 14:51:12.083491
#29 8.539 Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
2026-Jan-01 14:51:12.083491
#29 8.550 Downloading typing_inspection-0.4.2-py3-none-any.whl (14 kB)
2026-Jan-01 14:51:12.083491
#29 8.563 Downloading argon2_cffi_bindings-25.1.0-cp39-abi3-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl (87 kB)
2026-Jan-01 14:51:12.083491
#29 8.583 Downloading packaging-25.0-py3-none-any.whl (66 kB)
2026-Jan-01 14:51:12.083491
#29 8.593 Downloading pycparser-2.23-py3-none-any.whl (118 kB)
2026-Jan-01 14:51:12.282305
#29 8.793 Installing collected packages: passlib, async-property, websockets, uvloop, urllib3, tzlocal, typing-extensions, six, pyyaml, python-multipart, python-dotenv, pycryptodome, pycparser, pyasn1, psycopg2-binary, prometheus_client, packaging, idna, httptools, h11, greenlet, click, charset_normalizer, certifi, bcrypt, annotated-types, annotated-doc, aiofiles, uvicorn, typing-inspection, sqlalchemy, rsa, requests, pydantic-core, httpcore, ecdsa, deprecation, cffi, APScheduler, anyio, watchfiles, stripe, starlette, requests-toolbelt, python-jose, pydantic, httpx, cryptography, argon2-cffi-bindings, jwcrypto, fastapi, argon2-cffi, python-keycloak, minio
2026-Jan-01 14:51:17.691620
#29 ...
2026-Jan-01 14:51:17.691620
2026-Jan-01 14:51:17.691620
#26 [dashboard deps 4/4] RUN npm install
2026-Jan-01 14:51:17.691620
#26 35.76
2026-Jan-01 14:51:17.691620
#26 35.76 added 574 packages, and audited 575 packages in 35s
2026-Jan-01 14:51:17.853497
#26 35.76
2026-Jan-01 14:51:17.853497
#26 35.77 238 packages are looking for funding
2026-Jan-01 14:51:17.853497
#26 35.77   run `npm fund` for details
2026-Jan-01 14:51:17.853497
#26 35.77
2026-Jan-01 14:51:17.853497
#26 35.77 found 0 vulnerabilities
2026-Jan-01 14:51:17.853497
#26 35.77 npm notice
2026-Jan-01 14:51:17.853497
#26 35.77 npm notice New major version of npm available! 10.8.2 -> 11.7.0
2026-Jan-01 14:51:17.853497
#26 35.77 npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.7.0
2026-Jan-01 14:51:17.853497
#26 35.77 npm notice To update run: npm install -g npm@11.7.0
2026-Jan-01 14:51:17.853497
#26 35.77 npm notice
2026-Jan-01 14:51:18.189343
#26 DONE 36.3s
2026-Jan-01 14:51:18.189343
2026-Jan-01 14:51:18.189343
#29 [api 5/7] RUN pip install -r requirements.txt
2026-Jan-01 14:51:19.596673
#29 16.11 WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager, possibly rendering your system unusable. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv. Use the --root-user-action option if you know what you are doing and want to suppress this warning.
2026-Jan-01 14:51:19.596673
#29 16.11 Successfully installed APScheduler-3.11.2 aiofiles-25.1.0 annotated-doc-0.0.4 annotated-types-0.7.0 anyio-4.12.0 argon2-cffi-25.1.0 argon2-cffi-bindings-25.1.0 async-property-0.2.2 bcrypt-4.0.1 certifi-2025.11.12 cffi-2.0.0 charset_normalizer-3.4.4 click-8.3.1 cryptography-46.0.3 deprecation-2.1.0 ecdsa-0.19.1 fastapi-0.128.0 greenlet-3.3.0 h11-0.16.0 httpcore-1.0.9 httptools-0.7.1 httpx-0.28.1 idna-3.11 jwcrypto-1.5.6 minio-7.2.20 packaging-25.0 passlib-1.7.4 prometheus_client-0.23.1 psycopg2-binary-2.9.11 pyasn1-0.6.1 pycparser-2.23 pycryptodome-3.23.0 pydantic-2.12.5 pydantic-core-2.41.5 python-dotenv-1.2.1 python-jose-3.5.0 python-keycloak-6.0.0 python-multipart-0.0.21 pyyaml-6.0.3 requests-2.32.5 requests-toolbelt-1.0.0 rsa-4.9.1 six-1.17.0 sqlalchemy-2.0.45 starlette-0.50.0 stripe-14.1.0 typing-extensions-4.15.0 typing-inspection-0.4.2 tzlocal-5.3.1 urllib3-2.6.2 uvicorn-0.40.0 uvloop-0.22.1 watchfiles-1.1.1 websockets-15.0.1
2026-Jan-01 14:51:19.825974
#29 16.19
2026-Jan-01 14:51:19.825974
#29 16.19 [notice] A new release of pip is available: 25.0.1 -> 25.3
2026-Jan-01 14:51:19.825974
#29 16.19 [notice] To update, run: pip install --upgrade pip
2026-Jan-01 14:51:20.151151
#29 DONE 16.7s
2026-Jan-01 14:51:20.314855
#30 [api 6/7] COPY control-plane/api/src ./src
2026-Jan-01 14:51:20.314855
#30 DONE 0.1s
2026-Jan-01 14:51:20.314855
2026-Jan-01 14:51:20.314855
#31 [api 7/7] COPY data-plane/project-template ./data-plane/project-template
2026-Jan-01 14:51:20.314855
#31 DONE 0.1s
2026-Jan-01 14:51:20.468220
#32 [api] exporting to image
2026-Jan-01 14:51:20.468220
#32 exporting layers
2026-Jan-01 14:51:21.513841
#32 exporting layers 1.2s done
2026-Jan-01 14:51:21.513841
#32 writing image sha256:789df18154cd67fff173cc4f5a7a70a6bd443dd36959c0940005fc792a9e51ba
2026-Jan-01 14:51:21.749332
#32 writing image sha256:789df18154cd67fff173cc4f5a7a70a6bd443dd36959c0940005fc792a9e51ba 0.0s done
2026-Jan-01 14:51:21.749332
#32 naming to docker.io/library/sokwws8k80wcg0gss0k0goww-api 0.0s done
2026-Jan-01 14:51:21.749332
#32 DONE 1.2s
2026-Jan-01 14:51:21.749332
2026-Jan-01 14:51:21.749332
#33 [api] resolving provenance for metadata file
2026-Jan-01 14:51:21.749332
#33 DONE 0.0s
2026-Jan-01 14:51:24.816224
#34 [dashboard builder 3/5] COPY --from=deps /app/node_modules ./node_modules
2026-Jan-01 14:51:35.262879
#34 DONE 10.4s
2026-Jan-01 14:51:35.490839
#35 [dashboard builder 4/5] COPY . .
2026-Jan-01 14:51:35.490839
#35 DONE 0.1s
2026-Jan-01 14:51:35.490839
2026-Jan-01 14:51:35.490839
#36 [dashboard builder 5/5] RUN npm run build
2026-Jan-01 14:51:36.094805
#36 0.753
2026-Jan-01 14:51:36.094805
#36 0.753 > dashboard@0.1.0 build
2026-Jan-01 14:51:36.094805
#36 0.753 > next build
2026-Jan-01 14:51:36.094805
#36 0.753
2026-Jan-01 14:51:36.907281
#36 1.566 Attention: Next.js now collects completely anonymous telemetry regarding usage.
2026-Jan-01 14:51:37.035876
#36 1.567 This information is used to shape Next.js' roadmap and prioritize features.
2026-Jan-01 14:51:37.035876
#36 1.567 You can learn more, including how to opt-out if you'd not like to participate in this anonymous program, by visiting the following URL:
2026-Jan-01 14:51:37.035876
#36 1.567 https://nextjs.org/telemetry
2026-Jan-01 14:51:37.035876
#36 1.567
2026-Jan-01 14:51:37.035876
#36 1.579 ▲ Next.js 16.1.0 (Turbopack)
2026-Jan-01 14:51:37.035876
#36 1.579
2026-Jan-01 14:51:37.035876
#36 1.693   Creating an optimized production build ...
2026-Jan-01 14:51:58.736742
#36 23.40 ✓ Compiled successfully in 21.2s
2026-Jan-01 14:51:58.895789
#36 23.40   Running TypeScript ...
2026-Jan-01 14:52:10.359517
#36 35.02   Collecting page data using 1 worker ...
2026-Jan-01 14:52:11.106909
#36 35.77   Generating static pages using 1 worker (0/12) ...
2026-Jan-01 14:52:11.115702
2026-Jan-01 14:52:11.266334
#36 35.92 Failed to read docs directory Error: ENOENT: no such file or directory, scandir '/docs'
2026-Jan-01 14:52:11.266334
#36 35.92     at f (.next/server/chunks/ssr/[root-of-the-server]__7f51e285._.js:1:509)
2026-Jan-01 14:52:11.266334
#36 35.92     at stringify (<anonymous>) {
2026-Jan-01 14:52:11.274039
#36 35.92   errno: -2,
2026-Jan-01 14:52:11.274039
#36 35.92   code: 'ENOENT',
2026-Jan-01 14:52:11.274039
#36 35.92   syscall: 'scandir',
2026-Jan-01 14:52:11.274039
#36 35.92   path: '/docs'
2026-Jan-01 14:52:11.274039
#36 35.92 }
2026-Jan-01 14:52:11.384063
#36 36.04 Error occurred prerendering page "/docs". Read more: https://nextjs.org/docs/messages/prerender-error
2026-Jan-01 14:52:11.529704
#36 36.05 Error: ENOENT: no such file or directory, scandir '/docs'
2026-Jan-01 14:52:11.529704
#36 36.05     at n (.next/server/chunks/ssr/[root-of-the-server]__6c662ad3._.js:1:3302)
2026-Jan-01 14:52:11.529704
#36 36.05     at stringify (<anonymous>) {
2026-Jan-01 14:52:11.529704
#36 36.05   errno: -2,
2026-Jan-01 14:52:11.529704
#36 36.05   code: 'ENOENT',
2026-Jan-01 14:52:11.529704
#36 36.05   syscall: 'scandir',
2026-Jan-01 14:52:11.529704
#36 36.05   path: '/docs',
2026-Jan-01 14:52:11.529704
#36 36.05   digest: '1019816127'
2026-Jan-01 14:52:11.529704
#36 36.05 }
2026-Jan-01 14:52:11.529704
#36 36.05 Export encountered an error on /docs/page: /docs, exiting the build.
2026-Jan-01 14:52:11.529704
#36 36.08 ⨯ Next.js build worker exited with code: 1 and signal: null
2026-Jan-01 14:52:11.529704
#36 36.12 npm notice
2026-Jan-01 14:52:11.529704
#36 36.12 npm notice New major version of npm available! 10.8.2 -> 11.7.0
2026-Jan-01 14:52:11.529704
#36 36.12 npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.7.0
2026-Jan-01 14:52:11.529704
#36 36.12 npm notice To update run: npm install -g npm@11.7.0
2026-Jan-01 14:52:11.529704
#36 36.12 npm notice
2026-Jan-01 14:52:11.529704
#36 ERROR: process "/bin/sh -c npm run build" did not complete successfully: exit code: 1
2026-Jan-01 14:52:11.562101
------
2026-Jan-01 14:52:11.562101
> [dashboard builder 5/5] RUN npm run build:
2026-Jan-01 14:52:11.562101
36.05   path: '/docs',
2026-Jan-01 14:52:11.562101
36.05   digest: '1019816127'
2026-Jan-01 14:52:11.562101
36.05 }
2026-Jan-01 14:52:11.562101
36.05 Export encountered an error on /docs/page: /docs, exiting the build.
2026-Jan-01 14:52:11.562101
36.08 ⨯ Next.js build worker exited with code: 1 and signal: null
2026-Jan-01 14:52:11.562101
36.12 npm notice
2026-Jan-01 14:52:11.562101
36.12 npm notice New major version of npm available! 10.8.2 -> 11.7.0
2026-Jan-01 14:52:11.562101
36.12 npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.7.0
2026-Jan-01 14:52:11.562101
36.12 npm notice To update run: npm install -g npm@11.7.0
2026-Jan-01 14:52:11.562101
36.12 npm notice
2026-Jan-01 14:52:11.562101
------
2026-Jan-01 14:52:11.573496
Dockerfile:57
2026-Jan-01 14:52:11.573496
2026-Jan-01 14:52:11.573496
--------------------
2026-Jan-01 14:52:11.573496
2026-Jan-01 14:52:11.573496
55 |     ARG NEXT_PUBLIC_API_URL
2026-Jan-01 14:52:11.573496
2026-Jan-01 14:52:11.573496
56 |     ENV NEXT_PUBLIC_API_URL=${NEXT_PUBLIC_API_URL}
2026-Jan-01 14:52:11.573496
2026-Jan-01 14:52:11.573496
57 | >>> RUN npm run build
2026-Jan-01 14:52:11.573496
2026-Jan-01 14:52:11.573496
58 |
2026-Jan-01 14:52:11.573496
2026-Jan-01 14:52:11.573496
59 |     # Stage 3: Runner
2026-Jan-01 14:52:11.573496
2026-Jan-01 14:52:11.573496
--------------------
2026-Jan-01 14:52:11.573496
2026-Jan-01 14:52:11.573496
target dashboard: failed to solve: process "/bin/sh -c npm run build" did not complete successfully: exit code: 1
2026-Jan-01 14:52:11.597592
exit status 1
2026-Jan-01 14:52:11.654846
Oops something is not okay, are you okay? 😢
2026-Jan-01 14:52:11.672802
Dockerfile:57
2026-Jan-01 14:52:11.672802
2026-Jan-01 14:52:11.672802
--------------------
2026-Jan-01 14:52:11.672802
2026-Jan-01 14:52:11.672802
55 |     ARG NEXT_PUBLIC_API_URL
2026-Jan-01 14:52:11.672802
2026-Jan-01 14:52:11.672802
56 |     ENV NEXT_PUBLIC_API_URL=${NEXT_PUBLIC_API_URL}
2026-Jan-01 14:52:11.672802
2026-Jan-01 14:52:11.672802
57 | >>> RUN npm run build
2026-Jan-01 14:52:11.672802
2026-Jan-01 14:52:11.672802
58 |
2026-Jan-01 14:52:11.672802
2026-Jan-01 14:52:11.672802
59 |     # Stage 3: Runner
2026-Jan-01 14:52:11.672802
2026-Jan-01 14:52:11.672802
--------------------
2026-Jan-01 14:52:11.672802
2026-Jan-01 14:52:11.672802
target dashboard: failed to solve: process "/bin/sh -c npm run build" did not complete successfully: exit code: 1
2026-Jan-01 14:52:11.672802
2026-Jan-01 14:52:11.672802
exit status 1
2026-Jan-01 14:52:12.715104
Gracefully shutting down build container: fcsows88cs0gosg8os084wgc
2026-Jan-01 14:52:13.182616
[CMD]: docker stop --time=30 fcsows88cs0gosg8os084wgc
2026-Jan-01 14:52:13.182616
fcsows88cs0gosg8os084wgc
2026-Jan-01 14:52:13.602600
[CMD]: docker rm -f fcsows88cs0gosg8os084wgc
2026-Jan-01 14:52:13.602600
Error response from daemon: No such container: fcsows88cs0gosg8os084wgc