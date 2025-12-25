Deployment is Finished.


2025-Dec-25 12:34:34.902693
Starting deployment of supalove to localhost.
2025-Dec-25 12:34:35.524912
Preparing container with helper image: ghcr.io/coollabsio/coolify-helper:1.0.12
2025-Dec-25 12:34:35.877067
[CMD]: docker stop --time=30 q880oo44woko4gwocowocs8o
2025-Dec-25 12:34:35.877067
Error response from daemon: No such container: q880oo44woko4gwocowocs8o
2025-Dec-25 12:34:36.201833
[CMD]: docker rm -f q880oo44woko4gwocowocs8o
2025-Dec-25 12:34:36.201833
Error response from daemon: No such container: q880oo44woko4gwocowocs8o
2025-Dec-25 12:34:36.569511
[CMD]: docker run -d --network coolify --name q880oo44woko4gwocowocs8o  --rm -v /var/run/docker.sock:/var/run/docker.sock ghcr.io/coollabsio/coolify-helper:1.0.12
2025-Dec-25 12:34:36.569511
062b85585302420a9455e6a8d5971204e97c4c5d6b3ca352139c6700e3cf8a44
2025-Dec-25 12:34:37.866103
[CMD]: docker exec q880oo44woko4gwocowocs8o bash -c 'GIT_SSH_COMMAND="ssh -o ConnectTimeout=30 -p 22 -o Port=22 -o LogLevel=ERROR -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" git ls-remote https://github.com/farisnoaman/supalove refs/heads/main'
2025-Dec-25 12:34:37.866103
1947c1453bf49e0b50d7c166605c9143f285c782	refs/heads/main
2025-Dec-25 12:34:37.884211
----------------------------------------
2025-Dec-25 12:34:37.891652
Importing farisnoaman/supalove:main (commit sha 1947c1453bf49e0b50d7c166605c9143f285c782) to /artifacts/q880oo44woko4gwocowocs8o.
2025-Dec-25 12:34:38.276107
[CMD]: docker exec q880oo44woko4gwocowocs8o bash -c 'git clone --depth=1 --recurse-submodules --shallow-submodules -b 'main' 'https://github.com/farisnoaman/supalove' '/artifacts/q880oo44woko4gwocowocs8o' && cd '/artifacts/q880oo44woko4gwocowocs8o' && if [ -f .gitmodules ]; then sed -i "s#git@\(.*\):#https://\1/#g" '/artifacts/q880oo44woko4gwocowocs8o'/.gitmodules || true && git submodule sync && GIT_SSH_COMMAND="ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" git submodule update --init --recursive --depth=1; fi && cd '/artifacts/q880oo44woko4gwocowocs8o' && GIT_SSH_COMMAND="ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" git lfs pull'
2025-Dec-25 12:34:38.276107
Cloning into '/artifacts/q880oo44woko4gwocowocs8o'...
2025-Dec-25 12:34:44.552223
Updating files:  24% (3717/15084)
2025-Dec-25 12:34:44.564111
Updating files:  25% (3771/15084)
2025-Dec-25 12:34:44.594285
Updating files:  26% (3922/15084)
2025-Dec-25 12:34:44.655932
Updating files:  27% (4073/15084)
2025-Dec-25 12:34:44.687779
Updating files:  28% (4224/15084)
2025-Dec-25 12:34:44.711242
Updating files:  29% (4375/15084)
2025-Dec-25 12:34:44.732638
Updating files:  30% (4526/15084)
2025-Dec-25 12:34:44.747651
Updating files:  31% (4677/15084)
2025-Dec-25 12:34:44.763497
Updating files:  32% (4827/15084)
2025-Dec-25 12:34:44.780490
Updating files:  33% (4978/15084)
2025-Dec-25 12:34:44.825976
Updating files:  34% (5129/15084)
2025-Dec-25 12:34:44.864687
Updating files:  35% (5280/15084)
2025-Dec-25 12:34:44.919775
Updating files:  36% (5431/15084)
2025-Dec-25 12:34:44.959845
Updating files:  37% (5582/15084)
2025-Dec-25 12:34:44.981972
Updating files:  38% (5732/15084)
2025-Dec-25 12:34:45.001187
Updating files:  39% (5883/15084)
2025-Dec-25 12:34:45.029230
Updating files:  40% (6034/15084)
2025-Dec-25 12:34:45.047749
Updating files:  41% (6185/15084)
2025-Dec-25 12:34:45.065789
Updating files:  42% (6336/15084)
2025-Dec-25 12:34:45.078040
Updating files:  43% (6487/15084)
2025-Dec-25 12:34:45.089641
Updating files:  44% (6637/15084)
2025-Dec-25 12:34:45.101161
Updating files:  45% (6788/15084)
2025-Dec-25 12:34:45.115514
Updating files:  46% (6939/15084)
2025-Dec-25 12:34:45.127620
Updating files:  47% (7090/15084)
2025-Dec-25 12:34:45.139444
Updating files:  48% (7241/15084)
2025-Dec-25 12:34:45.150586
Updating files:  49% (7392/15084)
2025-Dec-25 12:34:45.161025
Updating files:  50% (7542/15084)
2025-Dec-25 12:34:45.171644
Updating files:  51% (7693/15084)
2025-Dec-25 12:34:45.185284
Updating files:  52% (7844/15084)
2025-Dec-25 12:34:45.198675
Updating files:  53% (7995/15084)
2025-Dec-25 12:34:45.214204
Updating files:  54% (8146/15084)
2025-Dec-25 12:34:45.295711
Updating files:  55% (8297/15084)
2025-Dec-25 12:34:45.333747
Updating files:  56% (8448/15084)
2025-Dec-25 12:34:45.344428
Updating files:  57% (8598/15084)
2025-Dec-25 12:34:45.357333
Updating files:  58% (8749/15084)
2025-Dec-25 12:34:45.378026
Updating files:  59% (8900/15084)
2025-Dec-25 12:34:45.391709
Updating files:  60% (9051/15084)
2025-Dec-25 12:34:45.408392
Updating files:  61% (9202/15084)
2025-Dec-25 12:34:45.424473
Updating files:  62% (9353/15084)
2025-Dec-25 12:34:45.437348
Updating files:  63% (9503/15084)
2025-Dec-25 12:34:45.451148
Updating files:  64% (9654/15084)
2025-Dec-25 12:34:45.526487
Updating files:  65% (9805/15084)
2025-Dec-25 12:34:45.537478
Updating files:  66% (9956/15084)
2025-Dec-25 12:34:45.551808
Updating files:  66% (10104/15084)
2025-Dec-25 12:34:45.554640
Updating files:  67% (10107/15084)
2025-Dec-25 12:34:45.570554
Updating files:  68% (10258/15084)
2025-Dec-25 12:34:45.590568
Updating files:  69% (10408/15084)
2025-Dec-25 12:34:45.607012
Updating files:  70% (10559/15084)
2025-Dec-25 12:34:45.621209
Updating files:  71% (10710/15084)
2025-Dec-25 12:34:45.636888
Updating files:  72% (10861/15084)
2025-Dec-25 12:34:45.650491
Updating files:  73% (11012/15084)
2025-Dec-25 12:34:45.661836
Updating files:  74% (11163/15084)
2025-Dec-25 12:34:45.676697
Updating files:  75% (11313/15084)
2025-Dec-25 12:34:45.695640
Updating files:  76% (11464/15084)
2025-Dec-25 12:34:45.712886
Updating files:  77% (11615/15084)
2025-Dec-25 12:34:45.726461
Updating files:  78% (11766/15084)
2025-Dec-25 12:34:45.738530
Updating files:  79% (11917/15084)
2025-Dec-25 12:34:45.802657
Updating files:  80% (12068/15084)
2025-Dec-25 12:34:45.815967
Updating files:  81% (12219/15084)
2025-Dec-25 12:34:45.856403
Updating files:  82% (12369/15084)
2025-Dec-25 12:34:45.867163
Updating files:  83% (12520/15084)
2025-Dec-25 12:34:45.885562
Updating files:  84% (12671/15084)
2025-Dec-25 12:34:45.902445
Updating files:  85% (12822/15084)
2025-Dec-25 12:34:45.925814
Updating files:  86% (12973/15084)
2025-Dec-25 12:34:45.942633
Updating files:  87% (13124/15084)
2025-Dec-25 12:34:46.009662
Updating files:  88% (13274/15084)
2025-Dec-25 12:34:46.032807
Updating files:  89% (13425/15084)
2025-Dec-25 12:34:46.058300
Updating files:  90% (13576/15084)
2025-Dec-25 12:34:46.082673
Updating files:  91% (13727/15084)
2025-Dec-25 12:34:46.095866
Updating files:  92% (13878/15084)
2025-Dec-25 12:34:46.107914
Updating files:  93% (14029/15084)
2025-Dec-25 12:34:46.199700
Updating files:  94% (14179/15084)
2025-Dec-25 12:34:46.229342
Updating files:  95% (14330/15084)
2025-Dec-25 12:34:46.251694
Updating files:  96% (14481/15084)
2025-Dec-25 12:34:46.273508
Updating files:  97% (14632/15084)
2025-Dec-25 12:34:46.288617
Updating files:  98% (14783/15084)
2025-Dec-25 12:34:46.310324
Updating files:  99% (14934/15084)
2025-Dec-25 12:34:46.324975
Updating files: 100% (15084/15084)
Updating files: 100% (15084/15084), done.
2025-Dec-25 12:34:47.581215
[CMD]: docker exec q880oo44woko4gwocowocs8o bash -c 'cd /artifacts/q880oo44woko4gwocowocs8o && git log -1 1947c1453bf49e0b50d7c166605c9143f285c782 --pretty=%B'
2025-Dec-25 12:34:47.581215
Push the latest fix to GitHub:
2025-Dec-25 12:34:47.581215
bash
2025-Dec-25 12:34:47.581215
cd /home/faris/Documents/MyApps/supalove
2025-Dec-25 12:34:47.581215
git add -A
2025-Dec-25 12:34:47.581215
git commit -m "fix: Add src directory to sys.path to resolve ModuleNotFoundError
2025-Dec-25 12:34:55.508299
[CMD]: docker exec q880oo44woko4gwocowocs8o bash -c 'test -f /artifacts/q880oo44woko4gwocowocs8o/control-plane/api/Dockerfile && echo 'exists' || echo 'not found''
2025-Dec-25 12:34:55.508299
exists
2025-Dec-25 12:34:56.191556
[CMD]: docker exec q880oo44woko4gwocowocs8o bash -c 'cat /artifacts/q880oo44woko4gwocowocs8o/control-plane/api/Dockerfile'
2025-Dec-25 12:34:56.191556
FROM python:3.12-slim
2025-Dec-25 12:34:56.191556
WORKDIR /app
2025-Dec-25 12:34:56.191556
COPY requirements.txt .
2025-Dec-25 12:34:56.191556
RUN pip install -r requirements.txt
2025-Dec-25 12:34:56.191556
COPY . .
2025-Dec-25 12:34:56.191556
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
2025-Dec-25 12:34:56.685737
Added 21 ARG declarations to Dockerfile for service api.
2025-Dec-25 12:34:57.051455
[CMD]: docker exec q880oo44woko4gwocowocs8o bash -c 'test -f /artifacts/q880oo44woko4gwocowocs8o/dashboard/Dockerfile && echo 'exists' || echo 'not found''
2025-Dec-25 12:34:57.051455
exists
2025-Dec-25 12:34:57.431811
[CMD]: docker exec q880oo44woko4gwocowocs8o bash -c 'cat /artifacts/q880oo44woko4gwocowocs8o/dashboard/Dockerfile'
2025-Dec-25 12:34:57.431811
# Stage 1: Dependencies
2025-Dec-25 12:34:57.431811
FROM node:20-alpine AS deps
2025-Dec-25 12:34:57.431811
WORKDIR /app
2025-Dec-25 12:34:57.431811
COPY package*.json ./
2025-Dec-25 12:34:57.431811
RUN npm install
2025-Dec-25 12:34:57.431811
2025-Dec-25 12:34:57.431811
# Stage 2: Builder
2025-Dec-25 12:34:57.431811
FROM node:20-alpine AS builder
2025-Dec-25 12:34:57.431811
WORKDIR /app
2025-Dec-25 12:34:57.431811
COPY --from=deps /app/node_modules ./node_modules
2025-Dec-25 12:34:57.431811
COPY . .
2025-Dec-25 12:34:57.431811
# Set environment variables for build if needed (e.g. backend URL)
2025-Dec-25 12:34:57.431811
# For Next.js client-side fetch, it might need to know the URL at build time if pre-rendering,
2025-Dec-25 12:34:57.431811
# but we are using "use client" so it's fine.
2025-Dec-25 12:34:57.431811
ARG NEXT_PUBLIC_API_URL
2025-Dec-25 12:34:57.431811
ENV NEXT_PUBLIC_API_URL=${NEXT_PUBLIC_API_URL}
2025-Dec-25 12:34:57.431811
RUN npm run build
2025-Dec-25 12:34:57.431811
2025-Dec-25 12:34:57.431811
# Stage 3: Runner
2025-Dec-25 12:34:57.431811
FROM node:20-alpine AS runner
2025-Dec-25 12:34:57.431811
WORKDIR /app
2025-Dec-25 12:34:57.431811
ENV NODE_ENV=production
2025-Dec-25 12:34:57.431811
COPY --from=builder /app/public ./public
2025-Dec-25 12:34:57.431811
COPY --from=builder /app/.next ./.next
2025-Dec-25 12:34:57.431811
COPY --from=builder /app/node_modules ./node_modules
2025-Dec-25 12:34:57.431811
COPY --from=builder /app/package.json ./package.json
2025-Dec-25 12:34:57.431811
2025-Dec-25 12:34:57.431811
EXPOSE 3000
2025-Dec-25 12:34:57.431811
CMD ["npm", "start"]
2025-Dec-25 12:34:57.832347
Added 63 ARG declarations to Dockerfile for service dashboard (multi-stage build, added to 3 stages).
2025-Dec-25 12:34:57.842654
Pulling & building required images.
2025-Dec-25 12:34:57.882278
Creating build-time .env file in /artifacts (outside Docker context).
2025-Dec-25 12:34:58.646536
[CMD]: docker exec q880oo44woko4gwocowocs8o bash -c 'cat /artifacts/build-time.env'
2025-Dec-25 12:34:58.646536
SOURCE_COMMIT='1947c1453bf49e0b50d7c166605c9143f285c782'
2025-Dec-25 12:34:58.646536
COOLIFY_URL=''
2025-Dec-25 12:34:58.646536
COOLIFY_FQDN=''
2025-Dec-25 12:34:58.646536
SERVICE_NAME_CONTROL-PLANE-DB='control-plane-db'
2025-Dec-25 12:34:58.646536
SERVICE_NAME_API='api'
2025-Dec-25 12:34:58.646536
SERVICE_NAME_DASHBOARD='dashboard'
2025-Dec-25 12:34:58.646536
SERVICE_NAME_KEYCLOAK='keycloak'
2025-Dec-25 12:34:58.646536
SERVICE_NAME_MINIO='minio'
2025-Dec-25 12:34:58.646536
SERVICE_URL_DASHBOARD='https://supalove.hayataxi.online'
2025-Dec-25 12:34:58.646536
SERVICE_FQDN_DASHBOARD='supalove.hayataxi.online'
2025-Dec-25 12:34:58.646536
SERVICE_URL_API='https://api.hayataxi.online'
2025-Dec-25 12:34:58.646536
SERVICE_FQDN_API='api.hayataxi.online'
2025-Dec-25 12:34:58.646536
SERVICE_URL_KEYCLOAK='https://auth.hayataxi.online'
2025-Dec-25 12:34:58.646536
SERVICE_FQDN_KEYCLOAK='auth.hayataxi.online'
2025-Dec-25 12:34:58.646536
SERVICE_URL_MINIO='https://s3.hayataxi.online'
2025-Dec-25 12:34:58.646536
SERVICE_FQDN_MINIO='s3.hayataxi.online'
2025-Dec-25 12:34:58.646536
ALLOWED_ORIGINS="http://localhost:3000,http://localhost:8000"
2025-Dec-25 12:34:58.646536
KEYCLOAK_ADMIN_PASSWORD="admin"
2025-Dec-25 12:34:58.646536
KEYCLOAK_ADMIN_USER="admin"
2025-Dec-25 12:34:58.646536
MINIO_ROOT_PASSWORD="minioadmin"
2025-Dec-25 12:34:58.646536
MINIO_ROOT_USER="minioadmin"
2025-Dec-25 12:34:58.646536
NEXT_PUBLIC_API_URL="https://api.hayataxi.online"
2025-Dec-25 12:34:58.646536
POSTGRES_DB="control_plane"
2025-Dec-25 12:34:58.646536
POSTGRES_PASSWORD="platform"
2025-Dec-25 12:34:58.646536
POSTGRES_USER="platform"
2025-Dec-25 12:34:58.646536
URL="http://localhost:8000"
2025-Dec-25 12:34:58.657196
Adding build arguments to Docker Compose build command.
2025-Dec-25 12:34:59.280433
[CMD]: docker exec q880oo44woko4gwocowocs8o bash -c 'SOURCE_COMMIT=1947c1453bf49e0b50d7c166605c9143f285c782 COOLIFY_BRANCH=main COOLIFY_RESOURCE_UUID=hck4w0k4ww8kk4gccw000ggg COOLIFY_CONTAINER_NAME=hck4w0k4ww8kk4gccw000ggg-123433651920  docker compose --env-file /artifacts/build-time.env --project-name hck4w0k4ww8kk4gccw000ggg --project-directory /artifacts/q880oo44woko4gwocowocs8o -f /artifacts/q880oo44woko4gwocowocs8o/docker-compose.coolify.yml build --pull --no-cache --build-arg SOURCE_COMMIT --build-arg COOLIFY_URL --build-arg COOLIFY_FQDN --build-arg SERVICE_FQDN_API --build-arg SERVICE_FQDN_DASHBOARD --build-arg SERVICE_FQDN_KEYCLOAK --build-arg SERVICE_FQDN_MINIO --build-arg SERVICE_URL_API --build-arg SERVICE_URL_DASHBOARD --build-arg SERVICE_URL_KEYCLOAK --build-arg SERVICE_URL_MINIO --build-arg ALLOWED_ORIGINS --build-arg KEYCLOAK_ADMIN_PASSWORD --build-arg KEYCLOAK_ADMIN_USER --build-arg MINIO_ROOT_PASSWORD --build-arg MINIO_ROOT_USER --build-arg NEXT_PUBLIC_API_URL --build-arg POSTGRES_DB --build-arg POSTGRES_PASSWORD --build-arg POSTGRES_USER --build-arg URL --build-arg COOLIFY_BUILD_SECRETS_HASH=3fa5667484bcc6d33cd9599abbd396bfba440d37232e41ff4e35e72c8abb7ffa'
2025-Dec-25 12:34:59.280433
#1 [internal] load local bake definitions
2025-Dec-25 12:34:59.387588
#1 reading from stdin 3.22kB done
2025-Dec-25 12:34:59.395429
#1 DONE 0.0s
2025-Dec-25 12:34:59.395429
2025-Dec-25 12:34:59.395429
#2 [dashboard internal] load build definition from Dockerfile
2025-Dec-25 12:34:59.395429
#2 transferring dockerfile: 2.20kB done
2025-Dec-25 12:34:59.395429
#2 DONE 0.0s
2025-Dec-25 12:34:59.395429
2025-Dec-25 12:34:59.395429
#3 [api internal] load build definition from Dockerfile
2025-Dec-25 12:34:59.395429
#3 transferring dockerfile: 658B done
2025-Dec-25 12:34:59.395429
#3 DONE 0.0s
2025-Dec-25 12:34:59.546230
#4 [dashboard internal] load metadata for docker.io/library/node:20-alpine
2025-Dec-25 12:35:00.036398
#4 ...
2025-Dec-25 12:35:00.041414
#5 [api internal] load metadata for docker.io/library/python:3.12-slim
2025-Dec-25 12:35:00.041414
#5 DONE 0.6s
2025-Dec-25 12:35:00.149683
#6 [api internal] load .dockerignore
2025-Dec-25 12:35:00.149683
#6 transferring context: 2B done
2025-Dec-25 12:35:00.149683
#6 DONE 0.0s
2025-Dec-25 12:35:00.149683
2025-Dec-25 12:35:00.149683
#7 [api 1/5] FROM docker.io/library/python:3.12-slim@sha256:fa48eefe2146644c2308b909d6bb7651a768178f84fc9550dcd495e4d6d84d01
2025-Dec-25 12:35:00.149683
#7 DONE 0.0s
2025-Dec-25 12:35:00.149683
2025-Dec-25 12:35:00.149683
#8 [api 2/5] WORKDIR /app
2025-Dec-25 12:35:00.149683
#8 CACHED
2025-Dec-25 12:35:00.149683
2025-Dec-25 12:35:00.149683
#4 [dashboard internal] load metadata for docker.io/library/node:20-alpine
2025-Dec-25 12:35:00.149683
#4 DONE 0.7s
2025-Dec-25 12:35:00.149683
2025-Dec-25 12:35:00.149683
#9 [dashboard internal] load .dockerignore
2025-Dec-25 12:35:00.255292
#9 transferring context: 2B done
2025-Dec-25 12:35:00.255292
#9 DONE 0.0s
2025-Dec-25 12:35:00.255292
2025-Dec-25 12:35:00.255292
#10 [dashboard deps 1/4] FROM docker.io/library/node:20-alpine@sha256:658d0f63e501824d6c23e06d4bb95c71e7d704537c9d9272f488ac03a370d448
2025-Dec-25 12:35:00.255292
#10 DONE 0.0s
2025-Dec-25 12:35:00.255292
2025-Dec-25 12:35:00.255292
#11 [dashboard deps 2/4] WORKDIR /app
2025-Dec-25 12:35:00.255292
#11 CACHED
2025-Dec-25 12:35:00.255292
2025-Dec-25 12:35:00.255292
#12 [dashboard internal] load build context
2025-Dec-25 12:35:00.255292
#12 transferring context: 837.69kB 0.1s done
2025-Dec-25 12:35:00.383580
#12 DONE 0.1s
2025-Dec-25 12:35:00.383580
2025-Dec-25 12:35:00.383580
#13 [dashboard deps 3/4] COPY package*.json ./
2025-Dec-25 12:35:00.383580
#13 DONE 0.1s
2025-Dec-25 12:35:00.383580
2025-Dec-25 12:35:00.383580
#14 [dashboard deps 4/4] RUN npm install
2025-Dec-25 12:35:05.479830
#14 ...
2025-Dec-25 12:35:05.479830
2025-Dec-25 12:35:05.479830
#15 [api internal] load build context
2025-Dec-25 12:35:05.479830
#15 transferring context: 116.17MB 5.4s
2025-Dec-25 12:35:10.421726
#15 transferring context: 330.52MB 10.3s done
2025-Dec-25 12:35:10.637958
#15 DONE 10.4s
2025-Dec-25 12:35:10.637958
2025-Dec-25 12:35:10.637958
#16 [api 3/5] COPY requirements.txt .
2025-Dec-25 12:35:10.852126
#16 DONE 0.4s
2025-Dec-25 12:35:10.852126
2025-Dec-25 12:35:10.852126
#14 [dashboard deps 4/4] RUN npm install
2025-Dec-25 12:35:11.010759
#14 ...
2025-Dec-25 12:35:11.010759
2025-Dec-25 12:35:11.010759
#17 [api 4/5] RUN pip install -r requirements.txt
2025-Dec-25 12:35:13.923737
#17 3.069 Collecting fastapi (from -r requirements.txt (line 1))
2025-Dec-25 12:35:14.099864
#17 3.093   Downloading fastapi-0.127.0-py3-none-any.whl.metadata (30 kB)
2025-Dec-25 12:35:14.180097
#17 3.325 Collecting sqlalchemy (from -r requirements.txt (line 3))
2025-Dec-25 12:35:14.320286
#17 3.331   Downloading sqlalchemy-2.0.45-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (9.5 kB)
2025-Dec-25 12:35:14.320286
#17 3.462 Collecting psycopg2-binary (from -r requirements.txt (line 4))
2025-Dec-25 12:35:14.453881
#17 3.469   Downloading psycopg2_binary-2.9.11-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (4.9 kB)
2025-Dec-25 12:35:14.453881
#17 3.521 Collecting httpx (from -r requirements.txt (line 5))
2025-Dec-25 12:35:14.453881
#17 3.527   Downloading httpx-0.28.1-py3-none-any.whl.metadata (7.1 kB)
2025-Dec-25 12:35:14.453881
#17 3.596 Collecting python-keycloak (from -r requirements.txt (line 6))
2025-Dec-25 12:35:14.578705
#17 3.604   Downloading python_keycloak-5.8.1-py3-none-any.whl.metadata (6.0 kB)
2025-Dec-25 12:35:14.578705
#17 3.660 Collecting minio (from -r requirements.txt (line 7))
2025-Dec-25 12:35:14.578705
#17 3.666   Downloading minio-7.2.20-py3-none-any.whl.metadata (6.5 kB)
2025-Dec-25 12:35:14.578705
#17 3.723 Collecting requests (from -r requirements.txt (line 8))
2025-Dec-25 12:35:14.693759
#17 3.735   Downloading requests-2.32.5-py3-none-any.whl.metadata (4.9 kB)
2025-Dec-25 12:35:14.699711
#17 3.791 Collecting python-dotenv (from -r requirements.txt (line 9))
2025-Dec-25 12:35:14.699711
#17 3.798   Downloading python_dotenv-1.2.1-py3-none-any.whl.metadata (25 kB)
2025-Dec-25 12:35:14.699711
#17 3.839 Collecting uvicorn[standard] (from -r requirements.txt (line 2))
2025-Dec-25 12:35:14.800777
#17 3.842   Downloading uvicorn-0.40.0-py3-none-any.whl.metadata (6.7 kB)
2025-Dec-25 12:35:14.800777
#17 3.866 Collecting passlib[bcrypt] (from -r requirements.txt (line 10))
2025-Dec-25 12:35:14.800777
#17 3.868   Downloading passlib-1.7.4-py2.py3-none-any.whl.metadata (1.7 kB)
2025-Dec-25 12:35:14.800777
#17 3.895 Collecting python-jose[cryptography] (from -r requirements.txt (line 11))
2025-Dec-25 12:35:14.800777
#17 3.902   Downloading python_jose-3.5.0-py2.py3-none-any.whl.metadata (5.5 kB)
2025-Dec-25 12:35:14.800777
#17 3.945 Collecting starlette<0.51.0,>=0.40.0 (from fastapi->-r requirements.txt (line 1))
2025-Dec-25 12:35:14.912919
#17 3.954   Downloading starlette-0.50.0-py3-none-any.whl.metadata (6.3 kB)
2025-Dec-25 12:35:14.912919
#17 4.058 Collecting pydantic>=2.7.0 (from fastapi->-r requirements.txt (line 1))
2025-Dec-25 12:35:15.014095
#17 4.065   Downloading pydantic-2.12.5-py3-none-any.whl.metadata (90 kB)
2025-Dec-25 12:35:15.014095
#17 4.100 Collecting typing-extensions>=4.8.0 (from fastapi->-r requirements.txt (line 1))
2025-Dec-25 12:35:15.014095
#17 4.102   Downloading typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
2025-Dec-25 12:35:15.014095
#17 4.118 Collecting annotated-doc>=0.0.2 (from fastapi->-r requirements.txt (line 1))
2025-Dec-25 12:35:15.014095
#17 4.122   Downloading annotated_doc-0.0.4-py3-none-any.whl.metadata (6.6 kB)
2025-Dec-25 12:35:15.014095
#17 4.159 Collecting click>=7.0 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 12:35:15.117683
#17 4.165   Downloading click-8.3.1-py3-none-any.whl.metadata (2.6 kB)
2025-Dec-25 12:35:15.117683
#17 4.188 Collecting h11>=0.8 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 12:35:15.117683
#17 4.192   Downloading h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
2025-Dec-25 12:35:15.117683
#17 4.263 Collecting httptools>=0.6.3 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 12:35:15.264541
#17 4.269   Downloading httptools-0.7.1-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (3.5 kB)
2025-Dec-25 12:35:15.264541
#17 4.338 Collecting pyyaml>=5.1 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 12:35:15.264541
#17 4.343   Downloading pyyaml-6.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.4 kB)
2025-Dec-25 12:35:15.264541
#17 4.405 Collecting uvloop>=0.15.1 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 12:35:15.434810
#17 4.413   Downloading uvloop-0.22.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (4.9 kB)
2025-Dec-25 12:35:15.434810
#17 4.496 Collecting watchfiles>=0.13 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 12:35:15.434810
#17 4.501   Downloading watchfiles-1.1.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.9 kB)
2025-Dec-25 12:35:15.434810
#17 4.579 Collecting websockets>=10.4 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 12:35:15.598247
#17 4.592   Downloading websockets-15.0.1-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.8 kB)
2025-Dec-25 12:35:15.614509
#17 4.759 Collecting greenlet>=1 (from sqlalchemy->-r requirements.txt (line 3))
2025-Dec-25 12:35:15.787582
#17 4.768   Downloading greenlet-3.3.0-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (4.1 kB)
2025-Dec-25 12:35:15.787582
#17 4.814 Collecting anyio (from httpx->-r requirements.txt (line 5))
2025-Dec-25 12:35:15.787582
#17 4.818   Downloading anyio-4.12.0-py3-none-any.whl.metadata (4.3 kB)
2025-Dec-25 12:35:15.787582
#17 4.840 Collecting certifi (from httpx->-r requirements.txt (line 5))
2025-Dec-25 12:35:15.787582
#17 4.846   Downloading certifi-2025.11.12-py3-none-any.whl.metadata (2.5 kB)
2025-Dec-25 12:35:15.787582
#17 4.928 Collecting httpcore==1.* (from httpx->-r requirements.txt (line 5))
2025-Dec-25 12:35:15.905928
#17 4.936   Downloading httpcore-1.0.9-py3-none-any.whl.metadata (21 kB)
2025-Dec-25 12:35:15.905928
#17 4.974 Collecting idna (from httpx->-r requirements.txt (line 5))
2025-Dec-25 12:35:15.905928
#17 4.980   Downloading idna-3.11-py3-none-any.whl.metadata (8.4 kB)
2025-Dec-25 12:35:15.905928
#17 5.023 Collecting aiofiles>=24.1.0 (from python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 12:35:15.905928
#17 5.027   Downloading aiofiles-25.1.0-py3-none-any.whl.metadata (6.3 kB)
2025-Dec-25 12:35:15.905928
#17 5.050 Collecting async-property>=0.2.2 (from python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 12:35:16.034568
#17 5.060   Downloading async_property-0.2.2-py2.py3-none-any.whl.metadata (5.3 kB)
2025-Dec-25 12:35:16.034568
#17 5.090 Collecting deprecation>=2.1.0 (from python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 12:35:16.034568
#17 5.095   Downloading deprecation-2.1.0-py2.py3-none-any.whl.metadata (4.6 kB)
2025-Dec-25 12:35:16.034568
#17 5.127 Collecting jwcrypto>=1.5.4 (from python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 12:35:16.034568
#17 5.137   Downloading jwcrypto-1.5.6-py3-none-any.whl.metadata (3.1 kB)
2025-Dec-25 12:35:16.034568
#17 5.179 Collecting requests-toolbelt>=0.6.0 (from python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 12:35:16.180299
#17 5.187   Downloading requests_toolbelt-1.0.0-py2.py3-none-any.whl.metadata (14 kB)
2025-Dec-25 12:35:16.190675
#17 5.230 Collecting argon2-cffi (from minio->-r requirements.txt (line 7))
2025-Dec-25 12:35:16.190675
#17 5.240   Downloading argon2_cffi-25.1.0-py3-none-any.whl.metadata (4.1 kB)
2025-Dec-25 12:35:16.190675
#17 5.323 Collecting pycryptodome (from minio->-r requirements.txt (line 7))
2025-Dec-25 12:35:16.341056
#17 5.330   Downloading pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (3.4 kB)
2025-Dec-25 12:35:16.341056
#17 5.398 Collecting urllib3 (from minio->-r requirements.txt (line 7))
2025-Dec-25 12:35:16.341056
#17 5.402   Downloading urllib3-2.6.2-py3-none-any.whl.metadata (6.6 kB)
2025-Dec-25 12:35:16.341056
#17 5.486 Collecting charset_normalizer<4,>=2 (from requests->-r requirements.txt (line 8))
2025-Dec-25 12:35:16.479717
#17 5.493   Downloading charset_normalizer-3.4.4-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (37 kB)
2025-Dec-25 12:35:16.479717
#17 5.624 Collecting bcrypt>=3.1.0 (from passlib[bcrypt]->-r requirements.txt (line 10))
2025-Dec-25 12:35:16.581446
#17 5.628   Downloading bcrypt-5.0.0-cp39-abi3-manylinux_2_34_x86_64.whl.metadata (10 kB)
2025-Dec-25 12:35:16.581446
#17 5.667 Collecting ecdsa!=0.15 (from python-jose[cryptography]->-r requirements.txt (line 11))
2025-Dec-25 12:35:16.581446
#17 5.677   Downloading ecdsa-0.19.1-py2.py3-none-any.whl.metadata (29 kB)
2025-Dec-25 12:35:16.581446
#17 5.718 Collecting rsa!=4.1.1,!=4.4,<5.0,>=4.0 (from python-jose[cryptography]->-r requirements.txt (line 11))
2025-Dec-25 12:35:16.581446
#17 5.726   Downloading rsa-4.9.1-py3-none-any.whl.metadata (5.6 kB)
2025-Dec-25 12:35:16.791638
#17 5.778 Collecting pyasn1>=0.5.0 (from python-jose[cryptography]->-r requirements.txt (line 11))
2025-Dec-25 12:35:16.791638
#17 5.783   Downloading pyasn1-0.6.1-py3-none-any.whl.metadata (8.4 kB)
2025-Dec-25 12:35:16.889508
#17 6.035 Collecting cryptography>=3.4.0 (from python-jose[cryptography]->-r requirements.txt (line 11))
2025-Dec-25 12:35:16.991240
#17 6.041   Downloading cryptography-46.0.3-cp311-abi3-manylinux_2_34_x86_64.whl.metadata (5.7 kB)
2025-Dec-25 12:35:16.991240
#17 6.135 Collecting cffi>=2.0.0 (from cryptography>=3.4.0->python-jose[cryptography]->-r requirements.txt (line 11))
2025-Dec-25 12:35:17.118965
#17 6.143   Downloading cffi-2.0.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (2.6 kB)
2025-Dec-25 12:35:17.118965
#17 6.172 Collecting packaging (from deprecation>=2.1.0->python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 12:35:17.118965
#17 6.177   Downloading packaging-25.0-py3-none-any.whl.metadata (3.3 kB)
2025-Dec-25 12:35:17.118965
#17 6.209 Collecting six>=1.9.0 (from ecdsa!=0.15->python-jose[cryptography]->-r requirements.txt (line 11))
2025-Dec-25 12:35:17.118965
#17 6.219   Downloading six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
2025-Dec-25 12:35:17.118965
#17 6.262 Collecting annotated-types>=0.6.0 (from pydantic>=2.7.0->fastapi->-r requirements.txt (line 1))
2025-Dec-25 12:35:17.276610
#17 6.269   Downloading annotated_types-0.7.0-py3-none-any.whl.metadata (15 kB)
2025-Dec-25 12:35:17.711925
#17 6.857 Collecting pydantic-core==2.41.5 (from pydantic>=2.7.0->fastapi->-r requirements.txt (line 1))
2025-Dec-25 12:35:17.855460
#17 6.865   Downloading pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (7.3 kB)
2025-Dec-25 12:35:17.860330
#17 6.900 Collecting typing-inspection>=0.4.2 (from pydantic>=2.7.0->fastapi->-r requirements.txt (line 1))
2025-Dec-25 12:35:17.860330
#17 6.908   Downloading typing_inspection-0.4.2-py3-none-any.whl.metadata (2.6 kB)
2025-Dec-25 12:35:17.860330
#17 7.000 Collecting argon2-cffi-bindings (from argon2-cffi->minio->-r requirements.txt (line 7))
2025-Dec-25 12:35:17.956576
#17 7.009   Downloading argon2_cffi_bindings-25.1.0-cp39-abi3-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl.metadata (7.4 kB)
2025-Dec-25 12:35:17.956576
#17 7.050 Collecting pycparser (from cffi>=2.0.0->cryptography>=3.4.0->python-jose[cryptography]->-r requirements.txt (line 11))
2025-Dec-25 12:35:17.956576
#17 7.055   Downloading pycparser-2.23-py3-none-any.whl.metadata (993 bytes)
2025-Dec-25 12:35:17.956576
#17 7.100 Downloading fastapi-0.127.0-py3-none-any.whl (112 kB)
2025-Dec-25 12:35:18.071193
#17 7.122 Downloading sqlalchemy-2.0.45-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (3.3 MB)
2025-Dec-25 12:35:18.071193
#17 7.195    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.3/3.3 MB 48.8 MB/s eta 0:00:00
2025-Dec-25 12:35:18.071193
#17 7.215 Downloading psycopg2_binary-2.9.11-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (4.2 MB)
2025-Dec-25 12:35:18.179571
#17 7.296    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.2/4.2 MB 54.0 MB/s eta 0:00:00
2025-Dec-25 12:35:18.179571
#17 7.304 Downloading httpx-0.28.1-py3-none-any.whl (73 kB)
2025-Dec-25 12:35:18.179571
#17 7.321 Downloading httpcore-1.0.9-py3-none-any.whl (78 kB)
2025-Dec-25 12:35:18.279879
#17 7.339 Downloading python_keycloak-5.8.1-py3-none-any.whl (77 kB)
2025-Dec-25 12:35:18.279879
#17 7.353 Downloading minio-7.2.20-py3-none-any.whl (93 kB)
2025-Dec-25 12:35:18.279879
#17 7.368 Downloading requests-2.32.5-py3-none-any.whl (64 kB)
2025-Dec-25 12:35:18.279879
#17 7.384 Downloading python_dotenv-1.2.1-py3-none-any.whl (21 kB)
2025-Dec-25 12:35:18.279879
#17 7.397 Downloading aiofiles-25.1.0-py3-none-any.whl (14 kB)
2025-Dec-25 12:35:18.279879
#17 7.410 Downloading annotated_doc-0.0.4-py3-none-any.whl (5.3 kB)
2025-Dec-25 12:35:18.279879
#17 7.425 Downloading async_property-0.2.2-py2.py3-none-any.whl (9.5 kB)
2025-Dec-25 12:35:18.421272
#17 7.435 Downloading bcrypt-5.0.0-cp39-abi3-manylinux_2_34_x86_64.whl (278 kB)
2025-Dec-25 12:35:18.421272
#17 7.449 Downloading certifi-2025.11.12-py3-none-any.whl (159 kB)
2025-Dec-25 12:35:18.421272
#17 7.462 Downloading charset_normalizer-3.4.4-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (153 kB)
2025-Dec-25 12:35:18.421272
#17 7.472 Downloading click-8.3.1-py3-none-any.whl (108 kB)
2025-Dec-25 12:35:18.421272
#17 7.486 Downloading cryptography-46.0.3-cp311-abi3-manylinux_2_34_x86_64.whl (4.5 MB)
2025-Dec-25 12:35:18.421272
#17 7.565    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.5/4.5 MB 56.8 MB/s eta 0:00:00
2025-Dec-25 12:35:18.524455
#17 7.574 Downloading deprecation-2.1.0-py2.py3-none-any.whl (11 kB)
2025-Dec-25 12:35:18.524455
#17 7.582 Downloading ecdsa-0.19.1-py2.py3-none-any.whl (150 kB)
2025-Dec-25 12:35:18.524455
#17 7.595 Downloading greenlet-3.3.0-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (609 kB)
2025-Dec-25 12:35:18.524455
#17 7.609    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 609.9/609.9 kB 38.5 MB/s eta 0:00:00
2025-Dec-25 12:35:18.524455
#17 7.615 Downloading h11-0.16.0-py3-none-any.whl (37 kB)
2025-Dec-25 12:35:18.524455
#17 7.638 Downloading httptools-0.7.1-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (517 kB)
2025-Dec-25 12:35:18.524455
#17 7.657 Downloading idna-3.11-py3-none-any.whl (71 kB)
2025-Dec-25 12:35:18.524455
#17 7.668 Downloading jwcrypto-1.5.6-py3-none-any.whl (92 kB)
2025-Dec-25 12:35:18.632474
#17 7.680 Downloading pyasn1-0.6.1-py3-none-any.whl (83 kB)
2025-Dec-25 12:35:18.632474
#17 7.690 Downloading pydantic-2.12.5-py3-none-any.whl (463 kB)
2025-Dec-25 12:35:18.632474
#17 7.713 Downloading pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.1 MB)
2025-Dec-25 12:35:18.632474
#17 7.776    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 34.4 MB/s eta 0:00:00
2025-Dec-25 12:35:18.749684
#17 7.786 Downloading pyyaml-6.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (807 kB)
2025-Dec-25 12:35:18.749684
#17 7.817    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 807.9/807.9 kB 28.7 MB/s eta 0:00:00
2025-Dec-25 12:35:18.749684
#17 7.829 Downloading requests_toolbelt-1.0.0-py2.py3-none-any.whl (54 kB)
2025-Dec-25 12:35:18.749684
#17 7.843 Downloading rsa-4.9.1-py3-none-any.whl (34 kB)
2025-Dec-25 12:35:18.749684
#17 7.855 Downloading starlette-0.50.0-py3-none-any.whl (74 kB)
2025-Dec-25 12:35:18.749684
#17 7.870 Downloading anyio-4.12.0-py3-none-any.whl (113 kB)
2025-Dec-25 12:35:18.749684
#17 7.885 Downloading typing_extensions-4.15.0-py3-none-any.whl (44 kB)
2025-Dec-25 12:35:18.869675
#17 7.906 Downloading urllib3-2.6.2-py3-none-any.whl (131 kB)
2025-Dec-25 12:35:18.869675
#17 7.936 Downloading uvloop-0.22.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (4.4 MB)
2025-Dec-25 12:35:18.869675
#17 8.012    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.4/4.4 MB 59.6 MB/s eta 0:00:00
2025-Dec-25 12:35:18.970011
#17 8.024 Downloading watchfiles-1.1.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (456 kB)
2025-Dec-25 12:35:18.970011
#17 8.047 Downloading websockets-15.0.1-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (182 kB)
2025-Dec-25 12:35:18.970011
#17 8.078 Downloading argon2_cffi-25.1.0-py3-none-any.whl (14 kB)
2025-Dec-25 12:35:18.970011
#17 8.092 Downloading passlib-1.7.4-py2.py3-none-any.whl (525 kB)
2025-Dec-25 12:35:18.970011
#17 8.114    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 525.6/525.6 kB 18.8 MB/s eta 0:00:00
2025-Dec-25 12:35:19.071920
#17 8.126 Downloading pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.3 MB)
2025-Dec-25 12:35:19.071920
#17 8.170    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.3/2.3 MB 57.2 MB/s eta 0:00:00
2025-Dec-25 12:35:19.071920
#17 8.176 Downloading python_jose-3.5.0-py2.py3-none-any.whl (34 kB)
2025-Dec-25 12:35:19.071920
#17 8.186 Downloading uvicorn-0.40.0-py3-none-any.whl (68 kB)
2025-Dec-25 12:35:19.071920
#17 8.196 Downloading annotated_types-0.7.0-py3-none-any.whl (13 kB)
2025-Dec-25 12:35:19.071920
#17 8.206 Downloading cffi-2.0.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (219 kB)
2025-Dec-25 12:35:19.071920
#17 8.216 Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
2025-Dec-25 12:35:19.268068
#17 8.228 Downloading typing_inspection-0.4.2-py3-none-any.whl (14 kB)
2025-Dec-25 12:35:19.268068
#17 8.237 Downloading argon2_cffi_bindings-25.1.0-cp39-abi3-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl (87 kB)
2025-Dec-25 12:35:19.268068
#17 8.248 Downloading packaging-25.0-py3-none-any.whl (66 kB)
2025-Dec-25 12:35:19.268068
#17 8.260 Downloading pycparser-2.23-py3-none-any.whl (118 kB)
2025-Dec-25 12:35:19.445522
#17 8.590 Installing collected packages: passlib, async-property, websockets, uvloop, urllib3, typing-extensions, six, pyyaml, python-dotenv, pycryptodome, pycparser, pyasn1, psycopg2-binary, packaging, idna, httptools, h11, greenlet, click, charset_normalizer, certifi, bcrypt, annotated-types, annotated-doc, aiofiles, uvicorn, typing-inspection, sqlalchemy, rsa, requests, pydantic-core, httpcore, ecdsa, deprecation, cffi, anyio, watchfiles, starlette, requests-toolbelt, python-jose, pydantic, httpx, cryptography, argon2-cffi-bindings, jwcrypto, fastapi, argon2-cffi, python-keycloak, minio
2025-Dec-25 12:35:25.758277
#17 14.90 Successfully installed aiofiles-25.1.0 annotated-doc-0.0.4 annotated-types-0.7.0 anyio-4.12.0 argon2-cffi-25.1.0 argon2-cffi-bindings-25.1.0 async-property-0.2.2 bcrypt-5.0.0 certifi-2025.11.12 cffi-2.0.0 charset_normalizer-3.4.4 click-8.3.1 cryptography-46.0.3 deprecation-2.1.0 ecdsa-0.19.1 fastapi-0.127.0 greenlet-3.3.0 h11-0.16.0 httpcore-1.0.9 httptools-0.7.1 httpx-0.28.1 idna-3.11 jwcrypto-1.5.6 minio-7.2.20 packaging-25.0 passlib-1.7.4 psycopg2-binary-2.9.11 pyasn1-0.6.1 pycparser-2.23 pycryptodome-3.23.0 pydantic-2.12.5 pydantic-core-2.41.5 python-dotenv-1.2.1 python-jose-3.5.0 python-keycloak-5.8.1 pyyaml-6.0.3 requests-2.32.5 requests-toolbelt-1.0.0 rsa-4.9.1 six-1.17.0 sqlalchemy-2.0.45 starlette-0.50.0 typing-extensions-4.15.0 typing-inspection-0.4.2 urllib3-2.6.2 uvicorn-0.40.0 uvloop-0.22.1 watchfiles-1.1.1 websockets-15.0.1
2025-Dec-25 12:35:25.967915
#17 14.90 WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager, possibly rendering your system unusable. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv. Use the --root-user-action option if you know what you are doing and want to suppress this warning.
2025-Dec-25 12:35:25.967915
#17 14.96
2025-Dec-25 12:35:25.967915
#17 14.96 [notice] A new release of pip is available: 25.0.1 -> 25.3
2025-Dec-25 12:35:25.967915
#17 14.96 [notice] To update, run: pip install --upgrade pip
2025-Dec-25 12:35:26.457418
#17 DONE 15.6s
2025-Dec-25 12:35:26.457418
2025-Dec-25 12:35:26.457418
#14 [dashboard deps 4/4] RUN npm install
2025-Dec-25 12:35:26.617303
#14 ...
2025-Dec-25 12:35:26.617303
2025-Dec-25 12:35:26.617303
#18 [api 5/5] COPY . .
2025-Dec-25 12:35:32.600541
#18 ...
2025-Dec-25 12:35:32.600541
2025-Dec-25 12:35:32.600541
#14 [dashboard deps 4/4] RUN npm install
2025-Dec-25 12:35:32.600541
#14 32.25
2025-Dec-25 12:35:32.600541
#14 32.25 added 473 packages, and audited 474 packages in 32s
2025-Dec-25 12:35:32.758362
#14 32.25
2025-Dec-25 12:35:32.758362
#14 32.25 154 packages are looking for funding
2025-Dec-25 12:35:32.758362
#14 32.25   run `npm fund` for details
2025-Dec-25 12:35:32.758362
#14 32.25
2025-Dec-25 12:35:32.758362
#14 32.25 found 0 vulnerabilities
2025-Dec-25 12:35:32.758362
#14 32.26 npm notice
2025-Dec-25 12:35:32.758362
#14 32.26 npm notice New major version of npm available! 10.8.2 -> 11.7.0
2025-Dec-25 12:35:32.758362
#14 32.26 npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.7.0
2025-Dec-25 12:35:32.758362
#14 32.26 npm notice To update run: npm install -g npm@11.7.0
2025-Dec-25 12:35:32.758362
#14 32.26 npm notice
2025-Dec-25 12:35:33.180603
#14 DONE 32.8s
2025-Dec-25 12:35:33.180603
2025-Dec-25 12:35:33.180603
#18 [api 5/5] COPY . .
2025-Dec-25 12:35:34.023062
#18 DONE 7.5s
2025-Dec-25 12:35:34.181144
#19 [api] exporting to image
2025-Dec-25 12:35:34.181144
#19 exporting layers
2025-Dec-25 12:35:37.363887
#19 exporting layers 3.3s done
2025-Dec-25 12:35:37.363887
#19 writing image sha256:d26bbee75bf5ab5e257f072ec2752950b5b8dc3bae76625fc7be421e68dd250f
2025-Dec-25 12:35:37.582345
#19 writing image sha256:d26bbee75bf5ab5e257f072ec2752950b5b8dc3bae76625fc7be421e68dd250f done
2025-Dec-25 12:35:37.582345
#19 naming to docker.io/library/hck4w0k4ww8kk4gccw000ggg-api done
2025-Dec-25 12:35:37.582345
#19 DONE 3.4s
2025-Dec-25 12:35:37.582345
2025-Dec-25 12:35:37.582345
#20 [api] resolving provenance for metadata file
2025-Dec-25 12:35:37.582345
#20 DONE 0.0s
2025-Dec-25 12:35:38.054118
#21 [dashboard builder 3/5] COPY --from=deps /app/node_modules ./node_modules
2025-Dec-25 12:35:48.996620
#21 DONE 10.9s
2025-Dec-25 12:35:49.223512
#22 [dashboard builder 4/5] COPY . .
2025-Dec-25 12:35:49.223512
#22 DONE 0.1s
2025-Dec-25 12:35:49.223512
2025-Dec-25 12:35:49.223512
#23 [dashboard builder 5/5] RUN npm run build
2025-Dec-25 12:35:49.763477
#23 0.688
2025-Dec-25 12:35:49.763477
#23 0.688 > dashboard@0.1.0 build
2025-Dec-25 12:35:49.763477
#23 0.688 > next build
2025-Dec-25 12:35:49.763477
#23 0.688
2025-Dec-25 12:35:50.554995
#23 1.482 Attention: Next.js now collects completely anonymous telemetry regarding usage.
2025-Dec-25 12:35:50.681661
#23 1.483 This information is used to shape Next.js' roadmap and prioritize features.
2025-Dec-25 12:35:50.681661
#23 1.483 You can learn more, including how to opt-out if you'd not like to participate in this anonymous program, by visiting the following URL:
2025-Dec-25 12:35:50.681661
#23 1.483 https://nextjs.org/telemetry
2025-Dec-25 12:35:50.681661
#23 1.483
2025-Dec-25 12:35:50.681661
#23 1.495 ▲ Next.js 16.1.0 (Turbopack)
2025-Dec-25 12:35:50.681661
#23 1.495
2025-Dec-25 12:35:50.681661
#23 1.609   Creating an optimized production build ...
2025-Dec-25 12:36:09.891056
#23 20.82 ✓ Compiled successfully in 18.7s
2025-Dec-25 12:36:10.058032
#23 20.83   Running TypeScript ...
2025-Dec-25 12:36:19.302564
#23 30.23   Collecting page data using 1 worker ...
2025-Dec-25 12:36:19.935162
#23 30.86   Generating static pages using 1 worker (0/11) ...
2025-Dec-25 12:36:19.942765
2025-Dec-25 12:36:20.273333
#23 31.20   Generating static pages using 1 worker (2/11)
2025-Dec-25 12:36:20.521735
#23 31.21   Generating static pages using 1 worker (5/11)
2025-Dec-25 12:36:20.521735
#23 31.21   Generating static pages using 1 worker (8/11)
2025-Dec-25 12:36:20.521735
#23 31.28 ✓ Generating static pages using 1 worker (11/11) in 417.5ms
2025-Dec-25 12:36:20.521735
#23 31.29   Finalizing page optimization ...
2025-Dec-25 12:36:20.521735
#23 31.30
2025-Dec-25 12:36:20.521735
#23 31.30 Route (app)
2025-Dec-25 12:36:20.521735
#23 31.30 ┌ ○ /
2025-Dec-25 12:36:20.521735
#23 31.30 ├ ○ /_not-found
2025-Dec-25 12:36:20.521735
#23 31.30 ├ ○ /login
2025-Dec-25 12:36:20.521735
#23 31.30 ├ ○ /org
2025-Dec-25 12:36:20.521735
#23 31.30 ├ ƒ /org/[orgId]/billing
2025-Dec-25 12:36:20.521735
#23 31.30 ├ ƒ /org/[orgId]/projects
2025-Dec-25 12:36:20.521735
#23 31.30 ├ ƒ /org/[orgId]/projects/new
2025-Dec-25 12:36:20.521735
#23 31.30 ├ ƒ /org/[orgId]/settings
2025-Dec-25 12:36:20.521735
#23 31.30 ├ ƒ /org/[orgId]/team
2025-Dec-25 12:36:20.521735
#23 31.30 ├ ○ /projects
2025-Dec-25 12:36:20.521735
#23 31.30 ├ ƒ /projects/[id]
2025-Dec-25 12:36:20.521735
#23 31.30 ├ ƒ /projects/[id]/auth
2025-Dec-25 12:36:20.521735
#23 31.30 ├ ƒ /projects/[id]/backups
2025-Dec-25 12:36:20.521735
#23 31.30 ├ ƒ /projects/[id]/database
2025-Dec-25 12:36:20.521735
#23 31.30 ├ ƒ /projects/[id]/database/[table]
2025-Dec-25 12:36:20.521735
#23 31.30 ├ ƒ /projects/[id]/edge-functions
2025-Dec-25 12:36:20.521735
#23 31.30 ├ ƒ /projects/[id]/logs
2025-Dec-25 12:36:20.521735
#23 31.30 ├ ƒ /projects/[id]/realtime
2025-Dec-25 12:36:20.521735
#23 31.30 ├ ƒ /projects/[id]/secrets
2025-Dec-25 12:36:20.521735
#23 31.30 ├ ƒ /projects/[id]/settings
2025-Dec-25 12:36:20.521735
#23 31.30 ├ ƒ /projects/[id]/settings/deployment
2025-Dec-25 12:36:20.521735
#23 31.30 ├ ƒ /projects/[id]/sql
2025-Dec-25 12:36:20.521735
#23 31.30 ├ ƒ /projects/[id]/storage
2025-Dec-25 12:36:20.521735
#23 31.30 ├ ○ /projects/new
2025-Dec-25 12:36:20.521735
#23 31.30 ├ ○ /settings/organization
2025-Dec-25 12:36:20.521735
#23 31.30 ├ ƒ /settings/organization/[id]
2025-Dec-25 12:36:20.521735
#23 31.30 ├ ○ /settings/profile
2025-Dec-25 12:36:20.521735
#23 31.30 └ ○ /signup
2025-Dec-25 12:36:20.521735
#23 31.30
2025-Dec-25 12:36:20.521735
#23 31.30
2025-Dec-25 12:36:20.521735
#23 31.30 ○  (Static)   prerendered as static content
2025-Dec-25 12:36:20.521735
#23 31.30 ƒ  (Dynamic)  server-rendered on demand
2025-Dec-25 12:36:20.521735
#23 31.30
2025-Dec-25 12:36:20.581535
#23 31.51 npm notice
2025-Dec-25 12:36:20.581535
#23 31.51 npm notice New major version of npm available! 10.8.2 -> 11.7.0
2025-Dec-25 12:36:20.581535
#23 31.51 npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.7.0
2025-Dec-25 12:36:20.581535
#23 31.51 npm notice To update run: npm install -g npm@11.7.0
2025-Dec-25 12:36:20.581535
#23 31.51 npm notice
2025-Dec-25 12:36:20.793402
#23 DONE 31.6s
2025-Dec-25 12:36:23.679313
#24 [dashboard runner 3/6] COPY --from=builder /app/public ./public
2025-Dec-25 12:36:23.849588
#24 DONE 0.0s
2025-Dec-25 12:36:23.849588
2025-Dec-25 12:36:23.849588
#25 [dashboard runner 4/6] COPY --from=builder /app/.next ./.next
2025-Dec-25 12:36:23.893638
#25 DONE 0.2s
2025-Dec-25 12:36:24.046803
#26 [dashboard runner 5/6] COPY --from=builder /app/node_modules ./node_modules
2025-Dec-25 12:36:30.381736
#26 DONE 6.5s
2025-Dec-25 12:36:30.586498
#27 [dashboard runner 6/6] COPY --from=builder /app/package.json ./package.json
2025-Dec-25 12:36:30.586498
#27 DONE 0.0s
2025-Dec-25 12:36:30.586498
2025-Dec-25 12:36:30.586498
#28 [dashboard] exporting to image
2025-Dec-25 12:36:30.586498
#28 exporting layers
2025-Dec-25 12:36:34.060377
#28 exporting layers 3.6s done
2025-Dec-25 12:36:34.122011
#28 writing image sha256:a0cd36e6498002058e37c5bc30648580061876debb47f836ff25bf37407405f5 done
2025-Dec-25 12:36:34.122011
#28 naming to docker.io/library/hck4w0k4ww8kk4gccw000ggg-dashboard done
2025-Dec-25 12:36:34.122011
#28 DONE 3.6s
2025-Dec-25 12:36:34.122011
2025-Dec-25 12:36:34.122011
#29 [dashboard] resolving provenance for metadata file
2025-Dec-25 12:36:34.122011
#29 DONE 0.0s
2025-Dec-25 12:36:34.128336
api  Built
2025-Dec-25 12:36:34.128336
dashboard  Built
2025-Dec-25 12:36:34.173251
Creating .env file with runtime variables for build phase.
2025-Dec-25 12:36:34.982102
[CMD]: docker exec q880oo44woko4gwocowocs8o bash -c 'cat /artifacts/q880oo44woko4gwocowocs8o/.env'
2025-Dec-25 12:36:34.982102
SOURCE_COMMIT=1947c1453bf49e0b50d7c166605c9143f285c782
2025-Dec-25 12:36:34.982102
COOLIFY_URL=
2025-Dec-25 12:36:34.982102
COOLIFY_FQDN=
2025-Dec-25 12:36:34.982102
SERVICE_URL_DASHBOARD=https://supalove.hayataxi.online
2025-Dec-25 12:36:34.982102
SERVICE_FQDN_DASHBOARD=supalove.hayataxi.online
2025-Dec-25 12:36:34.982102
SERVICE_URL_API=https://api.hayataxi.online
2025-Dec-25 12:36:34.982102
SERVICE_FQDN_API=api.hayataxi.online
2025-Dec-25 12:36:34.982102
SERVICE_URL_KEYCLOAK=https://auth.hayataxi.online
2025-Dec-25 12:36:34.982102
SERVICE_FQDN_KEYCLOAK=auth.hayataxi.online
2025-Dec-25 12:36:34.982102
SERVICE_URL_MINIO=https://s3.hayataxi.online
2025-Dec-25 12:36:34.982102
SERVICE_FQDN_MINIO=s3.hayataxi.online
2025-Dec-25 12:36:34.982102
SERVICE_NAME_CONTROL-PLANE-DB=control-plane-db
2025-Dec-25 12:36:34.982102
SERVICE_NAME_API=api
2025-Dec-25 12:36:34.982102
SERVICE_NAME_DASHBOARD=dashboard
2025-Dec-25 12:36:34.982102
SERVICE_NAME_KEYCLOAK=keycloak
2025-Dec-25 12:36:34.982102
SERVICE_NAME_MINIO=minio
2025-Dec-25 12:36:34.982102
POSTGRES_USER=platform
2025-Dec-25 12:36:34.982102
POSTGRES_PASSWORD=platform
2025-Dec-25 12:36:34.982102
POSTGRES_DB=control_plane
2025-Dec-25 12:36:34.982102
KEYCLOAK_ADMIN_USER=admin
2025-Dec-25 12:36:34.982102
KEYCLOAK_ADMIN_PASSWORD=admin
2025-Dec-25 12:36:34.982102
MINIO_ROOT_USER=minioadmin
2025-Dec-25 12:36:34.982102
MINIO_ROOT_PASSWORD=minioadmin
2025-Dec-25 12:36:34.982102
URL=http://localhost:8000
2025-Dec-25 12:36:34.982102
NEXT_PUBLIC_API_URL=https://api.hayataxi.online
2025-Dec-25 12:36:34.982102
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8000
2025-Dec-25 12:36:34.982102
HOST=0.0.0.0
2025-Dec-25 12:36:35.314426
Removing old containers.
2025-Dec-25 12:36:36.171407
[CMD]: docker stop --time=30 dashboard-hck4w0k4ww8kk4gccw000ggg-122223462028
2025-Dec-25 12:36:36.171407
dashboard-hck4w0k4ww8kk4gccw000ggg-122223462028
2025-Dec-25 12:36:36.568699
[CMD]: docker rm -f dashboard-hck4w0k4ww8kk4gccw000ggg-122223462028
2025-Dec-25 12:36:36.568699
dashboard-hck4w0k4ww8kk4gccw000ggg-122223462028
2025-Dec-25 12:36:36.950708
[CMD]: docker stop --time=30 api-hck4w0k4ww8kk4gccw000ggg-122223447780
2025-Dec-25 12:36:36.950708
api-hck4w0k4ww8kk4gccw000ggg-122223447780
2025-Dec-25 12:36:37.302010
[CMD]: docker rm -f api-hck4w0k4ww8kk4gccw000ggg-122223447780
2025-Dec-25 12:36:37.302010
api-hck4w0k4ww8kk4gccw000ggg-122223447780
2025-Dec-25 12:36:37.835498
[CMD]: docker stop --time=30 keycloak-hck4w0k4ww8kk4gccw000ggg-122223473415
2025-Dec-25 12:36:37.835498
keycloak-hck4w0k4ww8kk4gccw000ggg-122223473415
2025-Dec-25 12:36:38.225595
[CMD]: docker rm -f keycloak-hck4w0k4ww8kk4gccw000ggg-122223473415
2025-Dec-25 12:36:38.225595
keycloak-hck4w0k4ww8kk4gccw000ggg-122223473415
2025-Dec-25 12:36:38.786992
[CMD]: docker stop --time=30 control-plane-db-hck4w0k4ww8kk4gccw000ggg-122223431671
2025-Dec-25 12:36:38.786992
control-plane-db-hck4w0k4ww8kk4gccw000ggg-122223431671
2025-Dec-25 12:36:39.154397
[CMD]: docker rm -f control-plane-db-hck4w0k4ww8kk4gccw000ggg-122223431671
2025-Dec-25 12:36:39.154397
control-plane-db-hck4w0k4ww8kk4gccw000ggg-122223431671
2025-Dec-25 12:36:39.628339
[CMD]: docker stop --time=30 minio-hck4w0k4ww8kk4gccw000ggg-122223486757
2025-Dec-25 12:36:39.628339
minio-hck4w0k4ww8kk4gccw000ggg-122223486757
2025-Dec-25 12:36:40.027984
[CMD]: docker rm -f minio-hck4w0k4ww8kk4gccw000ggg-122223486757
2025-Dec-25 12:36:40.027984
minio-hck4w0k4ww8kk4gccw000ggg-122223486757
2025-Dec-25 12:36:40.037426
Starting new application.
2025-Dec-25 12:36:41.246102
[CMD]: docker exec q880oo44woko4gwocowocs8o bash -c 'SOURCE_COMMIT=1947c1453bf49e0b50d7c166605c9143f285c782 COOLIFY_BRANCH=main COOLIFY_RESOURCE_UUID=hck4w0k4ww8kk4gccw000ggg COOLIFY_CONTAINER_NAME=hck4w0k4ww8kk4gccw000ggg-123433651920  docker compose --env-file /artifacts/q880oo44woko4gwocowocs8o/.env --project-name hck4w0k4ww8kk4gccw000ggg --project-directory /artifacts/q880oo44woko4gwocowocs8o -f /artifacts/q880oo44woko4gwocowocs8o/docker-compose.coolify.yml up -d'
2025-Dec-25 12:36:41.246102
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-123454626379  Creating
2025-Dec-25 12:36:41.246102
Container minio-hck4w0k4ww8kk4gccw000ggg-123454680959  Creating
2025-Dec-25 12:36:41.299228
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-123454626379  Created
2025-Dec-25 12:36:41.299228
Container keycloak-hck4w0k4ww8kk4gccw000ggg-123454665242  Creating
2025-Dec-25 12:36:41.299228
Container minio-hck4w0k4ww8kk4gccw000ggg-123454680959  Created
2025-Dec-25 12:36:41.319477
Container keycloak-hck4w0k4ww8kk4gccw000ggg-123454665242  Created
2025-Dec-25 12:36:41.319477
Container api-hck4w0k4ww8kk4gccw000ggg-123454642996  Creating
2025-Dec-25 12:36:41.339884
Container api-hck4w0k4ww8kk4gccw000ggg-123454642996  Created
2025-Dec-25 12:36:41.339884
Container dashboard-hck4w0k4ww8kk4gccw000ggg-123454656284  Creating
2025-Dec-25 12:36:41.362882
Container dashboard-hck4w0k4ww8kk4gccw000ggg-123454656284  Created
2025-Dec-25 12:36:41.376694
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-123454626379  Starting
2025-Dec-25 12:36:41.376694
Container minio-hck4w0k4ww8kk4gccw000ggg-123454680959  Starting
2025-Dec-25 12:36:41.679598
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-123454626379  Started
2025-Dec-25 12:36:41.679598
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-123454626379  Waiting
2025-Dec-25 12:36:41.714489
Container minio-hck4w0k4ww8kk4gccw000ggg-123454680959  Started
2025-Dec-25 12:36:47.177041
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-123454626379  Healthy
2025-Dec-25 12:36:47.177041
Container keycloak-hck4w0k4ww8kk4gccw000ggg-123454665242  Starting
2025-Dec-25 12:36:47.397727
Container keycloak-hck4w0k4ww8kk4gccw000ggg-123454665242  Started
2025-Dec-25 12:36:47.397727
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-123454626379  Waiting
2025-Dec-25 12:36:47.902771
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-123454626379  Healthy
2025-Dec-25 12:36:47.902771
Container api-hck4w0k4ww8kk4gccw000ggg-123454642996  Starting
2025-Dec-25 12:36:48.228574
Container api-hck4w0k4ww8kk4gccw000ggg-123454642996  Started
2025-Dec-25 12:36:48.228574
Container dashboard-hck4w0k4ww8kk4gccw000ggg-123454656284  Starting
2025-Dec-25 12:36:48.821093
Container dashboard-hck4w0k4ww8kk4gccw000ggg-123454656284  Started
2025-Dec-25 12:36:51.153193
New container started.
2025-Dec-25 12:36:53.767520
Gracefully shutting down build container: q880oo44woko4gwocowocs8o
2025-Dec-25 12:36:54.561768
[CMD]: docker stop --time=30 q880oo44woko4gwocowocs8o
2025-Dec-25 12:36:54.561768
q880oo44woko4gwocowocs8o
2025-Dec-25 12:36:55.423740
[CMD]: docker rm -f q880oo44woko4gwocowocs8o
2025-Dec-25 12:36:55.423740
Error response from daemon: removal of container q880oo44woko4gwocowocs8o is already in progress