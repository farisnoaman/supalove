Deployment is Finished.


2025-Dec-25 12:22:02.797293
Starting deployment of supalove to localhost.
2025-Dec-25 12:22:03.442321
Preparing container with helper image: ghcr.io/coollabsio/coolify-helper:1.0.12
2025-Dec-25 12:22:03.791413
[CMD]: docker stop --time=30 vs8wgsg00s8o04k08ccogkss
2025-Dec-25 12:22:03.791413
Error response from daemon: No such container: vs8wgsg00s8o04k08ccogkss
2025-Dec-25 12:22:04.124157
[CMD]: docker rm -f vs8wgsg00s8o04k08ccogkss
2025-Dec-25 12:22:04.124157
Error response from daemon: No such container: vs8wgsg00s8o04k08ccogkss
2025-Dec-25 12:22:04.480956
[CMD]: docker run -d --network coolify --name vs8wgsg00s8o04k08ccogkss  --rm -v /var/run/docker.sock:/var/run/docker.sock ghcr.io/coollabsio/coolify-helper:1.0.12
2025-Dec-25 12:22:04.480956
39dda1ce5ba65623abb8ec3c74b99239072c94327a40fa9641121bc255a1b3a2
2025-Dec-25 12:22:05.795998
[CMD]: docker exec vs8wgsg00s8o04k08ccogkss bash -c 'GIT_SSH_COMMAND="ssh -o ConnectTimeout=30 -p 22 -o Port=22 -o LogLevel=ERROR -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" git ls-remote https://github.com/farisnoaman/supalove refs/heads/main'
2025-Dec-25 12:22:05.795998
651cc5f78dbb5286b263786e9c2134ad800200ea	refs/heads/main
2025-Dec-25 12:22:05.812614
----------------------------------------
2025-Dec-25 12:22:05.820585
Importing farisnoaman/supalove:main (commit sha 651cc5f78dbb5286b263786e9c2134ad800200ea) to /artifacts/vs8wgsg00s8o04k08ccogkss.
2025-Dec-25 12:22:06.216383
[CMD]: docker exec vs8wgsg00s8o04k08ccogkss bash -c 'git clone --depth=1 --recurse-submodules --shallow-submodules -b 'main' 'https://github.com/farisnoaman/supalove' '/artifacts/vs8wgsg00s8o04k08ccogkss' && cd '/artifacts/vs8wgsg00s8o04k08ccogkss' && if [ -f .gitmodules ]; then sed -i "s#git@\(.*\):#https://\1/#g" '/artifacts/vs8wgsg00s8o04k08ccogkss'/.gitmodules || true && git submodule sync && GIT_SSH_COMMAND="ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" git submodule update --init --recursive --depth=1; fi && cd '/artifacts/vs8wgsg00s8o04k08ccogkss' && GIT_SSH_COMMAND="ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" git lfs pull'
2025-Dec-25 12:22:06.216383
Cloning into '/artifacts/vs8wgsg00s8o04k08ccogkss'...
2025-Dec-25 12:22:12.751181
Updating files:  25% (3846/15084)
2025-Dec-25 12:22:12.765881
Updating files:  26% (3922/15084)
2025-Dec-25 12:22:12.823234
Updating files:  27% (4073/15084)
2025-Dec-25 12:22:12.854403
Updating files:  28% (4224/15084)
2025-Dec-25 12:22:12.883186
Updating files:  29% (4375/15084)
2025-Dec-25 12:22:12.908234
Updating files:  30% (4526/15084)
2025-Dec-25 12:22:12.926165
Updating files:  31% (4677/15084)
2025-Dec-25 12:22:12.945378
Updating files:  32% (4827/15084)
2025-Dec-25 12:22:12.961161
Updating files:  33% (4978/15084)
2025-Dec-25 12:22:13.011513
Updating files:  34% (5129/15084)
2025-Dec-25 12:22:13.047467
Updating files:  35% (5280/15084)
2025-Dec-25 12:22:13.114682
Updating files:  36% (5431/15084)
2025-Dec-25 12:22:13.162296
Updating files:  37% (5582/15084)
2025-Dec-25 12:22:13.187601
Updating files:  38% (5732/15084)
2025-Dec-25 12:22:13.216639
Updating files:  39% (5883/15084)
2025-Dec-25 12:22:13.235389
Updating files:  40% (6034/15084)
2025-Dec-25 12:22:13.254617
Updating files:  41% (6185/15084)
2025-Dec-25 12:22:13.276785
Updating files:  42% (6336/15084)
2025-Dec-25 12:22:13.290165
Updating files:  43% (6487/15084)
2025-Dec-25 12:22:13.301711
Updating files:  44% (6637/15084)
2025-Dec-25 12:22:13.313799
Updating files:  45% (6788/15084)
2025-Dec-25 12:22:13.328279
Updating files:  46% (6939/15084)
2025-Dec-25 12:22:13.340571
Updating files:  47% (7090/15084)
2025-Dec-25 12:22:13.353280
Updating files:  48% (7241/15084)
2025-Dec-25 12:22:13.364932
Updating files:  49% (7392/15084)
2025-Dec-25 12:22:13.375533
Updating files:  50% (7542/15084)
2025-Dec-25 12:22:13.386788
Updating files:  51% (7693/15084)
2025-Dec-25 12:22:13.401630
Updating files:  52% (7844/15084)
2025-Dec-25 12:22:13.415883
Updating files:  53% (7995/15084)
2025-Dec-25 12:22:13.432899
Updating files:  54% (8146/15084)
2025-Dec-25 12:22:13.515016
Updating files:  55% (8297/15084)
2025-Dec-25 12:22:13.547048
Updating files:  56% (8448/15084)
2025-Dec-25 12:22:13.558233
Updating files:  57% (8598/15084)
2025-Dec-25 12:22:13.572907
Updating files:  58% (8749/15084)
2025-Dec-25 12:22:13.592895
Updating files:  59% (8900/15084)
2025-Dec-25 12:22:13.606806
Updating files:  60% (9051/15084)
2025-Dec-25 12:22:13.626026
Updating files:  61% (9202/15084)
2025-Dec-25 12:22:13.644178
Updating files:  62% (9353/15084)
2025-Dec-25 12:22:13.660834
Updating files:  63% (9503/15084)
2025-Dec-25 12:22:13.679885
Updating files:  64% (9654/15084)
2025-Dec-25 12:22:13.753242
Updating files:  64% (9798/15084)
2025-Dec-25 12:22:13.755942
Updating files:  65% (9805/15084)
2025-Dec-25 12:22:13.767410
Updating files:  66% (9956/15084)
2025-Dec-25 12:22:13.783189
Updating files:  67% (10107/15084)
2025-Dec-25 12:22:13.803679
Updating files:  68% (10258/15084)
2025-Dec-25 12:22:13.824284
Updating files:  69% (10408/15084)
2025-Dec-25 12:22:13.841614
Updating files:  70% (10559/15084)
2025-Dec-25 12:22:13.856180
Updating files:  71% (10710/15084)
2025-Dec-25 12:22:13.870442
Updating files:  72% (10861/15084)
2025-Dec-25 12:22:13.888304
Updating files:  73% (11012/15084)
2025-Dec-25 12:22:13.903330
Updating files:  74% (11163/15084)
2025-Dec-25 12:22:13.919760
Updating files:  75% (11313/15084)
2025-Dec-25 12:22:13.938425
Updating files:  76% (11464/15084)
2025-Dec-25 12:22:13.950228
Updating files:  77% (11615/15084)
2025-Dec-25 12:22:13.961481
Updating files:  78% (11766/15084)
2025-Dec-25 12:22:13.977976
Updating files:  79% (11917/15084)
2025-Dec-25 12:22:14.044786
Updating files:  80% (12068/15084)
2025-Dec-25 12:22:14.060821
Updating files:  81% (12219/15084)
2025-Dec-25 12:22:14.104036
Updating files:  82% (12369/15084)
2025-Dec-25 12:22:14.114751
Updating files:  83% (12520/15084)
2025-Dec-25 12:22:14.133259
Updating files:  84% (12671/15084)
2025-Dec-25 12:22:14.154929
Updating files:  85% (12822/15084)
2025-Dec-25 12:22:14.168441
Updating files:  86% (12973/15084)
2025-Dec-25 12:22:14.184425
Updating files:  87% (13124/15084)
2025-Dec-25 12:22:14.223794
Updating files:  88% (13274/15084)
2025-Dec-25 12:22:14.248510
Updating files:  89% (13425/15084)
2025-Dec-25 12:22:14.277488
Updating files:  90% (13576/15084)
2025-Dec-25 12:22:14.302646
Updating files:  91% (13727/15084)
2025-Dec-25 12:22:14.319405
Updating files:  92% (13878/15084)
2025-Dec-25 12:22:14.329369
Updating files:  93% (14029/15084)
2025-Dec-25 12:22:14.426371
Updating files:  94% (14179/15084)
2025-Dec-25 12:22:14.458662
Updating files:  95% (14330/15084)
2025-Dec-25 12:22:14.478346
Updating files:  96% (14481/15084)
2025-Dec-25 12:22:14.497306
Updating files:  97% (14632/15084)
2025-Dec-25 12:22:14.515719
Updating files:  98% (14783/15084)
2025-Dec-25 12:22:14.550358
Updating files:  99% (14934/15084)
2025-Dec-25 12:22:14.564867
Updating files: 100% (15084/15084)
Updating files: 100% (15084/15084), done.
2025-Dec-25 12:22:16.389568
[CMD]: docker exec vs8wgsg00s8o04k08ccogkss bash -c 'cd /artifacts/vs8wgsg00s8o04k08ccogkss && git log -1 651cc5f78dbb5286b263786e9c2134ad800200ea --pretty=%B'
2025-Dec-25 12:22:16.389568
fix: Adjust `ROOT` path resolution to support local and Docker environments. Handle Docker path for ROOT in main.py
2025-Dec-25 12:22:24.471270
[CMD]: docker exec vs8wgsg00s8o04k08ccogkss bash -c 'test -f /artifacts/vs8wgsg00s8o04k08ccogkss/control-plane/api/Dockerfile && echo 'exists' || echo 'not found''
2025-Dec-25 12:22:24.471270
exists
2025-Dec-25 12:22:25.094836
[CMD]: docker exec vs8wgsg00s8o04k08ccogkss bash -c 'cat /artifacts/vs8wgsg00s8o04k08ccogkss/control-plane/api/Dockerfile'
2025-Dec-25 12:22:25.094836
FROM python:3.12-slim
2025-Dec-25 12:22:25.094836
WORKDIR /app
2025-Dec-25 12:22:25.094836
COPY requirements.txt .
2025-Dec-25 12:22:25.094836
RUN pip install -r requirements.txt
2025-Dec-25 12:22:25.094836
COPY . .
2025-Dec-25 12:22:25.094836
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
2025-Dec-25 12:22:25.487569
Added 21 ARG declarations to Dockerfile for service api.
2025-Dec-25 12:22:25.856924
[CMD]: docker exec vs8wgsg00s8o04k08ccogkss bash -c 'test -f /artifacts/vs8wgsg00s8o04k08ccogkss/dashboard/Dockerfile && echo 'exists' || echo 'not found''
2025-Dec-25 12:22:25.856924
exists
2025-Dec-25 12:22:26.237911
[CMD]: docker exec vs8wgsg00s8o04k08ccogkss bash -c 'cat /artifacts/vs8wgsg00s8o04k08ccogkss/dashboard/Dockerfile'
2025-Dec-25 12:22:26.237911
# Stage 1: Dependencies
2025-Dec-25 12:22:26.237911
FROM node:20-alpine AS deps
2025-Dec-25 12:22:26.237911
WORKDIR /app
2025-Dec-25 12:22:26.237911
COPY package*.json ./
2025-Dec-25 12:22:26.237911
RUN npm install
2025-Dec-25 12:22:26.237911
2025-Dec-25 12:22:26.237911
# Stage 2: Builder
2025-Dec-25 12:22:26.237911
FROM node:20-alpine AS builder
2025-Dec-25 12:22:26.237911
WORKDIR /app
2025-Dec-25 12:22:26.237911
COPY --from=deps /app/node_modules ./node_modules
2025-Dec-25 12:22:26.237911
COPY . .
2025-Dec-25 12:22:26.237911
# Set environment variables for build if needed (e.g. backend URL)
2025-Dec-25 12:22:26.237911
# For Next.js client-side fetch, it might need to know the URL at build time if pre-rendering,
2025-Dec-25 12:22:26.237911
# but we are using "use client" so it's fine.
2025-Dec-25 12:22:26.237911
ARG NEXT_PUBLIC_API_URL
2025-Dec-25 12:22:26.237911
ENV NEXT_PUBLIC_API_URL=${NEXT_PUBLIC_API_URL}
2025-Dec-25 12:22:26.237911
RUN npm run build
2025-Dec-25 12:22:26.237911
2025-Dec-25 12:22:26.237911
# Stage 3: Runner
2025-Dec-25 12:22:26.237911
FROM node:20-alpine AS runner
2025-Dec-25 12:22:26.237911
WORKDIR /app
2025-Dec-25 12:22:26.237911
ENV NODE_ENV=production
2025-Dec-25 12:22:26.237911
COPY --from=builder /app/public ./public
2025-Dec-25 12:22:26.237911
COPY --from=builder /app/.next ./.next
2025-Dec-25 12:22:26.237911
COPY --from=builder /app/node_modules ./node_modules
2025-Dec-25 12:22:26.237911
COPY --from=builder /app/package.json ./package.json
2025-Dec-25 12:22:26.237911
2025-Dec-25 12:22:26.237911
EXPOSE 3000
2025-Dec-25 12:22:26.237911
CMD ["npm", "start"]
2025-Dec-25 12:22:26.661018
Added 63 ARG declarations to Dockerfile for service dashboard (multi-stage build, added to 3 stages).
2025-Dec-25 12:22:26.671651
Pulling & building required images.
2025-Dec-25 12:22:26.706287
Creating build-time .env file in /artifacts (outside Docker context).
2025-Dec-25 12:22:27.518481
[CMD]: docker exec vs8wgsg00s8o04k08ccogkss bash -c 'cat /artifacts/build-time.env'
2025-Dec-25 12:22:27.518481
SOURCE_COMMIT='651cc5f78dbb5286b263786e9c2134ad800200ea'
2025-Dec-25 12:22:27.518481
COOLIFY_URL=''
2025-Dec-25 12:22:27.518481
COOLIFY_FQDN=''
2025-Dec-25 12:22:27.518481
SERVICE_NAME_CONTROL-PLANE-DB='control-plane-db'
2025-Dec-25 12:22:27.518481
SERVICE_NAME_API='api'
2025-Dec-25 12:22:27.518481
SERVICE_NAME_DASHBOARD='dashboard'
2025-Dec-25 12:22:27.518481
SERVICE_NAME_KEYCLOAK='keycloak'
2025-Dec-25 12:22:27.518481
SERVICE_NAME_MINIO='minio'
2025-Dec-25 12:22:27.518481
SERVICE_URL_DASHBOARD='https://supalove.hayataxi.online'
2025-Dec-25 12:22:27.518481
SERVICE_FQDN_DASHBOARD='supalove.hayataxi.online'
2025-Dec-25 12:22:27.518481
SERVICE_URL_API='https://api.hayataxi.online'
2025-Dec-25 12:22:27.518481
SERVICE_FQDN_API='api.hayataxi.online'
2025-Dec-25 12:22:27.518481
SERVICE_URL_KEYCLOAK='https://auth.hayataxi.online'
2025-Dec-25 12:22:27.518481
SERVICE_FQDN_KEYCLOAK='auth.hayataxi.online'
2025-Dec-25 12:22:27.518481
SERVICE_URL_MINIO='https://s3.hayataxi.online'
2025-Dec-25 12:22:27.518481
SERVICE_FQDN_MINIO='s3.hayataxi.online'
2025-Dec-25 12:22:27.518481
ALLOWED_ORIGINS="http://localhost:3000,http://localhost:8000"
2025-Dec-25 12:22:27.518481
KEYCLOAK_ADMIN_PASSWORD="admin"
2025-Dec-25 12:22:27.518481
KEYCLOAK_ADMIN_USER="admin"
2025-Dec-25 12:22:27.518481
MINIO_ROOT_PASSWORD="minioadmin"
2025-Dec-25 12:22:27.518481
MINIO_ROOT_USER="minioadmin"
2025-Dec-25 12:22:27.518481
NEXT_PUBLIC_API_URL="https://api.hayataxi.online"
2025-Dec-25 12:22:27.518481
POSTGRES_DB="control_plane"
2025-Dec-25 12:22:27.518481
POSTGRES_PASSWORD="platform"
2025-Dec-25 12:22:27.518481
POSTGRES_USER="platform"
2025-Dec-25 12:22:27.518481
URL="http://localhost:8000"
2025-Dec-25 12:22:27.526471
Adding build arguments to Docker Compose build command.
2025-Dec-25 12:22:28.088833
[CMD]: docker exec vs8wgsg00s8o04k08ccogkss bash -c 'SOURCE_COMMIT=651cc5f78dbb5286b263786e9c2134ad800200ea COOLIFY_BRANCH=main COOLIFY_RESOURCE_UUID=hck4w0k4ww8kk4gccw000ggg COOLIFY_CONTAINER_NAME=hck4w0k4ww8kk4gccw000ggg-122201499845  docker compose --env-file /artifacts/build-time.env --project-name hck4w0k4ww8kk4gccw000ggg --project-directory /artifacts/vs8wgsg00s8o04k08ccogkss -f /artifacts/vs8wgsg00s8o04k08ccogkss/docker-compose.coolify.yml build --pull --no-cache --build-arg SOURCE_COMMIT --build-arg COOLIFY_URL --build-arg COOLIFY_FQDN --build-arg SERVICE_FQDN_API --build-arg SERVICE_FQDN_DASHBOARD --build-arg SERVICE_FQDN_KEYCLOAK --build-arg SERVICE_FQDN_MINIO --build-arg SERVICE_URL_API --build-arg SERVICE_URL_DASHBOARD --build-arg SERVICE_URL_KEYCLOAK --build-arg SERVICE_URL_MINIO --build-arg ALLOWED_ORIGINS --build-arg KEYCLOAK_ADMIN_PASSWORD --build-arg KEYCLOAK_ADMIN_USER --build-arg MINIO_ROOT_PASSWORD --build-arg MINIO_ROOT_USER --build-arg NEXT_PUBLIC_API_URL --build-arg POSTGRES_DB --build-arg POSTGRES_PASSWORD --build-arg POSTGRES_USER --build-arg URL --build-arg COOLIFY_BUILD_SECRETS_HASH=5919701a6af98a83ceb04b3574c624bc0a07989d91c3dea0d7e0d08d265537f2'
2025-Dec-25 12:22:28.088833
#1 [internal] load local bake definitions
2025-Dec-25 12:22:28.190652
#1 reading from stdin 3.22kB done
2025-Dec-25 12:22:28.190652
#1 DONE 0.0s
2025-Dec-25 12:22:28.190652
2025-Dec-25 12:22:28.190652
#2 [api internal] load build definition from Dockerfile
2025-Dec-25 12:22:28.190652
#2 transferring dockerfile: 658B done
2025-Dec-25 12:22:28.190652
#2 DONE 0.0s
2025-Dec-25 12:22:28.190652
2025-Dec-25 12:22:28.190652
#3 [dashboard internal] load build definition from Dockerfile
2025-Dec-25 12:22:28.190652
#3 transferring dockerfile: 2.20kB done
2025-Dec-25 12:22:28.190652
#3 DONE 0.0s
2025-Dec-25 12:22:28.342966
#4 [dashboard internal] load metadata for docker.io/library/node:20-alpine
2025-Dec-25 12:22:28.928688
#4 DONE 0.6s
2025-Dec-25 12:22:28.928688
2025-Dec-25 12:22:28.928688
#5 [dashboard internal] load .dockerignore
2025-Dec-25 12:22:28.928688
#5 transferring context: 2B done
2025-Dec-25 12:22:28.928688
#5 DONE 0.0s
2025-Dec-25 12:22:28.928688
2025-Dec-25 12:22:28.928688
#6 [dashboard deps 1/4] FROM docker.io/library/node:20-alpine@sha256:658d0f63e501824d6c23e06d4bb95c71e7d704537c9d9272f488ac03a370d448
2025-Dec-25 12:22:28.928688
#6 DONE 0.0s
2025-Dec-25 12:22:28.928688
2025-Dec-25 12:22:28.928688
#7 [dashboard deps 2/4] WORKDIR /app
2025-Dec-25 12:22:28.928688
#7 CACHED
2025-Dec-25 12:22:28.928688
2025-Dec-25 12:22:28.928688
#8 [dashboard internal] load build context
2025-Dec-25 12:22:28.928688
#8 transferring context: 837.69kB 0.0s done
2025-Dec-25 12:22:28.928688
#8 DONE 0.0s
2025-Dec-25 12:22:28.928688
2025-Dec-25 12:22:28.928688
#9 [dashboard deps 3/4] COPY package*.json ./
2025-Dec-25 12:22:28.928688
#9 DONE 0.0s
2025-Dec-25 12:22:28.928688
2025-Dec-25 12:22:28.928688
#10 [api internal] load metadata for docker.io/library/python:3.12-slim
2025-Dec-25 12:22:28.928688
#10 DONE 0.7s
2025-Dec-25 12:22:28.928688
2025-Dec-25 12:22:28.928688
#11 [api internal] load .dockerignore
2025-Dec-25 12:22:28.928688
#11 transferring context: 2B done
2025-Dec-25 12:22:28.928688
#11 DONE 0.0s
2025-Dec-25 12:22:28.928688
2025-Dec-25 12:22:28.928688
#12 [dashboard deps 4/4] RUN npm install
2025-Dec-25 12:22:29.070389
#12 ...
2025-Dec-25 12:22:29.070389
2025-Dec-25 12:22:29.070389
#13 [api 1/5] FROM docker.io/library/python:3.12-slim@sha256:fa48eefe2146644c2308b909d6bb7651a768178f84fc9550dcd495e4d6d84d01
2025-Dec-25 12:22:29.070389
#13 DONE 0.0s
2025-Dec-25 12:22:29.070389
2025-Dec-25 12:22:29.070389
#14 [api 2/5] WORKDIR /app
2025-Dec-25 12:22:29.070389
#14 CACHED
2025-Dec-25 12:22:29.168194
#15 [api internal] load build context
2025-Dec-25 12:22:34.045520
#15 transferring context: 225.78MB 5.1s
2025-Dec-25 12:22:36.337707
#15 transferring context: 330.52MB 7.4s done
2025-Dec-25 12:22:36.450341
#15 DONE 7.4s
2025-Dec-25 12:22:36.450341
2025-Dec-25 12:22:36.450341
#16 [api 3/5] COPY requirements.txt .
2025-Dec-25 12:22:36.817743
#16 DONE 0.4s
2025-Dec-25 12:22:36.817743
2025-Dec-25 12:22:36.817743
#12 [dashboard deps 4/4] RUN npm install
2025-Dec-25 12:22:36.981508
#12 ...
2025-Dec-25 12:22:36.981508
2025-Dec-25 12:22:36.981508
#17 [api 4/5] RUN pip install -r requirements.txt
2025-Dec-25 12:22:39.673781
#17 2.855 Collecting fastapi (from -r requirements.txt (line 1))
2025-Dec-25 12:22:39.853359
#17 2.884   Downloading fastapi-0.127.0-py3-none-any.whl.metadata (30 kB)
2025-Dec-25 12:22:39.972322
#17 3.154 Collecting sqlalchemy (from -r requirements.txt (line 3))
2025-Dec-25 12:22:40.093938
#17 3.165   Downloading sqlalchemy-2.0.45-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (9.5 kB)
2025-Dec-25 12:22:40.093938
#17 3.227 Collecting psycopg2-binary (from -r requirements.txt (line 4))
2025-Dec-25 12:22:40.093938
#17 3.238   Downloading psycopg2_binary-2.9.11-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (4.9 kB)
2025-Dec-25 12:22:40.093938
#17 3.275 Collecting httpx (from -r requirements.txt (line 5))
2025-Dec-25 12:22:40.202230
#17 3.284   Downloading httpx-0.28.1-py3-none-any.whl.metadata (7.1 kB)
2025-Dec-25 12:22:40.202230
#17 3.332 Collecting python-keycloak (from -r requirements.txt (line 6))
2025-Dec-25 12:22:40.202230
#17 3.338   Downloading python_keycloak-5.8.1-py3-none-any.whl.metadata (6.0 kB)
2025-Dec-25 12:22:40.202230
#17 3.384 Collecting minio (from -r requirements.txt (line 7))
2025-Dec-25 12:22:40.318405
#17 3.392   Downloading minio-7.2.20-py3-none-any.whl.metadata (6.5 kB)
2025-Dec-25 12:22:40.318405
#17 3.443 Collecting requests (from -r requirements.txt (line 8))
2025-Dec-25 12:22:40.318405
#17 3.462   Downloading requests-2.32.5-py3-none-any.whl.metadata (4.9 kB)
2025-Dec-25 12:22:40.318405
#17 3.501 Collecting python-dotenv (from -r requirements.txt (line 9))
2025-Dec-25 12:22:40.442148
#17 3.508   Downloading python_dotenv-1.2.1-py3-none-any.whl.metadata (25 kB)
2025-Dec-25 12:22:40.442148
#17 3.554 Collecting uvicorn[standard] (from -r requirements.txt (line 2))
2025-Dec-25 12:22:40.442148
#17 3.559   Downloading uvicorn-0.40.0-py3-none-any.whl.metadata (6.7 kB)
2025-Dec-25 12:22:40.442148
#17 3.586 Collecting passlib[bcrypt] (from -r requirements.txt (line 10))
2025-Dec-25 12:22:40.442148
#17 3.593   Downloading passlib-1.7.4-py2.py3-none-any.whl.metadata (1.7 kB)
2025-Dec-25 12:22:40.442148
#17 3.623 Collecting python-jose[cryptography] (from -r requirements.txt (line 11))
2025-Dec-25 12:22:40.597159
#17 3.631   Downloading python_jose-3.5.0-py2.py3-none-any.whl.metadata (5.5 kB)
2025-Dec-25 12:22:40.597159
#17 3.679 Collecting starlette<0.51.0,>=0.40.0 (from fastapi->-r requirements.txt (line 1))
2025-Dec-25 12:22:40.597159
#17 3.685   Downloading starlette-0.50.0-py3-none-any.whl.metadata (6.3 kB)
2025-Dec-25 12:22:40.597159
#17 3.780 Collecting pydantic>=2.7.0 (from fastapi->-r requirements.txt (line 1))
2025-Dec-25 12:22:40.739630
#17 3.785   Downloading pydantic-2.12.5-py3-none-any.whl.metadata (90 kB)
2025-Dec-25 12:22:40.739630
#17 3.820 Collecting typing-extensions>=4.8.0 (from fastapi->-r requirements.txt (line 1))
2025-Dec-25 12:22:40.739630
#17 3.825   Downloading typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
2025-Dec-25 12:22:40.739630
#17 3.853 Collecting annotated-doc>=0.0.2 (from fastapi->-r requirements.txt (line 1))
2025-Dec-25 12:22:40.739630
#17 3.862   Downloading annotated_doc-0.0.4-py3-none-any.whl.metadata (6.6 kB)
2025-Dec-25 12:22:40.739630
#17 3.919 Collecting click>=7.0 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 12:22:40.849522
#17 3.941   Downloading click-8.3.1-py3-none-any.whl.metadata (2.6 kB)
2025-Dec-25 12:22:40.849522
#17 3.969 Collecting h11>=0.8 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 12:22:40.849522
#17 3.974   Downloading h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
2025-Dec-25 12:22:40.849522
#17 4.029 Collecting httptools>=0.6.3 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 12:22:40.977525
#17 4.035   Downloading httptools-0.7.1-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (3.5 kB)
2025-Dec-25 12:22:40.977525
#17 4.085 Collecting pyyaml>=5.1 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 12:22:40.977525
#17 4.089   Downloading pyyaml-6.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.4 kB)
2025-Dec-25 12:22:40.977525
#17 4.160 Collecting uvloop>=0.15.1 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 12:22:41.078456
#17 4.167   Downloading uvloop-0.22.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (4.9 kB)
2025-Dec-25 12:22:41.078456
#17 4.260 Collecting watchfiles>=0.13 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 12:22:41.206788
#17 4.267   Downloading watchfiles-1.1.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.9 kB)
2025-Dec-25 12:22:41.206788
#17 4.388 Collecting websockets>=10.4 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 12:22:41.346970
#17 4.394   Downloading websockets-15.0.1-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.8 kB)
2025-Dec-25 12:22:41.346970
#17 4.529 Collecting greenlet>=1 (from sqlalchemy->-r requirements.txt (line 3))
2025-Dec-25 12:22:41.492196
#17 4.533   Downloading greenlet-3.3.0-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (4.1 kB)
2025-Dec-25 12:22:41.492196
#17 4.567 Collecting anyio (from httpx->-r requirements.txt (line 5))
2025-Dec-25 12:22:41.492196
#17 4.571   Downloading anyio-4.12.0-py3-none-any.whl.metadata (4.3 kB)
2025-Dec-25 12:22:41.492196
#17 4.620 Collecting certifi (from httpx->-r requirements.txt (line 5))
2025-Dec-25 12:22:41.492196
#17 4.627   Downloading certifi-2025.11.12-py3-none-any.whl.metadata (2.5 kB)
2025-Dec-25 12:22:41.492196
#17 4.674 Collecting httpcore==1.* (from httpx->-r requirements.txt (line 5))
2025-Dec-25 12:22:41.595799
#17 4.680   Downloading httpcore-1.0.9-py3-none-any.whl.metadata (21 kB)
2025-Dec-25 12:22:41.606737
#17 4.726 Collecting idna (from httpx->-r requirements.txt (line 5))
2025-Dec-25 12:22:41.606737
#17 4.730   Downloading idna-3.11-py3-none-any.whl.metadata (8.4 kB)
2025-Dec-25 12:22:41.606737
#17 4.770 Collecting aiofiles>=24.1.0 (from python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 12:22:41.606737
#17 4.778   Downloading aiofiles-25.1.0-py3-none-any.whl.metadata (6.3 kB)
2025-Dec-25 12:22:41.704708
#17 4.814 Collecting async-property>=0.2.2 (from python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 12:22:41.710935
#17 4.822   Downloading async_property-0.2.2-py2.py3-none-any.whl.metadata (5.3 kB)
2025-Dec-25 12:22:41.710935
#17 4.848 Collecting deprecation>=2.1.0 (from python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 12:22:41.710935
#17 4.855   Downloading deprecation-2.1.0-py2.py3-none-any.whl.metadata (4.6 kB)
2025-Dec-25 12:22:41.710935
#17 4.885 Collecting jwcrypto>=1.5.4 (from python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 12:22:41.908579
#17 4.901   Downloading jwcrypto-1.5.6-py3-none-any.whl.metadata (3.1 kB)
2025-Dec-25 12:22:41.908579
#17 4.933 Collecting requests-toolbelt>=0.6.0 (from python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 12:22:41.908579
#17 4.938   Downloading requests_toolbelt-1.0.0-py2.py3-none-any.whl.metadata (14 kB)
2025-Dec-25 12:22:41.908579
#17 4.978 Collecting argon2-cffi (from minio->-r requirements.txt (line 7))
2025-Dec-25 12:22:41.908579
#17 4.987   Downloading argon2_cffi-25.1.0-py3-none-any.whl.metadata (4.1 kB)
2025-Dec-25 12:22:41.908579
#17 5.091 Collecting pycryptodome (from minio->-r requirements.txt (line 7))
2025-Dec-25 12:22:42.053855
#17 5.102   Downloading pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (3.4 kB)
2025-Dec-25 12:22:42.074875
#17 5.139 Collecting urllib3 (from minio->-r requirements.txt (line 7))
2025-Dec-25 12:22:42.074875
#17 5.142   Downloading urllib3-2.6.2-py3-none-any.whl.metadata (6.6 kB)
2025-Dec-25 12:22:42.074875
#17 5.232 Collecting charset_normalizer<4,>=2 (from requests->-r requirements.txt (line 8))
2025-Dec-25 12:22:42.220266
#17 5.252   Downloading charset_normalizer-3.4.4-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (37 kB)
2025-Dec-25 12:22:42.270067
#17 5.451 Collecting bcrypt>=3.1.0 (from passlib[bcrypt]->-r requirements.txt (line 10))
2025-Dec-25 12:22:42.377791
#17 5.460   Downloading bcrypt-5.0.0-cp39-abi3-manylinux_2_34_x86_64.whl.metadata (10 kB)
2025-Dec-25 12:22:42.385886
#17 5.496 Collecting ecdsa!=0.15 (from python-jose[cryptography]->-r requirements.txt (line 11))
2025-Dec-25 12:22:42.385886
#17 5.502   Downloading ecdsa-0.19.1-py2.py3-none-any.whl.metadata (29 kB)
2025-Dec-25 12:22:42.385886
#17 5.528 Collecting rsa!=4.1.1,!=4.4,<5.0,>=4.0 (from python-jose[cryptography]->-r requirements.txt (line 11))
2025-Dec-25 12:22:42.385886
#17 5.532   Downloading rsa-4.9.1-py3-none-any.whl.metadata (5.6 kB)
2025-Dec-25 12:22:42.385886
#17 5.560 Collecting pyasn1>=0.5.0 (from python-jose[cryptography]->-r requirements.txt (line 11))
2025-Dec-25 12:22:42.537534
#17 5.568   Downloading pyasn1-0.6.1-py3-none-any.whl.metadata (8.4 kB)
2025-Dec-25 12:22:42.549341
#17 5.732 Collecting cryptography>=3.4.0 (from python-jose[cryptography]->-r requirements.txt (line 11))
2025-Dec-25 12:22:42.686735
#17 5.740   Downloading cryptography-46.0.3-cp311-abi3-manylinux_2_34_x86_64.whl.metadata (5.7 kB)
2025-Dec-25 12:22:42.686735
#17 5.870 Collecting cffi>=2.0.0 (from cryptography>=3.4.0->python-jose[cryptography]->-r requirements.txt (line 11))
2025-Dec-25 12:22:42.792068
#17 5.877   Downloading cffi-2.0.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (2.6 kB)
2025-Dec-25 12:22:42.792068
#17 5.899 Collecting packaging (from deprecation>=2.1.0->python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 12:22:42.792068
#17 5.902   Downloading packaging-25.0-py3-none-any.whl.metadata (3.3 kB)
2025-Dec-25 12:22:42.792068
#17 5.927 Collecting six>=1.9.0 (from ecdsa!=0.15->python-jose[cryptography]->-r requirements.txt (line 11))
2025-Dec-25 12:22:42.792068
#17 5.932   Downloading six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
2025-Dec-25 12:22:42.792068
#17 5.974 Collecting annotated-types>=0.6.0 (from pydantic>=2.7.0->fastapi->-r requirements.txt (line 1))
2025-Dec-25 12:22:42.947036
#17 5.979   Downloading annotated_types-0.7.0-py3-none-any.whl.metadata (15 kB)
2025-Dec-25 12:22:43.715330
#17 6.897 Collecting pydantic-core==2.41.5 (from pydantic>=2.7.0->fastapi->-r requirements.txt (line 1))
2025-Dec-25 12:22:43.886197
#17 6.904   Downloading pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (7.3 kB)
2025-Dec-25 12:22:43.886197
#17 6.942 Collecting typing-inspection>=0.4.2 (from pydantic>=2.7.0->fastapi->-r requirements.txt (line 1))
2025-Dec-25 12:22:43.886197
#17 6.949   Downloading typing_inspection-0.4.2-py3-none-any.whl.metadata (2.6 kB)
2025-Dec-25 12:22:43.886197
#17 7.065 Collecting argon2-cffi-bindings (from argon2-cffi->minio->-r requirements.txt (line 7))
2025-Dec-25 12:22:44.042725
#17 7.075   Downloading argon2_cffi_bindings-25.1.0-cp39-abi3-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl.metadata (7.4 kB)
2025-Dec-25 12:22:44.042725
#17 7.150 Collecting pycparser (from cffi>=2.0.0->cryptography>=3.4.0->python-jose[cryptography]->-r requirements.txt (line 11))
2025-Dec-25 12:22:44.042725
#17 7.158   Downloading pycparser-2.23-py3-none-any.whl.metadata (993 bytes)
2025-Dec-25 12:22:44.042725
#17 7.225 Downloading fastapi-0.127.0-py3-none-any.whl (112 kB)
2025-Dec-25 12:22:44.240955
#17 7.244 Downloading sqlalchemy-2.0.45-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (3.3 MB)
2025-Dec-25 12:22:44.240955
#17 7.311    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.3/3.3 MB 57.8 MB/s eta 0:00:00
2025-Dec-25 12:22:44.240955
#17 7.323 Downloading psycopg2_binary-2.9.11-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (4.2 MB)
2025-Dec-25 12:22:44.240955
#17 7.423    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.2/4.2 MB 44.8 MB/s eta 0:00:00
2025-Dec-25 12:22:44.343480
#17 7.435 Downloading httpx-0.28.1-py3-none-any.whl (73 kB)
2025-Dec-25 12:22:44.343480
#17 7.452 Downloading httpcore-1.0.9-py3-none-any.whl (78 kB)
2025-Dec-25 12:22:44.343480
#17 7.473 Downloading python_keycloak-5.8.1-py3-none-any.whl (77 kB)
2025-Dec-25 12:22:44.343480
#17 7.490 Downloading minio-7.2.20-py3-none-any.whl (93 kB)
2025-Dec-25 12:22:44.343480
#17 7.508 Downloading requests-2.32.5-py3-none-any.whl (64 kB)
2025-Dec-25 12:22:44.343480
#17 7.526 Downloading python_dotenv-1.2.1-py3-none-any.whl (21 kB)
2025-Dec-25 12:22:44.459601
#17 7.541 Downloading aiofiles-25.1.0-py3-none-any.whl (14 kB)
2025-Dec-25 12:22:44.459601
#17 7.552 Downloading annotated_doc-0.0.4-py3-none-any.whl (5.3 kB)
2025-Dec-25 12:22:44.459601
#17 7.567 Downloading async_property-0.2.2-py2.py3-none-any.whl (9.5 kB)
2025-Dec-25 12:22:44.459601
#17 7.582 Downloading bcrypt-5.0.0-cp39-abi3-manylinux_2_34_x86_64.whl (278 kB)
2025-Dec-25 12:22:44.459601
#17 7.607 Downloading certifi-2025.11.12-py3-none-any.whl (159 kB)
2025-Dec-25 12:22:44.459601
#17 7.625 Downloading charset_normalizer-3.4.4-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (153 kB)
2025-Dec-25 12:22:44.459601
#17 7.640 Downloading click-8.3.1-py3-none-any.whl (108 kB)
2025-Dec-25 12:22:44.595619
#17 7.655 Downloading cryptography-46.0.3-cp311-abi3-manylinux_2_34_x86_64.whl (4.5 MB)
2025-Dec-25 12:22:44.595619
#17 7.778    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.5/4.5 MB 38.8 MB/s eta 0:00:00
2025-Dec-25 12:22:44.730540
#17 7.789 Downloading deprecation-2.1.0-py2.py3-none-any.whl (11 kB)
2025-Dec-25 12:22:44.730540
#17 7.801 Downloading ecdsa-0.19.1-py2.py3-none-any.whl (150 kB)
2025-Dec-25 12:22:44.730540
#17 7.820 Downloading greenlet-3.3.0-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (609 kB)
2025-Dec-25 12:22:44.730540
#17 7.842    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 609.9/609.9 kB 20.2 MB/s eta 0:00:00
2025-Dec-25 12:22:44.730540
#17 7.854 Downloading h11-0.16.0-py3-none-any.whl (37 kB)
2025-Dec-25 12:22:44.730540
#17 7.876 Downloading httptools-0.7.1-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (517 kB)
2025-Dec-25 12:22:44.730540
#17 7.904 Downloading idna-3.11-py3-none-any.whl (71 kB)
2025-Dec-25 12:22:44.846603
#17 7.919 Downloading jwcrypto-1.5.6-py3-none-any.whl (92 kB)
2025-Dec-25 12:22:44.846603
#17 7.947 Downloading pyasn1-0.6.1-py3-none-any.whl (83 kB)
2025-Dec-25 12:22:44.846603
#17 7.998 Downloading pydantic-2.12.5-py3-none-any.whl (463 kB)
2025-Dec-25 12:22:44.846603
#17 8.027 Downloading pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.1 MB)
2025-Dec-25 12:22:44.959631
#17 8.093    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 37.4 MB/s eta 0:00:00
2025-Dec-25 12:22:44.959631
#17 8.098 Downloading pyyaml-6.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (807 kB)
2025-Dec-25 12:22:44.959631
#17 8.139    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 807.9/807.9 kB 16.8 MB/s eta 0:00:00
2025-Dec-25 12:22:45.062191
#17 8.146 Downloading requests_toolbelt-1.0.0-py2.py3-none-any.whl (54 kB)
2025-Dec-25 12:22:45.062191
#17 8.163 Downloading rsa-4.9.1-py3-none-any.whl (34 kB)
2025-Dec-25 12:22:45.062191
#17 8.186 Downloading starlette-0.50.0-py3-none-any.whl (74 kB)
2025-Dec-25 12:22:45.062191
#17 8.225 Downloading anyio-4.12.0-py3-none-any.whl (113 kB)
2025-Dec-25 12:22:45.062191
#17 8.245 Downloading typing_extensions-4.15.0-py3-none-any.whl (44 kB)
2025-Dec-25 12:22:45.180924
#17 8.266 Downloading urllib3-2.6.2-py3-none-any.whl (131 kB)
2025-Dec-25 12:22:45.180924
#17 8.284 Downloading uvloop-0.22.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (4.4 MB)
2025-Dec-25 12:22:45.180924
#17 8.364    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.4/4.4 MB 56.4 MB/s eta 0:00:00
2025-Dec-25 12:22:45.281591
#17 8.375 Downloading watchfiles-1.1.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (456 kB)
2025-Dec-25 12:22:45.281591
#17 8.387 Downloading websockets-15.0.1-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (182 kB)
2025-Dec-25 12:22:45.291412
#17 8.396 Downloading argon2_cffi-25.1.0-py3-none-any.whl (14 kB)
2025-Dec-25 12:22:45.291412
#17 8.406 Downloading passlib-1.7.4-py2.py3-none-any.whl (525 kB)
2025-Dec-25 12:22:45.291412
#17 8.416    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 525.6/525.6 kB 36.8 MB/s eta 0:00:00
2025-Dec-25 12:22:45.291412
#17 8.421 Downloading pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.3 MB)
2025-Dec-25 12:22:45.291412
#17 8.451    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.3/2.3 MB 79.6 MB/s eta 0:00:00
2025-Dec-25 12:22:45.291412
#17 8.456 Downloading python_jose-3.5.0-py2.py3-none-any.whl (34 kB)
2025-Dec-25 12:22:45.291412
#17 8.463 Downloading uvicorn-0.40.0-py3-none-any.whl (68 kB)
2025-Dec-25 12:22:45.522550
#17 8.478 Downloading annotated_types-0.7.0-py3-none-any.whl (13 kB)
2025-Dec-25 12:22:45.522550
#17 8.497 Downloading cffi-2.0.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (219 kB)
2025-Dec-25 12:22:45.522550
#17 8.512 Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
2025-Dec-25 12:22:45.522550
#17 8.526 Downloading typing_inspection-0.4.2-py3-none-any.whl (14 kB)
2025-Dec-25 12:22:45.522550
#17 8.534 Downloading argon2_cffi_bindings-25.1.0-cp39-abi3-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl (87 kB)
2025-Dec-25 12:22:45.522550
#17 8.544 Downloading packaging-25.0-py3-none-any.whl (66 kB)
2025-Dec-25 12:22:45.522550
#17 8.555 Downloading pycparser-2.23-py3-none-any.whl (118 kB)
2025-Dec-25 12:22:45.546182
#17 8.728 Installing collected packages: passlib, async-property, websockets, uvloop, urllib3, typing-extensions, six, pyyaml, python-dotenv, pycryptodome, pycparser, pyasn1, psycopg2-binary, packaging, idna, httptools, h11, greenlet, click, charset_normalizer, certifi, bcrypt, annotated-types, annotated-doc, aiofiles, uvicorn, typing-inspection, sqlalchemy, rsa, requests, pydantic-core, httpcore, ecdsa, deprecation, cffi, anyio, watchfiles, starlette, requests-toolbelt, python-jose, pydantic, httpx, cryptography, argon2-cffi-bindings, jwcrypto, fastapi, argon2-cffi, python-keycloak, minio
2025-Dec-25 12:22:50.974205
#17 14.16 Successfully installed aiofiles-25.1.0 annotated-doc-0.0.4 annotated-types-0.7.0 anyio-4.12.0 argon2-cffi-25.1.0 argon2-cffi-bindings-25.1.0 async-property-0.2.2 bcrypt-5.0.0 certifi-2025.11.12 cffi-2.0.0 charset_normalizer-3.4.4 click-8.3.1 cryptography-46.0.3 deprecation-2.1.0 ecdsa-0.19.1 fastapi-0.127.0 greenlet-3.3.0 h11-0.16.0 httpcore-1.0.9 httptools-0.7.1 httpx-0.28.1 idna-3.11 jwcrypto-1.5.6 minio-7.2.20 packaging-25.0 passlib-1.7.4 psycopg2-binary-2.9.11 pyasn1-0.6.1 pycparser-2.23 pycryptodome-3.23.0 pydantic-2.12.5 pydantic-core-2.41.5 python-dotenv-1.2.1 python-jose-3.5.0 python-keycloak-5.8.1 pyyaml-6.0.3 requests-2.32.5 requests-toolbelt-1.0.0 rsa-4.9.1 six-1.17.0 sqlalchemy-2.0.45 starlette-0.50.0 typing-extensions-4.15.0 typing-inspection-0.4.2 urllib3-2.6.2 uvicorn-0.40.0 uvloop-0.22.1 watchfiles-1.1.1 websockets-15.0.1
2025-Dec-25 12:22:51.087840
#17 14.16 WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager, possibly rendering your system unusable. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv. Use the --root-user-action option if you know what you are doing and want to suppress this warning.
2025-Dec-25 12:22:51.087840
#17 14.27
2025-Dec-25 12:22:51.087840
#17 14.27 [notice] A new release of pip is available: 25.0.1 -> 25.3
2025-Dec-25 12:22:51.087840
#17 14.27 [notice] To update, run: pip install --upgrade pip
2025-Dec-25 12:22:51.816679
#17 DONE 15.0s
2025-Dec-25 12:22:51.816679
2025-Dec-25 12:22:51.816679
#12 [dashboard deps 4/4] RUN npm install
2025-Dec-25 12:22:51.977525
#12 ...
2025-Dec-25 12:22:51.977525
2025-Dec-25 12:22:51.977525
#18 [api 5/5] COPY . .
2025-Dec-25 12:22:58.685376
#18 DONE 6.9s
2025-Dec-25 12:22:58.695805
#12 [dashboard deps 4/4] RUN npm install
2025-Dec-25 12:22:58.852735
#12 ...
2025-Dec-25 12:22:58.852735
2025-Dec-25 12:22:58.852735
#19 [api] exporting to image
2025-Dec-25 12:22:58.852735
#19 exporting layers
2025-Dec-25 12:22:59.195351
#19 ...
2025-Dec-25 12:22:59.203406
#12 [dashboard deps 4/4] RUN npm install
2025-Dec-25 12:22:59.203406
#12 29.97 npm notice
2025-Dec-25 12:22:59.203406
#12 29.97 npm notice New major version of npm available! 10.8.2 -> 11.7.0
2025-Dec-25 12:22:59.203406
#12 29.97 npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.7.0
2025-Dec-25 12:22:59.203406
#12 29.97 npm notice To update run: npm install -g npm@11.7.0
2025-Dec-25 12:22:59.203406
#12 29.97 npm notice
2025-Dec-25 12:22:59.203406
#12 29.97
2025-Dec-25 12:22:59.203406
#12 29.97 added 473 packages, and audited 474 packages in 30s
2025-Dec-25 12:22:59.203406
#12 29.97
2025-Dec-25 12:22:59.203406
#12 29.97 154 packages are looking for funding
2025-Dec-25 12:22:59.203406
#12 29.97   run `npm fund` for details
2025-Dec-25 12:22:59.203406
#12 29.97
2025-Dec-25 12:22:59.203406
#12 29.97 found 0 vulnerabilities
2025-Dec-25 12:22:59.203406
#12 DONE 30.3s
2025-Dec-25 12:22:59.364479
#19 [api] exporting to image
2025-Dec-25 12:23:03.823180
#19 ...
2025-Dec-25 12:23:03.823180
2025-Dec-25 12:23:03.823180
#20 [dashboard builder 3/5] COPY --from=deps /app/node_modules ./node_modules
2025-Dec-25 12:23:04.153297
#20 ...
2025-Dec-25 12:23:04.153297
2025-Dec-25 12:23:04.153297
#19 [api] exporting to image
2025-Dec-25 12:23:04.153297
#19 exporting layers 5.2s done
2025-Dec-25 12:23:04.153297
#19 writing image sha256:50ecaf08c2c6db21f9e9ada712fa4e3d1928952955b6f6bb57b6dcde870fabe5 done
2025-Dec-25 12:23:04.153297
#19 naming to docker.io/library/hck4w0k4ww8kk4gccw000ggg-api done
2025-Dec-25 12:23:04.153297
#19 DONE 5.2s
2025-Dec-25 12:23:04.153297
2025-Dec-25 12:23:04.153297
#21 [api] resolving provenance for metadata file
2025-Dec-25 12:23:04.153297
#21 DONE 0.0s
2025-Dec-25 12:23:04.303477
#20 [dashboard builder 3/5] COPY --from=deps /app/node_modules ./node_modules
2025-Dec-25 12:23:15.566918
#20 DONE 11.9s
2025-Dec-25 12:23:15.787632
#22 [dashboard builder 4/5] COPY . .
2025-Dec-25 12:23:15.787632
#22 DONE 0.1s
2025-Dec-25 12:23:15.787632
2025-Dec-25 12:23:15.787632
#23 [dashboard builder 5/5] RUN npm run build
2025-Dec-25 12:23:16.191369
#23 0.554
2025-Dec-25 12:23:16.191369
#23 0.554 > dashboard@0.1.0 build
2025-Dec-25 12:23:16.191369
#23 0.554 > next build
2025-Dec-25 12:23:16.202006
#23 0.554
2025-Dec-25 12:23:16.978788
#23 1.342 Attention: Next.js now collects completely anonymous telemetry regarding usage.
2025-Dec-25 12:23:17.140543
#23 1.343 This information is used to shape Next.js' roadmap and prioritize features.
2025-Dec-25 12:23:17.140543
#23 1.343 You can learn more, including how to opt-out if you'd not like to participate in this anonymous program, by visiting the following URL:
2025-Dec-25 12:23:17.140543
#23 1.343 https://nextjs.org/telemetry
2025-Dec-25 12:23:17.140543
#23 1.343
2025-Dec-25 12:23:17.140543
#23 1.356 ▲ Next.js 16.1.0 (Turbopack)
2025-Dec-25 12:23:17.140543
#23 1.357
2025-Dec-25 12:23:17.140543
#23 1.503   Creating an optimized production build ...
2025-Dec-25 12:23:34.094927
#23 18.46 ✓ Compiled successfully in 16.5s
2025-Dec-25 12:23:34.278865
#23 18.49   Running TypeScript ...
2025-Dec-25 12:23:43.346664
#23 27.71   Collecting page data using 1 worker ...
2025-Dec-25 12:23:43.941905
#23 28.31   Generating static pages using 1 worker (0/11) ...
2025-Dec-25 12:23:44.330945
#23 28.69   Generating static pages using 1 worker (2/11)
2025-Dec-25 12:23:44.562846
#23 28.69   Generating static pages using 1 worker (5/11)
2025-Dec-25 12:23:44.562846
#23 28.70   Generating static pages using 1 worker (8/11)
2025-Dec-25 12:23:44.562846
#23 28.76 ✓ Generating static pages using 1 worker (11/11) in 452.4ms
2025-Dec-25 12:23:44.562846
#23 28.76   Finalizing page optimization ...
2025-Dec-25 12:23:44.562846
#23 28.77
2025-Dec-25 12:23:44.562846
#23 28.77 Route (app)
2025-Dec-25 12:23:44.562846
#23 28.77 ┌ ○ /
2025-Dec-25 12:23:44.562846
#23 28.77 ├ ○ /_not-found
2025-Dec-25 12:23:44.562846
#23 28.77 ├ ○ /login
2025-Dec-25 12:23:44.562846
#23 28.77 ├ ○ /org
2025-Dec-25 12:23:44.562846
#23 28.77 ├ ƒ /org/[orgId]/billing
2025-Dec-25 12:23:44.562846
#23 28.77 ├ ƒ /org/[orgId]/projects
2025-Dec-25 12:23:44.562846
#23 28.77 ├ ƒ /org/[orgId]/projects/new
2025-Dec-25 12:23:44.562846
#23 28.77 ├ ƒ /org/[orgId]/settings
2025-Dec-25 12:23:44.562846
#23 28.77 ├ ƒ /org/[orgId]/team
2025-Dec-25 12:23:44.562846
#23 28.77 ├ ○ /projects
2025-Dec-25 12:23:44.562846
#23 28.77 ├ ƒ /projects/[id]
2025-Dec-25 12:23:44.562846
#23 28.77 ├ ƒ /projects/[id]/auth
2025-Dec-25 12:23:44.562846
#23 28.77 ├ ƒ /projects/[id]/backups
2025-Dec-25 12:23:44.562846
#23 28.77 ├ ƒ /projects/[id]/database
2025-Dec-25 12:23:44.562846
#23 28.77 ├ ƒ /projects/[id]/database/[table]
2025-Dec-25 12:23:44.562846
#23 28.77 ├ ƒ /projects/[id]/edge-functions
2025-Dec-25 12:23:44.562846
#23 28.77 ├ ƒ /projects/[id]/logs
2025-Dec-25 12:23:44.562846
#23 28.77 ├ ƒ /projects/[id]/realtime
2025-Dec-25 12:23:44.562846
#23 28.77 ├ ƒ /projects/[id]/secrets
2025-Dec-25 12:23:44.562846
#23 28.77 ├ ƒ /projects/[id]/settings
2025-Dec-25 12:23:44.562846
#23 28.77 ├ ƒ /projects/[id]/settings/deployment
2025-Dec-25 12:23:44.562846
#23 28.77 ├ ƒ /projects/[id]/sql
2025-Dec-25 12:23:44.562846
#23 28.77 ├ ƒ /projects/[id]/storage
2025-Dec-25 12:23:44.562846
#23 28.77 ├ ○ /projects/new
2025-Dec-25 12:23:44.562846
#23 28.77 ├ ○ /settings/organization
2025-Dec-25 12:23:44.562846
#23 28.77 ├ ƒ /settings/organization/[id]
2025-Dec-25 12:23:44.562846
#23 28.77 ├ ○ /settings/profile
2025-Dec-25 12:23:44.562846
#23 28.77 └ ○ /signup
2025-Dec-25 12:23:44.562846
#23 28.77
2025-Dec-25 12:23:44.562846
#23 28.77
2025-Dec-25 12:23:44.562846
#23 28.77 ○  (Static)   prerendered as static content
2025-Dec-25 12:23:44.562846
#23 28.77 ƒ  (Dynamic)  server-rendered on demand
2025-Dec-25 12:23:44.562846
#23 28.78
2025-Dec-25 12:23:44.614372
#23 28.98 npm notice
2025-Dec-25 12:23:44.614372
#23 28.98 npm notice New major version of npm available! 10.8.2 -> 11.7.0
2025-Dec-25 12:23:44.614372
#23 28.98 npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.7.0
2025-Dec-25 12:23:44.614372
#23 28.98 npm notice To update run: npm install -g npm@11.7.0
2025-Dec-25 12:23:44.614372
#23 28.98 npm notice
2025-Dec-25 12:23:44.822883
#23 DONE 29.0s
2025-Dec-25 12:23:50.894255
#24 [dashboard runner 3/6] COPY --from=builder /app/public ./public
2025-Dec-25 12:23:51.074189
#24 DONE 0.0s
2025-Dec-25 12:23:51.139547
#25 [dashboard runner 4/6] COPY --from=builder /app/.next ./.next
2025-Dec-25 12:23:51.323213
#25 DONE 0.2s
2025-Dec-25 12:23:51.475339
#26 [dashboard runner 5/6] COPY --from=builder /app/node_modules ./node_modules
2025-Dec-25 12:23:58.119892
#26 DONE 6.8s
2025-Dec-25 12:23:58.324421
#27 [dashboard runner 6/6] COPY --from=builder /app/package.json ./package.json
2025-Dec-25 12:23:58.331638
#27 DONE 0.0s
2025-Dec-25 12:23:58.331638
2025-Dec-25 12:23:58.331638
#28 [dashboard] exporting to image
2025-Dec-25 12:23:58.331638
#28 exporting layers
2025-Dec-25 12:24:11.302213
#28 exporting layers 13.1s done
2025-Dec-25 12:24:11.358342
#28 writing image sha256:3fd2c4aeae47694cdcd85dd8bace0da006fda7c1a1ec22360c2881792b487999 done
2025-Dec-25 12:24:11.358342
#28 naming to docker.io/library/hck4w0k4ww8kk4gccw000ggg-dashboard done
2025-Dec-25 12:24:11.358342
#28 DONE 13.1s
2025-Dec-25 12:24:11.358342
2025-Dec-25 12:24:11.358342
#29 [dashboard] resolving provenance for metadata file
2025-Dec-25 12:24:11.358342
#29 DONE 0.0s
2025-Dec-25 12:24:11.363863
api  Built
2025-Dec-25 12:24:11.363863
dashboard  Built
2025-Dec-25 12:24:11.400289
Creating .env file with runtime variables for build phase.
2025-Dec-25 12:24:12.177511
[CMD]: docker exec vs8wgsg00s8o04k08ccogkss bash -c 'cat /artifacts/vs8wgsg00s8o04k08ccogkss/.env'
2025-Dec-25 12:24:12.177511
SOURCE_COMMIT=651cc5f78dbb5286b263786e9c2134ad800200ea
2025-Dec-25 12:24:12.177511
COOLIFY_URL=
2025-Dec-25 12:24:12.177511
COOLIFY_FQDN=
2025-Dec-25 12:24:12.177511
SERVICE_URL_DASHBOARD=https://supalove.hayataxi.online
2025-Dec-25 12:24:12.177511
SERVICE_FQDN_DASHBOARD=supalove.hayataxi.online
2025-Dec-25 12:24:12.177511
SERVICE_URL_API=https://api.hayataxi.online
2025-Dec-25 12:24:12.177511
SERVICE_FQDN_API=api.hayataxi.online
2025-Dec-25 12:24:12.177511
SERVICE_URL_KEYCLOAK=https://auth.hayataxi.online
2025-Dec-25 12:24:12.177511
SERVICE_FQDN_KEYCLOAK=auth.hayataxi.online
2025-Dec-25 12:24:12.177511
SERVICE_URL_MINIO=https://s3.hayataxi.online
2025-Dec-25 12:24:12.177511
SERVICE_FQDN_MINIO=s3.hayataxi.online
2025-Dec-25 12:24:12.177511
SERVICE_NAME_CONTROL-PLANE-DB=control-plane-db
2025-Dec-25 12:24:12.177511
SERVICE_NAME_API=api
2025-Dec-25 12:24:12.177511
SERVICE_NAME_DASHBOARD=dashboard
2025-Dec-25 12:24:12.177511
SERVICE_NAME_KEYCLOAK=keycloak
2025-Dec-25 12:24:12.177511
SERVICE_NAME_MINIO=minio
2025-Dec-25 12:24:12.177511
POSTGRES_USER=platform
2025-Dec-25 12:24:12.177511
POSTGRES_PASSWORD=platform
2025-Dec-25 12:24:12.177511
POSTGRES_DB=control_plane
2025-Dec-25 12:24:12.177511
KEYCLOAK_ADMIN_USER=admin
2025-Dec-25 12:24:12.177511
KEYCLOAK_ADMIN_PASSWORD=admin
2025-Dec-25 12:24:12.177511
MINIO_ROOT_USER=minioadmin
2025-Dec-25 12:24:12.177511
MINIO_ROOT_PASSWORD=minioadmin
2025-Dec-25 12:24:12.177511
URL=http://localhost:8000
2025-Dec-25 12:24:12.177511
NEXT_PUBLIC_API_URL=https://api.hayataxi.online
2025-Dec-25 12:24:12.177511
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8000
2025-Dec-25 12:24:12.177511
HOST=0.0.0.0
2025-Dec-25 12:24:12.506316
Removing old containers.
2025-Dec-25 12:24:13.345215
[CMD]: docker stop --time=30 dashboard-hck4w0k4ww8kk4gccw000ggg-121038807692
2025-Dec-25 12:24:13.345215
dashboard-hck4w0k4ww8kk4gccw000ggg-121038807692
2025-Dec-25 12:24:13.681356
[CMD]: docker rm -f dashboard-hck4w0k4ww8kk4gccw000ggg-121038807692
2025-Dec-25 12:24:13.681356
dashboard-hck4w0k4ww8kk4gccw000ggg-121038807692
2025-Dec-25 12:24:14.015685
[CMD]: docker stop --time=30 api-hck4w0k4ww8kk4gccw000ggg-121038792576
2025-Dec-25 12:24:14.015685
api-hck4w0k4ww8kk4gccw000ggg-121038792576
2025-Dec-25 12:24:14.359160
[CMD]: docker rm -f api-hck4w0k4ww8kk4gccw000ggg-121038792576
2025-Dec-25 12:24:14.359160
api-hck4w0k4ww8kk4gccw000ggg-121038792576
2025-Dec-25 12:24:14.965652
[CMD]: docker stop --time=30 keycloak-hck4w0k4ww8kk4gccw000ggg-121038819478
2025-Dec-25 12:24:14.965652
keycloak-hck4w0k4ww8kk4gccw000ggg-121038819478
2025-Dec-25 12:24:15.417426
[CMD]: docker rm -f keycloak-hck4w0k4ww8kk4gccw000ggg-121038819478
2025-Dec-25 12:24:15.417426
keycloak-hck4w0k4ww8kk4gccw000ggg-121038819478
2025-Dec-25 12:24:15.863191
[CMD]: docker stop --time=30 minio-hck4w0k4ww8kk4gccw000ggg-121038833020
2025-Dec-25 12:24:15.863191
minio-hck4w0k4ww8kk4gccw000ggg-121038833020
2025-Dec-25 12:24:16.208416
[CMD]: docker rm -f minio-hck4w0k4ww8kk4gccw000ggg-121038833020
2025-Dec-25 12:24:16.208416
minio-hck4w0k4ww8kk4gccw000ggg-121038833020
2025-Dec-25 12:24:16.659331
[CMD]: docker stop --time=30 control-plane-db-hck4w0k4ww8kk4gccw000ggg-121038775825
2025-Dec-25 12:24:16.659331
control-plane-db-hck4w0k4ww8kk4gccw000ggg-121038775825
2025-Dec-25 12:24:17.000379
[CMD]: docker rm -f control-plane-db-hck4w0k4ww8kk4gccw000ggg-121038775825
2025-Dec-25 12:24:17.000379
control-plane-db-hck4w0k4ww8kk4gccw000ggg-121038775825
2025-Dec-25 12:24:17.009782
Starting new application.
2025-Dec-25 12:24:18.149709
[CMD]: docker exec vs8wgsg00s8o04k08ccogkss bash -c 'SOURCE_COMMIT=651cc5f78dbb5286b263786e9c2134ad800200ea COOLIFY_BRANCH=main COOLIFY_RESOURCE_UUID=hck4w0k4ww8kk4gccw000ggg COOLIFY_CONTAINER_NAME=hck4w0k4ww8kk4gccw000ggg-122201499845  docker compose --env-file /artifacts/vs8wgsg00s8o04k08ccogkss/.env --project-name hck4w0k4ww8kk4gccw000ggg --project-directory /artifacts/vs8wgsg00s8o04k08ccogkss -f /artifacts/vs8wgsg00s8o04k08ccogkss/docker-compose.coolify.yml up -d'
2025-Dec-25 12:24:18.149709
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-122223431671  Creating
2025-Dec-25 12:24:18.158066
Container minio-hck4w0k4ww8kk4gccw000ggg-122223486757  Creating
2025-Dec-25 12:24:18.202930
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-122223431671  Created
2025-Dec-25 12:24:18.212050
Container minio-hck4w0k4ww8kk4gccw000ggg-122223486757  Created
2025-Dec-25 12:24:18.212050
Container keycloak-hck4w0k4ww8kk4gccw000ggg-122223473415  Creating
2025-Dec-25 12:24:18.226518
Container keycloak-hck4w0k4ww8kk4gccw000ggg-122223473415  Created
2025-Dec-25 12:24:18.233366
Container api-hck4w0k4ww8kk4gccw000ggg-122223447780  Creating
2025-Dec-25 12:24:18.244566
Container api-hck4w0k4ww8kk4gccw000ggg-122223447780  Created
2025-Dec-25 12:24:18.250832
Container dashboard-hck4w0k4ww8kk4gccw000ggg-122223462028  Creating
2025-Dec-25 12:24:18.263574
Container dashboard-hck4w0k4ww8kk4gccw000ggg-122223462028  Created
2025-Dec-25 12:24:18.274308
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-122223431671  Starting
2025-Dec-25 12:24:18.274308
Container minio-hck4w0k4ww8kk4gccw000ggg-122223486757  Starting
2025-Dec-25 12:24:18.533454
Container minio-hck4w0k4ww8kk4gccw000ggg-122223486757  Started
2025-Dec-25 12:24:18.567089
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-122223431671  Started
2025-Dec-25 12:24:18.567089
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-122223431671  Waiting
2025-Dec-25 12:24:24.065540
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-122223431671  Healthy
2025-Dec-25 12:24:24.065540
Container keycloak-hck4w0k4ww8kk4gccw000ggg-122223473415  Starting
2025-Dec-25 12:24:24.279007
Container keycloak-hck4w0k4ww8kk4gccw000ggg-122223473415  Started
2025-Dec-25 12:24:24.279007
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-122223431671  Waiting
2025-Dec-25 12:24:24.785818
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-122223431671  Healthy
2025-Dec-25 12:24:24.785818
Container api-hck4w0k4ww8kk4gccw000ggg-122223447780  Starting
2025-Dec-25 12:24:25.118409
Container api-hck4w0k4ww8kk4gccw000ggg-122223447780  Started
2025-Dec-25 12:24:25.118409
Container dashboard-hck4w0k4ww8kk4gccw000ggg-122223462028  Starting
2025-Dec-25 12:24:25.493622
Container dashboard-hck4w0k4ww8kk4gccw000ggg-122223462028  Started
2025-Dec-25 12:24:27.570162
New container started.
2025-Dec-25 12:24:29.752747
Gracefully shutting down build container: vs8wgsg00s8o04k08ccogkss
2025-Dec-25 12:24:30.709768
[CMD]: docker stop --time=30 vs8wgsg00s8o04k08ccogkss
2025-Dec-25 12:24:30.709768
vs8wgsg00s8o04k08ccogkss
2025-Dec-25 12:24:31.423333
[CMD]: docker rm -f vs8wgsg00s8o04k08ccogkss
2025-Dec-25 12:24:31.423333
Error response from daemon: removal of container vs8wgsg00s8o04k08ccogkss is already in progress