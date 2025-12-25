Deployment is Finished.


2025-Dec-25 13:55:33.316775
Starting deployment of supalove to localhost.
2025-Dec-25 13:55:33.532734
Preparing container with helper image: ghcr.io/coollabsio/coolify-helper:1.0.12
2025-Dec-25 13:55:33.647766
[CMD]: docker stop --time=30 w048wkk0go4o4wog84kckos4
2025-Dec-25 13:55:33.647766
Error response from daemon: No such container: w048wkk0go4o4wog84kckos4
2025-Dec-25 13:55:33.752412
[CMD]: docker rm -f w048wkk0go4o4wog84kckos4
2025-Dec-25 13:55:33.752412
Error response from daemon: No such container: w048wkk0go4o4wog84kckos4
2025-Dec-25 13:55:33.895721
[CMD]: docker run -d --network coolify --name w048wkk0go4o4wog84kckos4  --rm -v /var/run/docker.sock:/var/run/docker.sock ghcr.io/coollabsio/coolify-helper:1.0.12
2025-Dec-25 13:55:33.895721
79d8c814e40f4995f98acd5b5a577917cfc408b397d5708c7cb5b6c2146888af
2025-Dec-25 13:55:34.734586
[CMD]: docker exec w048wkk0go4o4wog84kckos4 bash -c 'GIT_SSH_COMMAND="ssh -o ConnectTimeout=30 -p 22 -o Port=22 -o LogLevel=ERROR -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" git ls-remote https://github.com/farisnoaman/supalove refs/heads/main'
2025-Dec-25 13:55:34.734586
56c01cf9744516479a759ba36fa3e4b320718c3f	refs/heads/main
2025-Dec-25 13:55:34.747515
----------------------------------------
2025-Dec-25 13:55:34.752492
Importing farisnoaman/supalove:main (commit sha 56c01cf9744516479a759ba36fa3e4b320718c3f) to /artifacts/w048wkk0go4o4wog84kckos4.
2025-Dec-25 13:55:34.905733
[CMD]: docker exec w048wkk0go4o4wog84kckos4 bash -c 'git clone --depth=1 --recurse-submodules --shallow-submodules -b 'main' 'https://github.com/farisnoaman/supalove' '/artifacts/w048wkk0go4o4wog84kckos4' && cd '/artifacts/w048wkk0go4o4wog84kckos4' && if [ -f .gitmodules ]; then sed -i "s#git@\(.*\):#https://\1/#g" '/artifacts/w048wkk0go4o4wog84kckos4'/.gitmodules || true && git submodule sync && GIT_SSH_COMMAND="ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" git submodule update --init --recursive --depth=1; fi && cd '/artifacts/w048wkk0go4o4wog84kckos4' && GIT_SSH_COMMAND="ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" git lfs pull'
2025-Dec-25 13:55:34.905733
Cloning into '/artifacts/w048wkk0go4o4wog84kckos4'...
2025-Dec-25 13:55:41.283537
Updating files:  23% (3605/15085)
2025-Dec-25 13:55:41.294488
Updating files:  24% (3621/15085)
2025-Dec-25 13:55:41.325788
Updating files:  25% (3772/15085)
2025-Dec-25 13:55:41.350567
Updating files:  26% (3923/15085)
2025-Dec-25 13:55:41.403610
Updating files:  27% (4073/15085)
2025-Dec-25 13:55:41.438241
Updating files:  28% (4224/15085)
2025-Dec-25 13:55:41.456471
Updating files:  29% (4375/15085)
2025-Dec-25 13:55:41.475208
Updating files:  30% (4526/15085)
2025-Dec-25 13:55:41.488945
Updating files:  31% (4677/15085)
2025-Dec-25 13:55:41.502325
Updating files:  32% (4828/15085)
2025-Dec-25 13:55:41.517686
Updating files:  33% (4979/15085)
2025-Dec-25 13:55:41.558252
Updating files:  34% (5129/15085)
2025-Dec-25 13:55:41.593297
Updating files:  35% (5280/15085)
2025-Dec-25 13:55:41.645237
Updating files:  36% (5431/15085)
2025-Dec-25 13:55:41.691561
Updating files:  37% (5582/15085)
2025-Dec-25 13:55:41.709955
Updating files:  38% (5733/15085)
2025-Dec-25 13:55:41.729160
Updating files:  39% (5884/15085)
2025-Dec-25 13:55:41.748209
Updating files:  40% (6034/15085)
2025-Dec-25 13:55:41.769620
Updating files:  41% (6185/15085)
2025-Dec-25 13:55:41.788922
Updating files:  42% (6336/15085)
2025-Dec-25 13:55:41.802048
Updating files:  43% (6487/15085)
2025-Dec-25 13:55:41.816253
Updating files:  44% (6638/15085)
2025-Dec-25 13:55:41.831203
Updating files:  45% (6789/15085)
2025-Dec-25 13:55:41.850284
Updating files:  46% (6940/15085)
2025-Dec-25 13:55:41.864966
Updating files:  47% (7090/15085)
2025-Dec-25 13:55:41.880735
Updating files:  48% (7241/15085)
2025-Dec-25 13:55:41.891441
Updating files:  49% (7392/15085)
2025-Dec-25 13:55:41.913881
Updating files:  50% (7543/15085)
2025-Dec-25 13:55:41.926037
Updating files:  51% (7694/15085)
2025-Dec-25 13:55:41.939632
Updating files:  52% (7845/15085)
2025-Dec-25 13:55:41.956626
Updating files:  53% (7996/15085)
2025-Dec-25 13:55:41.974793
Updating files:  54% (8146/15085)
2025-Dec-25 13:55:42.061361
Updating files:  55% (8297/15085)
2025-Dec-25 13:55:42.100388
Updating files:  56% (8448/15085)
2025-Dec-25 13:55:42.113749
Updating files:  57% (8599/15085)
2025-Dec-25 13:55:42.128354
Updating files:  58% (8750/15085)
2025-Dec-25 13:55:42.153589
Updating files:  59% (8901/15085)
2025-Dec-25 13:55:42.168846
Updating files:  60% (9051/15085)
2025-Dec-25 13:55:42.190956
Updating files:  61% (9202/15085)
2025-Dec-25 13:55:42.209415
Updating files:  62% (9353/15085)
2025-Dec-25 13:55:42.220940
Updating files:  63% (9504/15085)
2025-Dec-25 13:55:42.233198
Updating files:  64% (9655/15085)
2025-Dec-25 13:55:42.320574
Updating files:  64% (9798/15085)
2025-Dec-25 13:55:42.325730
Updating files:  65% (9806/15085)
2025-Dec-25 13:55:42.333765
Updating files:  66% (9957/15085)
2025-Dec-25 13:55:42.354037
Updating files:  67% (10107/15085)
2025-Dec-25 13:55:42.375787
Updating files:  68% (10258/15085)
2025-Dec-25 13:55:42.398141
Updating files:  69% (10409/15085)
2025-Dec-25 13:55:42.415985
Updating files:  70% (10560/15085)
2025-Dec-25 13:55:42.431396
Updating files:  71% (10711/15085)
2025-Dec-25 13:55:42.450592
Updating files:  72% (10862/15085)
2025-Dec-25 13:55:42.466335
Updating files:  73% (11013/15085)
2025-Dec-25 13:55:42.483458
Updating files:  74% (11163/15085)
2025-Dec-25 13:55:42.499757
Updating files:  75% (11314/15085)
2025-Dec-25 13:55:42.516756
Updating files:  76% (11465/15085)
2025-Dec-25 13:55:42.531065
Updating files:  77% (11616/15085)
2025-Dec-25 13:55:42.544396
Updating files:  78% (11767/15085)
2025-Dec-25 13:55:42.560021
Updating files:  79% (11918/15085)
2025-Dec-25 13:55:42.626413
Updating files:  80% (12068/15085)
2025-Dec-25 13:55:42.641496
Updating files:  81% (12219/15085)
2025-Dec-25 13:55:42.683630
Updating files:  82% (12370/15085)
2025-Dec-25 13:55:42.695681
Updating files:  83% (12521/15085)
2025-Dec-25 13:55:42.709813
Updating files:  84% (12672/15085)
2025-Dec-25 13:55:42.729461
Updating files:  85% (12823/15085)
2025-Dec-25 13:55:42.742212
Updating files:  86% (12974/15085)
2025-Dec-25 13:55:42.758750
Updating files:  87% (13124/15085)
2025-Dec-25 13:55:42.801665
Updating files:  88% (13275/15085)
2025-Dec-25 13:55:42.824841
Updating files:  89% (13426/15085)
2025-Dec-25 13:55:42.856027
Updating files:  90% (13577/15085)
2025-Dec-25 13:55:42.884472
Updating files:  91% (13728/15085)
2025-Dec-25 13:55:42.896837
Updating files:  92% (13879/15085)
2025-Dec-25 13:55:42.908655
Updating files:  93% (14030/15085)
2025-Dec-25 13:55:42.996373
Updating files:  94% (14180/15085)
2025-Dec-25 13:55:43.030658
Updating files:  95% (14331/15085)
2025-Dec-25 13:55:43.050766
Updating files:  96% (14482/15085)
2025-Dec-25 13:55:43.072970
Updating files:  97% (14633/15085)
2025-Dec-25 13:55:43.093670
Updating files:  98% (14784/15085)
2025-Dec-25 13:55:43.138234
Updating files:  99% (14935/15085)
2025-Dec-25 13:55:43.174934
Updating files: 100% (15085/15085)
Updating files: 100% (15085/15085), done.
2025-Dec-25 13:55:43.770335
[CMD]: docker exec w048wkk0go4o4wog84kckos4 bash -c 'cd /artifacts/w048wkk0go4o4wog84kckos4 && git log -1 56c01cf9744516479a759ba36fa3e4b320718c3f --pretty=%B'
2025-Dec-25 13:55:43.770335
fix: Mount data-plane and Docker socket in API container
2025-Dec-25 13:55:43.770335
2025-Dec-25 13:55:43.770335
Required for project provisioning to work in Coolify deployment:
2025-Dec-25 13:55:43.770335
- Docker socket: allows API to spawn project containers
2025-Dec-25 13:55:43.770335
- data-plane directory: contains project-template needed for provisioning
2025-Dec-25 13:55:50.317692
[CMD]: docker exec w048wkk0go4o4wog84kckos4 bash -c 'test -f /artifacts/w048wkk0go4o4wog84kckos4/control-plane/api/Dockerfile && echo 'exists' || echo 'not found''
2025-Dec-25 13:55:50.317692
exists
2025-Dec-25 13:55:50.465971
[CMD]: docker exec w048wkk0go4o4wog84kckos4 bash -c 'cat /artifacts/w048wkk0go4o4wog84kckos4/control-plane/api/Dockerfile'
2025-Dec-25 13:55:50.465971
FROM python:3.12-slim
2025-Dec-25 13:55:50.465971
WORKDIR /app
2025-Dec-25 13:55:50.465971
COPY requirements.txt .
2025-Dec-25 13:55:50.465971
RUN pip install -r requirements.txt
2025-Dec-25 13:55:50.465971
COPY . .
2025-Dec-25 13:55:50.465971
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
2025-Dec-25 13:55:50.674561
Added 21 ARG declarations to Dockerfile for service api.
2025-Dec-25 13:55:51.027531
[CMD]: docker exec w048wkk0go4o4wog84kckos4 bash -c 'test -f /artifacts/w048wkk0go4o4wog84kckos4/dashboard/Dockerfile && echo 'exists' || echo 'not found''
2025-Dec-25 13:55:51.027531
exists
2025-Dec-25 13:55:51.346918
[CMD]: docker exec w048wkk0go4o4wog84kckos4 bash -c 'cat /artifacts/w048wkk0go4o4wog84kckos4/dashboard/Dockerfile'
2025-Dec-25 13:55:51.346918
# Stage 1: Dependencies
2025-Dec-25 13:55:51.346918
FROM node:20-alpine AS deps
2025-Dec-25 13:55:51.346918
WORKDIR /app
2025-Dec-25 13:55:51.346918
COPY package*.json ./
2025-Dec-25 13:55:51.346918
RUN npm install
2025-Dec-25 13:55:51.346918
2025-Dec-25 13:55:51.346918
# Stage 2: Builder
2025-Dec-25 13:55:51.346918
FROM node:20-alpine AS builder
2025-Dec-25 13:55:51.346918
WORKDIR /app
2025-Dec-25 13:55:51.346918
COPY --from=deps /app/node_modules ./node_modules
2025-Dec-25 13:55:51.346918
COPY . .
2025-Dec-25 13:55:51.346918
# Set environment variables for build if needed (e.g. backend URL)
2025-Dec-25 13:55:51.346918
# For Next.js client-side fetch, it might need to know the URL at build time if pre-rendering,
2025-Dec-25 13:55:51.346918
# but we are using "use client" so it's fine.
2025-Dec-25 13:55:51.346918
ARG NEXT_PUBLIC_API_URL
2025-Dec-25 13:55:51.346918
ENV NEXT_PUBLIC_API_URL=${NEXT_PUBLIC_API_URL}
2025-Dec-25 13:55:51.346918
RUN npm run build
2025-Dec-25 13:55:51.346918
2025-Dec-25 13:55:51.346918
# Stage 3: Runner
2025-Dec-25 13:55:51.346918
FROM node:20-alpine AS runner
2025-Dec-25 13:55:51.346918
WORKDIR /app
2025-Dec-25 13:55:51.346918
ENV NODE_ENV=production
2025-Dec-25 13:55:51.346918
COPY --from=builder /app/public ./public
2025-Dec-25 13:55:51.346918
COPY --from=builder /app/.next ./.next
2025-Dec-25 13:55:51.346918
COPY --from=builder /app/node_modules ./node_modules
2025-Dec-25 13:55:51.346918
COPY --from=builder /app/package.json ./package.json
2025-Dec-25 13:55:51.346918
2025-Dec-25 13:55:51.346918
EXPOSE 3000
2025-Dec-25 13:55:51.346918
CMD ["npm", "start"]
2025-Dec-25 13:55:51.662252
Added 63 ARG declarations to Dockerfile for service dashboard (multi-stage build, added to 3 stages).
2025-Dec-25 13:55:51.682664
Pulling & building required images.
2025-Dec-25 13:55:51.736793
Creating build-time .env file in /artifacts (outside Docker context).
2025-Dec-25 13:55:52.313973
[CMD]: docker exec w048wkk0go4o4wog84kckos4 bash -c 'cat /artifacts/build-time.env'
2025-Dec-25 13:55:52.313973
SOURCE_COMMIT='56c01cf9744516479a759ba36fa3e4b320718c3f'
2025-Dec-25 13:55:52.313973
COOLIFY_URL=''
2025-Dec-25 13:55:52.313973
COOLIFY_FQDN=''
2025-Dec-25 13:55:52.313973
SERVICE_NAME_CONTROL-PLANE-DB='control-plane-db'
2025-Dec-25 13:55:52.313973
SERVICE_NAME_API='api'
2025-Dec-25 13:55:52.313973
SERVICE_NAME_DASHBOARD='dashboard'
2025-Dec-25 13:55:52.313973
SERVICE_NAME_KEYCLOAK='keycloak'
2025-Dec-25 13:55:52.313973
SERVICE_NAME_MINIO='minio'
2025-Dec-25 13:55:52.313973
SERVICE_URL_DASHBOARD='https://supalove.hayataxi.online'
2025-Dec-25 13:55:52.313973
SERVICE_FQDN_DASHBOARD='supalove.hayataxi.online'
2025-Dec-25 13:55:52.313973
SERVICE_URL_API='https://api.hayataxi.online'
2025-Dec-25 13:55:52.313973
SERVICE_FQDN_API='api.hayataxi.online'
2025-Dec-25 13:55:52.313973
SERVICE_URL_KEYCLOAK='https://auth.hayataxi.online'
2025-Dec-25 13:55:52.313973
SERVICE_FQDN_KEYCLOAK='auth.hayataxi.online'
2025-Dec-25 13:55:52.313973
SERVICE_URL_MINIO='https://s3.hayataxi.online'
2025-Dec-25 13:55:52.313973
SERVICE_FQDN_MINIO='s3.hayataxi.online'
2025-Dec-25 13:55:52.313973
ALLOWED_ORIGINS="http://localhost:3000,http://localhost:8000"
2025-Dec-25 13:55:52.313973
KEYCLOAK_ADMIN_PASSWORD="admin"
2025-Dec-25 13:55:52.313973
KEYCLOAK_ADMIN_USER="admin"
2025-Dec-25 13:55:52.313973
MINIO_ROOT_PASSWORD="minioadmin"
2025-Dec-25 13:55:52.313973
MINIO_ROOT_USER="minioadmin"
2025-Dec-25 13:55:52.313973
NEXT_PUBLIC_API_URL="https://api.hayataxi.online"
2025-Dec-25 13:55:52.313973
POSTGRES_DB="control_plane"
2025-Dec-25 13:55:52.313973
POSTGRES_PASSWORD="platform"
2025-Dec-25 13:55:52.313973
POSTGRES_USER="platform"
2025-Dec-25 13:55:52.313973
URL="http://localhost:8000"
2025-Dec-25 13:55:52.330947
Adding build arguments to Docker Compose build command.
2025-Dec-25 13:55:53.273500
[CMD]: docker exec w048wkk0go4o4wog84kckos4 bash -c 'SOURCE_COMMIT=56c01cf9744516479a759ba36fa3e4b320718c3f COOLIFY_BRANCH=main COOLIFY_RESOURCE_UUID=hck4w0k4ww8kk4gccw000ggg COOLIFY_CONTAINER_NAME=hck4w0k4ww8kk4gccw000ggg-135532163146  docker compose --env-file /artifacts/build-time.env --project-name hck4w0k4ww8kk4gccw000ggg --project-directory /artifacts/w048wkk0go4o4wog84kckos4 -f /artifacts/w048wkk0go4o4wog84kckos4/docker-compose.coolify.yml build --pull --no-cache --build-arg SOURCE_COMMIT --build-arg COOLIFY_URL --build-arg COOLIFY_FQDN --build-arg SERVICE_FQDN_API --build-arg SERVICE_FQDN_DASHBOARD --build-arg SERVICE_FQDN_KEYCLOAK --build-arg SERVICE_FQDN_MINIO --build-arg SERVICE_URL_API --build-arg SERVICE_URL_DASHBOARD --build-arg SERVICE_URL_KEYCLOAK --build-arg SERVICE_URL_MINIO --build-arg ALLOWED_ORIGINS --build-arg KEYCLOAK_ADMIN_PASSWORD --build-arg KEYCLOAK_ADMIN_USER --build-arg MINIO_ROOT_PASSWORD --build-arg MINIO_ROOT_USER --build-arg NEXT_PUBLIC_API_URL --build-arg POSTGRES_DB --build-arg POSTGRES_PASSWORD --build-arg POSTGRES_USER --build-arg URL --build-arg COOLIFY_BUILD_SECRETS_HASH=1b43d50472778b64c9fe11aaa16fcd4c362d89407567d3cb60d0725085d4cd48'
2025-Dec-25 13:55:53.273500
#1 [internal] load local bake definitions
2025-Dec-25 13:55:53.396133
#1 reading from stdin 3.22kB done
2025-Dec-25 13:55:53.396133
#1 DONE 0.0s
2025-Dec-25 13:55:53.593671
#2 [api internal] load build definition from Dockerfile
2025-Dec-25 13:55:53.593671
#2 transferring dockerfile: 658B done
2025-Dec-25 13:55:53.593671
#2 DONE 0.0s
2025-Dec-25 13:55:53.593671
2025-Dec-25 13:55:53.593671
#3 [dashboard internal] load build definition from Dockerfile
2025-Dec-25 13:55:53.593671
#3 transferring dockerfile: 2.20kB done
2025-Dec-25 13:55:53.593671
#3 DONE 0.0s
2025-Dec-25 13:55:53.593671
2025-Dec-25 13:55:53.593671
#4 [dashboard internal] load metadata for docker.io/library/node:20-alpine
2025-Dec-25 13:55:54.179436
#4 ...
2025-Dec-25 13:55:54.179436
2025-Dec-25 13:55:54.179436
#5 [api internal] load metadata for docker.io/library/python:3.12-slim
2025-Dec-25 13:55:54.179436
#5 DONE 0.7s
2025-Dec-25 13:55:54.282551
#6 [api internal] load .dockerignore
2025-Dec-25 13:55:54.282551
#6 transferring context: 2B done
2025-Dec-25 13:55:54.282551
#6 DONE 0.0s
2025-Dec-25 13:55:54.282551
2025-Dec-25 13:55:54.282551
#7 [api 1/5] FROM docker.io/library/python:3.12-slim@sha256:fa48eefe2146644c2308b909d6bb7651a768178f84fc9550dcd495e4d6d84d01
2025-Dec-25 13:55:54.282551
#7 DONE 0.0s
2025-Dec-25 13:55:54.282551
2025-Dec-25 13:55:54.282551
#8 [api 2/5] WORKDIR /app
2025-Dec-25 13:55:54.282551
#8 CACHED
2025-Dec-25 13:55:54.282551
2025-Dec-25 13:55:54.282551
#4 [dashboard internal] load metadata for docker.io/library/node:20-alpine
2025-Dec-25 13:55:54.386574
#4 DONE 0.8s
2025-Dec-25 13:55:54.386574
2025-Dec-25 13:55:54.386574
#9 [dashboard internal] load .dockerignore
2025-Dec-25 13:55:54.386574
#9 transferring context: 2B done
2025-Dec-25 13:55:54.386574
#9 DONE 0.0s
2025-Dec-25 13:55:54.386574
2025-Dec-25 13:55:54.386574
#10 [dashboard deps 1/4] FROM docker.io/library/node:20-alpine@sha256:658d0f63e501824d6c23e06d4bb95c71e7d704537c9d9272f488ac03a370d448
2025-Dec-25 13:55:54.386574
#10 DONE 0.0s
2025-Dec-25 13:55:54.386574
2025-Dec-25 13:55:54.386574
#11 [dashboard deps 2/4] WORKDIR /app
2025-Dec-25 13:55:54.386574
#11 CACHED
2025-Dec-25 13:55:54.386574
2025-Dec-25 13:55:54.386574
#12 [dashboard internal] load build context
2025-Dec-25 13:55:54.386574
#12 transferring context: 837.69kB 0.0s done
2025-Dec-25 13:55:54.386574
#12 DONE 0.1s
2025-Dec-25 13:55:54.386574
2025-Dec-25 13:55:54.386574
#13 [dashboard deps 3/4] COPY package*.json ./
2025-Dec-25 13:55:54.524540
#13 DONE 0.1s
2025-Dec-25 13:55:54.524540
2025-Dec-25 13:55:54.524540
#14 [api internal] load build context
2025-Dec-25 13:55:59.459068
#14 transferring context: 159.38MB 5.2s
2025-Dec-25 13:56:04.449437
#14 ...
2025-Dec-25 13:56:04.449437
2025-Dec-25 13:56:04.449437
#15 [dashboard deps 4/4] RUN npm install
2025-Dec-25 13:56:04.653135
#15 ...
2025-Dec-25 13:56:04.653135
2025-Dec-25 13:56:04.653135
#14 [api internal] load build context
2025-Dec-25 13:56:04.653135
#14 transferring context: 326.43MB 10.4s
2025-Dec-25 13:56:05.063665
#14 transferring context: 330.52MB 10.8s done
2025-Dec-25 13:56:05.189658
#14 DONE 11.0s
2025-Dec-25 13:56:05.189658
2025-Dec-25 13:56:05.189658
#16 [api 3/5] COPY requirements.txt .
2025-Dec-25 13:56:05.495908
#16 DONE 0.3s
2025-Dec-25 13:56:05.495908
2025-Dec-25 13:56:05.495908
#15 [dashboard deps 4/4] RUN npm install
2025-Dec-25 13:56:05.646997
#15 ...
2025-Dec-25 13:56:05.646997
2025-Dec-25 13:56:05.646997
#17 [api 4/5] RUN pip install -r requirements.txt
2025-Dec-25 13:56:08.904134
#17 3.409 Collecting fastapi (from -r requirements.txt (line 1))
2025-Dec-25 13:56:09.089714
#17 3.444   Downloading fastapi-0.127.0-py3-none-any.whl.metadata (30 kB)
2025-Dec-25 13:56:09.356739
#17 3.857 Collecting sqlalchemy (from -r requirements.txt (line 3))
2025-Dec-25 13:56:09.489479
#17 3.861   Downloading sqlalchemy-2.0.45-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (9.5 kB)
2025-Dec-25 13:56:09.489479
#17 3.943 Collecting psycopg2-binary (from -r requirements.txt (line 4))
2025-Dec-25 13:56:09.489479
#17 3.949   Downloading psycopg2_binary-2.9.11-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (4.9 kB)
2025-Dec-25 13:56:09.489479
#17 3.994 Collecting httpx (from -r requirements.txt (line 5))
2025-Dec-25 13:56:09.609581
#17 4.000   Downloading httpx-0.28.1-py3-none-any.whl.metadata (7.1 kB)
2025-Dec-25 13:56:09.609581
#17 4.057 Collecting python-keycloak (from -r requirements.txt (line 6))
2025-Dec-25 13:56:09.609581
#17 4.063   Downloading python_keycloak-5.8.1-py3-none-any.whl.metadata (6.0 kB)
2025-Dec-25 13:56:09.609581
#17 4.113 Collecting minio (from -r requirements.txt (line 7))
2025-Dec-25 13:56:09.828032
#17 4.124   Downloading minio-7.2.20-py3-none-any.whl.metadata (6.5 kB)
2025-Dec-25 13:56:09.828032
#17 4.164 Collecting requests (from -r requirements.txt (line 8))
2025-Dec-25 13:56:09.828032
#17 4.169   Downloading requests-2.32.5-py3-none-any.whl.metadata (4.9 kB)
2025-Dec-25 13:56:09.828032
#17 4.198 Collecting python-dotenv (from -r requirements.txt (line 9))
2025-Dec-25 13:56:09.828032
#17 4.202   Downloading python_dotenv-1.2.1-py3-none-any.whl.metadata (25 kB)
2025-Dec-25 13:56:09.828032
#17 4.326 Collecting bcrypt<4.1.0 (from -r requirements.txt (line 11))
2025-Dec-25 13:56:10.019746
#17 4.347   Downloading bcrypt-4.0.1-cp36-abi3-manylinux_2_28_x86_64.whl.metadata (9.0 kB)
2025-Dec-25 13:56:10.019746
#17 4.390 Collecting python-multipart (from -r requirements.txt (line 13))
2025-Dec-25 13:56:10.019746
#17 4.397   Downloading python_multipart-0.0.21-py3-none-any.whl.metadata (1.8 kB)
2025-Dec-25 13:56:10.019746
#17 4.520 Collecting stripe (from -r requirements.txt (line 14))
2025-Dec-25 13:56:10.117399
#17 4.533   Downloading stripe-14.1.0-py3-none-any.whl.metadata (18 kB)
2025-Dec-25 13:56:10.117399
#17 4.578 Collecting prometheus_client (from -r requirements.txt (line 15))
2025-Dec-25 13:56:10.117399
#17 4.583   Downloading prometheus_client-0.23.1-py3-none-any.whl.metadata (1.9 kB)
2025-Dec-25 13:56:10.117399
#17 4.620 Collecting APScheduler (from -r requirements.txt (line 16))
2025-Dec-25 13:56:10.221452
#17 4.630   Downloading apscheduler-3.11.2-py3-none-any.whl.metadata (6.4 kB)
2025-Dec-25 13:56:10.221452
#17 4.693 Collecting uvicorn[standard] (from -r requirements.txt (line 2))
2025-Dec-25 13:56:10.221452
#17 4.697   Downloading uvicorn-0.40.0-py3-none-any.whl.metadata (6.7 kB)
2025-Dec-25 13:56:10.221452
#17 4.726 Collecting passlib[bcrypt] (from -r requirements.txt (line 10))
2025-Dec-25 13:56:10.324760
#17 4.735   Downloading passlib-1.7.4-py2.py3-none-any.whl.metadata (1.7 kB)
2025-Dec-25 13:56:10.324760
#17 4.757 Collecting python-jose[cryptography] (from -r requirements.txt (line 12))
2025-Dec-25 13:56:10.324760
#17 4.763   Downloading python_jose-3.5.0-py2.py3-none-any.whl.metadata (5.5 kB)
2025-Dec-25 13:56:10.324760
#17 4.823 Collecting starlette<0.51.0,>=0.40.0 (from fastapi->-r requirements.txt (line 1))
2025-Dec-25 13:56:10.324760
#17 4.828   Downloading starlette-0.50.0-py3-none-any.whl.metadata (6.3 kB)
2025-Dec-25 13:56:10.463414
#17 4.968 Collecting pydantic>=2.7.0 (from fastapi->-r requirements.txt (line 1))
2025-Dec-25 13:56:10.580381
#17 4.973   Downloading pydantic-2.12.5-py3-none-any.whl.metadata (90 kB)
2025-Dec-25 13:56:10.580381
#17 5.065 Collecting typing-extensions>=4.8.0 (from fastapi->-r requirements.txt (line 1))
2025-Dec-25 13:56:10.580381
#17 5.079   Downloading typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
2025-Dec-25 13:56:10.687957
#17 5.110 Collecting annotated-doc>=0.0.2 (from fastapi->-r requirements.txt (line 1))
2025-Dec-25 13:56:10.687957
#17 5.120   Downloading annotated_doc-0.0.4-py3-none-any.whl.metadata (6.6 kB)
2025-Dec-25 13:56:10.687957
#17 5.163 Collecting click>=7.0 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 13:56:10.687957
#17 5.168   Downloading click-8.3.1-py3-none-any.whl.metadata (2.6 kB)
2025-Dec-25 13:56:10.687957
#17 5.193 Collecting h11>=0.8 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 13:56:10.880771
#17 5.202   Downloading h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
2025-Dec-25 13:56:10.880771
#17 5.261 Collecting httptools>=0.6.3 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 13:56:10.880771
#17 5.273   Downloading httptools-0.7.1-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (3.5 kB)
2025-Dec-25 13:56:10.880771
#17 5.384 Collecting pyyaml>=5.1 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 13:56:11.080916
#17 5.390   Downloading pyyaml-6.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.4 kB)
2025-Dec-25 13:56:11.080916
#17 5.462 Collecting uvloop>=0.15.1 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 13:56:11.080916
#17 5.467   Downloading uvloop-0.22.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (4.9 kB)
2025-Dec-25 13:56:11.080916
#17 5.586 Collecting watchfiles>=0.13 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 13:56:11.190343
#17 5.592   Downloading watchfiles-1.1.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.9 kB)
2025-Dec-25 13:56:11.190343
#17 5.695 Collecting websockets>=10.4 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 13:56:11.341493
#17 5.702   Downloading websockets-15.0.1-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.8 kB)
2025-Dec-25 13:56:11.341493
#17 5.846 Collecting greenlet>=1 (from sqlalchemy->-r requirements.txt (line 3))
2025-Dec-25 13:56:11.452706
#17 5.852   Downloading greenlet-3.3.0-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (4.1 kB)
2025-Dec-25 13:56:11.452706
#17 5.899 Collecting anyio (from httpx->-r requirements.txt (line 5))
2025-Dec-25 13:56:11.452706
#17 5.907   Downloading anyio-4.12.0-py3-none-any.whl.metadata (4.3 kB)
2025-Dec-25 13:56:11.452706
#17 5.956 Collecting certifi (from httpx->-r requirements.txt (line 5))
2025-Dec-25 13:56:11.573113
#17 5.966   Downloading certifi-2025.11.12-py3-none-any.whl.metadata (2.5 kB)
2025-Dec-25 13:56:11.573113
#17 6.017 Collecting httpcore==1.* (from httpx->-r requirements.txt (line 5))
2025-Dec-25 13:56:11.573113
#17 6.027   Downloading httpcore-1.0.9-py3-none-any.whl.metadata (21 kB)
2025-Dec-25 13:56:11.573113
#17 6.076 Collecting idna (from httpx->-r requirements.txt (line 5))
2025-Dec-25 13:56:11.687220
#17 6.086   Downloading idna-3.11-py3-none-any.whl.metadata (8.4 kB)
2025-Dec-25 13:56:11.687220
#17 6.136 Collecting aiofiles>=24.1.0 (from python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 13:56:11.687220
#17 6.144   Downloading aiofiles-25.1.0-py3-none-any.whl.metadata (6.3 kB)
2025-Dec-25 13:56:11.687220
#17 6.171 Collecting async-property>=0.2.2 (from python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 13:56:11.687220
#17 6.192   Downloading async_property-0.2.2-py2.py3-none-any.whl.metadata (5.3 kB)
2025-Dec-25 13:56:11.816029
#17 6.218 Collecting deprecation>=2.1.0 (from python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 13:56:11.816029
#17 6.225   Downloading deprecation-2.1.0-py2.py3-none-any.whl.metadata (4.6 kB)
2025-Dec-25 13:56:11.816029
#17 6.261 Collecting jwcrypto>=1.5.4 (from python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 13:56:11.816029
#17 6.269   Downloading jwcrypto-1.5.6-py3-none-any.whl.metadata (3.1 kB)
2025-Dec-25 13:56:11.816029
#17 6.321 Collecting requests-toolbelt>=0.6.0 (from python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 13:56:12.057480
#17 6.335   Downloading requests_toolbelt-1.0.0-py2.py3-none-any.whl.metadata (14 kB)
2025-Dec-25 13:56:12.057480
#17 6.403 Collecting argon2-cffi (from minio->-r requirements.txt (line 7))
2025-Dec-25 13:56:12.057480
#17 6.412   Downloading argon2_cffi-25.1.0-py3-none-any.whl.metadata (4.1 kB)
2025-Dec-25 13:56:12.087394
#17 6.592 Collecting pycryptodome (from minio->-r requirements.txt (line 7))
2025-Dec-25 13:56:12.282031
#17 6.602   Downloading pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (3.4 kB)
2025-Dec-25 13:56:12.282031
#17 6.641 Collecting urllib3 (from minio->-r requirements.txt (line 7))
2025-Dec-25 13:56:12.282031
#17 6.647   Downloading urllib3-2.6.2-py3-none-any.whl.metadata (6.6 kB)
2025-Dec-25 13:56:12.282031
#17 6.787 Collecting charset_normalizer<4,>=2 (from requests->-r requirements.txt (line 8))
2025-Dec-25 13:56:12.384471
#17 6.799   Downloading charset_normalizer-3.4.4-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (37 kB)
2025-Dec-25 13:56:12.384471
#17 6.880 Collecting ecdsa!=0.15 (from python-jose[cryptography]->-r requirements.txt (line 12))
2025-Dec-25 13:56:12.384471
#17 6.887   Downloading ecdsa-0.19.1-py2.py3-none-any.whl.metadata (29 kB)
2025-Dec-25 13:56:12.631790
#17 6.936 Collecting rsa!=4.1.1,!=4.4,<5.0,>=4.0 (from python-jose[cryptography]->-r requirements.txt (line 12))
2025-Dec-25 13:56:12.631790
#17 6.945   Downloading rsa-4.9.1-py3-none-any.whl.metadata (5.6 kB)
2025-Dec-25 13:56:12.631790
#17 6.981 Collecting pyasn1>=0.5.0 (from python-jose[cryptography]->-r requirements.txt (line 12))
2025-Dec-25 13:56:12.631790
#17 6.986   Downloading pyasn1-0.6.1-py3-none-any.whl.metadata (8.4 kB)
2025-Dec-25 13:56:12.662824
#17 7.167 Collecting cryptography>=3.4.0 (from python-jose[cryptography]->-r requirements.txt (line 12))
2025-Dec-25 13:56:12.847476
#17 7.171   Downloading cryptography-46.0.3-cp311-abi3-manylinux_2_34_x86_64.whl.metadata (5.7 kB)
2025-Dec-25 13:56:12.847476
#17 7.203 Collecting tzlocal>=3.0 (from APScheduler->-r requirements.txt (line 16))
2025-Dec-25 13:56:12.847476
#17 7.207   Downloading tzlocal-5.3.1-py3-none-any.whl.metadata (7.6 kB)
2025-Dec-25 13:56:12.847476
#17 7.352 Collecting cffi>=2.0.0 (from cryptography>=3.4.0->python-jose[cryptography]->-r requirements.txt (line 12))
2025-Dec-25 13:56:12.951406
#17 7.357   Downloading cffi-2.0.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (2.6 kB)
2025-Dec-25 13:56:12.963301
#17 7.397 Collecting packaging (from deprecation>=2.1.0->python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 13:56:12.963301
#17 7.406   Downloading packaging-25.0-py3-none-any.whl.metadata (3.3 kB)
2025-Dec-25 13:56:12.963301
#17 7.449 Collecting six>=1.9.0 (from ecdsa!=0.15->python-jose[cryptography]->-r requirements.txt (line 12))
2025-Dec-25 13:56:12.963301
#17 7.455   Downloading six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
2025-Dec-25 13:56:13.159574
#17 7.504 Collecting annotated-types>=0.6.0 (from pydantic>=2.7.0->fastapi->-r requirements.txt (line 1))
2025-Dec-25 13:56:13.159574
#17 7.510   Downloading annotated_types-0.7.0-py3-none-any.whl.metadata (15 kB)
2025-Dec-25 13:56:13.554576
#17 8.058 Collecting pydantic-core==2.41.5 (from pydantic>=2.7.0->fastapi->-r requirements.txt (line 1))
2025-Dec-25 13:56:13.679043
#17 8.063   Downloading pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (7.3 kB)
2025-Dec-25 13:56:13.679043
#17 8.089 Collecting typing-inspection>=0.4.2 (from pydantic>=2.7.0->fastapi->-r requirements.txt (line 1))
2025-Dec-25 13:56:13.679043
#17 8.097   Downloading typing_inspection-0.4.2-py3-none-any.whl.metadata (2.6 kB)
2025-Dec-25 13:56:13.679043
#17 8.183 Collecting argon2-cffi-bindings (from argon2-cffi->minio->-r requirements.txt (line 7))
2025-Dec-25 13:56:13.849497
#17 8.186   Downloading argon2_cffi_bindings-25.1.0-cp39-abi3-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl.metadata (7.4 kB)
2025-Dec-25 13:56:13.849497
#17 8.224 Collecting pycparser (from cffi>=2.0.0->cryptography>=3.4.0->python-jose[cryptography]->-r requirements.txt (line 12))
2025-Dec-25 13:56:13.849497
#17 8.228   Downloading pycparser-2.23-py3-none-any.whl.metadata (993 bytes)
2025-Dec-25 13:56:13.849497
#17 8.257 Downloading fastapi-0.127.0-py3-none-any.whl (112 kB)
2025-Dec-25 13:56:13.849497
#17 8.273 Downloading sqlalchemy-2.0.45-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (3.3 MB)
2025-Dec-25 13:56:13.849497
#17 8.354    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.3/3.3 MB 43.0 MB/s eta 0:00:00
2025-Dec-25 13:56:13.986371
#17 8.371 Downloading psycopg2_binary-2.9.11-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (4.2 MB)
2025-Dec-25 13:56:13.986371
#17 8.490    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.2/4.2 MB 37.8 MB/s eta 0:00:00
2025-Dec-25 13:56:14.090168
#17 8.498 Downloading httpx-0.28.1-py3-none-any.whl (73 kB)
2025-Dec-25 13:56:14.096979
#17 8.522 Downloading httpcore-1.0.9-py3-none-any.whl (78 kB)
2025-Dec-25 13:56:14.096979
#17 8.563 Downloading python_keycloak-5.8.1-py3-none-any.whl (77 kB)
2025-Dec-25 13:56:14.096979
#17 8.578 Downloading minio-7.2.20-py3-none-any.whl (93 kB)
2025-Dec-25 13:56:14.096979
#17 8.586 Downloading requests-2.32.5-py3-none-any.whl (64 kB)
2025-Dec-25 13:56:14.096979
#17 8.594 Downloading python_dotenv-1.2.1-py3-none-any.whl (21 kB)
2025-Dec-25 13:56:14.192739
#17 8.609 Downloading bcrypt-4.0.1-cp36-abi3-manylinux_2_28_x86_64.whl (593 kB)
2025-Dec-25 13:56:14.192739
#17 8.619    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 593.7/593.7 kB 55.6 MB/s eta 0:00:00
2025-Dec-25 13:56:14.192739
#17 8.624 Downloading python_multipart-0.0.21-py3-none-any.whl (24 kB)
2025-Dec-25 13:56:14.192739
#17 8.635 Downloading stripe-14.1.0-py3-none-any.whl (2.1 MB)
2025-Dec-25 13:56:14.192739
#17 8.669    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 72.8 MB/s eta 0:00:00
2025-Dec-25 13:56:14.192739
#17 8.674 Downloading prometheus_client-0.23.1-py3-none-any.whl (61 kB)
2025-Dec-25 13:56:14.192739
#17 8.685 Downloading apscheduler-3.11.2-py3-none-any.whl (64 kB)
2025-Dec-25 13:56:14.192739
#17 8.696 Downloading aiofiles-25.1.0-py3-none-any.whl (14 kB)
2025-Dec-25 13:56:14.411476
#17 8.706 Downloading annotated_doc-0.0.4-py3-none-any.whl (5.3 kB)
2025-Dec-25 13:56:14.411476
#17 8.716 Downloading async_property-0.2.2-py2.py3-none-any.whl (9.5 kB)
2025-Dec-25 13:56:14.411476
#17 8.727 Downloading certifi-2025.11.12-py3-none-any.whl (159 kB)
2025-Dec-25 13:56:14.411476
#17 8.739 Downloading charset_normalizer-3.4.4-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (153 kB)
2025-Dec-25 13:56:14.411476
#17 8.749 Downloading click-8.3.1-py3-none-any.whl (108 kB)
2025-Dec-25 13:56:14.411476
#17 8.761 Downloading cryptography-46.0.3-cp311-abi3-manylinux_2_34_x86_64.whl (4.5 MB)
2025-Dec-25 13:56:14.459889
#17 8.962    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.5/4.5 MB 57.3 MB/s eta 0:00:00
2025-Dec-25 13:56:14.559426
#17 8.968 Downloading deprecation-2.1.0-py2.py3-none-any.whl (11 kB)
2025-Dec-25 13:56:14.559426
#17 8.983 Downloading ecdsa-0.19.1-py2.py3-none-any.whl (150 kB)
2025-Dec-25 13:56:14.559426
#17 8.998 Downloading greenlet-3.3.0-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (609 kB)
2025-Dec-25 13:56:14.559426
#17 9.023    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 609.9/609.9 kB 31.2 MB/s eta 0:00:00
2025-Dec-25 13:56:14.559426
#17 9.030 Downloading h11-0.16.0-py3-none-any.whl (37 kB)
2025-Dec-25 13:56:14.559426
#17 9.047 Downloading httptools-0.7.1-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (517 kB)
2025-Dec-25 13:56:14.559426
#17 9.063 Downloading idna-3.11-py3-none-any.whl (71 kB)
2025-Dec-25 13:56:14.677027
#17 9.083 Downloading jwcrypto-1.5.6-py3-none-any.whl (92 kB)
2025-Dec-25 13:56:14.677027
#17 9.094 Downloading pyasn1-0.6.1-py3-none-any.whl (83 kB)
2025-Dec-25 13:56:14.677027
#17 9.109 Downloading pydantic-2.12.5-py3-none-any.whl (463 kB)
2025-Dec-25 13:56:14.677027
#17 9.122 Downloading pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.1 MB)
2025-Dec-25 13:56:14.677027
#17 9.154    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 73.4 MB/s eta 0:00:00
2025-Dec-25 13:56:14.677027
#17 9.158 Downloading pyyaml-6.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (807 kB)
2025-Dec-25 13:56:14.677027
#17 9.181    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 807.9/807.9 kB 35.5 MB/s eta 0:00:00
2025-Dec-25 13:56:14.788864
#17 9.186 Downloading requests_toolbelt-1.0.0-py2.py3-none-any.whl (54 kB)
2025-Dec-25 13:56:14.788864
#17 9.199 Downloading rsa-4.9.1-py3-none-any.whl (34 kB)
2025-Dec-25 13:56:14.788864
#17 9.210 Downloading starlette-0.50.0-py3-none-any.whl (74 kB)
2025-Dec-25 13:56:14.788864
#17 9.223 Downloading anyio-4.12.0-py3-none-any.whl (113 kB)
2025-Dec-25 13:56:14.788864
#17 9.236 Downloading typing_extensions-4.15.0-py3-none-any.whl (44 kB)
2025-Dec-25 13:56:14.788864
#17 9.252 Downloading tzlocal-5.3.1-py3-none-any.whl (18 kB)
2025-Dec-25 13:56:14.788864
#17 9.264 Downloading urllib3-2.6.2-py3-none-any.whl (131 kB)
2025-Dec-25 13:56:14.788864
#17 9.291 Downloading uvloop-0.22.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (4.4 MB)
2025-Dec-25 13:56:14.906667
#17 9.411    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.4/4.4 MB 37.3 MB/s eta 0:00:00
2025-Dec-25 13:56:15.015603
#17 9.421 Downloading watchfiles-1.1.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (456 kB)
2025-Dec-25 13:56:15.015603
#17 9.442 Downloading websockets-15.0.1-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (182 kB)
2025-Dec-25 13:56:15.015603
#17 9.453 Downloading argon2_cffi-25.1.0-py3-none-any.whl (14 kB)
2025-Dec-25 13:56:15.015603
#17 9.467 Downloading passlib-1.7.4-py2.py3-none-any.whl (525 kB)
2025-Dec-25 13:56:15.015603
#17 9.478    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 525.6/525.6 kB 39.2 MB/s eta 0:00:00
2025-Dec-25 13:56:15.015603
#17 9.486 Downloading pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.3 MB)
2025-Dec-25 13:56:15.015603
#17 9.519    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.3/2.3 MB 74.7 MB/s eta 0:00:00
2025-Dec-25 13:56:15.123547
#17 9.530 Downloading python_jose-3.5.0-py2.py3-none-any.whl (34 kB)
2025-Dec-25 13:56:15.123547
#17 9.548 Downloading uvicorn-0.40.0-py3-none-any.whl (68 kB)
2025-Dec-25 13:56:15.123547
#17 9.560 Downloading annotated_types-0.7.0-py3-none-any.whl (13 kB)
2025-Dec-25 13:56:15.123547
#17 9.574 Downloading cffi-2.0.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (219 kB)
2025-Dec-25 13:56:15.123547
#17 9.586 Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
2025-Dec-25 13:56:15.123547
#17 9.597 Downloading typing_inspection-0.4.2-py3-none-any.whl (14 kB)
2025-Dec-25 13:56:15.123547
#17 9.606 Downloading argon2_cffi_bindings-25.1.0-cp39-abi3-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl (87 kB)
2025-Dec-25 13:56:15.123547
#17 9.616 Downloading packaging-25.0-py3-none-any.whl (66 kB)
2025-Dec-25 13:56:15.123547
#17 9.628 Downloading pycparser-2.23-py3-none-any.whl (118 kB)
2025-Dec-25 13:56:15.286206
#17 9.788 Installing collected packages: passlib, async-property, websockets, uvloop, urllib3, tzlocal, typing-extensions, six, pyyaml, python-multipart, python-dotenv, pycryptodome, pycparser, pyasn1, psycopg2-binary, prometheus_client, packaging, idna, httptools, h11, greenlet, click, charset_normalizer, certifi, bcrypt, annotated-types, annotated-doc, aiofiles, uvicorn, typing-inspection, sqlalchemy, rsa, requests, pydantic-core, httpcore, ecdsa, deprecation, cffi, APScheduler, anyio, watchfiles, stripe, starlette, requests-toolbelt, python-jose, pydantic, httpx, cryptography, argon2-cffi-bindings, jwcrypto, fastapi, argon2-cffi, python-keycloak, minio
2025-Dec-25 13:56:22.954883
#17 17.46 Successfully installed APScheduler-3.11.2 aiofiles-25.1.0 annotated-doc-0.0.4 annotated-types-0.7.0 anyio-4.12.0 argon2-cffi-25.1.0 argon2-cffi-bindings-25.1.0 async-property-0.2.2 bcrypt-4.0.1 certifi-2025.11.12 cffi-2.0.0 charset_normalizer-3.4.4 click-8.3.1 cryptography-46.0.3 deprecation-2.1.0 ecdsa-0.19.1 fastapi-0.127.0 greenlet-3.3.0 h11-0.16.0 httpcore-1.0.9 httptools-0.7.1 httpx-0.28.1 idna-3.11 jwcrypto-1.5.6 minio-7.2.20 packaging-25.0 passlib-1.7.4 prometheus_client-0.23.1 psycopg2-binary-2.9.11 pyasn1-0.6.1 pycparser-2.23 pycryptodome-3.23.0 pydantic-2.12.5 pydantic-core-2.41.5 python-dotenv-1.2.1 python-jose-3.5.0 python-keycloak-5.8.1 python-multipart-0.0.21 pyyaml-6.0.3 requests-2.32.5 requests-toolbelt-1.0.0 rsa-4.9.1 six-1.17.0 sqlalchemy-2.0.45 starlette-0.50.0 stripe-14.1.0 typing-extensions-4.15.0 typing-inspection-0.4.2 tzlocal-5.3.1 urllib3-2.6.2 uvicorn-0.40.0 uvloop-0.22.1 watchfiles-1.1.1 websockets-15.0.1
2025-Dec-25 13:56:22.962400
2025-Dec-25 13:56:23.182554
#17 17.46 WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager, possibly rendering your system unusable. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv. Use the --root-user-action option if you know what you are doing and want to suppress this warning.
2025-Dec-25 13:56:23.182554
#17 17.53
2025-Dec-25 13:56:23.182554
#17 17.53 [notice] A new release of pip is available: 25.0.1 -> 25.3
2025-Dec-25 13:56:23.182554
#17 17.53 [notice] To update, run: pip install --upgrade pip
2025-Dec-25 13:56:23.623491
#17 DONE 18.1s
2025-Dec-25 13:56:23.623491
2025-Dec-25 13:56:23.623491
#15 [dashboard deps 4/4] RUN npm install
2025-Dec-25 13:56:23.780314
#15 ...
2025-Dec-25 13:56:23.786678
#18 [api 5/5] COPY . .
2025-Dec-25 13:56:27.054828
#18 ...
2025-Dec-25 13:56:27.054828
2025-Dec-25 13:56:27.054828
#15 [dashboard deps 4/4] RUN npm install
2025-Dec-25 13:56:27.054828
#15 32.25
2025-Dec-25 13:56:27.054828
#15 32.25 added 473 packages, and audited 474 packages in 32s
2025-Dec-25 13:56:27.054828
#15 32.25
2025-Dec-25 13:56:27.054828
#15 32.25 154 packages are looking for funding
2025-Dec-25 13:56:27.054828
#15 32.25   run `npm fund` for details
2025-Dec-25 13:56:27.054828
#15 32.25
2025-Dec-25 13:56:27.054828
#15 32.25 found 0 vulnerabilities
2025-Dec-25 13:56:27.054828
#15 32.25 npm notice
2025-Dec-25 13:56:27.054828
#15 32.25 npm notice New major version of npm available! 10.8.2 -> 11.7.0
2025-Dec-25 13:56:27.054828
#15 32.25 npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.7.0
2025-Dec-25 13:56:27.054828
#15 32.25 npm notice To update run: npm install -g npm@11.7.0
2025-Dec-25 13:56:27.054828
#15 32.25 npm notice
2025-Dec-25 13:56:27.054828
#15 DONE 32.6s
2025-Dec-25 13:56:27.206765
#18 [api 5/5] COPY . .
2025-Dec-25 13:56:31.304341
#18 DONE 7.7s
2025-Dec-25 13:56:31.459140
#19 [api] exporting to image
2025-Dec-25 13:56:31.459140
#19 exporting layers
2025-Dec-25 13:56:34.815514
#19 exporting layers 3.5s done
2025-Dec-25 13:56:34.931559
#19 writing image sha256:4079912a6b1fff062944927ef3edfd89d65f1dd3f28f3121a8fb88cd338482f9 done
2025-Dec-25 13:56:34.931559
#19 naming to docker.io/library/hck4w0k4ww8kk4gccw000ggg-api 0.0s done
2025-Dec-25 13:56:34.931559
#19 DONE 3.5s
2025-Dec-25 13:56:34.931559
2025-Dec-25 13:56:34.931559
#20 [api] resolving provenance for metadata file
2025-Dec-25 13:56:34.931559
#20 DONE 0.0s
2025-Dec-25 13:56:36.170776
#21 [dashboard builder 3/5] COPY --from=deps /app/node_modules ./node_modules
2025-Dec-25 13:56:48.217299
#21 DONE 12.0s
2025-Dec-25 13:56:48.447429
2025-Dec-25 13:56:48.457309
#22 [dashboard builder 4/5] COPY . .
2025-Dec-25 13:56:48.457309
#22 DONE 0.1s
2025-Dec-25 13:56:48.457309
2025-Dec-25 13:56:48.457309
#23 [dashboard builder 5/5] RUN npm run build
2025-Dec-25 13:56:49.124140
#23 0.826
2025-Dec-25 13:56:49.124140
#23 0.826 > dashboard@0.1.0 build
2025-Dec-25 13:56:49.124140
#23 0.826 > next build
2025-Dec-25 13:56:49.124140
#23 0.826
2025-Dec-25 13:56:49.928428
#23 1.631 Attention: Next.js now collects completely anonymous telemetry regarding usage.
2025-Dec-25 13:56:50.071753
#23 1.632 This information is used to shape Next.js' roadmap and prioritize features.
2025-Dec-25 13:56:50.071753
#23 1.635 You can learn more, including how to opt-out if you'd not like to participate in this anonymous program, by visiting the following URL:
2025-Dec-25 13:56:50.071753
#23 1.637 https://nextjs.org/telemetry
2025-Dec-25 13:56:50.071753
#23 1.637
2025-Dec-25 13:56:50.071753
#23 1.652 ▲ Next.js 16.1.0 (Turbopack)
2025-Dec-25 13:56:50.071753
#23 1.653
2025-Dec-25 13:56:50.071753
#23 1.775   Creating an optimized production build ...
2025-Dec-25 13:57:08.761920
#23 20.46 ✓ Compiled successfully in 18.3s
2025-Dec-25 13:57:08.926345
#23 20.48   Running TypeScript ...
2025-Dec-25 13:57:08.935779
2025-Dec-25 13:57:18.496777
#23 30.20   Collecting page data using 1 worker ...
2025-Dec-25 13:57:19.106278
#23 30.81   Generating static pages using 1 worker (0/11) ...
2025-Dec-25 13:57:19.408458
#23 31.11   Generating static pages using 1 worker (2/11)
2025-Dec-25 13:57:19.649514
#23 31.12   Generating static pages using 1 worker (5/11)
2025-Dec-25 13:57:19.649514
#23 31.12   Generating static pages using 1 worker (8/11)
2025-Dec-25 13:57:19.649514
#23 31.18 ✓ Generating static pages using 1 worker (11/11) in 374.8ms
2025-Dec-25 13:57:19.649514
#23 31.19   Finalizing page optimization ...
2025-Dec-25 13:57:19.649514
#23 31.20
2025-Dec-25 13:57:19.649514
#23 31.20 Route (app)
2025-Dec-25 13:57:19.649514
#23 31.20 ┌ ○ /
2025-Dec-25 13:57:19.649514
#23 31.20 ├ ○ /_not-found
2025-Dec-25 13:57:19.649514
#23 31.20 ├ ○ /login
2025-Dec-25 13:57:19.649514
#23 31.20 ├ ○ /org
2025-Dec-25 13:57:19.649514
#23 31.20 ├ ƒ /org/[orgId]/billing
2025-Dec-25 13:57:19.649514
#23 31.20 ├ ƒ /org/[orgId]/projects
2025-Dec-25 13:57:19.649514
#23 31.20 ├ ƒ /org/[orgId]/projects/new
2025-Dec-25 13:57:19.649514
#23 31.20 ├ ƒ /org/[orgId]/settings
2025-Dec-25 13:57:19.649514
#23 31.20 ├ ƒ /org/[orgId]/team
2025-Dec-25 13:57:19.649514
#23 31.20 ├ ○ /projects
2025-Dec-25 13:57:19.649514
#23 31.20 ├ ƒ /projects/[id]
2025-Dec-25 13:57:19.649514
#23 31.20 ├ ƒ /projects/[id]/auth
2025-Dec-25 13:57:19.649514
#23 31.20 ├ ƒ /projects/[id]/backups
2025-Dec-25 13:57:19.649514
#23 31.20 ├ ƒ /projects/[id]/database
2025-Dec-25 13:57:19.649514
#23 31.20 ├ ƒ /projects/[id]/database/[table]
2025-Dec-25 13:57:19.649514
#23 31.20 ├ ƒ /projects/[id]/edge-functions
2025-Dec-25 13:57:19.649514
#23 31.20 ├ ƒ /projects/[id]/logs
2025-Dec-25 13:57:19.649514
#23 31.20 ├ ƒ /projects/[id]/realtime
2025-Dec-25 13:57:19.649514
#23 31.20 ├ ƒ /projects/[id]/secrets
2025-Dec-25 13:57:19.649514
#23 31.20 ├ ƒ /projects/[id]/settings
2025-Dec-25 13:57:19.649514
#23 31.20 ├ ƒ /projects/[id]/settings/deployment
2025-Dec-25 13:57:19.649514
#23 31.20 ├ ƒ /projects/[id]/sql
2025-Dec-25 13:57:19.649514
#23 31.20 ├ ƒ /projects/[id]/storage
2025-Dec-25 13:57:19.649514
#23 31.20 ├ ○ /projects/new
2025-Dec-25 13:57:19.649514
#23 31.20 ├ ○ /settings/organization
2025-Dec-25 13:57:19.649514
#23 31.20 ├ ƒ /settings/organization/[id]
2025-Dec-25 13:57:19.649514
#23 31.20 ├ ○ /settings/profile
2025-Dec-25 13:57:19.649514
#23 31.20 └ ○ /signup
2025-Dec-25 13:57:19.649514
#23 31.20
2025-Dec-25 13:57:19.649514
#23 31.20
2025-Dec-25 13:57:19.649514
#23 31.20 ○  (Static)   prerendered as static content
2025-Dec-25 13:57:19.649514
#23 31.20 ƒ  (Dynamic)  server-rendered on demand
2025-Dec-25 13:57:19.649514
#23 31.20
2025-Dec-25 13:57:19.712958
#23 31.41 npm notice
2025-Dec-25 13:57:19.712958
#23 31.41 npm notice New major version of npm available! 10.8.2 -> 11.7.0
2025-Dec-25 13:57:19.712958
#23 31.41 npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.7.0
2025-Dec-25 13:57:19.712958
#23 31.41 npm notice To update run: npm install -g npm@11.7.0
2025-Dec-25 13:57:19.712958
#23 31.41 npm notice
2025-Dec-25 13:57:19.914549
#23 DONE 31.5s
2025-Dec-25 13:57:24.812021
#24 [dashboard runner 3/6] COPY --from=builder /app/public ./public
2025-Dec-25 13:57:25.002941
#24 DONE 0.0s
2025-Dec-25 13:57:25.002941
2025-Dec-25 13:57:25.002941
#25 [dashboard runner 4/6] COPY --from=builder /app/.next ./.next
2025-Dec-25 13:57:25.046343
#25 DONE 0.2s
2025-Dec-25 13:57:25.203655
#26 [dashboard runner 5/6] COPY --from=builder /app/node_modules ./node_modules
2025-Dec-25 13:57:34.072812
#26 DONE 9.0s
2025-Dec-25 13:57:34.257441
#27 [dashboard runner 6/6] COPY --from=builder /app/package.json ./package.json
2025-Dec-25 13:57:34.257441
#27 DONE 0.0s
2025-Dec-25 13:57:34.257441
2025-Dec-25 13:57:34.257441
#28 [dashboard] exporting to image
2025-Dec-25 13:57:34.257441
#28 exporting layers
2025-Dec-25 13:57:37.712659
#28 exporting layers 3.6s done
2025-Dec-25 13:57:37.780608
#28 writing image sha256:85a4b92c5fd3c7e9f06ee7f6ee5cf5cc4bc37651c3017c7d3dc576dc8e4aec6f done
2025-Dec-25 13:57:37.780608
#28 naming to docker.io/library/hck4w0k4ww8kk4gccw000ggg-dashboard done
2025-Dec-25 13:57:37.780608
#28 DONE 3.6s
2025-Dec-25 13:57:37.780608
2025-Dec-25 13:57:37.780608
#29 [dashboard] resolving provenance for metadata file
2025-Dec-25 13:57:37.780608
#29 DONE 0.0s
2025-Dec-25 13:57:37.789310
api  Built
2025-Dec-25 13:57:37.789310
dashboard  Built
2025-Dec-25 13:57:37.826508
Creating .env file with runtime variables for build phase.
2025-Dec-25 13:57:38.144982
[CMD]: docker exec w048wkk0go4o4wog84kckos4 bash -c 'cat /artifacts/w048wkk0go4o4wog84kckos4/.env'
2025-Dec-25 13:57:38.144982
SOURCE_COMMIT=56c01cf9744516479a759ba36fa3e4b320718c3f
2025-Dec-25 13:57:38.144982
COOLIFY_URL=
2025-Dec-25 13:57:38.144982
COOLIFY_FQDN=
2025-Dec-25 13:57:38.144982
SERVICE_URL_DASHBOARD=https://supalove.hayataxi.online
2025-Dec-25 13:57:38.144982
SERVICE_FQDN_DASHBOARD=supalove.hayataxi.online
2025-Dec-25 13:57:38.144982
SERVICE_URL_API=https://api.hayataxi.online
2025-Dec-25 13:57:38.144982
SERVICE_FQDN_API=api.hayataxi.online
2025-Dec-25 13:57:38.144982
SERVICE_URL_KEYCLOAK=https://auth.hayataxi.online
2025-Dec-25 13:57:38.144982
SERVICE_FQDN_KEYCLOAK=auth.hayataxi.online
2025-Dec-25 13:57:38.144982
SERVICE_URL_MINIO=https://s3.hayataxi.online
2025-Dec-25 13:57:38.144982
SERVICE_FQDN_MINIO=s3.hayataxi.online
2025-Dec-25 13:57:38.144982
SERVICE_NAME_CONTROL-PLANE-DB=control-plane-db
2025-Dec-25 13:57:38.144982
SERVICE_NAME_API=api
2025-Dec-25 13:57:38.144982
SERVICE_NAME_DASHBOARD=dashboard
2025-Dec-25 13:57:38.144982
SERVICE_NAME_KEYCLOAK=keycloak
2025-Dec-25 13:57:38.144982
SERVICE_NAME_MINIO=minio
2025-Dec-25 13:57:38.144982
POSTGRES_USER=platform
2025-Dec-25 13:57:38.144982
POSTGRES_PASSWORD=platform
2025-Dec-25 13:57:38.144982
POSTGRES_DB=control_plane
2025-Dec-25 13:57:38.144982
KEYCLOAK_ADMIN_USER=admin
2025-Dec-25 13:57:38.144982
KEYCLOAK_ADMIN_PASSWORD=admin
2025-Dec-25 13:57:38.144982
MINIO_ROOT_USER=minioadmin
2025-Dec-25 13:57:38.144982
MINIO_ROOT_PASSWORD=minioadmin
2025-Dec-25 13:57:38.144982
URL=http://localhost:8000
2025-Dec-25 13:57:38.144982
NEXT_PUBLIC_API_URL=https://api.hayataxi.online
2025-Dec-25 13:57:38.144982
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8000
2025-Dec-25 13:57:38.144982
HOST=0.0.0.0
2025-Dec-25 13:57:38.272471
Removing old containers.
2025-Dec-25 13:57:38.753543
[CMD]: docker stop --time=30 dashboard-hck4w0k4ww8kk4gccw000ggg-133924677957
2025-Dec-25 13:57:38.753543
dashboard-hck4w0k4ww8kk4gccw000ggg-133924677957
2025-Dec-25 13:57:38.930802
[CMD]: docker rm -f dashboard-hck4w0k4ww8kk4gccw000ggg-133924677957
2025-Dec-25 13:57:38.930802
dashboard-hck4w0k4ww8kk4gccw000ggg-133924677957
2025-Dec-25 13:57:39.558231
[CMD]: docker stop --time=30 api-hck4w0k4ww8kk4gccw000ggg-133924664772
2025-Dec-25 13:57:39.558231
api-hck4w0k4ww8kk4gccw000ggg-133924664772
2025-Dec-25 13:57:39.696051
[CMD]: docker rm -f api-hck4w0k4ww8kk4gccw000ggg-133924664772
2025-Dec-25 13:57:39.696051
api-hck4w0k4ww8kk4gccw000ggg-133924664772
2025-Dec-25 13:57:40.072506
[CMD]: docker stop --time=30 keycloak-hck4w0k4ww8kk4gccw000ggg-133924686692
2025-Dec-25 13:57:40.072506
keycloak-hck4w0k4ww8kk4gccw000ggg-133924686692
2025-Dec-25 13:57:40.309939
[CMD]: docker rm -f keycloak-hck4w0k4ww8kk4gccw000ggg-133924686692
2025-Dec-25 13:57:40.309939
keycloak-hck4w0k4ww8kk4gccw000ggg-133924686692
2025-Dec-25 13:57:40.563549
[CMD]: docker stop --time=30 minio-hck4w0k4ww8kk4gccw000ggg-133924698723
2025-Dec-25 13:57:40.563549
minio-hck4w0k4ww8kk4gccw000ggg-133924698723
2025-Dec-25 13:57:40.711445
[CMD]: docker rm -f minio-hck4w0k4ww8kk4gccw000ggg-133924698723
2025-Dec-25 13:57:40.711445
minio-hck4w0k4ww8kk4gccw000ggg-133924698723
2025-Dec-25 13:57:40.997663
[CMD]: docker stop --time=30 control-plane-db-hck4w0k4ww8kk4gccw000ggg-133924649774
2025-Dec-25 13:57:40.997663
control-plane-db-hck4w0k4ww8kk4gccw000ggg-133924649774
2025-Dec-25 13:57:41.129575
[CMD]: docker rm -f control-plane-db-hck4w0k4ww8kk4gccw000ggg-133924649774
2025-Dec-25 13:57:41.129575
control-plane-db-hck4w0k4ww8kk4gccw000ggg-133924649774
2025-Dec-25 13:57:41.137376
Starting new application.
2025-Dec-25 13:57:41.680299
[CMD]: docker exec w048wkk0go4o4wog84kckos4 bash -c 'SOURCE_COMMIT=56c01cf9744516479a759ba36fa3e4b320718c3f COOLIFY_BRANCH=main COOLIFY_RESOURCE_UUID=hck4w0k4ww8kk4gccw000ggg COOLIFY_CONTAINER_NAME=hck4w0k4ww8kk4gccw000ggg-135532163146  docker compose --env-file /artifacts/w048wkk0go4o4wog84kckos4/.env --project-name hck4w0k4ww8kk4gccw000ggg --project-directory /artifacts/w048wkk0go4o4wog84kckos4 -f /artifacts/w048wkk0go4o4wog84kckos4/docker-compose.coolify.yml up -d'
2025-Dec-25 13:57:41.680299
Container minio-hck4w0k4ww8kk4gccw000ggg-135549972652  Creating
2025-Dec-25 13:57:41.680299
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-135549922244  Creating
2025-Dec-25 13:57:41.735993
Container minio-hck4w0k4ww8kk4gccw000ggg-135549972652  Created
2025-Dec-25 13:57:41.735993
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-135549922244  Created
2025-Dec-25 13:57:41.735993
Container keycloak-hck4w0k4ww8kk4gccw000ggg-135549962525  Creating
2025-Dec-25 13:57:41.756097
Container keycloak-hck4w0k4ww8kk4gccw000ggg-135549962525  Created
2025-Dec-25 13:57:41.756097
Container api-hck4w0k4ww8kk4gccw000ggg-135549935663  Creating
2025-Dec-25 13:57:41.778755
Container api-hck4w0k4ww8kk4gccw000ggg-135549935663  Created
2025-Dec-25 13:57:41.786238
Container dashboard-hck4w0k4ww8kk4gccw000ggg-135549953619  Creating
2025-Dec-25 13:57:41.799001
Container dashboard-hck4w0k4ww8kk4gccw000ggg-135549953619  Created
2025-Dec-25 13:57:41.808467
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-135549922244  Starting
2025-Dec-25 13:57:41.808467
Container minio-hck4w0k4ww8kk4gccw000ggg-135549972652  Starting
2025-Dec-25 13:57:42.105337
Container minio-hck4w0k4ww8kk4gccw000ggg-135549972652  Started
2025-Dec-25 13:57:42.141671
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-135549922244  Started
2025-Dec-25 13:57:42.141671
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-135549922244  Waiting
2025-Dec-25 13:57:47.643656
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-135549922244  Healthy
2025-Dec-25 13:57:47.643656
Container keycloak-hck4w0k4ww8kk4gccw000ggg-135549962525  Starting
2025-Dec-25 13:57:47.866352
Container keycloak-hck4w0k4ww8kk4gccw000ggg-135549962525  Started
2025-Dec-25 13:57:47.866352
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-135549922244  Waiting
2025-Dec-25 13:57:48.368727
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-135549922244  Healthy
2025-Dec-25 13:57:48.368727
Container api-hck4w0k4ww8kk4gccw000ggg-135549935663  Starting
2025-Dec-25 13:57:48.710496
Container api-hck4w0k4ww8kk4gccw000ggg-135549935663  Started
2025-Dec-25 13:57:48.710496
Container dashboard-hck4w0k4ww8kk4gccw000ggg-135549953619  Starting
2025-Dec-25 13:57:49.249682
Container dashboard-hck4w0k4ww8kk4gccw000ggg-135549953619  Started
2025-Dec-25 13:57:49.888205
New container started.
2025-Dec-25 13:57:51.186293
Gracefully shutting down build container: w048wkk0go4o4wog84kckos4
2025-Dec-25 13:57:51.953209
[CMD]: docker stop --time=30 w048wkk0go4o4wog84kckos4
2025-Dec-25 13:57:51.953209
w048wkk0go4o4wog84kckos4
2025-Dec-25 13:57:52.488730
[CMD]: docker rm -f w048wkk0go4o4wog84kckos4
2025-Dec-25 13:57:52.488730
Error response from daemon: removal of container w048wkk0go4o4wog84kckos4 is already in progress