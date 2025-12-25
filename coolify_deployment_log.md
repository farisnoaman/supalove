Deployment is Finished.


2025-Dec-25 13:39:02.424584
Starting deployment of supalove to localhost.
2025-Dec-25 13:39:03.347638
Preparing container with helper image: ghcr.io/coollabsio/coolify-helper:1.0.12
2025-Dec-25 13:39:03.760122
[CMD]: docker stop --time=30 e8cs4g4gsskkkg8cc0o0c4wc
2025-Dec-25 13:39:03.760122
Error response from daemon: No such container: e8cs4g4gsskkkg8cc0o0c4wc
2025-Dec-25 13:39:04.182999
[CMD]: docker rm -f e8cs4g4gsskkkg8cc0o0c4wc
2025-Dec-25 13:39:04.182999
Error response from daemon: No such container: e8cs4g4gsskkkg8cc0o0c4wc
2025-Dec-25 13:39:04.727256
[CMD]: docker run -d --network coolify --name e8cs4g4gsskkkg8cc0o0c4wc  --rm -v /var/run/docker.sock:/var/run/docker.sock ghcr.io/coollabsio/coolify-helper:1.0.12
2025-Dec-25 13:39:04.727256
5c3ec864ba43dce4b5556689451bc1584fe7411e5b879293620e94118b9187b0
2025-Dec-25 13:39:06.426253
[CMD]: docker exec e8cs4g4gsskkkg8cc0o0c4wc bash -c 'GIT_SSH_COMMAND="ssh -o ConnectTimeout=30 -p 22 -o Port=22 -o LogLevel=ERROR -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" git ls-remote https://github.com/farisnoaman/supalove refs/heads/main'
2025-Dec-25 13:39:06.426253
7b283b8ff2bc018b8733ef1d1ca76bdc6726bd38	refs/heads/main
2025-Dec-25 13:39:06.448293
----------------------------------------
2025-Dec-25 13:39:06.457706
Importing farisnoaman/supalove:main (commit sha 7b283b8ff2bc018b8733ef1d1ca76bdc6726bd38) to /artifacts/e8cs4g4gsskkkg8cc0o0c4wc.
2025-Dec-25 13:39:06.922201
[CMD]: docker exec e8cs4g4gsskkkg8cc0o0c4wc bash -c 'git clone --depth=1 --recurse-submodules --shallow-submodules -b 'main' 'https://github.com/farisnoaman/supalove' '/artifacts/e8cs4g4gsskkkg8cc0o0c4wc' && cd '/artifacts/e8cs4g4gsskkkg8cc0o0c4wc' && if [ -f .gitmodules ]; then sed -i "s#git@\(.*\):#https://\1/#g" '/artifacts/e8cs4g4gsskkkg8cc0o0c4wc'/.gitmodules || true && git submodule sync && GIT_SSH_COMMAND="ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" git submodule update --init --recursive --depth=1; fi && cd '/artifacts/e8cs4g4gsskkkg8cc0o0c4wc' && GIT_SSH_COMMAND="ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" git lfs pull'
2025-Dec-25 13:39:06.922201
Cloning into '/artifacts/e8cs4g4gsskkkg8cc0o0c4wc'...
2025-Dec-25 13:39:13.562936
Updating files:  19% (2885/15085)
2025-Dec-25 13:39:13.593943
Updating files:  20% (3017/15085)
2025-Dec-25 13:39:13.632168
Updating files:  21% (3168/15085)
2025-Dec-25 13:39:13.668004
Updating files:  22% (3319/15085)
2025-Dec-25 13:39:13.700578
Updating files:  23% (3470/15085)
2025-Dec-25 13:39:13.846522
Updating files:  24% (3621/15085)
2025-Dec-25 13:39:13.885126
Updating files:  25% (3772/15085)
2025-Dec-25 13:39:13.915708
Updating files:  26% (3923/15085)
2025-Dec-25 13:39:13.972450
Updating files:  27% (4073/15085)
2025-Dec-25 13:39:14.003116
Updating files:  28% (4224/15085)
2025-Dec-25 13:39:14.025274
Updating files:  29% (4375/15085)
2025-Dec-25 13:39:14.046420
Updating files:  30% (4526/15085)
2025-Dec-25 13:39:14.059671
Updating files:  31% (4677/15085)
2025-Dec-25 13:39:14.074486
Updating files:  32% (4828/15085)
2025-Dec-25 13:39:14.092205
Updating files:  33% (4979/15085)
2025-Dec-25 13:39:14.148066
Updating files:  34% (5129/15085)
2025-Dec-25 13:39:14.182485
Updating files:  35% (5280/15085)
2025-Dec-25 13:39:14.233587
Updating files:  36% (5431/15085)
2025-Dec-25 13:39:14.272799
Updating files:  37% (5582/15085)
2025-Dec-25 13:39:14.289422
Updating files:  38% (5733/15085)
2025-Dec-25 13:39:14.310147
Updating files:  39% (5884/15085)
2025-Dec-25 13:39:14.326748
Updating files:  40% (6034/15085)
2025-Dec-25 13:39:14.344092
Updating files:  41% (6185/15085)
2025-Dec-25 13:39:14.361666
Updating files:  42% (6336/15085)
2025-Dec-25 13:39:14.375138
Updating files:  43% (6487/15085)
2025-Dec-25 13:39:14.393375
Updating files:  44% (6638/15085)
2025-Dec-25 13:39:14.408061
Updating files:  45% (6789/15085)
2025-Dec-25 13:39:14.422775
Updating files:  46% (6940/15085)
2025-Dec-25 13:39:14.436388
Updating files:  47% (7090/15085)
2025-Dec-25 13:39:14.448468
Updating files:  48% (7241/15085)
2025-Dec-25 13:39:14.460995
Updating files:  49% (7392/15085)
2025-Dec-25 13:39:14.476448
Updating files:  50% (7543/15085)
2025-Dec-25 13:39:14.489343
Updating files:  51% (7694/15085)
2025-Dec-25 13:39:14.504046
Updating files:  52% (7845/15085)
2025-Dec-25 13:39:14.520136
Updating files:  53% (7996/15085)
2025-Dec-25 13:39:14.539995
Updating files:  54% (8146/15085)
2025-Dec-25 13:39:14.645313
Updating files:  54% (8283/15085)
2025-Dec-25 13:39:14.650052
Updating files:  55% (8297/15085)
2025-Dec-25 13:39:14.689919
Updating files:  56% (8448/15085)
2025-Dec-25 13:39:14.701269
Updating files:  57% (8599/15085)
2025-Dec-25 13:39:14.716899
Updating files:  58% (8750/15085)
2025-Dec-25 13:39:14.740609
Updating files:  59% (8901/15085)
2025-Dec-25 13:39:14.760901
Updating files:  60% (9051/15085)
2025-Dec-25 13:39:14.783534
Updating files:  61% (9202/15085)
2025-Dec-25 13:39:14.803310
Updating files:  62% (9353/15085)
2025-Dec-25 13:39:14.817948
Updating files:  63% (9504/15085)
2025-Dec-25 13:39:14.833361
Updating files:  64% (9655/15085)
2025-Dec-25 13:39:14.914130
Updating files:  65% (9806/15085)
2025-Dec-25 13:39:14.925316
Updating files:  66% (9957/15085)
2025-Dec-25 13:39:14.940025
Updating files:  67% (10107/15085)
2025-Dec-25 13:39:14.957869
Updating files:  68% (10258/15085)
2025-Dec-25 13:39:14.977637
Updating files:  69% (10409/15085)
2025-Dec-25 13:39:14.999000
Updating files:  70% (10560/15085)
2025-Dec-25 13:39:15.016724
Updating files:  71% (10711/15085)
2025-Dec-25 13:39:15.035953
Updating files:  72% (10862/15085)
2025-Dec-25 13:39:15.058895
Updating files:  73% (11013/15085)
2025-Dec-25 13:39:15.074286
Updating files:  74% (11163/15085)
2025-Dec-25 13:39:15.090878
Updating files:  75% (11314/15085)
2025-Dec-25 13:39:15.106768
Updating files:  76% (11465/15085)
2025-Dec-25 13:39:15.121046
Updating files:  77% (11616/15085)
2025-Dec-25 13:39:15.132775
Updating files:  78% (11767/15085)
2025-Dec-25 13:39:15.149183
Updating files:  79% (11918/15085)
2025-Dec-25 13:39:15.270948
Updating files:  80% (12068/15085)
2025-Dec-25 13:39:15.304669
Updating files:  81% (12219/15085)
2025-Dec-25 13:39:15.357218
Updating files:  82% (12370/15085)
2025-Dec-25 13:39:15.371776
Updating files:  83% (12521/15085)
2025-Dec-25 13:39:15.394041
Updating files:  84% (12672/15085)
2025-Dec-25 13:39:15.415448
Updating files:  85% (12823/15085)
2025-Dec-25 13:39:15.425751
Updating files:  86% (12974/15085)
2025-Dec-25 13:39:15.440504
Updating files:  87% (13124/15085)
2025-Dec-25 13:39:15.481051
Updating files:  88% (13275/15085)
2025-Dec-25 13:39:15.502307
Updating files:  89% (13426/15085)
2025-Dec-25 13:39:15.526979
Updating files:  90% (13577/15085)
2025-Dec-25 13:39:15.549148
Updating files:  91% (13728/15085)
2025-Dec-25 13:39:15.566674
Updating files:  92% (13879/15085)
Updating files:  92% (13894/15085)
2025-Dec-25 13:39:15.573044
Updating files:  93% (14030/15085)
2025-Dec-25 13:39:15.658507
Updating files:  94% (14180/15085)
2025-Dec-25 13:39:15.691913
Updating files:  95% (14331/15085)
2025-Dec-25 13:39:15.714591
Updating files:  96% (14482/15085)
2025-Dec-25 13:39:15.734563
Updating files:  97% (14633/15085)
2025-Dec-25 13:39:15.751671
Updating files:  98% (14784/15085)
2025-Dec-25 13:39:15.775579
Updating files:  99% (14935/15085)
2025-Dec-25 13:39:15.790364
Updating files: 100% (15085/15085)
Updating files: 100% (15085/15085), done.
2025-Dec-25 13:39:17.145529
[CMD]: docker exec e8cs4g4gsskkkg8cc0o0c4wc bash -c 'cd /artifacts/e8cs4g4gsskkkg8cc0o0c4wc && git log -1 7b283b8ff2bc018b8733ef1d1ca76bdc6726bd38 --pretty=%B'
2025-Dec-25 13:39:17.145529
fix: Pin bcrypt<4.1.0 to resolve passlib compatibility issue
2025-Dec-25 13:39:17.154739
bcrypt>=4.1.0 removed the __about__ module that passlib uses for
2025-Dec-25 13:39:17.154739
version detection, causing registration to fail with a 500 error.
2025-Dec-25 13:39:25.615486
[CMD]: docker exec e8cs4g4gsskkkg8cc0o0c4wc bash -c 'test -f /artifacts/e8cs4g4gsskkkg8cc0o0c4wc/control-plane/api/Dockerfile && echo 'exists' || echo 'not found''
2025-Dec-25 13:39:25.615486
exists
2025-Dec-25 13:39:26.250004
[CMD]: docker exec e8cs4g4gsskkkg8cc0o0c4wc bash -c 'cat /artifacts/e8cs4g4gsskkkg8cc0o0c4wc/control-plane/api/Dockerfile'
2025-Dec-25 13:39:26.250004
FROM python:3.12-slim
2025-Dec-25 13:39:26.250004
WORKDIR /app
2025-Dec-25 13:39:26.250004
COPY requirements.txt .
2025-Dec-25 13:39:26.250004
RUN pip install -r requirements.txt
2025-Dec-25 13:39:26.250004
COPY . .
2025-Dec-25 13:39:26.250004
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
2025-Dec-25 13:39:26.774761
Added 21 ARG declarations to Dockerfile for service api.
2025-Dec-25 13:39:27.185916
[CMD]: docker exec e8cs4g4gsskkkg8cc0o0c4wc bash -c 'test -f /artifacts/e8cs4g4gsskkkg8cc0o0c4wc/dashboard/Dockerfile && echo 'exists' || echo 'not found''
2025-Dec-25 13:39:27.185916
exists
2025-Dec-25 13:39:27.558193
[CMD]: docker exec e8cs4g4gsskkkg8cc0o0c4wc bash -c 'cat /artifacts/e8cs4g4gsskkkg8cc0o0c4wc/dashboard/Dockerfile'
2025-Dec-25 13:39:27.558193
# Stage 1: Dependencies
2025-Dec-25 13:39:27.558193
FROM node:20-alpine AS deps
2025-Dec-25 13:39:27.558193
WORKDIR /app
2025-Dec-25 13:39:27.558193
COPY package*.json ./
2025-Dec-25 13:39:27.558193
RUN npm install
2025-Dec-25 13:39:27.558193
2025-Dec-25 13:39:27.558193
# Stage 2: Builder
2025-Dec-25 13:39:27.558193
FROM node:20-alpine AS builder
2025-Dec-25 13:39:27.558193
WORKDIR /app
2025-Dec-25 13:39:27.558193
COPY --from=deps /app/node_modules ./node_modules
2025-Dec-25 13:39:27.558193
COPY . .
2025-Dec-25 13:39:27.558193
# Set environment variables for build if needed (e.g. backend URL)
2025-Dec-25 13:39:27.558193
# For Next.js client-side fetch, it might need to know the URL at build time if pre-rendering,
2025-Dec-25 13:39:27.558193
# but we are using "use client" so it's fine.
2025-Dec-25 13:39:27.558193
ARG NEXT_PUBLIC_API_URL
2025-Dec-25 13:39:27.558193
ENV NEXT_PUBLIC_API_URL=${NEXT_PUBLIC_API_URL}
2025-Dec-25 13:39:27.558193
RUN npm run build
2025-Dec-25 13:39:27.558193
2025-Dec-25 13:39:27.558193
# Stage 3: Runner
2025-Dec-25 13:39:27.558193
FROM node:20-alpine AS runner
2025-Dec-25 13:39:27.558193
WORKDIR /app
2025-Dec-25 13:39:27.558193
ENV NODE_ENV=production
2025-Dec-25 13:39:27.558193
COPY --from=builder /app/public ./public
2025-Dec-25 13:39:27.558193
COPY --from=builder /app/.next ./.next
2025-Dec-25 13:39:27.558193
COPY --from=builder /app/node_modules ./node_modules
2025-Dec-25 13:39:27.558193
COPY --from=builder /app/package.json ./package.json
2025-Dec-25 13:39:27.558193
2025-Dec-25 13:39:27.558193
EXPOSE 3000
2025-Dec-25 13:39:27.558193
CMD ["npm", "start"]
2025-Dec-25 13:39:27.961489
Added 63 ARG declarations to Dockerfile for service dashboard (multi-stage build, added to 3 stages).
2025-Dec-25 13:39:27.968453
Pulling & building required images.
2025-Dec-25 13:39:27.996715
Creating build-time .env file in /artifacts (outside Docker context).
2025-Dec-25 13:39:28.776519
[CMD]: docker exec e8cs4g4gsskkkg8cc0o0c4wc bash -c 'cat /artifacts/build-time.env'
2025-Dec-25 13:39:28.776519
SOURCE_COMMIT='7b283b8ff2bc018b8733ef1d1ca76bdc6726bd38'
2025-Dec-25 13:39:28.776519
COOLIFY_URL=''
2025-Dec-25 13:39:28.776519
COOLIFY_FQDN=''
2025-Dec-25 13:39:28.776519
SERVICE_NAME_CONTROL-PLANE-DB='control-plane-db'
2025-Dec-25 13:39:28.776519
SERVICE_NAME_API='api'
2025-Dec-25 13:39:28.776519
SERVICE_NAME_DASHBOARD='dashboard'
2025-Dec-25 13:39:28.776519
SERVICE_NAME_KEYCLOAK='keycloak'
2025-Dec-25 13:39:28.776519
SERVICE_NAME_MINIO='minio'
2025-Dec-25 13:39:28.776519
SERVICE_URL_DASHBOARD='https://supalove.hayataxi.online'
2025-Dec-25 13:39:28.776519
SERVICE_FQDN_DASHBOARD='supalove.hayataxi.online'
2025-Dec-25 13:39:28.776519
SERVICE_URL_API='https://api.hayataxi.online'
2025-Dec-25 13:39:28.776519
SERVICE_FQDN_API='api.hayataxi.online'
2025-Dec-25 13:39:28.776519
SERVICE_URL_KEYCLOAK='https://auth.hayataxi.online'
2025-Dec-25 13:39:28.776519
SERVICE_FQDN_KEYCLOAK='auth.hayataxi.online'
2025-Dec-25 13:39:28.776519
SERVICE_URL_MINIO='https://s3.hayataxi.online'
2025-Dec-25 13:39:28.776519
SERVICE_FQDN_MINIO='s3.hayataxi.online'
2025-Dec-25 13:39:28.776519
ALLOWED_ORIGINS="http://localhost:3000,http://localhost:8000"
2025-Dec-25 13:39:28.776519
KEYCLOAK_ADMIN_PASSWORD="admin"
2025-Dec-25 13:39:28.776519
KEYCLOAK_ADMIN_USER="admin"
2025-Dec-25 13:39:28.776519
MINIO_ROOT_PASSWORD="minioadmin"
2025-Dec-25 13:39:28.776519
MINIO_ROOT_USER="minioadmin"
2025-Dec-25 13:39:28.776519
NEXT_PUBLIC_API_URL="https://api.hayataxi.online"
2025-Dec-25 13:39:28.776519
POSTGRES_DB="control_plane"
2025-Dec-25 13:39:28.776519
POSTGRES_PASSWORD="platform"
2025-Dec-25 13:39:28.776519
POSTGRES_USER="platform"
2025-Dec-25 13:39:28.776519
URL="http://localhost:8000"
2025-Dec-25 13:39:28.786000
Adding build arguments to Docker Compose build command.
2025-Dec-25 13:39:29.737729
[CMD]: docker exec e8cs4g4gsskkkg8cc0o0c4wc bash -c 'SOURCE_COMMIT=7b283b8ff2bc018b8733ef1d1ca76bdc6726bd38 COOLIFY_BRANCH=main COOLIFY_RESOURCE_UUID=hck4w0k4ww8kk4gccw000ggg COOLIFY_CONTAINER_NAME=hck4w0k4ww8kk4gccw000ggg-133859807144  docker compose --env-file /artifacts/build-time.env --project-name hck4w0k4ww8kk4gccw000ggg --project-directory /artifacts/e8cs4g4gsskkkg8cc0o0c4wc -f /artifacts/e8cs4g4gsskkkg8cc0o0c4wc/docker-compose.coolify.yml build --pull --no-cache --build-arg SOURCE_COMMIT --build-arg COOLIFY_URL --build-arg COOLIFY_FQDN --build-arg SERVICE_FQDN_API --build-arg SERVICE_FQDN_DASHBOARD --build-arg SERVICE_FQDN_KEYCLOAK --build-arg SERVICE_FQDN_MINIO --build-arg SERVICE_URL_API --build-arg SERVICE_URL_DASHBOARD --build-arg SERVICE_URL_KEYCLOAK --build-arg SERVICE_URL_MINIO --build-arg ALLOWED_ORIGINS --build-arg KEYCLOAK_ADMIN_PASSWORD --build-arg KEYCLOAK_ADMIN_USER --build-arg MINIO_ROOT_PASSWORD --build-arg MINIO_ROOT_USER --build-arg NEXT_PUBLIC_API_URL --build-arg POSTGRES_DB --build-arg POSTGRES_PASSWORD --build-arg POSTGRES_USER --build-arg URL --build-arg COOLIFY_BUILD_SECRETS_HASH=27293a7ce1ded9bd2dfddcfcb40e6b1b96bb03a2f4984aae9a890d0797dc7db2'
2025-Dec-25 13:39:29.737729
#1 [internal] load local bake definitions
2025-Dec-25 13:39:29.842538
#1 reading from stdin 3.22kB done
2025-Dec-25 13:39:29.842538
#1 DONE 0.0s
2025-Dec-25 13:39:29.842538
2025-Dec-25 13:39:29.842538
#2 [api internal] load build definition from Dockerfile
2025-Dec-25 13:39:29.842538
#2 transferring dockerfile:
2025-Dec-25 13:39:30.012196
#2 transferring dockerfile: 658B done
2025-Dec-25 13:39:30.012196
#2 DONE 0.0s
2025-Dec-25 13:39:30.012196
2025-Dec-25 13:39:30.012196
#3 [dashboard internal] load build definition from Dockerfile
2025-Dec-25 13:39:30.012196
#3 transferring dockerfile: 2.20kB done
2025-Dec-25 13:39:30.012196
#3 DONE 0.0s
2025-Dec-25 13:39:30.012196
2025-Dec-25 13:39:30.012196
#4 [dashboard internal] load metadata for docker.io/library/node:20-alpine
2025-Dec-25 13:39:30.593980
#4 ...
2025-Dec-25 13:39:30.593980
2025-Dec-25 13:39:30.593980
#5 [api internal] load metadata for docker.io/library/python:3.12-slim
2025-Dec-25 13:39:30.593980
#5 DONE 0.7s
2025-Dec-25 13:39:30.729342
#4 [dashboard internal] load metadata for docker.io/library/node:20-alpine
2025-Dec-25 13:39:30.729342
#4 DONE 0.7s
2025-Dec-25 13:39:30.729342
2025-Dec-25 13:39:30.729342
#6 [api internal] load .dockerignore
2025-Dec-25 13:39:30.729342
#6 transferring context: 2B done
2025-Dec-25 13:39:30.745370
#6 DONE 0.0s
2025-Dec-25 13:39:30.745370
2025-Dec-25 13:39:30.745370
#7 [dashboard internal] load .dockerignore
2025-Dec-25 13:39:30.745370
#7 transferring context: 2B done
2025-Dec-25 13:39:30.745370
#7 DONE 0.0s
2025-Dec-25 13:39:30.745370
2025-Dec-25 13:39:30.745370
#8 [api 1/5] FROM docker.io/library/python:3.12-slim@sha256:fa48eefe2146644c2308b909d6bb7651a768178f84fc9550dcd495e4d6d84d01
2025-Dec-25 13:39:30.745370
#8 DONE 0.0s
2025-Dec-25 13:39:30.745370
2025-Dec-25 13:39:30.745370
#9 [api 2/5] WORKDIR /app
2025-Dec-25 13:39:30.745370
#9 CACHED
2025-Dec-25 13:39:30.745370
2025-Dec-25 13:39:30.745370
#10 [dashboard deps 1/4] FROM docker.io/library/node:20-alpine@sha256:658d0f63e501824d6c23e06d4bb95c71e7d704537c9d9272f488ac03a370d448
2025-Dec-25 13:39:30.745370
#10 DONE 0.0s
2025-Dec-25 13:39:30.745370
2025-Dec-25 13:39:30.745370
#11 [dashboard deps 2/4] WORKDIR /app
2025-Dec-25 13:39:30.745370
#11 CACHED
2025-Dec-25 13:39:30.745370
2025-Dec-25 13:39:30.745370
#12 [dashboard internal] load build context
2025-Dec-25 13:39:30.745370
#12 transferring context: 837.69kB 0.0s done
2025-Dec-25 13:39:30.745370
#12 DONE 0.0s
2025-Dec-25 13:39:30.745370
2025-Dec-25 13:39:30.745370
#13 [api internal] load build context
2025-Dec-25 13:39:30.865627
#13 ...
2025-Dec-25 13:39:30.865627
2025-Dec-25 13:39:30.865627
#14 [dashboard deps 3/4] COPY package*.json ./
2025-Dec-25 13:39:30.865627
#14 DONE 0.2s
2025-Dec-25 13:39:30.865627
2025-Dec-25 13:39:30.865627
#13 [api internal] load build context
2025-Dec-25 13:39:35.709223
#13 transferring context: 178.25MB 5.1s
2025-Dec-25 13:39:39.684203
#13 transferring context: 330.52MB 9.0s done
2025-Dec-25 13:39:39.684203
#13 DONE 9.1s
2025-Dec-25 13:39:39.684203
2025-Dec-25 13:39:39.684203
#15 [dashboard deps 4/4] RUN npm install
2025-Dec-25 13:39:39.896635
#15 ...
2025-Dec-25 13:39:39.896635
2025-Dec-25 13:39:39.896635
#16 [api 3/5] COPY requirements.txt .
2025-Dec-25 13:39:40.101026
#16 DONE 0.4s
2025-Dec-25 13:39:40.107456
#15 [dashboard deps 4/4] RUN npm install
2025-Dec-25 13:39:40.261847
#15 ...
2025-Dec-25 13:39:40.261847
2025-Dec-25 13:39:40.261847
#17 [api 4/5] RUN pip install -r requirements.txt
2025-Dec-25 13:39:43.808223
#17 3.700 Collecting fastapi (from -r requirements.txt (line 1))
2025-Dec-25 13:39:44.000865
#17 3.741   Downloading fastapi-0.127.0-py3-none-any.whl.metadata (30 kB)
2025-Dec-25 13:39:44.276660
#17 4.169 Collecting sqlalchemy (from -r requirements.txt (line 3))
2025-Dec-25 13:39:44.426068
#17 4.175   Downloading sqlalchemy-2.0.45-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (9.5 kB)
2025-Dec-25 13:39:44.426068
#17 4.260 Collecting psycopg2-binary (from -r requirements.txt (line 4))
2025-Dec-25 13:39:44.426068
#17 4.266   Downloading psycopg2_binary-2.9.11-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (4.9 kB)
2025-Dec-25 13:39:44.426068
#17 4.319 Collecting httpx (from -r requirements.txt (line 5))
2025-Dec-25 13:39:44.562059
#17 4.328   Downloading httpx-0.28.1-py3-none-any.whl.metadata (7.1 kB)
2025-Dec-25 13:39:44.562059
#17 4.384 Collecting python-keycloak (from -r requirements.txt (line 6))
2025-Dec-25 13:39:44.562059
#17 4.392   Downloading python_keycloak-5.8.1-py3-none-any.whl.metadata (6.0 kB)
2025-Dec-25 13:39:44.562059
#17 4.453 Collecting minio (from -r requirements.txt (line 7))
2025-Dec-25 13:39:44.665596
#17 4.466   Downloading minio-7.2.20-py3-none-any.whl.metadata (6.5 kB)
2025-Dec-25 13:39:44.665596
#17 4.521 Collecting requests (from -r requirements.txt (line 8))
2025-Dec-25 13:39:44.665596
#17 4.525   Downloading requests-2.32.5-py3-none-any.whl.metadata (4.9 kB)
2025-Dec-25 13:39:44.665596
#17 4.558 Collecting python-dotenv (from -r requirements.txt (line 9))
2025-Dec-25 13:39:44.768618
#17 4.567   Downloading python_dotenv-1.2.1-py3-none-any.whl.metadata (25 kB)
2025-Dec-25 13:39:44.768618
#17 4.621 Collecting bcrypt<4.1.0 (from -r requirements.txt (line 11))
2025-Dec-25 13:39:44.768618
#17 4.626   Downloading bcrypt-4.0.1-cp36-abi3-manylinux_2_28_x86_64.whl.metadata (9.0 kB)
2025-Dec-25 13:39:44.768618
#17 4.659 Collecting python-multipart (from -r requirements.txt (line 13))
2025-Dec-25 13:39:44.898446
#17 4.663   Downloading python_multipart-0.0.21-py3-none-any.whl.metadata (1.8 kB)
2025-Dec-25 13:39:44.898446
#17 4.788 Collecting stripe (from -r requirements.txt (line 14))
2025-Dec-25 13:39:44.999755
#17 4.798   Downloading stripe-14.1.0-py3-none-any.whl.metadata (18 kB)
2025-Dec-25 13:39:44.999755
#17 4.837 Collecting prometheus_client (from -r requirements.txt (line 15))
2025-Dec-25 13:39:44.999755
#17 4.847   Downloading prometheus_client-0.23.1-py3-none-any.whl.metadata (1.9 kB)
2025-Dec-25 13:39:44.999755
#17 4.885 Collecting APScheduler (from -r requirements.txt (line 16))
2025-Dec-25 13:39:44.999755
#17 4.892   Downloading apscheduler-3.11.2-py3-none-any.whl.metadata (6.4 kB)
2025-Dec-25 13:39:45.105167
#17 4.968 Collecting uvicorn[standard] (from -r requirements.txt (line 2))
2025-Dec-25 13:39:45.105167
#17 4.976   Downloading uvicorn-0.40.0-py3-none-any.whl.metadata (6.7 kB)
2025-Dec-25 13:39:45.105167
#17 4.999 Collecting passlib[bcrypt] (from -r requirements.txt (line 10))
2025-Dec-25 13:39:45.309689
#17 5.005   Downloading passlib-1.7.4-py2.py3-none-any.whl.metadata (1.7 kB)
2025-Dec-25 13:39:45.309689
#17 5.030 Collecting python-jose[cryptography] (from -r requirements.txt (line 12))
2025-Dec-25 13:39:45.309689
#17 5.038   Downloading python_jose-3.5.0-py2.py3-none-any.whl.metadata (5.5 kB)
2025-Dec-25 13:39:45.309689
#17 5.079 Collecting starlette<0.51.0,>=0.40.0 (from fastapi->-r requirements.txt (line 1))
2025-Dec-25 13:39:45.309689
#17 5.084   Downloading starlette-0.50.0-py3-none-any.whl.metadata (6.3 kB)
2025-Dec-25 13:39:45.309689
#17 5.201 Collecting pydantic>=2.7.0 (from fastapi->-r requirements.txt (line 1))
2025-Dec-25 13:39:45.467215
#17 5.211   Downloading pydantic-2.12.5-py3-none-any.whl.metadata (90 kB)
2025-Dec-25 13:39:45.467215
#17 5.255 Collecting typing-extensions>=4.8.0 (from fastapi->-r requirements.txt (line 1))
2025-Dec-25 13:39:45.467215
#17 5.263   Downloading typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
2025-Dec-25 13:39:45.467215
#17 5.291 Collecting annotated-doc>=0.0.2 (from fastapi->-r requirements.txt (line 1))
2025-Dec-25 13:39:45.467215
#17 5.298   Downloading annotated_doc-0.0.4-py3-none-any.whl.metadata (6.6 kB)
2025-Dec-25 13:39:45.467215
#17 5.360 Collecting click>=7.0 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 13:39:45.595625
#17 5.368   Downloading click-8.3.1-py3-none-any.whl.metadata (2.6 kB)
2025-Dec-25 13:39:45.595625
#17 5.404 Collecting h11>=0.8 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 13:39:45.595625
#17 5.412   Downloading h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
2025-Dec-25 13:39:45.595625
#17 5.489 Collecting httptools>=0.6.3 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 13:39:45.751600
#17 5.500   Downloading httptools-0.7.1-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (3.5 kB)
2025-Dec-25 13:39:45.751600
#17 5.562 Collecting pyyaml>=5.1 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 13:39:45.751600
#17 5.568   Downloading pyyaml-6.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.4 kB)
2025-Dec-25 13:39:45.751600
#17 5.643 Collecting uvloop>=0.15.1 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 13:39:45.906317
#17 5.649   Downloading uvloop-0.22.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (4.9 kB)
2025-Dec-25 13:39:45.931167
#17 5.825 Collecting watchfiles>=0.13 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 13:39:46.177382
#17 5.835   Downloading watchfiles-1.1.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.9 kB)
2025-Dec-25 13:39:46.177382
#17 5.916 Collecting websockets>=10.4 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 13:39:46.177382
#17 5.921   Downloading websockets-15.0.1-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.8 kB)
2025-Dec-25 13:39:46.231472
#17 6.125 Collecting greenlet>=1 (from sqlalchemy->-r requirements.txt (line 3))
2025-Dec-25 13:39:46.360944
#17 6.133   Downloading greenlet-3.3.0-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (4.1 kB)
2025-Dec-25 13:39:46.360944
#17 6.177 Collecting anyio (from httpx->-r requirements.txt (line 5))
2025-Dec-25 13:39:46.360944
#17 6.181   Downloading anyio-4.12.0-py3-none-any.whl.metadata (4.3 kB)
2025-Dec-25 13:39:46.360944
#17 6.213 Collecting certifi (from httpx->-r requirements.txt (line 5))
2025-Dec-25 13:39:46.360944
#17 6.221   Downloading certifi-2025.11.12-py3-none-any.whl.metadata (2.5 kB)
2025-Dec-25 13:39:46.360944
#17 6.253 Collecting httpcore==1.* (from httpx->-r requirements.txt (line 5))
2025-Dec-25 13:39:46.480316
#17 6.262   Downloading httpcore-1.0.9-py3-none-any.whl.metadata (21 kB)
2025-Dec-25 13:39:46.486790
#17 6.291 Collecting idna (from httpx->-r requirements.txt (line 5))
2025-Dec-25 13:39:46.486790
#17 6.298   Downloading idna-3.11-py3-none-any.whl.metadata (8.4 kB)
2025-Dec-25 13:39:46.486790
#17 6.333 Collecting aiofiles>=24.1.0 (from python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 13:39:46.486790
#17 6.346   Downloading aiofiles-25.1.0-py3-none-any.whl.metadata (6.3 kB)
2025-Dec-25 13:39:46.486790
#17 6.373 Collecting async-property>=0.2.2 (from python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 13:39:46.581648
#17 6.380   Downloading async_property-0.2.2-py2.py3-none-any.whl.metadata (5.3 kB)
2025-Dec-25 13:39:46.581648
#17 6.418 Collecting deprecation>=2.1.0 (from python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 13:39:46.581648
#17 6.423   Downloading deprecation-2.1.0-py2.py3-none-any.whl.metadata (4.6 kB)
2025-Dec-25 13:39:46.581648
#17 6.473 Collecting jwcrypto>=1.5.4 (from python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 13:39:46.689375
#17 6.482   Downloading jwcrypto-1.5.6-py3-none-any.whl.metadata (3.1 kB)
2025-Dec-25 13:39:46.689375
#17 6.520 Collecting requests-toolbelt>=0.6.0 (from python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 13:39:46.689375
#17 6.527   Downloading requests_toolbelt-1.0.0-py2.py3-none-any.whl.metadata (14 kB)
2025-Dec-25 13:39:46.689375
#17 6.583 Collecting argon2-cffi (from minio->-r requirements.txt (line 7))
2025-Dec-25 13:39:46.834407
#17 6.592   Downloading argon2_cffi-25.1.0-py3-none-any.whl.metadata (4.1 kB)
2025-Dec-25 13:39:46.834407
#17 6.727 Collecting pycryptodome (from minio->-r requirements.txt (line 7))
2025-Dec-25 13:39:47.015189
#17 6.734   Downloading pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (3.4 kB)
2025-Dec-25 13:39:47.015189
#17 6.776 Collecting urllib3 (from minio->-r requirements.txt (line 7))
2025-Dec-25 13:39:47.015189
#17 6.785   Downloading urllib3-2.6.2-py3-none-any.whl.metadata (6.6 kB)
2025-Dec-25 13:39:47.015189
#17 6.909 Collecting charset_normalizer<4,>=2 (from requests->-r requirements.txt (line 8))
2025-Dec-25 13:39:47.134590
#17 6.912   Downloading charset_normalizer-3.4.4-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (37 kB)
2025-Dec-25 13:39:47.134590
#17 6.984 Collecting ecdsa!=0.15 (from python-jose[cryptography]->-r requirements.txt (line 12))
2025-Dec-25 13:39:47.134590
#17 6.991   Downloading ecdsa-0.19.1-py2.py3-none-any.whl.metadata (29 kB)
2025-Dec-25 13:39:47.134590
#17 7.028 Collecting rsa!=4.1.1,!=4.4,<5.0,>=4.0 (from python-jose[cryptography]->-r requirements.txt (line 12))
2025-Dec-25 13:39:47.327860
#17 7.036   Downloading rsa-4.9.1-py3-none-any.whl.metadata (5.6 kB)
2025-Dec-25 13:39:47.327860
#17 7.065 Collecting pyasn1>=0.5.0 (from python-jose[cryptography]->-r requirements.txt (line 12))
2025-Dec-25 13:39:47.327860
#17 7.068   Downloading pyasn1-0.6.1-py3-none-any.whl.metadata (8.4 kB)
2025-Dec-25 13:39:47.327860
#17 7.220 Collecting cryptography>=3.4.0 (from python-jose[cryptography]->-r requirements.txt (line 12))
2025-Dec-25 13:39:47.556558
#17 7.233   Downloading cryptography-46.0.3-cp311-abi3-manylinux_2_34_x86_64.whl.metadata (5.7 kB)
2025-Dec-25 13:39:47.556558
#17 7.294 Collecting tzlocal>=3.0 (from APScheduler->-r requirements.txt (line 16))
2025-Dec-25 13:39:47.556558
#17 7.300   Downloading tzlocal-5.3.1-py3-none-any.whl.metadata (7.6 kB)
2025-Dec-25 13:39:47.777471
#17 7.671 Collecting cffi>=2.0.0 (from cryptography>=3.4.0->python-jose[cryptography]->-r requirements.txt (line 12))
2025-Dec-25 13:39:47.882317
#17 7.678   Downloading cffi-2.0.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (2.6 kB)
2025-Dec-25 13:39:47.882317
#17 7.722 Collecting packaging (from deprecation>=2.1.0->python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 13:39:47.882317
#17 7.730   Downloading packaging-25.0-py3-none-any.whl.metadata (3.3 kB)
2025-Dec-25 13:39:47.882317
#17 7.760 Collecting six>=1.9.0 (from ecdsa!=0.15->python-jose[cryptography]->-r requirements.txt (line 12))
2025-Dec-25 13:39:47.889962
#17 7.775   Downloading six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
2025-Dec-25 13:39:48.090926
#17 7.825 Collecting annotated-types>=0.6.0 (from pydantic>=2.7.0->fastapi->-r requirements.txt (line 1))
2025-Dec-25 13:39:48.090926
#17 7.830   Downloading annotated_types-0.7.0-py3-none-any.whl.metadata (15 kB)
2025-Dec-25 13:39:48.571533
#17 8.465 Collecting pydantic-core==2.41.5 (from pydantic>=2.7.0->fastapi->-r requirements.txt (line 1))
2025-Dec-25 13:39:48.588529
2025-Dec-25 13:39:48.758118
#17 8.471   Downloading pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (7.3 kB)
2025-Dec-25 13:39:48.758118
#17 8.520 Collecting typing-inspection>=0.4.2 (from pydantic>=2.7.0->fastapi->-r requirements.txt (line 1))
2025-Dec-25 13:39:48.758118
#17 8.529   Downloading typing_inspection-0.4.2-py3-none-any.whl.metadata (2.6 kB)
2025-Dec-25 13:39:48.758118
#17 8.649 Collecting argon2-cffi-bindings (from argon2-cffi->minio->-r requirements.txt (line 7))
2025-Dec-25 13:39:48.862541
#17 8.653   Downloading argon2_cffi_bindings-25.1.0-cp39-abi3-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl.metadata (7.4 kB)
2025-Dec-25 13:39:48.862541
#17 8.687 Collecting pycparser (from cffi>=2.0.0->cryptography>=3.4.0->python-jose[cryptography]->-r requirements.txt (line 12))
2025-Dec-25 13:39:48.862541
#17 8.694   Downloading pycparser-2.23-py3-none-any.whl.metadata (993 bytes)
2025-Dec-25 13:39:48.862541
#17 8.756 Downloading fastapi-0.127.0-py3-none-any.whl (112 kB)
2025-Dec-25 13:39:48.981557
#17 8.782 Downloading sqlalchemy-2.0.45-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (3.3 MB)
2025-Dec-25 13:39:48.981557
#17 8.875    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.3/3.3 MB 37.8 MB/s eta 0:00:00
2025-Dec-25 13:39:49.090113
#17 8.880 Downloading psycopg2_binary-2.9.11-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (4.2 MB)
2025-Dec-25 13:39:49.090113
#17 8.974    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.2/4.2 MB 47.1 MB/s eta 0:00:00
2025-Dec-25 13:39:49.090113
#17 8.982 Downloading httpx-0.28.1-py3-none-any.whl (73 kB)
2025-Dec-25 13:39:49.207714
#17 8.997 Downloading httpcore-1.0.9-py3-none-any.whl (78 kB)
2025-Dec-25 13:39:49.213900
#17 9.009 Downloading python_keycloak-5.8.1-py3-none-any.whl (77 kB)
2025-Dec-25 13:39:49.213900
#17 9.021 Downloading minio-7.2.20-py3-none-any.whl (93 kB)
2025-Dec-25 13:39:49.213900
#17 9.029 Downloading requests-2.32.5-py3-none-any.whl (64 kB)
2025-Dec-25 13:39:49.213900
#17 9.037 Downloading python_dotenv-1.2.1-py3-none-any.whl (21 kB)
2025-Dec-25 13:39:49.213900
#17 9.048 Downloading bcrypt-4.0.1-cp36-abi3-manylinux_2_28_x86_64.whl (593 kB)
2025-Dec-25 13:39:49.213900
#17 9.072    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 593.7/593.7 kB 18.3 MB/s eta 0:00:00
2025-Dec-25 13:39:49.213900
#17 9.081 Downloading python_multipart-0.0.21-py3-none-any.whl (24 kB)
2025-Dec-25 13:39:49.213900
#17 9.102 Downloading stripe-14.1.0-py3-none-any.whl (2.1 MB)
2025-Dec-25 13:39:49.369514
#17 9.138    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 56.1 MB/s eta 0:00:00
2025-Dec-25 13:39:49.369514
#17 9.145 Downloading prometheus_client-0.23.1-py3-none-any.whl (61 kB)
2025-Dec-25 13:39:49.369514
#17 9.162 Downloading apscheduler-3.11.2-py3-none-any.whl (64 kB)
2025-Dec-25 13:39:49.369514
#17 9.190 Downloading aiofiles-25.1.0-py3-none-any.whl (14 kB)
2025-Dec-25 13:39:49.369514
#17 9.244 Downloading annotated_doc-0.0.4-py3-none-any.whl (5.3 kB)
2025-Dec-25 13:39:49.469513
#17 9.257 Downloading async_property-0.2.2-py2.py3-none-any.whl (9.5 kB)
2025-Dec-25 13:39:49.469513
#17 9.284 Downloading certifi-2025.11.12-py3-none-any.whl (159 kB)
2025-Dec-25 13:39:49.469513
#17 9.310 Downloading charset_normalizer-3.4.4-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (153 kB)
2025-Dec-25 13:39:49.469513
#17 9.338 Downloading click-8.3.1-py3-none-any.whl (108 kB)
2025-Dec-25 13:39:49.469513
#17 9.357 Downloading cryptography-46.0.3-cp311-abi3-manylinux_2_34_x86_64.whl (4.5 MB)
2025-Dec-25 13:39:49.646577
#17 9.539    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.5/4.5 MB 47.7 MB/s eta 0:00:00
2025-Dec-25 13:39:49.749369
#17 9.547 Downloading deprecation-2.1.0-py2.py3-none-any.whl (11 kB)
2025-Dec-25 13:39:49.749369
#17 9.561 Downloading ecdsa-0.19.1-py2.py3-none-any.whl (150 kB)
2025-Dec-25 13:39:49.749369
#17 9.575 Downloading greenlet-3.3.0-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (609 kB)
2025-Dec-25 13:39:49.749369
#17 9.595    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 609.9/609.9 kB 28.3 MB/s eta 0:00:00
2025-Dec-25 13:39:49.749369
#17 9.600 Downloading h11-0.16.0-py3-none-any.whl (37 kB)
2025-Dec-25 13:39:49.749369
#17 9.615 Downloading httptools-0.7.1-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (517 kB)
2025-Dec-25 13:39:49.749369
#17 9.632 Downloading idna-3.11-py3-none-any.whl (71 kB)
2025-Dec-25 13:39:49.749369
#17 9.642 Downloading jwcrypto-1.5.6-py3-none-any.whl (92 kB)
2025-Dec-25 13:39:49.855701
#17 9.652 Downloading pyasn1-0.6.1-py3-none-any.whl (83 kB)
2025-Dec-25 13:39:49.855701
#17 9.662 Downloading pydantic-2.12.5-py3-none-any.whl (463 kB)
2025-Dec-25 13:39:49.855701
#17 9.678 Downloading pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.1 MB)
2025-Dec-25 13:39:49.855701
#17 9.717    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 56.7 MB/s eta 0:00:00
2025-Dec-25 13:39:49.855701
#17 9.720 Downloading pyyaml-6.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (807 kB)
2025-Dec-25 13:39:49.855701
#17 9.739    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 807.9/807.9 kB 44.9 MB/s eta 0:00:00
2025-Dec-25 13:39:49.855701
#17 9.747 Downloading requests_toolbelt-1.0.0-py2.py3-none-any.whl (54 kB)
2025-Dec-25 13:39:50.079103
#17 9.760 Downloading rsa-4.9.1-py3-none-any.whl (34 kB)
2025-Dec-25 13:39:50.079103
#17 9.771 Downloading starlette-0.50.0-py3-none-any.whl (74 kB)
2025-Dec-25 13:39:50.079103
#17 9.784 Downloading anyio-4.12.0-py3-none-any.whl (113 kB)
2025-Dec-25 13:39:50.079103
#17 9.795 Downloading typing_extensions-4.15.0-py3-none-any.whl (44 kB)
2025-Dec-25 13:39:50.079103
#17 9.807 Downloading tzlocal-5.3.1-py3-none-any.whl (18 kB)
2025-Dec-25 13:39:50.079103
#17 9.817 Downloading urllib3-2.6.2-py3-none-any.whl (131 kB)
2025-Dec-25 13:39:50.079103
#17 9.826 Downloading uvloop-0.22.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (4.4 MB)
2025-Dec-25 13:39:50.079103
#17 9.967    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.4/4.4 MB 32.1 MB/s eta 0:00:00
2025-Dec-25 13:39:50.187394
#17 9.977 Downloading watchfiles-1.1.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (456 kB)
2025-Dec-25 13:39:50.187394
#17 10.000 Downloading websockets-15.0.1-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (182 kB)
2025-Dec-25 13:39:50.187394
#17 10.01 Downloading argon2_cffi-25.1.0-py3-none-any.whl (14 kB)
2025-Dec-25 13:39:50.187394
#17 10.02 Downloading passlib-1.7.4-py2.py3-none-any.whl (525 kB)
2025-Dec-25 13:39:50.187394
#17 10.03    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 525.6/525.6 kB 40.5 MB/s eta 0:00:00
2025-Dec-25 13:39:50.187394
#17 10.04 Downloading pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.3 MB)
2025-Dec-25 13:39:50.187394
#17 10.08    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.3/2.3 MB 60.6 MB/s eta 0:00:00
2025-Dec-25 13:39:50.289755
#17 10.09 Downloading python_jose-3.5.0-py2.py3-none-any.whl (34 kB)
2025-Dec-25 13:39:50.289755
#17 10.10 Downloading uvicorn-0.40.0-py3-none-any.whl (68 kB)
2025-Dec-25 13:39:50.289755
#17 10.12 Downloading annotated_types-0.7.0-py3-none-any.whl (13 kB)
2025-Dec-25 13:39:50.289755
#17 10.12 Downloading cffi-2.0.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (219 kB)
2025-Dec-25 13:39:50.289755
#17 10.14 Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
2025-Dec-25 13:39:50.289755
#17 10.15 Downloading typing_inspection-0.4.2-py3-none-any.whl (14 kB)
2025-Dec-25 13:39:50.289755
#17 10.16 Downloading argon2_cffi_bindings-25.1.0-cp39-abi3-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl (87 kB)
2025-Dec-25 13:39:50.289755
#17 10.17 Downloading packaging-25.0-py3-none-any.whl (66 kB)
2025-Dec-25 13:39:50.289755
#17 10.18 Downloading pycparser-2.23-py3-none-any.whl (118 kB)
2025-Dec-25 13:39:50.530393
#17 10.42 Installing collected packages: passlib, async-property, websockets, uvloop, urllib3, tzlocal, typing-extensions, six, pyyaml, python-multipart, python-dotenv, pycryptodome, pycparser, pyasn1, psycopg2-binary, prometheus_client, packaging, idna, httptools, h11, greenlet, click, charset_normalizer, certifi, bcrypt, annotated-types, annotated-doc, aiofiles, uvicorn, typing-inspection, sqlalchemy, rsa, requests, pydantic-core, httpcore, ecdsa, deprecation, cffi, APScheduler, anyio, watchfiles, stripe, starlette, requests-toolbelt, python-jose, pydantic, httpx, cryptography, argon2-cffi-bindings, jwcrypto, fastapi, argon2-cffi, python-keycloak, minio
2025-Dec-25 13:39:50.543004
2025-Dec-25 13:39:59.684857
#17 19.58 Successfully installed APScheduler-3.11.2 aiofiles-25.1.0 annotated-doc-0.0.4 annotated-types-0.7.0 anyio-4.12.0 argon2-cffi-25.1.0 argon2-cffi-bindings-25.1.0 async-property-0.2.2 bcrypt-4.0.1 certifi-2025.11.12 cffi-2.0.0 charset_normalizer-3.4.4 click-8.3.1 cryptography-46.0.3 deprecation-2.1.0 ecdsa-0.19.1 fastapi-0.127.0 greenlet-3.3.0 h11-0.16.0 httpcore-1.0.9 httptools-0.7.1 httpx-0.28.1 idna-3.11 jwcrypto-1.5.6 minio-7.2.20 packaging-25.0 passlib-1.7.4 prometheus_client-0.23.1 psycopg2-binary-2.9.11 pyasn1-0.6.1 pycparser-2.23 pycryptodome-3.23.0 pydantic-2.12.5 pydantic-core-2.41.5 python-dotenv-1.2.1 python-jose-3.5.0 python-keycloak-5.8.1 python-multipart-0.0.21 pyyaml-6.0.3 requests-2.32.5 requests-toolbelt-1.0.0 rsa-4.9.1 six-1.17.0 sqlalchemy-2.0.45 starlette-0.50.0 stripe-14.1.0 typing-extensions-4.15.0 typing-inspection-0.4.2 tzlocal-5.3.1 urllib3-2.6.2 uvicorn-0.40.0 uvloop-0.22.1 watchfiles-1.1.1 websockets-15.0.1
2025-Dec-25 13:39:59.793616
#17 19.58 WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager, possibly rendering your system unusable. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv. Use the --root-user-action option if you know what you are doing and want to suppress this warning.
2025-Dec-25 13:39:59.793616
#17 19.69
2025-Dec-25 13:39:59.793616
#17 19.69 [notice] A new release of pip is available: 25.0.1 -> 25.3
2025-Dec-25 13:39:59.793616
#17 19.69 [notice] To update, run: pip install --upgrade pip
2025-Dec-25 13:40:00.443940
#17 DONE 20.3s
2025-Dec-25 13:40:00.443940
2025-Dec-25 13:40:00.443940
#15 [dashboard deps 4/4] RUN npm install
2025-Dec-25 13:40:00.588387
#15 ...
2025-Dec-25 13:40:00.588387
2025-Dec-25 13:40:00.588387
#18 [api 5/5] COPY . .
2025-Dec-25 13:40:10.319887
#18 DONE 9.9s
2025-Dec-25 13:40:10.319887
2025-Dec-25 13:40:10.319887
#15 [dashboard deps 4/4] RUN npm install
2025-Dec-25 13:40:10.487980
#15 39.46
2025-Dec-25 13:40:10.487980
#15 39.46 added 473 packages, and audited 474 packages in 39s
2025-Dec-25 13:40:10.487980
#15 39.46
2025-Dec-25 13:40:10.487980
#15 39.46 154 packages are looking for funding
2025-Dec-25 13:40:10.487980
#15 39.46   run `npm fund` for details
2025-Dec-25 13:40:10.487980
#15 39.47
2025-Dec-25 13:40:10.487980
#15 39.47 found 0 vulnerabilities
2025-Dec-25 13:40:10.487980
#15 39.47 npm notice
2025-Dec-25 13:40:10.487980
#15 39.47 npm notice New major version of npm available! 10.8.2 -> 11.7.0
2025-Dec-25 13:40:10.487980
#15 39.47 npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.7.0
2025-Dec-25 13:40:10.487980
#15 39.47 npm notice To update run: npm install -g npm@11.7.0
2025-Dec-25 13:40:10.487980
#15 39.47 npm notice
2025-Dec-25 13:40:10.854270
#15 DONE 40.0s
2025-Dec-25 13:40:10.854270
2025-Dec-25 13:40:10.854270
#19 [api] exporting to image
2025-Dec-25 13:40:10.854270
#19 exporting layers
2025-Dec-25 13:40:15.919743
#19 exporting layers 5.6s done
2025-Dec-25 13:40:15.930505
#19 writing image sha256:3804bc2bf7a069a502382ec269b2403e20e2a82d01cb0348e4fc1b21b4a15535
2025-Dec-25 13:40:16.141561
#19 writing image sha256:3804bc2bf7a069a502382ec269b2403e20e2a82d01cb0348e4fc1b21b4a15535 done
2025-Dec-25 13:40:16.141561
#19 naming to docker.io/library/hck4w0k4ww8kk4gccw000ggg-api done
2025-Dec-25 13:40:16.141561
#19 DONE 5.6s
2025-Dec-25 13:40:16.141561
2025-Dec-25 13:40:16.141561
#20 [api] resolving provenance for metadata file
2025-Dec-25 13:40:16.141561
#20 DONE 0.0s
2025-Dec-25 13:40:19.746887
#21 [dashboard builder 3/5] COPY --from=deps /app/node_modules ./node_modules
2025-Dec-25 13:40:32.915272
#21 DONE 13.2s
2025-Dec-25 13:40:33.124366
#22 [dashboard builder 4/5] COPY . .
2025-Dec-25 13:40:33.124366
#22 DONE 0.0s
2025-Dec-25 13:40:33.124366
2025-Dec-25 13:40:33.124366
#23 [dashboard builder 5/5] RUN npm run build
2025-Dec-25 13:40:33.915432
#23 0.944
2025-Dec-25 13:40:33.915432
#23 0.944 > dashboard@0.1.0 build
2025-Dec-25 13:40:33.915432
#23 0.944 > next build
2025-Dec-25 13:40:33.915432
#23 0.944
2025-Dec-25 13:40:34.895974
#23 1.925 Attention: Next.js now collects completely anonymous telemetry regarding usage.
2025-Dec-25 13:40:35.023899
#23 1.925 This information is used to shape Next.js' roadmap and prioritize features.
2025-Dec-25 13:40:35.023899
#23 1.925 You can learn more, including how to opt-out if you'd not like to participate in this anonymous program, by visiting the following URL:
2025-Dec-25 13:40:35.023899
#23 1.925 https://nextjs.org/telemetry
2025-Dec-25 13:40:35.023899
#23 1.925
2025-Dec-25 13:40:35.023899
#23 1.936 ▲ Next.js 16.1.0 (Turbopack)
2025-Dec-25 13:40:35.023899
#23 1.937
2025-Dec-25 13:40:35.023899
#23 2.053   Creating an optimized production build ...
2025-Dec-25 13:40:55.378131
#23 22.41 ✓ Compiled successfully in 19.8s
2025-Dec-25 13:40:55.540956
#23 22.42   Running TypeScript ...
2025-Dec-25 13:41:07.606662
#23 34.64   Collecting page data using 1 worker ...
2025-Dec-25 13:41:08.353172
#23 35.38   Generating static pages using 1 worker (0/11) ...
2025-Dec-25 13:41:08.722965
#23 35.75   Generating static pages using 1 worker (2/11)
2025-Dec-25 13:41:08.826111
#23 35.76   Generating static pages using 1 worker (5/11)
2025-Dec-25 13:41:08.834604
#23 35.76   Generating static pages using 1 worker (8/11)
2025-Dec-25 13:41:08.834604
#23 35.84 ✓ Generating static pages using 1 worker (11/11) in 456.9ms
2025-Dec-25 13:41:08.834604
#23 35.85   Finalizing page optimization ...
2025-Dec-25 13:41:08.834604
#23 35.85
2025-Dec-25 13:41:08.983355
#23 35.86 Route (app)
2025-Dec-25 13:41:08.983355
#23 35.86 ┌ ○ /
2025-Dec-25 13:41:08.983355
#23 35.86 ├ ○ /_not-found
2025-Dec-25 13:41:08.983355
#23 35.86 ├ ○ /login
2025-Dec-25 13:41:08.983355
#23 35.86 ├ ○ /org
2025-Dec-25 13:41:08.983355
#23 35.86 ├ ƒ /org/[orgId]/billing
2025-Dec-25 13:41:08.983355
#23 35.86 ├ ƒ /org/[orgId]/projects
2025-Dec-25 13:41:08.983355
#23 35.86 ├ ƒ /org/[orgId]/projects/new
2025-Dec-25 13:41:08.983355
#23 35.86 ├ ƒ /org/[orgId]/settings
2025-Dec-25 13:41:08.983355
#23 35.86 ├ ƒ /org/[orgId]/team
2025-Dec-25 13:41:08.983355
#23 35.86 ├ ○ /projects
2025-Dec-25 13:41:08.983355
#23 35.86 ├ ƒ /projects/[id]
2025-Dec-25 13:41:08.983355
#23 35.86 ├ ƒ /projects/[id]/auth
2025-Dec-25 13:41:08.983355
#23 35.86 ├ ƒ /projects/[id]/backups
2025-Dec-25 13:41:08.983355
#23 35.86 ├ ƒ /projects/[id]/database
2025-Dec-25 13:41:08.983355
#23 35.86 ├ ƒ /projects/[id]/database/[table]
2025-Dec-25 13:41:08.983355
#23 35.86 ├ ƒ /projects/[id]/edge-functions
2025-Dec-25 13:41:08.983355
#23 35.86 ├ ƒ /projects/[id]/logs
2025-Dec-25 13:41:08.983355
#23 35.86 ├ ƒ /projects/[id]/realtime
2025-Dec-25 13:41:08.983355
#23 35.86 ├ ƒ /projects/[id]/secrets
2025-Dec-25 13:41:08.983355
#23 35.86 ├ ƒ /projects/[id]/settings
2025-Dec-25 13:41:08.983355
#23 35.86 ├ ƒ /projects/[id]/settings/deployment
2025-Dec-25 13:41:08.983355
#23 35.86 ├ ƒ /projects/[id]/sql
2025-Dec-25 13:41:08.983355
#23 35.86 ├ ƒ /projects/[id]/storage
2025-Dec-25 13:41:08.983355
#23 35.86 ├ ○ /projects/new
2025-Dec-25 13:41:08.983355
#23 35.86 ├ ○ /settings/organization
2025-Dec-25 13:41:08.983355
#23 35.86 ├ ƒ /settings/organization/[id]
2025-Dec-25 13:41:08.983355
#23 35.86 ├ ○ /settings/profile
2025-Dec-25 13:41:08.990048
#23 35.86 └ ○ /signup
2025-Dec-25 13:41:08.990048
#23 35.86
2025-Dec-25 13:41:08.990048
#23 35.86
2025-Dec-25 13:41:08.990048
#23 35.86 ○  (Static)   prerendered as static content
2025-Dec-25 13:41:08.990048
#23 35.86 ƒ  (Dynamic)  server-rendered on demand
2025-Dec-25 13:41:08.990048
#23 35.86
2025-Dec-25 13:41:09.057260
#23 36.09 npm notice
2025-Dec-25 13:41:09.057260
#23 36.09 npm notice New major version of npm available! 10.8.2 -> 11.7.0
2025-Dec-25 13:41:09.057260
#23 36.09 npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.7.0
2025-Dec-25 13:41:09.057260
#23 36.09 npm notice To update run: npm install -g npm@11.7.0
2025-Dec-25 13:41:09.057260
#23 36.09 npm notice
2025-Dec-25 13:41:09.202225
#23 DONE 36.2s
2025-Dec-25 13:41:15.430955
#24 [dashboard runner 3/6] COPY --from=builder /app/public ./public
2025-Dec-25 13:41:15.656560
#24 DONE 0.1s
2025-Dec-25 13:41:15.656560
2025-Dec-25 13:41:15.656560
#25 [dashboard runner 4/6] COPY --from=builder /app/.next ./.next
2025-Dec-25 13:41:15.719949
#25 DONE 0.2s
2025-Dec-25 13:41:15.871514
#26 [dashboard runner 5/6] COPY --from=builder /app/node_modules ./node_modules
2025-Dec-25 13:41:24.368184
#26 DONE 8.6s
2025-Dec-25 13:41:24.576859
#27 [dashboard runner 6/6] COPY --from=builder /app/package.json ./package.json
2025-Dec-25 13:41:24.576859
#27 DONE 0.0s
2025-Dec-25 13:41:24.576859
2025-Dec-25 13:41:24.576859
#28 [dashboard] exporting to image
2025-Dec-25 13:41:24.576859
#28 exporting layers
2025-Dec-25 13:41:34.035827
#28 exporting layers 9.6s done
2025-Dec-25 13:41:34.091473
#28 writing image sha256:73664299ce91a2d7a2f7df3f915e9176ab9674de9ea75c7d0bca369c757ad64c done
2025-Dec-25 13:41:34.097633
#28 naming to docker.io/library/hck4w0k4ww8kk4gccw000ggg-dashboard done
2025-Dec-25 13:41:34.097633
#28 DONE 9.6s
2025-Dec-25 13:41:34.097633
2025-Dec-25 13:41:34.097633
#29 [dashboard] resolving provenance for metadata file
2025-Dec-25 13:41:34.097633
#29 DONE 0.0s
2025-Dec-25 13:41:34.107008
dashboard  Built
2025-Dec-25 13:41:34.107008
api  Built
2025-Dec-25 13:41:34.142771
Creating .env file with runtime variables for build phase.
2025-Dec-25 13:41:34.971588
[CMD]: docker exec e8cs4g4gsskkkg8cc0o0c4wc bash -c 'cat /artifacts/e8cs4g4gsskkkg8cc0o0c4wc/.env'
2025-Dec-25 13:41:34.971588
SOURCE_COMMIT=7b283b8ff2bc018b8733ef1d1ca76bdc6726bd38
2025-Dec-25 13:41:34.971588
COOLIFY_URL=
2025-Dec-25 13:41:34.971588
COOLIFY_FQDN=
2025-Dec-25 13:41:34.971588
SERVICE_URL_DASHBOARD=https://supalove.hayataxi.online
2025-Dec-25 13:41:34.971588
SERVICE_FQDN_DASHBOARD=supalove.hayataxi.online
2025-Dec-25 13:41:34.971588
SERVICE_URL_API=https://api.hayataxi.online
2025-Dec-25 13:41:34.971588
SERVICE_FQDN_API=api.hayataxi.online
2025-Dec-25 13:41:34.971588
SERVICE_URL_KEYCLOAK=https://auth.hayataxi.online
2025-Dec-25 13:41:34.971588
SERVICE_FQDN_KEYCLOAK=auth.hayataxi.online
2025-Dec-25 13:41:34.971588
SERVICE_URL_MINIO=https://s3.hayataxi.online
2025-Dec-25 13:41:34.971588
SERVICE_FQDN_MINIO=s3.hayataxi.online
2025-Dec-25 13:41:34.971588
SERVICE_NAME_CONTROL-PLANE-DB=control-plane-db
2025-Dec-25 13:41:34.971588
SERVICE_NAME_API=api
2025-Dec-25 13:41:34.971588
SERVICE_NAME_DASHBOARD=dashboard
2025-Dec-25 13:41:34.971588
SERVICE_NAME_KEYCLOAK=keycloak
2025-Dec-25 13:41:34.971588
SERVICE_NAME_MINIO=minio
2025-Dec-25 13:41:34.971588
POSTGRES_USER=platform
2025-Dec-25 13:41:34.971588
POSTGRES_PASSWORD=platform
2025-Dec-25 13:41:34.971588
POSTGRES_DB=control_plane
2025-Dec-25 13:41:34.971588
KEYCLOAK_ADMIN_USER=admin
2025-Dec-25 13:41:34.971588
KEYCLOAK_ADMIN_PASSWORD=admin
2025-Dec-25 13:41:34.971588
MINIO_ROOT_USER=minioadmin
2025-Dec-25 13:41:34.971588
MINIO_ROOT_PASSWORD=minioadmin
2025-Dec-25 13:41:34.971588
URL=http://localhost:8000
2025-Dec-25 13:41:34.971588
NEXT_PUBLIC_API_URL=https://api.hayataxi.online
2025-Dec-25 13:41:34.971588
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8000
2025-Dec-25 13:41:34.971588
HOST=0.0.0.0
2025-Dec-25 13:41:35.333637
Removing old containers.
2025-Dec-25 13:41:36.274493
[CMD]: docker stop --time=30 dashboard-hck4w0k4ww8kk4gccw000ggg-132201995907
2025-Dec-25 13:41:36.274493
dashboard-hck4w0k4ww8kk4gccw000ggg-132201995907
2025-Dec-25 13:41:36.740261
[CMD]: docker rm -f dashboard-hck4w0k4ww8kk4gccw000ggg-132201995907
2025-Dec-25 13:41:36.740261
dashboard-hck4w0k4ww8kk4gccw000ggg-132201995907
2025-Dec-25 13:41:37.613149
[CMD]: docker stop --time=30 api-hck4w0k4ww8kk4gccw000ggg-132201978563
2025-Dec-25 13:41:37.613149
api-hck4w0k4ww8kk4gccw000ggg-132201978563
2025-Dec-25 13:41:38.002355
[CMD]: docker rm -f api-hck4w0k4ww8kk4gccw000ggg-132201978563
2025-Dec-25 13:41:38.002355
api-hck4w0k4ww8kk4gccw000ggg-132201978563
2025-Dec-25 13:41:38.574558
[CMD]: docker stop --time=30 keycloak-hck4w0k4ww8kk4gccw000ggg-132202009031
2025-Dec-25 13:41:38.574558
keycloak-hck4w0k4ww8kk4gccw000ggg-132202009031
2025-Dec-25 13:41:39.064956
[CMD]: docker rm -f keycloak-hck4w0k4ww8kk4gccw000ggg-132202009031
2025-Dec-25 13:41:39.064956
keycloak-hck4w0k4ww8kk4gccw000ggg-132202009031
2025-Dec-25 13:41:39.564686
[CMD]: docker stop --time=30 minio-hck4w0k4ww8kk4gccw000ggg-132202024876
2025-Dec-25 13:41:39.564686
minio-hck4w0k4ww8kk4gccw000ggg-132202024876
2025-Dec-25 13:41:39.972834
[CMD]: docker rm -f minio-hck4w0k4ww8kk4gccw000ggg-132202024876
2025-Dec-25 13:41:39.972834
minio-hck4w0k4ww8kk4gccw000ggg-132202024876
2025-Dec-25 13:41:40.508535
[CMD]: docker stop --time=30 control-plane-db-hck4w0k4ww8kk4gccw000ggg-132201958859
2025-Dec-25 13:41:40.508535
control-plane-db-hck4w0k4ww8kk4gccw000ggg-132201958859
2025-Dec-25 13:41:40.893923
[CMD]: docker rm -f control-plane-db-hck4w0k4ww8kk4gccw000ggg-132201958859
2025-Dec-25 13:41:40.893923
control-plane-db-hck4w0k4ww8kk4gccw000ggg-132201958859
2025-Dec-25 13:41:40.907587
Starting new application.
2025-Dec-25 13:41:42.153538
[CMD]: docker exec e8cs4g4gsskkkg8cc0o0c4wc bash -c 'SOURCE_COMMIT=7b283b8ff2bc018b8733ef1d1ca76bdc6726bd38 COOLIFY_BRANCH=main COOLIFY_RESOURCE_UUID=hck4w0k4ww8kk4gccw000ggg COOLIFY_CONTAINER_NAME=hck4w0k4ww8kk4gccw000ggg-133859807144  docker compose --env-file /artifacts/e8cs4g4gsskkkg8cc0o0c4wc/.env --project-name hck4w0k4ww8kk4gccw000ggg --project-directory /artifacts/e8cs4g4gsskkkg8cc0o0c4wc -f /artifacts/e8cs4g4gsskkkg8cc0o0c4wc/docker-compose.coolify.yml up -d'
2025-Dec-25 13:41:42.153538
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-133924649774  Creating
2025-Dec-25 13:41:42.153538
Container minio-hck4w0k4ww8kk4gccw000ggg-133924698723  Creating
2025-Dec-25 13:41:42.219614
Container minio-hck4w0k4ww8kk4gccw000ggg-133924698723  Created
2025-Dec-25 13:41:42.219614
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-133924649774  Created
2025-Dec-25 13:41:42.219614
Container keycloak-hck4w0k4ww8kk4gccw000ggg-133924686692  Creating
2025-Dec-25 13:41:42.241914
Container keycloak-hck4w0k4ww8kk4gccw000ggg-133924686692  Created
2025-Dec-25 13:41:42.248148
Container api-hck4w0k4ww8kk4gccw000ggg-133924664772  Creating
2025-Dec-25 13:41:42.268566
Container api-hck4w0k4ww8kk4gccw000ggg-133924664772  Created
2025-Dec-25 13:41:42.268566
Container dashboard-hck4w0k4ww8kk4gccw000ggg-133924677957  Creating
2025-Dec-25 13:41:42.289935
Container dashboard-hck4w0k4ww8kk4gccw000ggg-133924677957  Created
2025-Dec-25 13:41:42.305443
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-133924649774  Starting
2025-Dec-25 13:41:42.305443
Container minio-hck4w0k4ww8kk4gccw000ggg-133924698723  Starting
2025-Dec-25 13:41:42.683529
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-133924649774  Started
2025-Dec-25 13:41:42.683529
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-133924649774  Waiting
2025-Dec-25 13:41:42.716384
Container minio-hck4w0k4ww8kk4gccw000ggg-133924698723  Started
2025-Dec-25 13:41:48.186554
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-133924649774  Healthy
2025-Dec-25 13:41:48.186554
Container keycloak-hck4w0k4ww8kk4gccw000ggg-133924686692  Starting
2025-Dec-25 13:41:48.446200
Container keycloak-hck4w0k4ww8kk4gccw000ggg-133924686692  Started
2025-Dec-25 13:41:48.446200
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-133924649774  Waiting
2025-Dec-25 13:41:48.948352
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-133924649774  Healthy
2025-Dec-25 13:41:48.948352
Container api-hck4w0k4ww8kk4gccw000ggg-133924664772  Starting
2025-Dec-25 13:41:49.216674
Container api-hck4w0k4ww8kk4gccw000ggg-133924664772  Started
2025-Dec-25 13:41:49.216674
Container dashboard-hck4w0k4ww8kk4gccw000ggg-133924677957  Starting
2025-Dec-25 13:41:49.711768
Container dashboard-hck4w0k4ww8kk4gccw000ggg-133924677957  Started
2025-Dec-25 13:41:52.013713
New container started.
2025-Dec-25 13:41:54.228424
Gracefully shutting down build container: e8cs4g4gsskkkg8cc0o0c4wc
2025-Dec-25 13:41:55.168842
[CMD]: docker stop --time=30 e8cs4g4gsskkkg8cc0o0c4wc
2025-Dec-25 13:41:55.168842
e8cs4g4gsskkkg8cc0o0c4wc
2025-Dec-25 13:41:55.847716
[CMD]: docker rm -f e8cs4g4gsskkkg8cc0o0c4wc
2025-Dec-25 13:41:55.847716
Error response from daemon: removal of container e8cs4g4gsskkkg8cc0o0c4wc is already in progress