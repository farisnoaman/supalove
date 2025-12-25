Deployment is Finished.


2025-Dec-25 13:21:44.018054
Starting deployment of supalove to localhost.
2025-Dec-25 13:21:44.230949
Preparing container with helper image: ghcr.io/coollabsio/coolify-helper:1.0.12
2025-Dec-25 13:21:44.351784
[CMD]: docker stop --time=30 d8cwk4kwosg0c08w0gk0kcow
2025-Dec-25 13:21:44.351784
Error response from daemon: No such container: d8cwk4kwosg0c08w0gk0kcow
2025-Dec-25 13:21:44.470213
[CMD]: docker rm -f d8cwk4kwosg0c08w0gk0kcow
2025-Dec-25 13:21:44.470213
Error response from daemon: No such container: d8cwk4kwosg0c08w0gk0kcow
2025-Dec-25 13:21:44.671570
[CMD]: docker run -d --network coolify --name d8cwk4kwosg0c08w0gk0kcow  --rm -v /var/run/docker.sock:/var/run/docker.sock ghcr.io/coollabsio/coolify-helper:1.0.12
2025-Dec-25 13:21:44.671570
805b3620bcaefdfb5231fc196063d68f3d15d83a88d1dce6e7a941197bb1d17c
2025-Dec-25 13:21:45.551481
[CMD]: docker exec d8cwk4kwosg0c08w0gk0kcow bash -c 'GIT_SSH_COMMAND="ssh -o ConnectTimeout=30 -p 22 -o Port=22 -o LogLevel=ERROR -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" git ls-remote https://github.com/farisnoaman/supalove refs/heads/main'
2025-Dec-25 13:21:45.551481
b073128f92a4c217303a00090740e2745f9c297c	refs/heads/main
2025-Dec-25 13:21:45.568054
----------------------------------------
2025-Dec-25 13:21:45.573569
Importing farisnoaman/supalove:main (commit sha b073128f92a4c217303a00090740e2745f9c297c) to /artifacts/d8cwk4kwosg0c08w0gk0kcow.
2025-Dec-25 13:21:45.735168
[CMD]: docker exec d8cwk4kwosg0c08w0gk0kcow bash -c 'git clone --depth=1 --recurse-submodules --shallow-submodules -b 'main' 'https://github.com/farisnoaman/supalove' '/artifacts/d8cwk4kwosg0c08w0gk0kcow' && cd '/artifacts/d8cwk4kwosg0c08w0gk0kcow' && if [ -f .gitmodules ]; then sed -i "s#git@\(.*\):#https://\1/#g" '/artifacts/d8cwk4kwosg0c08w0gk0kcow'/.gitmodules || true && git submodule sync && GIT_SSH_COMMAND="ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" git submodule update --init --recursive --depth=1; fi && cd '/artifacts/d8cwk4kwosg0c08w0gk0kcow' && GIT_SSH_COMMAND="ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" git lfs pull'
2025-Dec-25 13:21:45.735168
Cloning into '/artifacts/d8cwk4kwosg0c08w0gk0kcow'...
2025-Dec-25 13:21:52.457620
Updating files:  22% (3454/15085)
2025-Dec-25 13:21:52.460202
Updating files:  23% (3470/15085)
2025-Dec-25 13:21:52.534462
Updating files:  24% (3621/15085)
2025-Dec-25 13:21:52.565476
Updating files:  25% (3772/15085)
2025-Dec-25 13:21:52.596096
Updating files:  26% (3923/15085)
2025-Dec-25 13:21:52.655405
Updating files:  27% (4073/15085)
2025-Dec-25 13:21:52.689120
Updating files:  28% (4224/15085)
2025-Dec-25 13:21:52.710143
Updating files:  29% (4375/15085)
2025-Dec-25 13:21:52.729231
Updating files:  30% (4526/15085)
2025-Dec-25 13:21:52.742549
Updating files:  31% (4677/15085)
2025-Dec-25 13:21:52.756786
Updating files:  32% (4828/15085)
2025-Dec-25 13:21:52.772491
Updating files:  33% (4979/15085)
2025-Dec-25 13:21:52.811719
Updating files:  34% (5129/15085)
2025-Dec-25 13:21:52.845356
Updating files:  35% (5280/15085)
2025-Dec-25 13:21:52.891780
Updating files:  36% (5431/15085)
2025-Dec-25 13:21:52.932183
Updating files:  37% (5582/15085)
2025-Dec-25 13:21:52.947584
Updating files:  38% (5733/15085)
2025-Dec-25 13:21:52.971724
Updating files:  39% (5884/15085)
2025-Dec-25 13:21:52.995643
Updating files:  40% (6034/15085)
2025-Dec-25 13:21:53.030058
Updating files:  41% (6185/15085)
2025-Dec-25 13:21:53.065584
Updating files:  42% (6336/15085)
2025-Dec-25 13:21:53.089946
Updating files:  43% (6487/15085)
2025-Dec-25 13:21:53.104407
Updating files:  44% (6638/15085)
2025-Dec-25 13:21:53.126506
Updating files:  45% (6789/15085)
2025-Dec-25 13:21:53.152872
Updating files:  46% (6940/15085)
2025-Dec-25 13:21:53.172254
Updating files:  47% (7090/15085)
2025-Dec-25 13:21:53.190225
Updating files:  48% (7241/15085)
2025-Dec-25 13:21:53.202382
Updating files:  49% (7392/15085)
2025-Dec-25 13:21:53.215307
Updating files:  50% (7543/15085)
2025-Dec-25 13:21:53.227496
Updating files:  51% (7694/15085)
2025-Dec-25 13:21:53.242526
Updating files:  52% (7845/15085)
2025-Dec-25 13:21:53.256290
Updating files:  53% (7996/15085)
2025-Dec-25 13:21:53.278251
Updating files:  54% (8146/15085)
2025-Dec-25 13:21:53.367140
Updating files:  55% (8297/15085)
2025-Dec-25 13:21:53.405186
Updating files:  56% (8448/15085)
2025-Dec-25 13:21:53.417638
Updating files:  57% (8599/15085)
2025-Dec-25 13:21:53.432805
Updating files:  58% (8750/15085)
2025-Dec-25 13:21:53.458112
Updating files:  58% (8894/15085)
2025-Dec-25 13:21:53.464757
Updating files:  59% (8901/15085)
2025-Dec-25 13:21:53.477347
Updating files:  60% (9051/15085)
2025-Dec-25 13:21:53.500221
Updating files:  61% (9202/15085)
2025-Dec-25 13:21:53.518950
Updating files:  62% (9353/15085)
2025-Dec-25 13:21:53.534264
Updating files:  63% (9504/15085)
2025-Dec-25 13:21:53.549596
Updating files:  64% (9655/15085)
2025-Dec-25 13:21:53.633928
Updating files:  65% (9806/15085)
2025-Dec-25 13:21:53.652970
Updating files:  66% (9957/15085)
2025-Dec-25 13:21:53.685404
Updating files:  67% (10107/15085)
2025-Dec-25 13:21:53.710470
Updating files:  68% (10258/15085)
2025-Dec-25 13:21:53.737789
Updating files:  69% (10409/15085)
2025-Dec-25 13:21:53.760792
Updating files:  70% (10560/15085)
2025-Dec-25 13:21:53.777691
Updating files:  71% (10711/15085)
2025-Dec-25 13:21:53.797971
Updating files:  72% (10862/15085)
2025-Dec-25 13:21:53.814439
Updating files:  73% (11013/15085)
2025-Dec-25 13:21:53.827720
Updating files:  74% (11163/15085)
2025-Dec-25 13:21:53.843534
Updating files:  75% (11314/15085)
2025-Dec-25 13:21:53.859818
Updating files:  76% (11465/15085)
2025-Dec-25 13:21:53.874009
Updating files:  77% (11616/15085)
2025-Dec-25 13:21:53.887558
Updating files:  78% (11767/15085)
2025-Dec-25 13:21:53.901166
Updating files:  79% (11918/15085)
2025-Dec-25 13:21:53.982581
Updating files:  80% (12068/15085)
2025-Dec-25 13:21:54.004433
Updating files:  81% (12219/15085)
2025-Dec-25 13:21:54.062558
Updating files:  82% (12370/15085)
2025-Dec-25 13:21:54.077375
Updating files:  83% (12521/15085)
2025-Dec-25 13:21:54.095720
Updating files:  84% (12672/15085)
2025-Dec-25 13:21:54.115813
Updating files:  85% (12823/15085)
2025-Dec-25 13:21:54.128054
Updating files:  86% (12974/15085)
2025-Dec-25 13:21:54.139982
Updating files:  87% (13124/15085)
2025-Dec-25 13:21:54.178515
Updating files:  88% (13275/15085)
2025-Dec-25 13:21:54.202567
Updating files:  89% (13426/15085)
2025-Dec-25 13:21:54.229532
Updating files:  90% (13577/15085)
2025-Dec-25 13:21:54.254105
Updating files:  91% (13728/15085)
2025-Dec-25 13:21:54.268406
Updating files:  92% (13879/15085)
2025-Dec-25 13:21:54.281223
Updating files:  93% (14030/15085)
2025-Dec-25 13:21:54.373354
Updating files:  94% (14180/15085)
2025-Dec-25 13:21:54.424191
Updating files:  95% (14331/15085)
2025-Dec-25 13:21:54.458476
Updating files:  95% (14465/15085)
2025-Dec-25 13:21:54.474174
Updating files:  96% (14482/15085)
2025-Dec-25 13:21:54.503395
Updating files:  97% (14633/15085)
2025-Dec-25 13:21:54.521657
Updating files:  98% (14784/15085)
2025-Dec-25 13:21:54.546587
Updating files:  99% (14935/15085)
2025-Dec-25 13:21:54.562012
Updating files: 100% (15085/15085)
Updating files: 100% (15085/15085), done.
2025-Dec-25 13:21:55.233988
[CMD]: docker exec d8cwk4kwosg0c08w0gk0kcow bash -c 'cd /artifacts/d8cwk4kwosg0c08w0gk0kcow && git log -1 b073128f92a4c217303a00090740e2745f9c297c --pretty=%B'
2025-Dec-25 13:21:55.233988
feat: Robustly determine PROJECT_ROOT for local and Docker environments and add VPS logs.
2025-Dec-25 13:22:02.484407
[CMD]: docker exec d8cwk4kwosg0c08w0gk0kcow bash -c 'test -f /artifacts/d8cwk4kwosg0c08w0gk0kcow/control-plane/api/Dockerfile && echo 'exists' || echo 'not found''
2025-Dec-25 13:22:02.484407
exists
2025-Dec-25 13:22:02.809033
[CMD]: docker exec d8cwk4kwosg0c08w0gk0kcow bash -c 'cat /artifacts/d8cwk4kwosg0c08w0gk0kcow/control-plane/api/Dockerfile'
2025-Dec-25 13:22:02.809033
FROM python:3.12-slim
2025-Dec-25 13:22:02.809033
WORKDIR /app
2025-Dec-25 13:22:02.809033
COPY requirements.txt .
2025-Dec-25 13:22:02.809033
RUN pip install -r requirements.txt
2025-Dec-25 13:22:02.809033
COPY . .
2025-Dec-25 13:22:02.809033
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
2025-Dec-25 13:22:03.150969
Added 21 ARG declarations to Dockerfile for service api.
2025-Dec-25 13:22:03.525716
[CMD]: docker exec d8cwk4kwosg0c08w0gk0kcow bash -c 'test -f /artifacts/d8cwk4kwosg0c08w0gk0kcow/dashboard/Dockerfile && echo 'exists' || echo 'not found''
2025-Dec-25 13:22:03.525716
exists
2025-Dec-25 13:22:03.806132
[CMD]: docker exec d8cwk4kwosg0c08w0gk0kcow bash -c 'cat /artifacts/d8cwk4kwosg0c08w0gk0kcow/dashboard/Dockerfile'
2025-Dec-25 13:22:03.806132
# Stage 1: Dependencies
2025-Dec-25 13:22:03.806132
FROM node:20-alpine AS deps
2025-Dec-25 13:22:03.806132
WORKDIR /app
2025-Dec-25 13:22:03.806132
COPY package*.json ./
2025-Dec-25 13:22:03.806132
RUN npm install
2025-Dec-25 13:22:03.806132
2025-Dec-25 13:22:03.806132
# Stage 2: Builder
2025-Dec-25 13:22:03.806132
FROM node:20-alpine AS builder
2025-Dec-25 13:22:03.806132
WORKDIR /app
2025-Dec-25 13:22:03.806132
COPY --from=deps /app/node_modules ./node_modules
2025-Dec-25 13:22:03.806132
COPY . .
2025-Dec-25 13:22:03.806132
# Set environment variables for build if needed (e.g. backend URL)
2025-Dec-25 13:22:03.806132
# For Next.js client-side fetch, it might need to know the URL at build time if pre-rendering,
2025-Dec-25 13:22:03.806132
# but we are using "use client" so it's fine.
2025-Dec-25 13:22:03.806132
ARG NEXT_PUBLIC_API_URL
2025-Dec-25 13:22:03.806132
ENV NEXT_PUBLIC_API_URL=${NEXT_PUBLIC_API_URL}
2025-Dec-25 13:22:03.806132
RUN npm run build
2025-Dec-25 13:22:03.806132
2025-Dec-25 13:22:03.806132
# Stage 3: Runner
2025-Dec-25 13:22:03.806132
FROM node:20-alpine AS runner
2025-Dec-25 13:22:03.806132
WORKDIR /app
2025-Dec-25 13:22:03.806132
ENV NODE_ENV=production
2025-Dec-25 13:22:03.806132
COPY --from=builder /app/public ./public
2025-Dec-25 13:22:03.806132
COPY --from=builder /app/.next ./.next
2025-Dec-25 13:22:03.806132
COPY --from=builder /app/node_modules ./node_modules
2025-Dec-25 13:22:03.806132
COPY --from=builder /app/package.json ./package.json
2025-Dec-25 13:22:03.806132
2025-Dec-25 13:22:03.806132
EXPOSE 3000
2025-Dec-25 13:22:03.806132
CMD ["npm", "start"]
2025-Dec-25 13:22:04.120865
Added 63 ARG declarations to Dockerfile for service dashboard (multi-stage build, added to 3 stages).
2025-Dec-25 13:22:04.147144
Pulling & building required images.
2025-Dec-25 13:22:04.217740
Creating build-time .env file in /artifacts (outside Docker context).
2025-Dec-25 13:22:04.635388
[CMD]: docker exec d8cwk4kwosg0c08w0gk0kcow bash -c 'cat /artifacts/build-time.env'
2025-Dec-25 13:22:04.635388
SOURCE_COMMIT='b073128f92a4c217303a00090740e2745f9c297c'
2025-Dec-25 13:22:04.635388
COOLIFY_URL=''
2025-Dec-25 13:22:04.635388
COOLIFY_FQDN=''
2025-Dec-25 13:22:04.635388
SERVICE_NAME_CONTROL-PLANE-DB='control-plane-db'
2025-Dec-25 13:22:04.635388
SERVICE_NAME_API='api'
2025-Dec-25 13:22:04.635388
SERVICE_NAME_DASHBOARD='dashboard'
2025-Dec-25 13:22:04.635388
SERVICE_NAME_KEYCLOAK='keycloak'
2025-Dec-25 13:22:04.635388
SERVICE_NAME_MINIO='minio'
2025-Dec-25 13:22:04.635388
SERVICE_URL_DASHBOARD='https://supalove.hayataxi.online'
2025-Dec-25 13:22:04.635388
SERVICE_FQDN_DASHBOARD='supalove.hayataxi.online'
2025-Dec-25 13:22:04.635388
SERVICE_URL_API='https://api.hayataxi.online'
2025-Dec-25 13:22:04.635388
SERVICE_FQDN_API='api.hayataxi.online'
2025-Dec-25 13:22:04.635388
SERVICE_URL_KEYCLOAK='https://auth.hayataxi.online'
2025-Dec-25 13:22:04.635388
SERVICE_FQDN_KEYCLOAK='auth.hayataxi.online'
2025-Dec-25 13:22:04.635388
SERVICE_URL_MINIO='https://s3.hayataxi.online'
2025-Dec-25 13:22:04.635388
SERVICE_FQDN_MINIO='s3.hayataxi.online'
2025-Dec-25 13:22:04.635388
ALLOWED_ORIGINS="http://localhost:3000,http://localhost:8000"
2025-Dec-25 13:22:04.635388
KEYCLOAK_ADMIN_PASSWORD="admin"
2025-Dec-25 13:22:04.635388
KEYCLOAK_ADMIN_USER="admin"
2025-Dec-25 13:22:04.635388
MINIO_ROOT_PASSWORD="minioadmin"
2025-Dec-25 13:22:04.635388
MINIO_ROOT_USER="minioadmin"
2025-Dec-25 13:22:04.635388
NEXT_PUBLIC_API_URL="https://api.hayataxi.online"
2025-Dec-25 13:22:04.635388
POSTGRES_DB="control_plane"
2025-Dec-25 13:22:04.635388
POSTGRES_PASSWORD="platform"
2025-Dec-25 13:22:04.635388
POSTGRES_USER="platform"
2025-Dec-25 13:22:04.635388
URL="http://localhost:8000"
2025-Dec-25 13:22:04.654931
Adding build arguments to Docker Compose build command.
2025-Dec-25 13:22:05.263020
[CMD]: docker exec d8cwk4kwosg0c08w0gk0kcow bash -c 'SOURCE_COMMIT=b073128f92a4c217303a00090740e2745f9c297c COOLIFY_BRANCH=main COOLIFY_RESOURCE_UUID=hck4w0k4ww8kk4gccw000ggg COOLIFY_CONTAINER_NAME=hck4w0k4ww8kk4gccw000ggg-132143017536  docker compose --env-file /artifacts/build-time.env --project-name hck4w0k4ww8kk4gccw000ggg --project-directory /artifacts/d8cwk4kwosg0c08w0gk0kcow -f /artifacts/d8cwk4kwosg0c08w0gk0kcow/docker-compose.coolify.yml build --pull --no-cache --build-arg SOURCE_COMMIT --build-arg COOLIFY_URL --build-arg COOLIFY_FQDN --build-arg SERVICE_FQDN_API --build-arg SERVICE_FQDN_DASHBOARD --build-arg SERVICE_FQDN_KEYCLOAK --build-arg SERVICE_FQDN_MINIO --build-arg SERVICE_URL_API --build-arg SERVICE_URL_DASHBOARD --build-arg SERVICE_URL_KEYCLOAK --build-arg SERVICE_URL_MINIO --build-arg ALLOWED_ORIGINS --build-arg KEYCLOAK_ADMIN_PASSWORD --build-arg KEYCLOAK_ADMIN_USER --build-arg MINIO_ROOT_PASSWORD --build-arg MINIO_ROOT_USER --build-arg NEXT_PUBLIC_API_URL --build-arg POSTGRES_DB --build-arg POSTGRES_PASSWORD --build-arg POSTGRES_USER --build-arg URL --build-arg COOLIFY_BUILD_SECRETS_HASH=b2712e1e9d8502f4c65a28c3e0d2c8e45e16f70ecff06890d4067af565b8567e'
2025-Dec-25 13:22:05.263020
#1 [internal] load local bake definitions
2025-Dec-25 13:22:05.385909
#1 reading from stdin 3.22kB done
2025-Dec-25 13:22:05.385909
#1 DONE 0.0s
2025-Dec-25 13:22:05.580586
#2 [api internal] load build definition from Dockerfile
2025-Dec-25 13:22:05.580586
#2 transferring dockerfile: 658B done
2025-Dec-25 13:22:05.580586
#2 DONE 0.0s
2025-Dec-25 13:22:05.580586
2025-Dec-25 13:22:05.580586
#3 [dashboard internal] load build definition from Dockerfile
2025-Dec-25 13:22:05.580586
#3 transferring dockerfile: 2.20kB done
2025-Dec-25 13:22:05.580586
#3 DONE 0.0s
2025-Dec-25 13:22:05.580586
2025-Dec-25 13:22:05.580586
#4 [dashboard internal] load metadata for docker.io/library/node:20-alpine
2025-Dec-25 13:22:06.162948
#4 ...
2025-Dec-25 13:22:06.162948
2025-Dec-25 13:22:06.162948
#5 [api internal] load metadata for docker.io/library/python:3.12-slim
2025-Dec-25 13:22:06.162948
#5 DONE 0.7s
2025-Dec-25 13:22:06.268419
#6 [api internal] load .dockerignore
2025-Dec-25 13:22:06.268419
#6 transferring context: 2B done
2025-Dec-25 13:22:06.268419
#6 DONE 0.0s
2025-Dec-25 13:22:06.268419
2025-Dec-25 13:22:06.268419
#7 [api 1/5] FROM docker.io/library/python:3.12-slim@sha256:fa48eefe2146644c2308b909d6bb7651a768178f84fc9550dcd495e4d6d84d01
2025-Dec-25 13:22:06.268419
#7 DONE 0.0s
2025-Dec-25 13:22:06.268419
2025-Dec-25 13:22:06.268419
#8 [api 2/5] WORKDIR /app
2025-Dec-25 13:22:06.268419
#8 CACHED
2025-Dec-25 13:22:06.268419
2025-Dec-25 13:22:06.268419
#4 [dashboard internal] load metadata for docker.io/library/node:20-alpine
2025-Dec-25 13:22:06.268419
#4 DONE 0.8s
2025-Dec-25 13:22:06.268419
2025-Dec-25 13:22:06.268419
#9 [api internal] load build context
2025-Dec-25 13:22:06.408794
#9 ...
2025-Dec-25 13:22:06.428492
#10 [dashboard internal] load .dockerignore
2025-Dec-25 13:22:06.428492
#10 transferring context: 2B done
2025-Dec-25 13:22:06.428492
#10 DONE 0.0s
2025-Dec-25 13:22:06.428492
2025-Dec-25 13:22:06.428492
#11 [dashboard deps 1/4] FROM docker.io/library/node:20-alpine@sha256:658d0f63e501824d6c23e06d4bb95c71e7d704537c9d9272f488ac03a370d448
2025-Dec-25 13:22:06.428492
#11 DONE 0.0s
2025-Dec-25 13:22:06.428492
2025-Dec-25 13:22:06.428492
#12 [dashboard deps 2/4] WORKDIR /app
2025-Dec-25 13:22:06.428492
#12 CACHED
2025-Dec-25 13:22:06.428492
2025-Dec-25 13:22:06.428492
#9 [api internal] load build context
2025-Dec-25 13:22:06.547888
#9 ...
2025-Dec-25 13:22:06.547888
2025-Dec-25 13:22:06.547888
#13 [dashboard internal] load build context
2025-Dec-25 13:22:06.547888
#13 transferring context: 837.69kB 0.1s done
2025-Dec-25 13:22:06.547888
#13 DONE 0.1s
2025-Dec-25 13:22:06.547888
2025-Dec-25 13:22:06.547888
#14 [dashboard deps 3/4] COPY package*.json ./
2025-Dec-25 13:22:06.547888
#14 DONE 0.1s
2025-Dec-25 13:22:06.547888
2025-Dec-25 13:22:06.547888
#9 [api internal] load build context
2025-Dec-25 13:22:11.470609
#9 transferring context: 151.43MB 5.3s
2025-Dec-25 13:22:16.491488
#9 transferring context: 272.97MB 10.3s
2025-Dec-25 13:22:16.708768
#9 ...
2025-Dec-25 13:22:16.708768
2025-Dec-25 13:22:16.708768
#15 [dashboard deps 4/4] RUN npm install
2025-Dec-25 13:22:16.890582
#15 ...
2025-Dec-25 13:22:16.890582
2025-Dec-25 13:22:16.890582
#9 [api internal] load build context
2025-Dec-25 13:22:17.526977
#9 transferring context: 330.52MB 11.3s done
2025-Dec-25 13:22:17.711561
#9 DONE 11.4s
2025-Dec-25 13:22:17.724670
#16 [api 3/5] COPY requirements.txt .
2025-Dec-25 13:22:17.888035
#16 DONE 0.3s
2025-Dec-25 13:22:17.915017
#15 [dashboard deps 4/4] RUN npm install
2025-Dec-25 13:22:18.044378
#15 ...
2025-Dec-25 13:22:18.044378
2025-Dec-25 13:22:18.044378
#17 [api 4/5] RUN pip install -r requirements.txt
2025-Dec-25 13:22:21.374309
#17 3.484 Collecting fastapi (from -r requirements.txt (line 1))
2025-Dec-25 13:22:21.567234
#17 3.523   Downloading fastapi-0.127.0-py3-none-any.whl.metadata (30 kB)
2025-Dec-25 13:22:21.747024
#17 3.855 Collecting sqlalchemy (from -r requirements.txt (line 3))
2025-Dec-25 13:22:21.898689
#17 3.859   Downloading sqlalchemy-2.0.45-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (9.5 kB)
2025-Dec-25 13:22:21.898689
#17 3.944 Collecting psycopg2-binary (from -r requirements.txt (line 4))
2025-Dec-25 13:22:21.898689
#17 3.949   Downloading psycopg2_binary-2.9.11-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (4.9 kB)
2025-Dec-25 13:22:21.898689
#17 4.006 Collecting httpx (from -r requirements.txt (line 5))
2025-Dec-25 13:22:22.024561
#17 4.012   Downloading httpx-0.28.1-py3-none-any.whl.metadata (7.1 kB)
2025-Dec-25 13:22:22.024561
#17 4.063 Collecting python-keycloak (from -r requirements.txt (line 6))
2025-Dec-25 13:22:22.024561
#17 4.072   Downloading python_keycloak-5.8.1-py3-none-any.whl.metadata (6.0 kB)
2025-Dec-25 13:22:22.024561
#17 4.126 Collecting minio (from -r requirements.txt (line 7))
2025-Dec-25 13:22:22.141259
#17 4.130   Downloading minio-7.2.20-py3-none-any.whl.metadata (6.5 kB)
2025-Dec-25 13:22:22.141259
#17 4.180 Collecting requests (from -r requirements.txt (line 8))
2025-Dec-25 13:22:22.141259
#17 4.186   Downloading requests-2.32.5-py3-none-any.whl.metadata (4.9 kB)
2025-Dec-25 13:22:22.141259
#17 4.215 Collecting python-dotenv (from -r requirements.txt (line 9))
2025-Dec-25 13:22:22.141259
#17 4.220   Downloading python_dotenv-1.2.1-py3-none-any.whl.metadata (25 kB)
2025-Dec-25 13:22:22.141259
#17 4.248 Collecting python-multipart (from -r requirements.txt (line 12))
2025-Dec-25 13:22:22.300592
#17 4.259   Downloading python_multipart-0.0.21-py3-none-any.whl.metadata (1.8 kB)
2025-Dec-25 13:22:22.331303
#17 4.441 Collecting stripe (from -r requirements.txt (line 13))
2025-Dec-25 13:22:22.463755
#17 4.451   Downloading stripe-14.1.0-py3-none-any.whl.metadata (18 kB)
2025-Dec-25 13:22:22.463755
#17 4.482 Collecting prometheus_client (from -r requirements.txt (line 14))
2025-Dec-25 13:22:22.463755
#17 4.485   Downloading prometheus_client-0.23.1-py3-none-any.whl.metadata (1.9 kB)
2025-Dec-25 13:22:22.463755
#17 4.518 Collecting APScheduler (from -r requirements.txt (line 15))
2025-Dec-25 13:22:22.463755
#17 4.522   Downloading apscheduler-3.11.2-py3-none-any.whl.metadata (6.4 kB)
2025-Dec-25 13:22:22.463755
#17 4.574 Collecting uvicorn[standard] (from -r requirements.txt (line 2))
2025-Dec-25 13:22:22.614974
#17 4.582   Downloading uvicorn-0.40.0-py3-none-any.whl.metadata (6.7 kB)
2025-Dec-25 13:22:22.614974
#17 4.616 Collecting passlib[bcrypt] (from -r requirements.txt (line 10))
2025-Dec-25 13:22:22.614974
#17 4.622   Downloading passlib-1.7.4-py2.py3-none-any.whl.metadata (1.7 kB)
2025-Dec-25 13:22:22.614974
#17 4.659 Collecting python-jose[cryptography] (from -r requirements.txt (line 11))
2025-Dec-25 13:22:22.614974
#17 4.667   Downloading python_jose-3.5.0-py2.py3-none-any.whl.metadata (5.5 kB)
2025-Dec-25 13:22:22.614974
#17 4.725 Collecting starlette<0.51.0,>=0.40.0 (from fastapi->-r requirements.txt (line 1))
2025-Dec-25 13:22:22.739894
#17 4.732   Downloading starlette-0.50.0-py3-none-any.whl.metadata (6.3 kB)
2025-Dec-25 13:22:22.739894
#17 4.849 Collecting pydantic>=2.7.0 (from fastapi->-r requirements.txt (line 1))
2025-Dec-25 13:22:22.845251
#17 4.857   Downloading pydantic-2.12.5-py3-none-any.whl.metadata (90 kB)
2025-Dec-25 13:22:22.845251
#17 4.908 Collecting typing-extensions>=4.8.0 (from fastapi->-r requirements.txt (line 1))
2025-Dec-25 13:22:22.845251
#17 4.914   Downloading typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
2025-Dec-25 13:22:22.845251
#17 4.955 Collecting annotated-doc>=0.0.2 (from fastapi->-r requirements.txt (line 1))
2025-Dec-25 13:22:22.962530
#17 4.961   Downloading annotated_doc-0.0.4-py3-none-any.whl.metadata (6.6 kB)
2025-Dec-25 13:22:22.962530
#17 4.993 Collecting click>=7.0 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 13:22:22.962530
#17 4.999   Downloading click-8.3.1-py3-none-any.whl.metadata (2.6 kB)
2025-Dec-25 13:22:22.962530
#17 5.018 Collecting h11>=0.8 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 13:22:22.962530
#17 5.023   Downloading h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
2025-Dec-25 13:22:22.962530
#17 5.069 Collecting httptools>=0.6.3 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 13:22:23.105243
#17 5.078   Downloading httptools-0.7.1-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (3.5 kB)
2025-Dec-25 13:22:23.105243
#17 5.214 Collecting pyyaml>=5.1 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 13:22:23.243001
#17 5.223   Downloading pyyaml-6.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.4 kB)
2025-Dec-25 13:22:23.253113
#17 5.266 Collecting uvloop>=0.15.1 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 13:22:23.253113
#17 5.274   Downloading uvloop-0.22.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (4.9 kB)
2025-Dec-25 13:22:23.253113
#17 5.353 Collecting watchfiles>=0.13 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 13:22:23.360335
#17 5.359   Downloading watchfiles-1.1.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.9 kB)
2025-Dec-25 13:22:23.360335
#17 5.470 Collecting websockets>=10.4 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 13:22:23.497641
#17 5.474   Downloading websockets-15.0.1-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.8 kB)
2025-Dec-25 13:22:23.497641
#17 5.607 Collecting greenlet>=1 (from sqlalchemy->-r requirements.txt (line 3))
2025-Dec-25 13:22:23.608665
#17 5.610   Downloading greenlet-3.3.0-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (4.1 kB)
2025-Dec-25 13:22:23.608665
#17 5.656 Collecting anyio (from httpx->-r requirements.txt (line 5))
2025-Dec-25 13:22:23.608665
#17 5.663   Downloading anyio-4.12.0-py3-none-any.whl.metadata (4.3 kB)
2025-Dec-25 13:22:23.608665
#17 5.718 Collecting certifi (from httpx->-r requirements.txt (line 5))
2025-Dec-25 13:22:23.714068
#17 5.724   Downloading certifi-2025.11.12-py3-none-any.whl.metadata (2.5 kB)
2025-Dec-25 13:22:23.714068
#17 5.765 Collecting httpcore==1.* (from httpx->-r requirements.txt (line 5))
2025-Dec-25 13:22:23.714068
#17 5.769   Downloading httpcore-1.0.9-py3-none-any.whl.metadata (21 kB)
2025-Dec-25 13:22:23.714068
#17 5.792 Collecting idna (from httpx->-r requirements.txt (line 5))
2025-Dec-25 13:22:23.714068
#17 5.795   Downloading idna-3.11-py3-none-any.whl.metadata (8.4 kB)
2025-Dec-25 13:22:23.714068
#17 5.824 Collecting aiofiles>=24.1.0 (from python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 13:22:23.844564
#17 5.830   Downloading aiofiles-25.1.0-py3-none-any.whl.metadata (6.3 kB)
2025-Dec-25 13:22:23.844564
#17 5.867 Collecting async-property>=0.2.2 (from python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 13:22:23.844564
#17 5.875   Downloading async_property-0.2.2-py2.py3-none-any.whl.metadata (5.3 kB)
2025-Dec-25 13:22:23.850875
#17 5.904 Collecting deprecation>=2.1.0 (from python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 13:22:23.850875
#17 5.909   Downloading deprecation-2.1.0-py2.py3-none-any.whl.metadata (4.6 kB)
2025-Dec-25 13:22:23.850875
#17 5.953 Collecting jwcrypto>=1.5.4 (from python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 13:22:24.048835
#17 5.960   Downloading jwcrypto-1.5.6-py3-none-any.whl.metadata (3.1 kB)
2025-Dec-25 13:22:24.061738
#17 5.987 Collecting requests-toolbelt>=0.6.0 (from python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 13:22:24.061738
#17 5.993   Downloading requests_toolbelt-1.0.0-py2.py3-none-any.whl.metadata (14 kB)
2025-Dec-25 13:22:24.061738
#17 6.023 Collecting argon2-cffi (from minio->-r requirements.txt (line 7))
2025-Dec-25 13:22:24.061738
#17 6.028   Downloading argon2_cffi-25.1.0-py3-none-any.whl.metadata (4.1 kB)
2025-Dec-25 13:22:24.061738
#17 6.159 Collecting pycryptodome (from minio->-r requirements.txt (line 7))
2025-Dec-25 13:22:24.270215
#17 6.167   Downloading pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (3.4 kB)
2025-Dec-25 13:22:24.270215
#17 6.223 Collecting urllib3 (from minio->-r requirements.txt (line 7))
2025-Dec-25 13:22:24.270215
#17 6.230   Downloading urllib3-2.6.2-py3-none-any.whl.metadata (6.6 kB)
2025-Dec-25 13:22:24.297278
#17 6.405 Collecting charset_normalizer<4,>=2 (from requests->-r requirements.txt (line 8))
2025-Dec-25 13:22:24.308255
2025-Dec-25 13:22:24.404576
#17 6.417   Downloading charset_normalizer-3.4.4-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (37 kB)
2025-Dec-25 13:22:24.404576
#17 6.515 Collecting bcrypt>=3.1.0 (from passlib[bcrypt]->-r requirements.txt (line 10))
2025-Dec-25 13:22:24.556260
#17 6.524   Downloading bcrypt-5.0.0-cp39-abi3-manylinux_2_34_x86_64.whl.metadata (10 kB)
2025-Dec-25 13:22:24.556260
#17 6.557 Collecting ecdsa!=0.15 (from python-jose[cryptography]->-r requirements.txt (line 11))
2025-Dec-25 13:22:24.556260
#17 6.563   Downloading ecdsa-0.19.1-py2.py3-none-any.whl.metadata (29 kB)
2025-Dec-25 13:22:24.556260
#17 6.608 Collecting rsa!=4.1.1,!=4.4,<5.0,>=4.0 (from python-jose[cryptography]->-r requirements.txt (line 11))
2025-Dec-25 13:22:24.556260
#17 6.613   Downloading rsa-4.9.1-py3-none-any.whl.metadata (5.6 kB)
2025-Dec-25 13:22:24.556260
#17 6.661 Collecting pyasn1>=0.5.0 (from python-jose[cryptography]->-r requirements.txt (line 11))
2025-Dec-25 13:22:24.710493
#17 6.668   Downloading pyasn1-0.6.1-py3-none-any.whl.metadata (8.4 kB)
2025-Dec-25 13:22:24.759867
#17 6.870 Collecting cryptography>=3.4.0 (from python-jose[cryptography]->-r requirements.txt (line 11))
2025-Dec-25 13:22:24.958457
#17 6.879   Downloading cryptography-46.0.3-cp311-abi3-manylinux_2_34_x86_64.whl.metadata (5.7 kB)
2025-Dec-25 13:22:24.958457
#17 6.914 Collecting tzlocal>=3.0 (from APScheduler->-r requirements.txt (line 15))
2025-Dec-25 13:22:24.958457
#17 6.918   Downloading tzlocal-5.3.1-py3-none-any.whl.metadata (7.6 kB)
2025-Dec-25 13:22:25.073508
#17 7.181 Collecting cffi>=2.0.0 (from cryptography>=3.4.0->python-jose[cryptography]->-r requirements.txt (line 11))
2025-Dec-25 13:22:25.171422
#17 7.189   Downloading cffi-2.0.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (2.6 kB)
2025-Dec-25 13:22:25.171422
#17 7.239 Collecting packaging (from deprecation>=2.1.0->python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 13:22:25.171422
#17 7.244   Downloading packaging-25.0-py3-none-any.whl.metadata (3.3 kB)
2025-Dec-25 13:22:25.171422
#17 7.281 Collecting six>=1.9.0 (from ecdsa!=0.15->python-jose[cryptography]->-r requirements.txt (line 11))
2025-Dec-25 13:22:25.400589
#17 7.286   Downloading six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
2025-Dec-25 13:22:25.400589
#17 7.349 Collecting annotated-types>=0.6.0 (from pydantic>=2.7.0->fastapi->-r requirements.txt (line 1))
2025-Dec-25 13:22:25.400589
#17 7.357   Downloading annotated_types-0.7.0-py3-none-any.whl.metadata (15 kB)
2025-Dec-25 13:22:26.115514
#17 8.225 Collecting pydantic-core==2.41.5 (from pydantic>=2.7.0->fastapi->-r requirements.txt (line 1))
2025-Dec-25 13:22:26.320453
#17 8.232   Downloading pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (7.3 kB)
2025-Dec-25 13:22:26.320453
#17 8.284 Collecting typing-inspection>=0.4.2 (from pydantic>=2.7.0->fastapi->-r requirements.txt (line 1))
2025-Dec-25 13:22:26.320453
#17 8.290   Downloading typing_inspection-0.4.2-py3-none-any.whl.metadata (2.6 kB)
2025-Dec-25 13:22:26.320453
#17 8.427 Collecting argon2-cffi-bindings (from argon2-cffi->minio->-r requirements.txt (line 7))
2025-Dec-25 13:22:26.453606
#17 8.438   Downloading argon2_cffi_bindings-25.1.0-cp39-abi3-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl.metadata (7.4 kB)
2025-Dec-25 13:22:26.464751
#17 8.502 Collecting pycparser (from cffi>=2.0.0->cryptography>=3.4.0->python-jose[cryptography]->-r requirements.txt (line 11))
2025-Dec-25 13:22:26.464751
#17 8.509   Downloading pycparser-2.23-py3-none-any.whl.metadata (993 bytes)
2025-Dec-25 13:22:26.464751
#17 8.563 Downloading fastapi-0.127.0-py3-none-any.whl (112 kB)
2025-Dec-25 13:22:26.562319
#17 8.578 Downloading sqlalchemy-2.0.45-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (3.3 MB)
2025-Dec-25 13:22:26.575669
#17 8.653    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.3/3.3 MB 55.2 MB/s eta 0:00:00
2025-Dec-25 13:22:26.575669
#17 8.671 Downloading psycopg2_binary-2.9.11-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (4.2 MB)
2025-Dec-25 13:22:26.680832
#17 8.737    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.2/4.2 MB 63.1 MB/s eta 0:00:00
2025-Dec-25 13:22:26.688567
#17 8.751 Downloading httpx-0.28.1-py3-none-any.whl (73 kB)
2025-Dec-25 13:22:26.688567
#17 8.785 Downloading httpcore-1.0.9-py3-none-any.whl (78 kB)
2025-Dec-25 13:22:26.783577
#17 8.842 Downloading python_keycloak-5.8.1-py3-none-any.whl (77 kB)
2025-Dec-25 13:22:26.783577
#17 8.869 Downloading minio-7.2.20-py3-none-any.whl (93 kB)
2025-Dec-25 13:22:26.783577
#17 8.893 Downloading requests-2.32.5-py3-none-any.whl (64 kB)
2025-Dec-25 13:22:26.888739
#17 8.906 Downloading python_dotenv-1.2.1-py3-none-any.whl (21 kB)
2025-Dec-25 13:22:26.888739
#17 8.916 Downloading python_multipart-0.0.21-py3-none-any.whl (24 kB)
2025-Dec-25 13:22:26.888739
#17 8.927 Downloading stripe-14.1.0-py3-none-any.whl (2.1 MB)
2025-Dec-25 13:22:26.888739
#17 8.957    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 79.2 MB/s eta 0:00:00
2025-Dec-25 13:22:26.888739
#17 8.963 Downloading prometheus_client-0.23.1-py3-none-any.whl (61 kB)
2025-Dec-25 13:22:26.888739
#17 8.971 Downloading apscheduler-3.11.2-py3-none-any.whl (64 kB)
2025-Dec-25 13:22:26.888739
#17 8.980 Downloading aiofiles-25.1.0-py3-none-any.whl (14 kB)
2025-Dec-25 13:22:26.888739
#17 8.988 Downloading annotated_doc-0.0.4-py3-none-any.whl (5.3 kB)
2025-Dec-25 13:22:26.888739
#17 8.998 Downloading async_property-0.2.2-py2.py3-none-any.whl (9.5 kB)
2025-Dec-25 13:22:27.003543
#17 9.010 Downloading bcrypt-5.0.0-cp39-abi3-manylinux_2_34_x86_64.whl (278 kB)
2025-Dec-25 13:22:27.009289
#17 9.019 Downloading certifi-2025.11.12-py3-none-any.whl (159 kB)
2025-Dec-25 13:22:27.009289
#17 9.029 Downloading charset_normalizer-3.4.4-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (153 kB)
2025-Dec-25 13:22:27.009289
#17 9.043 Downloading click-8.3.1-py3-none-any.whl (108 kB)
2025-Dec-25 13:22:27.009289
#17 9.056 Downloading cryptography-46.0.3-cp311-abi3-manylinux_2_34_x86_64.whl (4.5 MB)
2025-Dec-25 13:22:27.009289
#17 9.114    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.5/4.5 MB 81.5 MB/s eta 0:00:00
2025-Dec-25 13:22:27.114540
#17 9.127 Downloading deprecation-2.1.0-py2.py3-none-any.whl (11 kB)
2025-Dec-25 13:22:27.114540
#17 9.142 Downloading ecdsa-0.19.1-py2.py3-none-any.whl (150 kB)
2025-Dec-25 13:22:27.114540
#17 9.154 Downloading greenlet-3.3.0-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (609 kB)
2025-Dec-25 13:22:27.114540
#17 9.168    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 609.9/609.9 kB 59.5 MB/s eta 0:00:00
2025-Dec-25 13:22:27.114540
#17 9.173 Downloading h11-0.16.0-py3-none-any.whl (37 kB)
2025-Dec-25 13:22:27.114540
#17 9.187 Downloading httptools-0.7.1-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (517 kB)
2025-Dec-25 13:22:27.114540
#17 9.202 Downloading idna-3.11-py3-none-any.whl (71 kB)
2025-Dec-25 13:22:27.114540
#17 9.213 Downloading jwcrypto-1.5.6-py3-none-any.whl (92 kB)
2025-Dec-25 13:22:27.114540
#17 9.224 Downloading pyasn1-0.6.1-py3-none-any.whl (83 kB)
2025-Dec-25 13:22:27.217812
#17 9.238 Downloading pydantic-2.12.5-py3-none-any.whl (463 kB)
2025-Dec-25 13:22:27.217812
#17 9.250 Downloading pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.1 MB)
2025-Dec-25 13:22:27.217812
#17 9.285    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 63.8 MB/s eta 0:00:00
2025-Dec-25 13:22:27.217812
#17 9.293 Downloading pyyaml-6.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (807 kB)
2025-Dec-25 13:22:27.217812
#17 9.305    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 807.9/807.9 kB 75.3 MB/s eta 0:00:00
2025-Dec-25 13:22:27.217812
#17 9.309 Downloading requests_toolbelt-1.0.0-py2.py3-none-any.whl (54 kB)
2025-Dec-25 13:22:27.217812
#17 9.320 Downloading rsa-4.9.1-py3-none-any.whl (34 kB)
2025-Dec-25 13:22:27.217812
#17 9.328 Downloading starlette-0.50.0-py3-none-any.whl (74 kB)
2025-Dec-25 13:22:27.337311
#17 9.337 Downloading anyio-4.12.0-py3-none-any.whl (113 kB)
2025-Dec-25 13:22:27.337311
#17 9.346 Downloading typing_extensions-4.15.0-py3-none-any.whl (44 kB)
2025-Dec-25 13:22:27.337311
#17 9.354 Downloading tzlocal-5.3.1-py3-none-any.whl (18 kB)
2025-Dec-25 13:22:27.337311
#17 9.367 Downloading urllib3-2.6.2-py3-none-any.whl (131 kB)
2025-Dec-25 13:22:27.337311
#17 9.384 Downloading uvloop-0.22.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (4.4 MB)
2025-Dec-25 13:22:27.337311
#17 9.447    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.4/4.4 MB 72.3 MB/s eta 0:00:00
2025-Dec-25 13:22:27.440603
#17 9.460 Downloading watchfiles-1.1.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (456 kB)
2025-Dec-25 13:22:27.440603
#17 9.471 Downloading websockets-15.0.1-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (182 kB)
2025-Dec-25 13:22:27.440603
#17 9.489 Downloading argon2_cffi-25.1.0-py3-none-any.whl (14 kB)
2025-Dec-25 13:22:27.440603
#17 9.506 Downloading passlib-1.7.4-py2.py3-none-any.whl (525 kB)
2025-Dec-25 13:22:27.440603
#17 9.534    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 525.6/525.6 kB 19.7 MB/s eta 0:00:00
2025-Dec-25 13:22:27.440603
#17 9.551 Downloading pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.3 MB)
2025-Dec-25 13:22:27.552520
#17 9.577    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.3/2.3 MB 95.8 MB/s eta 0:00:00
2025-Dec-25 13:22:27.552520
#17 9.580 Downloading python_jose-3.5.0-py2.py3-none-any.whl (34 kB)
2025-Dec-25 13:22:27.552520
#17 9.586 Downloading uvicorn-0.40.0-py3-none-any.whl (68 kB)
2025-Dec-25 13:22:27.552520
#17 9.595 Downloading annotated_types-0.7.0-py3-none-any.whl (13 kB)
2025-Dec-25 13:22:27.552520
#17 9.604 Downloading cffi-2.0.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (219 kB)
2025-Dec-25 13:22:27.552520
#17 9.615 Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
2025-Dec-25 13:22:27.552520
#17 9.625 Downloading typing_inspection-0.4.2-py3-none-any.whl (14 kB)
2025-Dec-25 13:22:27.552520
#17 9.635 Downloading argon2_cffi_bindings-25.1.0-cp39-abi3-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl (87 kB)
2025-Dec-25 13:22:27.552520
#17 9.647 Downloading packaging-25.0-py3-none-any.whl (66 kB)
2025-Dec-25 13:22:27.552520
#17 9.663 Downloading pycparser-2.23-py3-none-any.whl (118 kB)
2025-Dec-25 13:22:27.791486
#17 9.902 Installing collected packages: passlib, async-property, websockets, uvloop, urllib3, tzlocal, typing-extensions, six, pyyaml, python-multipart, python-dotenv, pycryptodome, pycparser, pyasn1, psycopg2-binary, prometheus_client, packaging, idna, httptools, h11, greenlet, click, charset_normalizer, certifi, bcrypt, annotated-types, annotated-doc, aiofiles, uvicorn, typing-inspection, sqlalchemy, rsa, requests, pydantic-core, httpcore, ecdsa, deprecation, cffi, APScheduler, anyio, watchfiles, stripe, starlette, requests-toolbelt, python-jose, pydantic, httpx, cryptography, argon2-cffi-bindings, jwcrypto, fastapi, argon2-cffi, python-keycloak, minio
2025-Dec-25 13:22:36.187027
#17 18.30 Successfully installed APScheduler-3.11.2 aiofiles-25.1.0 annotated-doc-0.0.4 annotated-types-0.7.0 anyio-4.12.0 argon2-cffi-25.1.0 argon2-cffi-bindings-25.1.0 async-property-0.2.2 bcrypt-5.0.0 certifi-2025.11.12 cffi-2.0.0 charset_normalizer-3.4.4 click-8.3.1 cryptography-46.0.3 deprecation-2.1.0 ecdsa-0.19.1 fastapi-0.127.0 greenlet-3.3.0 h11-0.16.0 httpcore-1.0.9 httptools-0.7.1 httpx-0.28.1 idna-3.11 jwcrypto-1.5.6 minio-7.2.20 packaging-25.0 passlib-1.7.4 prometheus_client-0.23.1 psycopg2-binary-2.9.11 pyasn1-0.6.1 pycparser-2.23 pycryptodome-3.23.0 pydantic-2.12.5 pydantic-core-2.41.5 python-dotenv-1.2.1 python-jose-3.5.0 python-keycloak-5.8.1 python-multipart-0.0.21 pyyaml-6.0.3 requests-2.32.5 requests-toolbelt-1.0.0 rsa-4.9.1 six-1.17.0 sqlalchemy-2.0.45 starlette-0.50.0 stripe-14.1.0 typing-extensions-4.15.0 typing-inspection-0.4.2 tzlocal-5.3.1 urllib3-2.6.2 uvicorn-0.40.0 uvloop-0.22.1 watchfiles-1.1.1 websockets-15.0.1
2025-Dec-25 13:22:36.423527
#17 18.30 WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager, possibly rendering your system unusable. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv. Use the --root-user-action option if you know what you are doing and want to suppress this warning.
2025-Dec-25 13:22:36.423527
#17 18.38
2025-Dec-25 13:22:36.423527
#17 18.38 [notice] A new release of pip is available: 25.0.1 -> 25.3
2025-Dec-25 13:22:36.423527
#17 18.38 [notice] To update, run: pip install --upgrade pip
2025-Dec-25 13:22:36.910854
#17 DONE 19.0s
2025-Dec-25 13:22:36.922321
#15 [dashboard deps 4/4] RUN npm install
2025-Dec-25 13:22:37.076695
#15 ...
2025-Dec-25 13:22:37.076695
2025-Dec-25 13:22:37.076695
#18 [api 5/5] COPY . .
2025-Dec-25 13:22:41.945885
#18 ...
2025-Dec-25 13:22:41.945885
2025-Dec-25 13:22:41.945885
#15 [dashboard deps 4/4] RUN npm install
2025-Dec-25 13:22:41.945885
#15 34.91
2025-Dec-25 13:22:41.945885
#15 34.91 added 473 packages, and audited 474 packages in 34s
2025-Dec-25 13:22:41.945885
#15 34.91
2025-Dec-25 13:22:41.945885
#15 34.91 154 packages are looking for funding
2025-Dec-25 13:22:41.945885
#15 34.91   run `npm fund` for details
2025-Dec-25 13:22:41.945885
#15 34.92
2025-Dec-25 13:22:41.945885
#15 34.92 found 0 vulnerabilities
2025-Dec-25 13:22:41.945885
#15 34.92 npm notice
2025-Dec-25 13:22:41.945885
#15 34.92 npm notice New major version of npm available! 10.8.2 -> 11.7.0
2025-Dec-25 13:22:41.945885
#15 34.92 npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.7.0
2025-Dec-25 13:22:41.945885
#15 34.92 npm notice To update run: npm install -g npm@11.7.0
2025-Dec-25 13:22:41.945885
#15 34.92 npm notice
2025-Dec-25 13:22:41.945885
#15 DONE 35.4s
2025-Dec-25 13:22:42.096045
#18 [api 5/5] COPY . .
2025-Dec-25 13:22:44.436191
#18 DONE 7.5s
2025-Dec-25 13:22:44.594686
#19 [api] exporting to image
2025-Dec-25 13:22:44.594686
#19 exporting layers
2025-Dec-25 13:22:48.568915
#19 exporting layers 4.1s done
2025-Dec-25 13:22:48.568915
#19 writing image sha256:a613d100696198a3056880a63f6977fefb1e4b0778e15d7eb63a22356eaf2de4
2025-Dec-25 13:22:48.777109
#19 writing image sha256:a613d100696198a3056880a63f6977fefb1e4b0778e15d7eb63a22356eaf2de4 done
2025-Dec-25 13:22:48.777109
#19 naming to docker.io/library/hck4w0k4ww8kk4gccw000ggg-api done
2025-Dec-25 13:22:48.777109
#19 DONE 4.1s
2025-Dec-25 13:22:48.777109
2025-Dec-25 13:22:48.777109
#20 [api] resolving provenance for metadata file
2025-Dec-25 13:22:48.777109
#20 DONE 0.0s
2025-Dec-25 13:22:52.250153
#21 [dashboard builder 3/5] COPY --from=deps /app/node_modules ./node_modules
2025-Dec-25 13:23:05.181875
#21 DONE 12.9s
2025-Dec-25 13:23:05.382601
#22 [dashboard builder 4/5] COPY . .
2025-Dec-25 13:23:05.382601
#22 DONE 0.0s
2025-Dec-25 13:23:05.382601
2025-Dec-25 13:23:05.382601
#23 [dashboard builder 5/5] RUN npm run build
2025-Dec-25 13:23:06.006611
#23 0.777
2025-Dec-25 13:23:06.006611
#23 0.777 > dashboard@0.1.0 build
2025-Dec-25 13:23:06.006611
#23 0.777 > next build
2025-Dec-25 13:23:06.006611
#23 0.777
2025-Dec-25 13:23:06.887170
#23 1.658 Attention: Next.js now collects completely anonymous telemetry regarding usage.
2025-Dec-25 13:23:07.011651
#23 1.660 This information is used to shape Next.js' roadmap and prioritize features.
2025-Dec-25 13:23:07.021503
#23 1.660 You can learn more, including how to opt-out if you'd not like to participate in this anonymous program, by visiting the following URL:
2025-Dec-25 13:23:07.021503
#23 1.660 https://nextjs.org/telemetry
2025-Dec-25 13:23:07.021503
#23 1.660
2025-Dec-25 13:23:07.021503
#23 1.672 ▲ Next.js 16.1.0 (Turbopack)
2025-Dec-25 13:23:07.021503
#23 1.672
2025-Dec-25 13:23:07.021503
#23 1.781   Creating an optimized production build ...
2025-Dec-25 13:23:25.193458
#23 19.96 ✓ Compiled successfully in 17.7s
2025-Dec-25 13:23:25.380715
#23 20.00   Running TypeScript ...
2025-Dec-25 13:23:34.823508
#23 29.59   Collecting page data using 1 worker ...
2025-Dec-25 13:23:35.559481
#23 30.33   Generating static pages using 1 worker (0/11) ...
2025-Dec-25 13:23:35.864397
#23 30.64   Generating static pages using 1 worker (2/11)
2025-Dec-25 13:23:36.091128
#23 30.64   Generating static pages using 1 worker (5/11)
2025-Dec-25 13:23:36.091128
#23 30.64   Generating static pages using 1 worker (8/11)
2025-Dec-25 13:23:36.091128
#23 30.69 ✓ Generating static pages using 1 worker (11/11) in 364.3ms
2025-Dec-25 13:23:36.091128
#23 30.70   Finalizing page optimization ...
2025-Dec-25 13:23:36.091128
#23 30.71
2025-Dec-25 13:23:36.091128
#23 30.71 Route (app)
2025-Dec-25 13:23:36.091128
#23 30.71 ┌ ○ /
2025-Dec-25 13:23:36.091128
#23 30.71 ├ ○ /_not-found
2025-Dec-25 13:23:36.091128
#23 30.71 ├ ○ /login
2025-Dec-25 13:23:36.091128
#23 30.71 ├ ○ /org
2025-Dec-25 13:23:36.091128
#23 30.71 ├ ƒ /org/[orgId]/billing
2025-Dec-25 13:23:36.091128
#23 30.71 ├ ƒ /org/[orgId]/projects
2025-Dec-25 13:23:36.091128
#23 30.71 ├ ƒ /org/[orgId]/projects/new
2025-Dec-25 13:23:36.091128
#23 30.71 ├ ƒ /org/[orgId]/settings
2025-Dec-25 13:23:36.091128
#23 30.71 ├ ƒ /org/[orgId]/team
2025-Dec-25 13:23:36.091128
#23 30.71 ├ ○ /projects
2025-Dec-25 13:23:36.091128
#23 30.71 ├ ƒ /projects/[id]
2025-Dec-25 13:23:36.091128
#23 30.71 ├ ƒ /projects/[id]/auth
2025-Dec-25 13:23:36.091128
#23 30.71 ├ ƒ /projects/[id]/backups
2025-Dec-25 13:23:36.091128
#23 30.71 ├ ƒ /projects/[id]/database
2025-Dec-25 13:23:36.091128
#23 30.71 ├ ƒ /projects/[id]/database/[table]
2025-Dec-25 13:23:36.091128
#23 30.71 ├ ƒ /projects/[id]/edge-functions
2025-Dec-25 13:23:36.091128
#23 30.71 ├ ƒ /projects/[id]/logs
2025-Dec-25 13:23:36.091128
#23 30.71 ├ ƒ /projects/[id]/realtime
2025-Dec-25 13:23:36.091128
#23 30.71 ├ ƒ /projects/[id]/secrets
2025-Dec-25 13:23:36.091128
#23 30.71 ├ ƒ /projects/[id]/settings
2025-Dec-25 13:23:36.091128
#23 30.71 ├ ƒ /projects/[id]/settings/deployment
2025-Dec-25 13:23:36.091128
#23 30.71 ├ ƒ /projects/[id]/sql
2025-Dec-25 13:23:36.091128
#23 30.71 ├ ƒ /projects/[id]/storage
2025-Dec-25 13:23:36.091128
#23 30.71 ├ ○ /projects/new
2025-Dec-25 13:23:36.091128
#23 30.71 ├ ○ /settings/organization
2025-Dec-25 13:23:36.091128
#23 30.71 ├ ƒ /settings/organization/[id]
2025-Dec-25 13:23:36.091128
#23 30.71 ├ ○ /settings/profile
2025-Dec-25 13:23:36.091128
#23 30.71 └ ○ /signup
2025-Dec-25 13:23:36.091128
#23 30.71
2025-Dec-25 13:23:36.091128
#23 30.71
2025-Dec-25 13:23:36.091128
#23 30.71 ○  (Static)   prerendered as static content
2025-Dec-25 13:23:36.091128
#23 30.71 ƒ  (Dynamic)  server-rendered on demand
2025-Dec-25 13:23:36.091128
#23 30.71
2025-Dec-25 13:23:36.146968
#23 30.92 npm notice
2025-Dec-25 13:23:36.146968
#23 30.92 npm notice New major version of npm available! 10.8.2 -> 11.7.0
2025-Dec-25 13:23:36.146968
#23 30.92 npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.7.0
2025-Dec-25 13:23:36.146968
#23 30.92 npm notice To update run: npm install -g npm@11.7.0
2025-Dec-25 13:23:36.146968
#23 30.92 npm notice
2025-Dec-25 13:23:36.380939
#23 DONE 31.0s
2025-Dec-25 13:23:37.163354
#24 [dashboard runner 3/6] COPY --from=builder /app/public ./public
2025-Dec-25 13:23:37.348254
#24 DONE 0.0s
2025-Dec-25 13:23:43.852540
#25 [dashboard runner 4/6] COPY --from=builder /app/.next ./.next
2025-Dec-25 13:23:44.057275
#25 DONE 0.2s
2025-Dec-25 13:23:44.213260
#26 [dashboard runner 5/6] COPY --from=builder /app/node_modules ./node_modules
2025-Dec-25 13:23:53.204719
#26 DONE 9.1s
2025-Dec-25 13:23:53.403600
#27 [dashboard runner 6/6] COPY --from=builder /app/package.json ./package.json
2025-Dec-25 13:23:53.403600
#27 DONE 0.0s
2025-Dec-25 13:23:53.403600
2025-Dec-25 13:23:53.403600
#28 [dashboard] exporting to image
2025-Dec-25 13:23:53.403600
#28 exporting layers
2025-Dec-25 13:24:06.852841
#28 exporting layers 13.6s done
2025-Dec-25 13:24:06.924157
#28 writing image sha256:523bb8845603ccab7735369911e48e499c9ea3e5c5af89d4b79c816b677b74d6 done
2025-Dec-25 13:24:06.924157
#28 naming to docker.io/library/hck4w0k4ww8kk4gccw000ggg-dashboard done
2025-Dec-25 13:24:06.924157
#28 DONE 13.6s
2025-Dec-25 13:24:06.924157
2025-Dec-25 13:24:06.924157
#29 [dashboard] resolving provenance for metadata file
2025-Dec-25 13:24:06.924157
#29 DONE 0.0s
2025-Dec-25 13:24:06.938746
api  Built
2025-Dec-25 13:24:06.938746
dashboard  Built
2025-Dec-25 13:24:06.974808
Creating .env file with runtime variables for build phase.
2025-Dec-25 13:24:07.308980
[CMD]: docker exec d8cwk4kwosg0c08w0gk0kcow bash -c 'cat /artifacts/d8cwk4kwosg0c08w0gk0kcow/.env'
2025-Dec-25 13:24:07.308980
SOURCE_COMMIT=b073128f92a4c217303a00090740e2745f9c297c
2025-Dec-25 13:24:07.308980
COOLIFY_URL=
2025-Dec-25 13:24:07.308980
COOLIFY_FQDN=
2025-Dec-25 13:24:07.308980
SERVICE_URL_DASHBOARD=https://supalove.hayataxi.online
2025-Dec-25 13:24:07.308980
SERVICE_FQDN_DASHBOARD=supalove.hayataxi.online
2025-Dec-25 13:24:07.308980
SERVICE_URL_API=https://api.hayataxi.online
2025-Dec-25 13:24:07.308980
SERVICE_FQDN_API=api.hayataxi.online
2025-Dec-25 13:24:07.308980
SERVICE_URL_KEYCLOAK=https://auth.hayataxi.online
2025-Dec-25 13:24:07.308980
SERVICE_FQDN_KEYCLOAK=auth.hayataxi.online
2025-Dec-25 13:24:07.308980
SERVICE_URL_MINIO=https://s3.hayataxi.online
2025-Dec-25 13:24:07.308980
SERVICE_FQDN_MINIO=s3.hayataxi.online
2025-Dec-25 13:24:07.308980
SERVICE_NAME_CONTROL-PLANE-DB=control-plane-db
2025-Dec-25 13:24:07.308980
SERVICE_NAME_API=api
2025-Dec-25 13:24:07.308980
SERVICE_NAME_DASHBOARD=dashboard
2025-Dec-25 13:24:07.308980
SERVICE_NAME_KEYCLOAK=keycloak
2025-Dec-25 13:24:07.308980
SERVICE_NAME_MINIO=minio
2025-Dec-25 13:24:07.308980
POSTGRES_USER=platform
2025-Dec-25 13:24:07.308980
POSTGRES_PASSWORD=platform
2025-Dec-25 13:24:07.308980
POSTGRES_DB=control_plane
2025-Dec-25 13:24:07.308980
KEYCLOAK_ADMIN_USER=admin
2025-Dec-25 13:24:07.308980
KEYCLOAK_ADMIN_PASSWORD=admin
2025-Dec-25 13:24:07.308980
MINIO_ROOT_USER=minioadmin
2025-Dec-25 13:24:07.308980
MINIO_ROOT_PASSWORD=minioadmin
2025-Dec-25 13:24:07.308980
URL=http://localhost:8000
2025-Dec-25 13:24:07.308980
NEXT_PUBLIC_API_URL=https://api.hayataxi.online
2025-Dec-25 13:24:07.308980
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8000
2025-Dec-25 13:24:07.308980
HOST=0.0.0.0
2025-Dec-25 13:24:07.474473
Removing old containers.
2025-Dec-25 13:24:07.965046
[CMD]: docker stop --time=30 dashboard-hck4w0k4ww8kk4gccw000ggg-130422668472
2025-Dec-25 13:24:07.965046
dashboard-hck4w0k4ww8kk4gccw000ggg-130422668472
2025-Dec-25 13:24:08.103272
[CMD]: docker rm -f dashboard-hck4w0k4ww8kk4gccw000ggg-130422668472
2025-Dec-25 13:24:08.103272
dashboard-hck4w0k4ww8kk4gccw000ggg-130422668472
2025-Dec-25 13:24:08.830694
[CMD]: docker stop --time=30 api-hck4w0k4ww8kk4gccw000ggg-130422654801
2025-Dec-25 13:24:08.830694
api-hck4w0k4ww8kk4gccw000ggg-130422654801
2025-Dec-25 13:24:09.057356
[CMD]: docker rm -f api-hck4w0k4ww8kk4gccw000ggg-130422654801
2025-Dec-25 13:24:09.057356
api-hck4w0k4ww8kk4gccw000ggg-130422654801
2025-Dec-25 13:24:09.431664
[CMD]: docker stop --time=30 keycloak-hck4w0k4ww8kk4gccw000ggg-130422676997
2025-Dec-25 13:24:09.431664
keycloak-hck4w0k4ww8kk4gccw000ggg-130422676997
2025-Dec-25 13:24:09.607603
[CMD]: docker rm -f keycloak-hck4w0k4ww8kk4gccw000ggg-130422676997
2025-Dec-25 13:24:09.607603
keycloak-hck4w0k4ww8kk4gccw000ggg-130422676997
2025-Dec-25 13:24:09.865611
[CMD]: docker stop --time=30 minio-hck4w0k4ww8kk4gccw000ggg-130422687909
2025-Dec-25 13:24:09.865611
minio-hck4w0k4ww8kk4gccw000ggg-130422687909
2025-Dec-25 13:24:10.012148
[CMD]: docker rm -f minio-hck4w0k4ww8kk4gccw000ggg-130422687909
2025-Dec-25 13:24:10.012148
minio-hck4w0k4ww8kk4gccw000ggg-130422687909
2025-Dec-25 13:24:10.279746
[CMD]: docker stop --time=30 control-plane-db-hck4w0k4ww8kk4gccw000ggg-130422638422
2025-Dec-25 13:24:10.279746
control-plane-db-hck4w0k4ww8kk4gccw000ggg-130422638422
2025-Dec-25 13:24:10.407771
[CMD]: docker rm -f control-plane-db-hck4w0k4ww8kk4gccw000ggg-130422638422
2025-Dec-25 13:24:10.407771
control-plane-db-hck4w0k4ww8kk4gccw000ggg-130422638422
2025-Dec-25 13:24:10.417909
Starting new application.
2025-Dec-25 13:24:10.958280
[CMD]: docker exec d8cwk4kwosg0c08w0gk0kcow bash -c 'SOURCE_COMMIT=b073128f92a4c217303a00090740e2745f9c297c COOLIFY_BRANCH=main COOLIFY_RESOURCE_UUID=hck4w0k4ww8kk4gccw000ggg COOLIFY_CONTAINER_NAME=hck4w0k4ww8kk4gccw000ggg-132143017536  docker compose --env-file /artifacts/d8cwk4kwosg0c08w0gk0kcow/.env --project-name hck4w0k4ww8kk4gccw000ggg --project-directory /artifacts/d8cwk4kwosg0c08w0gk0kcow -f /artifacts/d8cwk4kwosg0c08w0gk0kcow/docker-compose.coolify.yml up -d'
2025-Dec-25 13:24:10.958280
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-132201958859  Creating
2025-Dec-25 13:24:10.966499
Container minio-hck4w0k4ww8kk4gccw000ggg-132202024876  Creating
2025-Dec-25 13:24:11.011852
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-132201958859  Created
2025-Dec-25 13:24:11.011852
Container keycloak-hck4w0k4ww8kk4gccw000ggg-132202009031  Creating
2025-Dec-25 13:24:11.019715
Container minio-hck4w0k4ww8kk4gccw000ggg-132202024876  Created
2025-Dec-25 13:24:11.031506
Container keycloak-hck4w0k4ww8kk4gccw000ggg-132202009031  Created
2025-Dec-25 13:24:11.031506
Container api-hck4w0k4ww8kk4gccw000ggg-132201978563  Creating
2025-Dec-25 13:24:11.049767
Container api-hck4w0k4ww8kk4gccw000ggg-132201978563  Created
2025-Dec-25 13:24:11.049767
Container dashboard-hck4w0k4ww8kk4gccw000ggg-132201995907  Creating
2025-Dec-25 13:24:11.065879
Container dashboard-hck4w0k4ww8kk4gccw000ggg-132201995907  Created
2025-Dec-25 13:24:11.077440
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-132201958859  Starting
2025-Dec-25 13:24:11.077440
Container minio-hck4w0k4ww8kk4gccw000ggg-132202024876  Starting
2025-Dec-25 13:24:11.378644
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-132201958859  Started
2025-Dec-25 13:24:11.378644
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-132201958859  Waiting
2025-Dec-25 13:24:11.453136
Container minio-hck4w0k4ww8kk4gccw000ggg-132202024876  Started
2025-Dec-25 13:24:16.877652
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-132201958859  Healthy
2025-Dec-25 13:24:16.903828
Container keycloak-hck4w0k4ww8kk4gccw000ggg-132202009031  Starting
2025-Dec-25 13:24:17.106256
Container keycloak-hck4w0k4ww8kk4gccw000ggg-132202009031  Started
2025-Dec-25 13:24:17.106256
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-132201958859  Waiting
2025-Dec-25 13:24:17.608994
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-132201958859  Healthy
2025-Dec-25 13:24:17.608994
Container api-hck4w0k4ww8kk4gccw000ggg-132201978563  Starting
2025-Dec-25 13:24:17.912511
Container api-hck4w0k4ww8kk4gccw000ggg-132201978563  Started
2025-Dec-25 13:24:17.912511
Container dashboard-hck4w0k4ww8kk4gccw000ggg-132201995907  Starting
2025-Dec-25 13:24:18.455806
Container dashboard-hck4w0k4ww8kk4gccw000ggg-132201995907  Started
2025-Dec-25 13:24:19.295320
New container started.
2025-Dec-25 13:24:20.285960
Gracefully shutting down build container: d8cwk4kwosg0c08w0gk0kcow
2025-Dec-25 13:24:20.985596
[CMD]: docker stop --time=30 d8cwk4kwosg0c08w0gk0kcow
2025-Dec-25 13:24:20.985596
d8cwk4kwosg0c08w0gk0kcow
2025-Dec-25 13:24:21.868670
[CMD]: docker rm -f d8cwk4kwosg0c08w0gk0kcow
2025-Dec-25 13:24:21.868670
Error response from daemon: removal of container d8cwk4kwosg0c08w0gk0kcow is already in progress