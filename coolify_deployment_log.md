Deployment is Finished.


2025-Dec-25 12:03:09.587666
Starting deployment of supalove to localhost.
2025-Dec-25 12:03:10.211968
Preparing container with helper image: ghcr.io/coollabsio/coolify-helper:1.0.12
2025-Dec-25 12:03:10.561794
[CMD]: docker stop --time=30 fg488844ckk48o4socc0kkog
2025-Dec-25 12:03:10.561794
Error response from daemon: No such container: fg488844ckk48o4socc0kkog
2025-Dec-25 12:03:10.921337
[CMD]: docker rm -f fg488844ckk48o4socc0kkog
2025-Dec-25 12:03:10.921337
Error response from daemon: No such container: fg488844ckk48o4socc0kkog
2025-Dec-25 12:03:11.276865
[CMD]: docker run -d --network coolify --name fg488844ckk48o4socc0kkog  --rm -v /var/run/docker.sock:/var/run/docker.sock ghcr.io/coollabsio/coolify-helper:1.0.12
2025-Dec-25 12:03:11.276865
6604c5af4f0c84d9d4d95cb46efb8e0e024a3353402e6f974627d8d1a56faba7
2025-Dec-25 12:03:12.519686
[CMD]: docker exec fg488844ckk48o4socc0kkog bash -c 'GIT_SSH_COMMAND="ssh -o ConnectTimeout=30 -p 22 -o Port=22 -o LogLevel=ERROR -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" git ls-remote https://github.com/farisnoaman/supalove refs/heads/main'
2025-Dec-25 12:03:12.519686
adfe8fa5a39b856c90990f4b611f7dd2c7068352	refs/heads/main
2025-Dec-25 12:03:12.534600
----------------------------------------
2025-Dec-25 12:03:12.540503
Importing farisnoaman/supalove:main (commit sha adfe8fa5a39b856c90990f4b611f7dd2c7068352) to /artifacts/fg488844ckk48o4socc0kkog.
2025-Dec-25 12:03:12.905744
[CMD]: docker exec fg488844ckk48o4socc0kkog bash -c 'git clone --depth=1 --recurse-submodules --shallow-submodules -b 'main' 'https://github.com/farisnoaman/supalove' '/artifacts/fg488844ckk48o4socc0kkog' && cd '/artifacts/fg488844ckk48o4socc0kkog' && if [ -f .gitmodules ]; then sed -i "s#git@\(.*\):#https://\1/#g" '/artifacts/fg488844ckk48o4socc0kkog'/.gitmodules || true && git submodule sync && GIT_SSH_COMMAND="ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" git submodule update --init --recursive --depth=1; fi && cd '/artifacts/fg488844ckk48o4socc0kkog' && GIT_SSH_COMMAND="ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" git lfs pull'
2025-Dec-25 12:03:12.905744
Cloning into '/artifacts/fg488844ckk48o4socc0kkog'...
2025-Dec-25 12:03:19.091734
Updating files:  24% (3704/15084)
2025-Dec-25 12:03:19.109762
Updating files:  25% (3771/15084)
2025-Dec-25 12:03:19.147016
Updating files:  26% (3922/15084)
2025-Dec-25 12:03:19.206710
Updating files:  27% (4073/15084)
2025-Dec-25 12:03:19.236654
Updating files:  28% (4224/15084)
2025-Dec-25 12:03:19.259476
Updating files:  29% (4375/15084)
2025-Dec-25 12:03:19.278788
Updating files:  30% (4526/15084)
2025-Dec-25 12:03:19.292745
Updating files:  31% (4677/15084)
2025-Dec-25 12:03:19.310793
Updating files:  32% (4827/15084)
2025-Dec-25 12:03:19.324638
Updating files:  33% (4978/15084)
2025-Dec-25 12:03:19.364580
Updating files:  34% (5129/15084)
2025-Dec-25 12:03:19.404506
Updating files:  35% (5280/15084)
2025-Dec-25 12:03:19.460152
Updating files:  36% (5431/15084)
2025-Dec-25 12:03:19.496970
Updating files:  37% (5582/15084)
2025-Dec-25 12:03:19.514271
Updating files:  38% (5732/15084)
2025-Dec-25 12:03:19.532864
Updating files:  39% (5883/15084)
2025-Dec-25 12:03:19.551297
Updating files:  40% (6034/15084)
2025-Dec-25 12:03:19.571185
Updating files:  41% (6185/15084)
2025-Dec-25 12:03:19.591159
Updating files:  42% (6336/15084)
2025-Dec-25 12:03:19.603576
Updating files:  43% (6487/15084)
2025-Dec-25 12:03:19.616241
Updating files:  44% (6637/15084)
2025-Dec-25 12:03:19.628705
Updating files:  45% (6788/15084)
2025-Dec-25 12:03:19.644816
Updating files:  46% (6939/15084)
2025-Dec-25 12:03:19.658028
Updating files:  47% (7090/15084)
2025-Dec-25 12:03:19.669685
Updating files:  48% (7241/15084)
2025-Dec-25 12:03:19.681902
Updating files:  49% (7392/15084)
2025-Dec-25 12:03:19.693548
Updating files:  50% (7542/15084)
2025-Dec-25 12:03:19.704927
Updating files:  51% (7693/15084)
2025-Dec-25 12:03:19.718770
Updating files:  52% (7844/15084)
2025-Dec-25 12:03:19.731158
Updating files:  53% (7995/15084)
2025-Dec-25 12:03:19.747839
Updating files:  54% (8146/15084)
2025-Dec-25 12:03:19.843185
Updating files:  55% (8297/15084)
2025-Dec-25 12:03:19.879842
Updating files:  56% (8448/15084)
2025-Dec-25 12:03:19.891539
Updating files:  57% (8598/15084)
2025-Dec-25 12:03:19.905393
Updating files:  58% (8749/15084)
2025-Dec-25 12:03:19.927206
Updating files:  59% (8900/15084)
2025-Dec-25 12:03:19.939847
Updating files:  60% (9051/15084)
2025-Dec-25 12:03:19.958430
Updating files:  61% (9202/15084)
2025-Dec-25 12:03:19.973872
Updating files:  62% (9353/15084)
2025-Dec-25 12:03:19.985722
Updating files:  63% (9503/15084)
2025-Dec-25 12:03:19.999176
Updating files:  64% (9654/15084)
2025-Dec-25 12:03:20.078959
Updating files:  65% (9805/15084)
2025-Dec-25 12:03:20.091437
Updating files:  65% (9953/15084)
Updating files:  66% (9956/15084)
2025-Dec-25 12:03:20.104706
Updating files:  67% (10107/15084)
2025-Dec-25 12:03:20.123615
Updating files:  68% (10258/15084)
2025-Dec-25 12:03:20.143134
Updating files:  69% (10408/15084)
2025-Dec-25 12:03:20.159590
Updating files:  70% (10559/15084)
2025-Dec-25 12:03:20.173378
Updating files:  71% (10710/15084)
2025-Dec-25 12:03:20.189399
Updating files:  72% (10861/15084)
2025-Dec-25 12:03:20.203545
Updating files:  73% (11012/15084)
2025-Dec-25 12:03:20.219614
Updating files:  74% (11163/15084)
2025-Dec-25 12:03:20.242643
Updating files:  75% (11313/15084)
2025-Dec-25 12:03:20.264984
Updating files:  76% (11464/15084)
2025-Dec-25 12:03:20.281690
Updating files:  77% (11615/15084)
2025-Dec-25 12:03:20.295681
Updating files:  78% (11766/15084)
2025-Dec-25 12:03:20.308999
Updating files:  79% (11917/15084)
2025-Dec-25 12:03:20.380962
Updating files:  80% (12068/15084)
2025-Dec-25 12:03:20.403521
Updating files:  81% (12219/15084)
2025-Dec-25 12:03:20.477049
Updating files:  82% (12369/15084)
2025-Dec-25 12:03:20.491499
Updating files:  83% (12520/15084)
2025-Dec-25 12:03:20.508579
Updating files:  84% (12671/15084)
2025-Dec-25 12:03:20.531612
Updating files:  85% (12822/15084)
2025-Dec-25 12:03:20.545811
Updating files:  86% (12973/15084)
2025-Dec-25 12:03:20.561611
Updating files:  87% (13124/15084)
2025-Dec-25 12:03:20.604549
Updating files:  88% (13274/15084)
2025-Dec-25 12:03:20.627157
Updating files:  89% (13425/15084)
2025-Dec-25 12:03:20.657766
Updating files:  90% (13576/15084)
2025-Dec-25 12:03:20.683367
Updating files:  91% (13727/15084)
2025-Dec-25 12:03:20.695042
Updating files:  92% (13878/15084)
2025-Dec-25 12:03:20.708219
Updating files:  93% (14029/15084)
2025-Dec-25 12:03:20.808109
Updating files:  94% (14179/15084)
2025-Dec-25 12:03:20.842585
Updating files:  95% (14330/15084)
2025-Dec-25 12:03:20.867237
Updating files:  96% (14481/15084)
2025-Dec-25 12:03:20.890924
Updating files:  97% (14632/15084)
2025-Dec-25 12:03:20.909444
Updating files:  98% (14783/15084)
2025-Dec-25 12:03:20.935599
Updating files:  99% (14934/15084)
2025-Dec-25 12:03:20.949181
Updating files: 100% (15084/15084)
Updating files: 100% (15084/15084), done.
2025-Dec-25 12:03:22.167383
[CMD]: docker exec fg488844ckk48o4socc0kkog bash -c 'cd /artifacts/fg488844ckk48o4socc0kkog && git log -1 adfe8fa5a39b856c90990f4b611f7dd2c7068352 --pretty=%B'
2025-Dec-25 12:03:22.167383
feat: Add service `expose` configurations to docker-compose and create `coolify_deployment_log.md`.
2025-Dec-25 12:03:30.486691
[CMD]: docker exec fg488844ckk48o4socc0kkog bash -c 'test -f /artifacts/fg488844ckk48o4socc0kkog/control-plane/api/Dockerfile && echo 'exists' || echo 'not found''
2025-Dec-25 12:03:30.486691
exists
2025-Dec-25 12:03:31.100679
[CMD]: docker exec fg488844ckk48o4socc0kkog bash -c 'cat /artifacts/fg488844ckk48o4socc0kkog/control-plane/api/Dockerfile'
2025-Dec-25 12:03:31.100679
FROM python:3.12-slim
2025-Dec-25 12:03:31.100679
WORKDIR /app
2025-Dec-25 12:03:31.100679
COPY requirements.txt .
2025-Dec-25 12:03:31.100679
RUN pip install -r requirements.txt
2025-Dec-25 12:03:31.100679
COPY . .
2025-Dec-25 12:03:31.100679
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
2025-Dec-25 12:03:31.638128
Added 20 ARG declarations to Dockerfile for service api.
2025-Dec-25 12:03:32.021005
[CMD]: docker exec fg488844ckk48o4socc0kkog bash -c 'test -f /artifacts/fg488844ckk48o4socc0kkog/dashboard/Dockerfile && echo 'exists' || echo 'not found''
2025-Dec-25 12:03:32.021005
exists
2025-Dec-25 12:03:32.479013
[CMD]: docker exec fg488844ckk48o4socc0kkog bash -c 'cat /artifacts/fg488844ckk48o4socc0kkog/dashboard/Dockerfile'
2025-Dec-25 12:03:32.479013
# Stage 1: Dependencies
2025-Dec-25 12:03:32.479013
FROM node:20-alpine AS deps
2025-Dec-25 12:03:32.479013
WORKDIR /app
2025-Dec-25 12:03:32.479013
COPY package*.json ./
2025-Dec-25 12:03:32.479013
RUN npm install
2025-Dec-25 12:03:32.479013
2025-Dec-25 12:03:32.479013
# Stage 2: Builder
2025-Dec-25 12:03:32.479013
FROM node:20-alpine AS builder
2025-Dec-25 12:03:32.479013
WORKDIR /app
2025-Dec-25 12:03:32.479013
COPY --from=deps /app/node_modules ./node_modules
2025-Dec-25 12:03:32.479013
COPY . .
2025-Dec-25 12:03:32.479013
# Set environment variables for build if needed (e.g. backend URL)
2025-Dec-25 12:03:32.479013
# For Next.js client-side fetch, it might need to know the URL at build time if pre-rendering,
2025-Dec-25 12:03:32.479013
# but we are using "use client" so it's fine.
2025-Dec-25 12:03:32.479013
ARG NEXT_PUBLIC_API_URL
2025-Dec-25 12:03:32.479013
ENV NEXT_PUBLIC_API_URL=${NEXT_PUBLIC_API_URL}
2025-Dec-25 12:03:32.479013
RUN npm run build
2025-Dec-25 12:03:32.479013
2025-Dec-25 12:03:32.479013
# Stage 3: Runner
2025-Dec-25 12:03:32.479013
FROM node:20-alpine AS runner
2025-Dec-25 12:03:32.479013
WORKDIR /app
2025-Dec-25 12:03:32.479013
ENV NODE_ENV=production
2025-Dec-25 12:03:32.479013
COPY --from=builder /app/public ./public
2025-Dec-25 12:03:32.479013
COPY --from=builder /app/.next ./.next
2025-Dec-25 12:03:32.479013
COPY --from=builder /app/node_modules ./node_modules
2025-Dec-25 12:03:32.479013
COPY --from=builder /app/package.json ./package.json
2025-Dec-25 12:03:32.479013
2025-Dec-25 12:03:32.479013
EXPOSE 3000
2025-Dec-25 12:03:32.479013
CMD ["npm", "start"]
2025-Dec-25 12:03:32.875520
Added 60 ARG declarations to Dockerfile for service dashboard (multi-stage build, added to 3 stages).
2025-Dec-25 12:03:32.887115
Pulling & building required images.
2025-Dec-25 12:03:32.921751
Creating build-time .env file in /artifacts (outside Docker context).
2025-Dec-25 12:03:33.752603
[CMD]: docker exec fg488844ckk48o4socc0kkog bash -c 'cat /artifacts/build-time.env'
2025-Dec-25 12:03:33.752603
SOURCE_COMMIT='adfe8fa5a39b856c90990f4b611f7dd2c7068352'
2025-Dec-25 12:03:33.752603
COOLIFY_URL=''
2025-Dec-25 12:03:33.752603
COOLIFY_FQDN=''
2025-Dec-25 12:03:33.752603
SERVICE_NAME_CONTROL-PLANE-DB='control-plane-db'
2025-Dec-25 12:03:33.752603
SERVICE_NAME_API='api'
2025-Dec-25 12:03:33.752603
SERVICE_NAME_DASHBOARD='dashboard'
2025-Dec-25 12:03:33.752603
SERVICE_NAME_KEYCLOAK='keycloak'
2025-Dec-25 12:03:33.752603
SERVICE_NAME_MINIO='minio'
2025-Dec-25 12:03:33.752603
SERVICE_URL_DASHBOARD='https://supalove.hayataxi.online'
2025-Dec-25 12:03:33.752603
SERVICE_FQDN_DASHBOARD='supalove.hayataxi.online'
2025-Dec-25 12:03:33.752603
SERVICE_URL_API='https://api.hayataxi.online'
2025-Dec-25 12:03:33.752603
SERVICE_FQDN_API='api.hayataxi.online'
2025-Dec-25 12:03:33.752603
SERVICE_URL_KEYCLOAK='https://auth.hayataxi.online'
2025-Dec-25 12:03:33.752603
SERVICE_FQDN_KEYCLOAK='auth.hayataxi.online'
2025-Dec-25 12:03:33.752603
SERVICE_URL_MINIO='https://s3.hayataxi.online'
2025-Dec-25 12:03:33.752603
SERVICE_FQDN_MINIO='s3.hayataxi.online'
2025-Dec-25 12:03:33.752603
KEYCLOAK_ADMIN_PASSWORD="admin"
2025-Dec-25 12:03:33.752603
KEYCLOAK_ADMIN_USER="admin"
2025-Dec-25 12:03:33.752603
MINIO_ROOT_PASSWORD="minioadmin"
2025-Dec-25 12:03:33.752603
MINIO_ROOT_USER="minioadmin"
2025-Dec-25 12:03:33.752603
NEXT_PUBLIC_API_URL="https://api.hayataxi.online"
2025-Dec-25 12:03:33.752603
POSTGRES_DB="control_plane"
2025-Dec-25 12:03:33.752603
POSTGRES_PASSWORD="platform"
2025-Dec-25 12:03:33.752603
POSTGRES_USER="platform"
2025-Dec-25 12:03:33.752603
URL="http://localhost:8000"
2025-Dec-25 12:03:33.764534
Adding build arguments to Docker Compose build command.
2025-Dec-25 12:03:34.340305
[CMD]: docker exec fg488844ckk48o4socc0kkog bash -c 'SOURCE_COMMIT=adfe8fa5a39b856c90990f4b611f7dd2c7068352 COOLIFY_BRANCH=main COOLIFY_RESOURCE_UUID=hck4w0k4ww8kk4gccw000ggg COOLIFY_CONTAINER_NAME=hck4w0k4ww8kk4gccw000ggg-120309019930  docker compose --env-file /artifacts/build-time.env --project-name hck4w0k4ww8kk4gccw000ggg --project-directory /artifacts/fg488844ckk48o4socc0kkog -f /artifacts/fg488844ckk48o4socc0kkog/docker-compose.coolify.yml build --pull --no-cache --build-arg SOURCE_COMMIT --build-arg COOLIFY_URL --build-arg COOLIFY_FQDN --build-arg SERVICE_FQDN_API --build-arg SERVICE_FQDN_DASHBOARD --build-arg SERVICE_FQDN_KEYCLOAK --build-arg SERVICE_FQDN_MINIO --build-arg SERVICE_URL_API --build-arg SERVICE_URL_DASHBOARD --build-arg SERVICE_URL_KEYCLOAK --build-arg SERVICE_URL_MINIO --build-arg KEYCLOAK_ADMIN_PASSWORD --build-arg KEYCLOAK_ADMIN_USER --build-arg MINIO_ROOT_PASSWORD --build-arg MINIO_ROOT_USER --build-arg NEXT_PUBLIC_API_URL --build-arg POSTGRES_DB --build-arg POSTGRES_PASSWORD --build-arg POSTGRES_USER --build-arg URL --build-arg COOLIFY_BUILD_SECRETS_HASH=4c819fa5df5c04789c5f7cb9aa73b6cace616eda24902a18c85abe1870744a87'
2025-Dec-25 12:03:34.340305
#1 [internal] load local bake definitions
2025-Dec-25 12:03:34.447355
#1 reading from stdin 3.07kB done
2025-Dec-25 12:03:34.447355
#1 DONE 0.0s
2025-Dec-25 12:03:34.447355
2025-Dec-25 12:03:34.447355
#2 [dashboard internal] load build definition from Dockerfile
2025-Dec-25 12:03:34.447355
#2 transferring dockerfile: 2.14kB done
2025-Dec-25 12:03:34.633797
#2 DONE 0.0s
2025-Dec-25 12:03:34.633797
2025-Dec-25 12:03:34.633797
#3 [api internal] load build definition from Dockerfile
2025-Dec-25 12:03:34.633797
#3 transferring dockerfile: 638B done
2025-Dec-25 12:03:34.633797
#3 DONE 0.0s
2025-Dec-25 12:03:34.633797
2025-Dec-25 12:03:34.633797
#4 [dashboard internal] load metadata for docker.io/library/node:20-alpine
2025-Dec-25 12:03:35.132710
#4 ...
2025-Dec-25 12:03:35.137758
#5 [api internal] load metadata for docker.io/library/python:3.12-slim
2025-Dec-25 12:03:35.137758
#5 DONE 0.6s
2025-Dec-25 12:03:35.242672
#6 [api internal] load .dockerignore
2025-Dec-25 12:03:35.242672
#6 transferring context: 2B done
2025-Dec-25 12:03:35.242672
#6 DONE 0.0s
2025-Dec-25 12:03:35.242672
2025-Dec-25 12:03:35.242672
#7 [api 1/5] FROM docker.io/library/python:3.12-slim@sha256:fa48eefe2146644c2308b909d6bb7651a768178f84fc9550dcd495e4d6d84d01
2025-Dec-25 12:03:35.242672
#7 DONE 0.0s
2025-Dec-25 12:03:35.242672
2025-Dec-25 12:03:35.242672
#8 [api 2/5] WORKDIR /app
2025-Dec-25 12:03:35.242672
#8 CACHED
2025-Dec-25 12:03:35.242672
2025-Dec-25 12:03:35.242672
#4 [dashboard internal] load metadata for docker.io/library/node:20-alpine
2025-Dec-25 12:03:35.341742
#4 DONE 0.8s
2025-Dec-25 12:03:35.341742
2025-Dec-25 12:03:35.341742
#9 [dashboard internal] load .dockerignore
2025-Dec-25 12:03:35.341742
#9 transferring context: 2B done
2025-Dec-25 12:03:35.341742
#9 DONE 0.0s
2025-Dec-25 12:03:35.341742
2025-Dec-25 12:03:35.341742
#10 [dashboard deps 1/4] FROM docker.io/library/node:20-alpine@sha256:658d0f63e501824d6c23e06d4bb95c71e7d704537c9d9272f488ac03a370d448
2025-Dec-25 12:03:35.341742
#10 DONE 0.0s
2025-Dec-25 12:03:35.341742
2025-Dec-25 12:03:35.341742
#11 [dashboard deps 2/4] WORKDIR /app
2025-Dec-25 12:03:35.341742
#11 CACHED
2025-Dec-25 12:03:35.341742
2025-Dec-25 12:03:35.341742
#12 [dashboard internal] load build context
2025-Dec-25 12:03:35.341742
#12 transferring context: 837.63kB 0.1s done
2025-Dec-25 12:03:35.341742
#12 DONE 0.1s
2025-Dec-25 12:03:35.341742
2025-Dec-25 12:03:35.341742
#13 [dashboard deps 3/4] COPY package*.json ./
2025-Dec-25 12:03:35.466694
#13 DONE 0.1s
2025-Dec-25 12:03:35.466694
2025-Dec-25 12:03:35.466694
#14 [api internal] load build context
2025-Dec-25 12:03:40.352154
#14 transferring context: 251.35MB 5.2s
2025-Dec-25 12:03:42.210836
#14 transferring context: 330.52MB 7.0s done
2025-Dec-25 12:03:42.416345
#14 DONE 7.1s
2025-Dec-25 12:03:42.416345
2025-Dec-25 12:03:42.416345
#15 [api 3/5] COPY requirements.txt .
2025-Dec-25 12:03:42.635260
#15 DONE 0.4s
2025-Dec-25 12:03:42.635260
2025-Dec-25 12:03:42.635260
#16 [dashboard deps 4/4] RUN npm install
2025-Dec-25 12:03:42.788063
#16 ...
2025-Dec-25 12:03:42.788063
2025-Dec-25 12:03:42.788063
#17 [api 4/5] RUN pip install -r requirements.txt
2025-Dec-25 12:03:45.648316
#17 3.013 Collecting fastapi (from -r requirements.txt (line 1))
2025-Dec-25 12:03:45.840464
#17 3.203   Downloading fastapi-0.127.0-py3-none-any.whl.metadata (30 kB)
2025-Dec-25 12:03:46.217517
#17 3.583 Collecting sqlalchemy (from -r requirements.txt (line 3))
2025-Dec-25 12:03:46.343670
#17 3.588   Downloading sqlalchemy-2.0.45-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (9.5 kB)
2025-Dec-25 12:03:46.343670
#17 3.662 Collecting psycopg2-binary (from -r requirements.txt (line 4))
2025-Dec-25 12:03:46.343670
#17 3.669   Downloading psycopg2_binary-2.9.11-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (4.9 kB)
2025-Dec-25 12:03:46.343670
#17 3.709 Collecting httpx (from -r requirements.txt (line 5))
2025-Dec-25 12:03:46.455821
#17 3.715   Downloading httpx-0.28.1-py3-none-any.whl.metadata (7.1 kB)
2025-Dec-25 12:03:46.455821
#17 3.755 Collecting python-keycloak (from -r requirements.txt (line 6))
2025-Dec-25 12:03:46.455821
#17 3.763   Downloading python_keycloak-5.8.1-py3-none-any.whl.metadata (6.0 kB)
2025-Dec-25 12:03:46.455821
#17 3.821 Collecting minio (from -r requirements.txt (line 7))
2025-Dec-25 12:03:46.574799
#17 3.826   Downloading minio-7.2.20-py3-none-any.whl.metadata (6.5 kB)
2025-Dec-25 12:03:46.574799
#17 3.878 Collecting requests (from -r requirements.txt (line 8))
2025-Dec-25 12:03:46.574799
#17 3.888   Downloading requests-2.32.5-py3-none-any.whl.metadata (4.9 kB)
2025-Dec-25 12:03:46.574799
#17 3.934 Collecting python-dotenv (from -r requirements.txt (line 9))
2025-Dec-25 12:03:46.686395
#17 3.941   Downloading python_dotenv-1.2.1-py3-none-any.whl.metadata (25 kB)
2025-Dec-25 12:03:46.686395
#17 3.991 Collecting uvicorn[standard] (from -r requirements.txt (line 2))
2025-Dec-25 12:03:46.686395
#17 3.999   Downloading uvicorn-0.40.0-py3-none-any.whl.metadata (6.7 kB)
2025-Dec-25 12:03:46.686395
#17 4.027 Collecting passlib[bcrypt] (from -r requirements.txt (line 10))
2025-Dec-25 12:03:46.686395
#17 4.030   Downloading passlib-1.7.4-py2.py3-none-any.whl.metadata (1.7 kB)
2025-Dec-25 12:03:46.686395
#17 4.051 Collecting python-jose[cryptography] (from -r requirements.txt (line 11))
2025-Dec-25 12:03:46.900612
#17 4.059   Downloading python_jose-3.5.0-py2.py3-none-any.whl.metadata (5.5 kB)
2025-Dec-25 12:03:46.900612
#17 4.110 Collecting starlette<0.51.0,>=0.40.0 (from fastapi->-r requirements.txt (line 1))
2025-Dec-25 12:03:46.900612
#17 4.119   Downloading starlette-0.50.0-py3-none-any.whl.metadata (6.3 kB)
2025-Dec-25 12:03:46.900612
#17 4.264 Collecting pydantic>=2.7.0 (from fastapi->-r requirements.txt (line 1))
2025-Dec-25 12:03:47.010399
#17 4.289   Downloading pydantic-2.12.5-py3-none-any.whl.metadata (90 kB)
2025-Dec-25 12:03:47.010399
#17 4.321 Collecting typing-extensions>=4.8.0 (from fastapi->-r requirements.txt (line 1))
2025-Dec-25 12:03:47.016730
#17 4.326   Downloading typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
2025-Dec-25 12:03:47.016730
#17 4.341 Collecting annotated-doc>=0.0.2 (from fastapi->-r requirements.txt (line 1))
2025-Dec-25 12:03:47.016730
#17 4.345   Downloading annotated_doc-0.0.4-py3-none-any.whl.metadata (6.6 kB)
2025-Dec-25 12:03:47.016730
#17 4.376 Collecting click>=7.0 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 12:03:47.126461
#17 4.386   Downloading click-8.3.1-py3-none-any.whl.metadata (2.6 kB)
2025-Dec-25 12:03:47.126461
#17 4.409 Collecting h11>=0.8 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 12:03:47.126461
#17 4.413   Downloading h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
2025-Dec-25 12:03:47.126461
#17 4.450 Collecting httptools>=0.6.3 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 12:03:47.126461
#17 4.454   Downloading httptools-0.7.1-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (3.5 kB)
2025-Dec-25 12:03:47.126461
#17 4.491 Collecting pyyaml>=5.1 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 12:03:47.267534
#17 4.497   Downloading pyyaml-6.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.4 kB)
2025-Dec-25 12:03:47.267534
#17 4.546 Collecting uvloop>=0.15.1 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 12:03:47.267534
#17 4.551   Downloading uvloop-0.22.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (4.9 kB)
2025-Dec-25 12:03:47.267534
#17 4.626 Collecting watchfiles>=0.13 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 12:03:47.372126
#17 4.633   Downloading watchfiles-1.1.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.9 kB)
2025-Dec-25 12:03:47.372126
#17 4.737 Collecting websockets>=10.4 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 12:03:47.531962
#17 4.743   Downloading websockets-15.0.1-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.8 kB)
2025-Dec-25 12:03:47.599598
#17 4.964 Collecting greenlet>=1 (from sqlalchemy->-r requirements.txt (line 3))
2025-Dec-25 12:03:47.712118
#17 4.972   Downloading greenlet-3.3.0-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (4.1 kB)
2025-Dec-25 12:03:47.712118
#17 5.005 Collecting anyio (from httpx->-r requirements.txt (line 5))
2025-Dec-25 12:03:47.712118
#17 5.008   Downloading anyio-4.12.0-py3-none-any.whl.metadata (4.3 kB)
2025-Dec-25 12:03:47.712118
#17 5.037 Collecting certifi (from httpx->-r requirements.txt (line 5))
2025-Dec-25 12:03:47.712118
#17 5.041   Downloading certifi-2025.11.12-py3-none-any.whl.metadata (2.5 kB)
2025-Dec-25 12:03:47.712118
#17 5.076 Collecting httpcore==1.* (from httpx->-r requirements.txt (line 5))
2025-Dec-25 12:03:47.722951
2025-Dec-25 12:03:47.840267
#17 5.084   Downloading httpcore-1.0.9-py3-none-any.whl.metadata (21 kB)
2025-Dec-25 12:03:47.840267
#17 5.124 Collecting idna (from httpx->-r requirements.txt (line 5))
2025-Dec-25 12:03:47.840267
#17 5.129   Downloading idna-3.11-py3-none-any.whl.metadata (8.4 kB)
2025-Dec-25 12:03:47.851156
#17 5.167 Collecting aiofiles>=24.1.0 (from python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 12:03:47.851156
#17 5.173   Downloading aiofiles-25.1.0-py3-none-any.whl.metadata (6.3 kB)
2025-Dec-25 12:03:47.851156
#17 5.204 Collecting async-property>=0.2.2 (from python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 12:03:47.959830
#17 5.212   Downloading async_property-0.2.2-py2.py3-none-any.whl.metadata (5.3 kB)
2025-Dec-25 12:03:47.967744
#17 5.240 Collecting deprecation>=2.1.0 (from python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 12:03:47.967744
#17 5.244   Downloading deprecation-2.1.0-py2.py3-none-any.whl.metadata (4.6 kB)
2025-Dec-25 12:03:47.967744
#17 5.268 Collecting jwcrypto>=1.5.4 (from python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 12:03:47.967744
#17 5.273   Downloading jwcrypto-1.5.6-py3-none-any.whl.metadata (3.1 kB)
2025-Dec-25 12:03:47.967744
#17 5.299 Collecting requests-toolbelt>=0.6.0 (from python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 12:03:47.967744
#17 5.302   Downloading requests_toolbelt-1.0.0-py2.py3-none-any.whl.metadata (14 kB)
2025-Dec-25 12:03:47.967744
#17 5.326 Collecting argon2-cffi (from minio->-r requirements.txt (line 7))
2025-Dec-25 12:03:48.076390
#17 5.331   Downloading argon2_cffi-25.1.0-py3-none-any.whl.metadata (4.1 kB)
2025-Dec-25 12:03:48.076390
#17 5.406 Collecting pycryptodome (from minio->-r requirements.txt (line 7))
2025-Dec-25 12:03:48.076390
#17 5.412   Downloading pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (3.4 kB)
2025-Dec-25 12:03:48.076390
#17 5.442 Collecting urllib3 (from minio->-r requirements.txt (line 7))
2025-Dec-25 12:03:48.247955
#17 5.449   Downloading urllib3-2.6.2-py3-none-any.whl.metadata (6.6 kB)
2025-Dec-25 12:03:48.247955
#17 5.532 Collecting charset_normalizer<4,>=2 (from requests->-r requirements.txt (line 8))
2025-Dec-25 12:03:48.247955
#17 5.536   Downloading charset_normalizer-3.4.4-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (37 kB)
2025-Dec-25 12:03:48.247955
#17 5.613 Collecting bcrypt>=3.1.0 (from passlib[bcrypt]->-r requirements.txt (line 10))
2025-Dec-25 12:03:48.359725
#17 5.617   Downloading bcrypt-5.0.0-cp39-abi3-manylinux_2_34_x86_64.whl.metadata (10 kB)
2025-Dec-25 12:03:48.359725
#17 5.645 Collecting ecdsa!=0.15 (from python-jose[cryptography]->-r requirements.txt (line 11))
2025-Dec-25 12:03:48.359725
#17 5.652   Downloading ecdsa-0.19.1-py2.py3-none-any.whl.metadata (29 kB)
2025-Dec-25 12:03:48.359725
#17 5.683 Collecting rsa!=4.1.1,!=4.4,<5.0,>=4.0 (from python-jose[cryptography]->-r requirements.txt (line 11))
2025-Dec-25 12:03:48.359725
#17 5.692   Downloading rsa-4.9.1-py3-none-any.whl.metadata (5.6 kB)
2025-Dec-25 12:03:48.359725
#17 5.724 Collecting pyasn1>=0.5.0 (from python-jose[cryptography]->-r requirements.txt (line 11))
2025-Dec-25 12:03:48.515254
#17 5.728   Downloading pyasn1-0.6.1-py3-none-any.whl.metadata (8.4 kB)
2025-Dec-25 12:03:48.601944
#17 5.965 Collecting cryptography>=3.4.0 (from python-jose[cryptography]->-r requirements.txt (line 11))
2025-Dec-25 12:03:48.763543
#17 5.975   Downloading cryptography-46.0.3-cp311-abi3-manylinux_2_34_x86_64.whl.metadata (5.7 kB)
2025-Dec-25 12:03:48.772666
#17 6.137 Collecting cffi>=2.0.0 (from cryptography>=3.4.0->python-jose[cryptography]->-r requirements.txt (line 11))
2025-Dec-25 12:03:48.873865
#17 6.141   Downloading cffi-2.0.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (2.6 kB)
2025-Dec-25 12:03:48.873865
#17 6.179 Collecting packaging (from deprecation>=2.1.0->python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 12:03:48.873865
#17 6.182   Downloading packaging-25.0-py3-none-any.whl.metadata (3.3 kB)
2025-Dec-25 12:03:48.873865
#17 6.204 Collecting six>=1.9.0 (from ecdsa!=0.15->python-jose[cryptography]->-r requirements.txt (line 11))
2025-Dec-25 12:03:48.873865
#17 6.208   Downloading six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
2025-Dec-25 12:03:48.873865
#17 6.236 Collecting annotated-types>=0.6.0 (from pydantic>=2.7.0->fastapi->-r requirements.txt (line 1))
2025-Dec-25 12:03:48.873865
#17 6.239   Downloading annotated_types-0.7.0-py3-none-any.whl.metadata (15 kB)
2025-Dec-25 12:03:49.717059
#17 7.083 Collecting pydantic-core==2.41.5 (from pydantic>=2.7.0->fastapi->-r requirements.txt (line 1))
2025-Dec-25 12:03:49.821928
#17 7.090   Downloading pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (7.3 kB)
2025-Dec-25 12:03:49.821928
#17 7.118 Collecting typing-inspection>=0.4.2 (from pydantic>=2.7.0->fastapi->-r requirements.txt (line 1))
2025-Dec-25 12:03:49.821928
#17 7.121   Downloading typing_inspection-0.4.2-py3-none-any.whl.metadata (2.6 kB)
2025-Dec-25 12:03:49.821928
#17 7.187 Collecting argon2-cffi-bindings (from argon2-cffi->minio->-r requirements.txt (line 7))
2025-Dec-25 12:03:49.947504
#17 7.192   Downloading argon2_cffi_bindings-25.1.0-cp39-abi3-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl.metadata (7.4 kB)
2025-Dec-25 12:03:49.947504
#17 7.226 Collecting pycparser (from cffi>=2.0.0->cryptography>=3.4.0->python-jose[cryptography]->-r requirements.txt (line 11))
2025-Dec-25 12:03:49.947504
#17 7.231   Downloading pycparser-2.23-py3-none-any.whl.metadata (993 bytes)
2025-Dec-25 12:03:49.947504
#17 7.257 Downloading fastapi-0.127.0-py3-none-any.whl (112 kB)
2025-Dec-25 12:03:49.947504
#17 7.265 Downloading sqlalchemy-2.0.45-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (3.3 MB)
2025-Dec-25 12:03:49.947504
#17 7.312    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.3/3.3 MB 73.5 MB/s eta 0:00:00
2025-Dec-25 12:03:50.053715
#17 7.323 Downloading psycopg2_binary-2.9.11-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (4.2 MB)
2025-Dec-25 12:03:50.053715
#17 7.382    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.2/4.2 MB 71.3 MB/s eta 0:00:00
2025-Dec-25 12:03:50.053715
#17 7.385 Downloading httpx-0.28.1-py3-none-any.whl (73 kB)
2025-Dec-25 12:03:50.053715
#17 7.393 Downloading httpcore-1.0.9-py3-none-any.whl (78 kB)
2025-Dec-25 12:03:50.053715
#17 7.401 Downloading python_keycloak-5.8.1-py3-none-any.whl (77 kB)
2025-Dec-25 12:03:50.053715
#17 7.410 Downloading minio-7.2.20-py3-none-any.whl (93 kB)
2025-Dec-25 12:03:50.053715
#17 7.419 Downloading requests-2.32.5-py3-none-any.whl (64 kB)
2025-Dec-25 12:03:50.172191
#17 7.436 Downloading python_dotenv-1.2.1-py3-none-any.whl (21 kB)
2025-Dec-25 12:03:50.172191
#17 7.448 Downloading aiofiles-25.1.0-py3-none-any.whl (14 kB)
2025-Dec-25 12:03:50.172191
#17 7.457 Downloading annotated_doc-0.0.4-py3-none-any.whl (5.3 kB)
2025-Dec-25 12:03:50.172191
#17 7.464 Downloading async_property-0.2.2-py2.py3-none-any.whl (9.5 kB)
2025-Dec-25 12:03:50.172191
#17 7.474 Downloading bcrypt-5.0.0-cp39-abi3-manylinux_2_34_x86_64.whl (278 kB)
2025-Dec-25 12:03:50.172191
#17 7.489 Downloading certifi-2025.11.12-py3-none-any.whl (159 kB)
2025-Dec-25 12:03:50.172191
#17 7.514 Downloading charset_normalizer-3.4.4-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (153 kB)
2025-Dec-25 12:03:50.172191
#17 7.533 Downloading click-8.3.1-py3-none-any.whl (108 kB)
2025-Dec-25 12:03:50.282893
#17 7.555 Downloading cryptography-46.0.3-cp311-abi3-manylinux_2_34_x86_64.whl (4.5 MB)
2025-Dec-25 12:03:50.282893
#17 7.615    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.5/4.5 MB 82.0 MB/s eta 0:00:00
2025-Dec-25 12:03:50.282893
#17 7.618 Downloading deprecation-2.1.0-py2.py3-none-any.whl (11 kB)
2025-Dec-25 12:03:50.282893
#17 7.630 Downloading ecdsa-0.19.1-py2.py3-none-any.whl (150 kB)
2025-Dec-25 12:03:50.282893
#17 7.646 Downloading greenlet-3.3.0-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (609 kB)
2025-Dec-25 12:03:50.391003
#17 7.664    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 609.9/609.9 kB 32.8 MB/s eta 0:00:00
2025-Dec-25 12:03:50.391003
#17 7.668 Downloading h11-0.16.0-py3-none-any.whl (37 kB)
2025-Dec-25 12:03:50.391003
#17 7.680 Downloading httptools-0.7.1-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (517 kB)
2025-Dec-25 12:03:50.391003
#17 7.701 Downloading idna-3.11-py3-none-any.whl (71 kB)
2025-Dec-25 12:03:50.391003
#17 7.716 Downloading jwcrypto-1.5.6-py3-none-any.whl (92 kB)
2025-Dec-25 12:03:50.391003
#17 7.728 Downloading pyasn1-0.6.1-py3-none-any.whl (83 kB)
2025-Dec-25 12:03:50.391003
#17 7.741 Downloading pydantic-2.12.5-py3-none-any.whl (463 kB)
2025-Dec-25 12:03:50.391003
#17 7.756 Downloading pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.1 MB)
2025-Dec-25 12:03:50.504117
#17 7.799    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 62.9 MB/s eta 0:00:00
2025-Dec-25 12:03:50.504117
#17 7.804 Downloading pyyaml-6.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (807 kB)
2025-Dec-25 12:03:50.504117
#17 7.827    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 807.9/807.9 kB 37.4 MB/s eta 0:00:00
2025-Dec-25 12:03:50.504117
#17 7.836 Downloading requests_toolbelt-1.0.0-py2.py3-none-any.whl (54 kB)
2025-Dec-25 12:03:50.504117
#17 7.846 Downloading rsa-4.9.1-py3-none-any.whl (34 kB)
2025-Dec-25 12:03:50.504117
#17 7.856 Downloading starlette-0.50.0-py3-none-any.whl (74 kB)
2025-Dec-25 12:03:50.504117
#17 7.868 Downloading anyio-4.12.0-py3-none-any.whl (113 kB)
2025-Dec-25 12:03:50.638195
#17 7.895 Downloading typing_extensions-4.15.0-py3-none-any.whl (44 kB)
2025-Dec-25 12:03:50.638195
#17 7.910 Downloading urllib3-2.6.2-py3-none-any.whl (131 kB)
2025-Dec-25 12:03:50.638195
#17 7.924 Downloading uvloop-0.22.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (4.4 MB)
2025-Dec-25 12:03:50.638195
#17 8.003    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.4/4.4 MB 62.3 MB/s eta 0:00:00
2025-Dec-25 12:03:50.738230
#17 8.014 Downloading watchfiles-1.1.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (456 kB)
2025-Dec-25 12:03:50.743278
#17 8.029 Downloading websockets-15.0.1-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (182 kB)
2025-Dec-25 12:03:50.743278
#17 8.036 Downloading argon2_cffi-25.1.0-py3-none-any.whl (14 kB)
2025-Dec-25 12:03:50.743278
#17 8.047 Downloading passlib-1.7.4-py2.py3-none-any.whl (525 kB)
2025-Dec-25 12:03:50.743278
#17 8.057    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 525.6/525.6 kB 50.3 MB/s eta 0:00:00
2025-Dec-25 12:03:50.743278
#17 8.063 Downloading pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.3 MB)
2025-Dec-25 12:03:50.743278
#17 8.091    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.3/2.3 MB 79.3 MB/s eta 0:00:00
2025-Dec-25 12:03:50.743278
#17 8.097 Downloading python_jose-3.5.0-py2.py3-none-any.whl (34 kB)
2025-Dec-25 12:03:50.743278
#17 8.104 Downloading uvicorn-0.40.0-py3-none-any.whl (68 kB)
2025-Dec-25 12:03:50.948358
#17 8.116 Downloading annotated_types-0.7.0-py3-none-any.whl (13 kB)
2025-Dec-25 12:03:50.948358
#17 8.123 Downloading cffi-2.0.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (219 kB)
2025-Dec-25 12:03:50.948358
#17 8.147 Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
2025-Dec-25 12:03:50.948358
#17 8.159 Downloading typing_inspection-0.4.2-py3-none-any.whl (14 kB)
2025-Dec-25 12:03:50.948358
#17 8.167 Downloading argon2_cffi_bindings-25.1.0-cp39-abi3-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl (87 kB)
2025-Dec-25 12:03:50.948358
#17 8.177 Downloading packaging-25.0-py3-none-any.whl (66 kB)
2025-Dec-25 12:03:50.948358
#17 8.186 Downloading pycparser-2.23-py3-none-any.whl (118 kB)
2025-Dec-25 12:03:50.948358
#17 8.313 Installing collected packages: passlib, async-property, websockets, uvloop, urllib3, typing-extensions, six, pyyaml, python-dotenv, pycryptodome, pycparser, pyasn1, psycopg2-binary, packaging, idna, httptools, h11, greenlet, click, charset_normalizer, certifi, bcrypt, annotated-types, annotated-doc, aiofiles, uvicorn, typing-inspection, sqlalchemy, rsa, requests, pydantic-core, httpcore, ecdsa, deprecation, cffi, anyio, watchfiles, starlette, requests-toolbelt, python-jose, pydantic, httpx, cryptography, argon2-cffi-bindings, jwcrypto, fastapi, argon2-cffi, python-keycloak, minio
2025-Dec-25 12:03:56.448678
#17 13.81 WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager, possibly rendering your system unusable. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv. Use the --root-user-action option if you know what you are doing and want to suppress this warning.
2025-Dec-25 12:03:56.689368
#17 13.81 Successfully installed aiofiles-25.1.0 annotated-doc-0.0.4 annotated-types-0.7.0 anyio-4.12.0 argon2-cffi-25.1.0 argon2-cffi-bindings-25.1.0 async-property-0.2.2 bcrypt-5.0.0 certifi-2025.11.12 cffi-2.0.0 charset_normalizer-3.4.4 click-8.3.1 cryptography-46.0.3 deprecation-2.1.0 ecdsa-0.19.1 fastapi-0.127.0 greenlet-3.3.0 h11-0.16.0 httpcore-1.0.9 httptools-0.7.1 httpx-0.28.1 idna-3.11 jwcrypto-1.5.6 minio-7.2.20 packaging-25.0 passlib-1.7.4 psycopg2-binary-2.9.11 pyasn1-0.6.1 pycparser-2.23 pycryptodome-3.23.0 pydantic-2.12.5 pydantic-core-2.41.5 python-dotenv-1.2.1 python-jose-3.5.0 python-keycloak-5.8.1 pyyaml-6.0.3 requests-2.32.5 requests-toolbelt-1.0.0 rsa-4.9.1 six-1.17.0 sqlalchemy-2.0.45 starlette-0.50.0 typing-extensions-4.15.0 typing-inspection-0.4.2 urllib3-2.6.2 uvicorn-0.40.0 uvloop-0.22.1 watchfiles-1.1.1 websockets-15.0.1
2025-Dec-25 12:03:56.689368
#17 13.90
2025-Dec-25 12:03:56.689368
#17 13.90 [notice] A new release of pip is available: 25.0.1 -> 25.3
2025-Dec-25 12:03:56.689368
#17 13.90 [notice] To update, run: pip install --upgrade pip
2025-Dec-25 12:03:57.188060
#17 DONE 14.6s
2025-Dec-25 12:03:57.188060
2025-Dec-25 12:03:57.188060
#16 [dashboard deps 4/4] RUN npm install
2025-Dec-25 12:03:57.343373
#16 ...
2025-Dec-25 12:03:57.343373
2025-Dec-25 12:03:57.343373
#18 [api 5/5] COPY . .
2025-Dec-25 12:04:06.180597
#18 DONE 9.0s
2025-Dec-25 12:04:06.180597
2025-Dec-25 12:04:06.180597
#16 [dashboard deps 4/4] RUN npm install
2025-Dec-25 12:04:06.337756
#16 ...
2025-Dec-25 12:04:06.337756
2025-Dec-25 12:04:06.337756
#19 [api] exporting to image
2025-Dec-25 12:04:06.337756
#19 exporting layers
2025-Dec-25 12:04:07.324710
#19 ...
2025-Dec-25 12:04:07.324710
2025-Dec-25 12:04:07.324710
#16 [dashboard deps 4/4] RUN npm install
2025-Dec-25 12:04:07.324710
#16 31.49
2025-Dec-25 12:04:07.324710
#16 31.49 added 473 packages, and audited 474 packages in 31s
2025-Dec-25 12:04:07.324710
#16 31.49
2025-Dec-25 12:04:07.324710
#16 31.49 154 packages are looking for funding
2025-Dec-25 12:04:07.324710
#16 31.49   run `npm fund` for details
2025-Dec-25 12:04:07.324710
#16 31.49
2025-Dec-25 12:04:07.324710
#16 31.49 found 0 vulnerabilities
2025-Dec-25 12:04:07.324710
#16 31.49 npm notice
2025-Dec-25 12:04:07.324710
#16 31.49 npm notice New major version of npm available! 10.8.2 -> 11.7.0
2025-Dec-25 12:04:07.324710
#16 31.49 npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.7.0
2025-Dec-25 12:04:07.324710
#16 31.49 npm notice To update run: npm install -g npm@11.7.0
2025-Dec-25 12:04:07.324710
#16 31.49 npm notice
2025-Dec-25 12:04:07.324710
#16 DONE 31.9s
2025-Dec-25 12:04:07.480042
#19 [api] exporting to image
2025-Dec-25 12:04:10.187807
#19 exporting layers 4.0s done
2025-Dec-25 12:04:10.401018
#19 writing image sha256:55ca79c02388f06afb9f7a3a59648cbb165ef3e880da22cc0e0bb8f7c80ccd0d done
2025-Dec-25 12:04:10.401018
#19 naming to docker.io/library/hck4w0k4ww8kk4gccw000ggg-api done
2025-Dec-25 12:04:10.401018
#19 DONE 4.0s
2025-Dec-25 12:04:10.401018
2025-Dec-25 12:04:10.401018
#20 [api] resolving provenance for metadata file
2025-Dec-25 12:04:10.401018
#20 DONE 0.0s
2025-Dec-25 12:04:12.774257
#21 [dashboard builder 3/5] COPY --from=deps /app/node_modules ./node_modules
2025-Dec-25 12:04:22.493275
#21 DONE 9.7s
2025-Dec-25 12:04:22.717473
#22 [dashboard builder 4/5] COPY . .
2025-Dec-25 12:04:22.723823
#22 DONE 0.1s
2025-Dec-25 12:04:22.723823
2025-Dec-25 12:04:22.723823
#23 [dashboard builder 5/5] RUN npm run build
2025-Dec-25 12:04:23.314268
#23 0.745
2025-Dec-25 12:04:23.328571
#23 0.745 > dashboard@0.1.0 build
2025-Dec-25 12:04:23.328571
#23 0.745 > next build
2025-Dec-25 12:04:23.328571
#23 0.745
2025-Dec-25 12:04:24.191371
#23 1.624 Attention: Next.js now collects completely anonymous telemetry regarding usage.
2025-Dec-25 12:04:24.321035
#23 1.624 This information is used to shape Next.js' roadmap and prioritize features.
2025-Dec-25 12:04:24.321035
#23 1.624 You can learn more, including how to opt-out if you'd not like to participate in this anonymous program, by visiting the following URL:
2025-Dec-25 12:04:24.321035
#23 1.624 https://nextjs.org/telemetry
2025-Dec-25 12:04:24.321035
#23 1.624
2025-Dec-25 12:04:24.321035
#23 1.637 ▲ Next.js 16.1.0 (Turbopack)
2025-Dec-25 12:04:24.321035
#23 1.637
2025-Dec-25 12:04:24.321035
#23 1.754   Creating an optimized production build ...
2025-Dec-25 12:04:39.966199
#23 17.40 ✓ Compiled successfully in 15.2s
2025-Dec-25 12:04:40.141828
#23 17.42   Running TypeScript ...
2025-Dec-25 12:04:50.017896
#23 27.45   Collecting page data using 1 worker ...
2025-Dec-25 12:04:50.723384
#23 28.16   Generating static pages using 1 worker (0/11) ...
2025-Dec-25 12:04:51.083828
#23 28.52   Generating static pages using 1 worker (2/11)
2025-Dec-25 12:04:51.099162
2025-Dec-25 12:04:51.184549
#23 28.52   Generating static pages using 1 worker (5/11)
2025-Dec-25 12:04:51.184549
#23 28.52   Generating static pages using 1 worker (8/11)
2025-Dec-25 12:04:51.184549
#23 28.62 ✓ Generating static pages using 1 worker (11/11) in 462.4ms
2025-Dec-25 12:04:51.354809
#23 28.63   Finalizing page optimization ...
2025-Dec-25 12:04:51.354809
#23 28.63
2025-Dec-25 12:04:51.354809
#23 28.64 Route (app)
2025-Dec-25 12:04:51.354809
#23 28.64 ┌ ○ /
2025-Dec-25 12:04:51.354809
#23 28.64 ├ ○ /_not-found
2025-Dec-25 12:04:51.354809
#23 28.64 ├ ○ /login
2025-Dec-25 12:04:51.354809
#23 28.64 ├ ○ /org
2025-Dec-25 12:04:51.354809
#23 28.64 ├ ƒ /org/[orgId]/billing
2025-Dec-25 12:04:51.354809
#23 28.64 ├ ƒ /org/[orgId]/projects
2025-Dec-25 12:04:51.354809
#23 28.64 ├ ƒ /org/[orgId]/projects/new
2025-Dec-25 12:04:51.354809
#23 28.64 ├ ƒ /org/[orgId]/settings
2025-Dec-25 12:04:51.354809
#23 28.64 ├ ƒ /org/[orgId]/team
2025-Dec-25 12:04:51.354809
#23 28.64 ├ ○ /projects
2025-Dec-25 12:04:51.354809
#23 28.64 ├ ƒ /projects/[id]
2025-Dec-25 12:04:51.354809
#23 28.64 ├ ƒ /projects/[id]/auth
2025-Dec-25 12:04:51.354809
#23 28.64 ├ ƒ /projects/[id]/backups
2025-Dec-25 12:04:51.354809
#23 28.64 ├ ƒ /projects/[id]/database
2025-Dec-25 12:04:51.354809
#23 28.64 ├ ƒ /projects/[id]/database/[table]
2025-Dec-25 12:04:51.354809
#23 28.64 ├ ƒ /projects/[id]/edge-functions
2025-Dec-25 12:04:51.354809
#23 28.64 ├ ƒ /projects/[id]/logs
2025-Dec-25 12:04:51.354809
#23 28.64 ├ ƒ /projects/[id]/realtime
2025-Dec-25 12:04:51.354809
#23 28.64 ├ ƒ /projects/[id]/secrets
2025-Dec-25 12:04:51.354809
#23 28.64 ├ ƒ /projects/[id]/settings
2025-Dec-25 12:04:51.354809
#23 28.64 ├ ƒ /projects/[id]/settings/deployment
2025-Dec-25 12:04:51.354809
#23 28.64 ├ ƒ /projects/[id]/sql
2025-Dec-25 12:04:51.354809
#23 28.64 ├ ƒ /projects/[id]/storage
2025-Dec-25 12:04:51.354809
#23 28.64 ├ ○ /projects/new
2025-Dec-25 12:04:51.354809
#23 28.64 ├ ○ /settings/organization
2025-Dec-25 12:04:51.354809
#23 28.64 ├ ƒ /settings/organization/[id]
2025-Dec-25 12:04:51.354809
#23 28.64 ├ ○ /settings/profile
2025-Dec-25 12:04:51.354809
#23 28.64 └ ○ /signup
2025-Dec-25 12:04:51.354809
#23 28.64
2025-Dec-25 12:04:51.354809
#23 28.64
2025-Dec-25 12:04:51.354809
#23 28.64 ○  (Static)   prerendered as static content
2025-Dec-25 12:04:51.354809
#23 28.64 ƒ  (Dynamic)  server-rendered on demand
2025-Dec-25 12:04:51.354809
#23 28.64
2025-Dec-25 12:04:51.416737
#23 28.85 npm notice
2025-Dec-25 12:04:51.416737
#23 28.85 npm notice New major version of npm available! 10.8.2 -> 11.7.0
2025-Dec-25 12:04:51.416737
#23 28.85 npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.7.0
2025-Dec-25 12:04:51.416737
#23 28.85 npm notice To update run: npm install -g npm@11.7.0
2025-Dec-25 12:04:51.416737
#23 28.85 npm notice
2025-Dec-25 12:04:51.623706
#23 DONE 28.9s
2025-Dec-25 12:04:52.283823
#24 [dashboard runner 3/6] COPY --from=builder /app/public ./public
2025-Dec-25 12:04:52.505033
#24 DONE 0.0s
2025-Dec-25 12:04:52.505033
2025-Dec-25 12:04:52.505033
#25 [dashboard runner 4/6] COPY --from=builder /app/.next ./.next
2025-Dec-25 12:04:52.609833
#25 DONE 0.3s
2025-Dec-25 12:04:54.735460
#26 [dashboard runner 5/6] COPY --from=builder /app/node_modules ./node_modules
2025-Dec-25 12:05:00.770433
#26 DONE 6.0s
2025-Dec-25 12:05:00.975863
#27 [dashboard runner 6/6] COPY --from=builder /app/package.json ./package.json
2025-Dec-25 12:05:00.975863
#27 DONE 0.0s
2025-Dec-25 12:05:00.975863
2025-Dec-25 12:05:00.975863
#28 [dashboard] exporting to image
2025-Dec-25 12:05:00.975863
#28 exporting layers
2025-Dec-25 12:05:05.198939
#28 exporting layers 4.4s done
2025-Dec-25 12:05:05.255214
#28 writing image sha256:443c175dd31e5dabbea5dedba849d839a4b68d4d43cb2200040f7e658f6ee11d done
2025-Dec-25 12:05:05.255214
#28 naming to docker.io/library/hck4w0k4ww8kk4gccw000ggg-dashboard done
2025-Dec-25 12:05:05.255214
#28 DONE 4.4s
2025-Dec-25 12:05:05.255214
2025-Dec-25 12:05:05.255214
#29 [dashboard] resolving provenance for metadata file
2025-Dec-25 12:05:05.255214
#29 DONE 0.0s
2025-Dec-25 12:05:05.266432
api  Built
2025-Dec-25 12:05:05.266432
dashboard  Built
2025-Dec-25 12:05:05.303799
Creating .env file with runtime variables for build phase.
2025-Dec-25 12:05:06.126653
[CMD]: docker exec fg488844ckk48o4socc0kkog bash -c 'cat /artifacts/fg488844ckk48o4socc0kkog/.env'
2025-Dec-25 12:05:06.126653
SOURCE_COMMIT=adfe8fa5a39b856c90990f4b611f7dd2c7068352
2025-Dec-25 12:05:06.126653
COOLIFY_URL=
2025-Dec-25 12:05:06.126653
COOLIFY_FQDN=
2025-Dec-25 12:05:06.126653
SERVICE_URL_DASHBOARD=https://supalove.hayataxi.online
2025-Dec-25 12:05:06.126653
SERVICE_FQDN_DASHBOARD=supalove.hayataxi.online
2025-Dec-25 12:05:06.126653
SERVICE_URL_API=https://api.hayataxi.online
2025-Dec-25 12:05:06.126653
SERVICE_FQDN_API=api.hayataxi.online
2025-Dec-25 12:05:06.126653
SERVICE_URL_KEYCLOAK=https://auth.hayataxi.online
2025-Dec-25 12:05:06.126653
SERVICE_FQDN_KEYCLOAK=auth.hayataxi.online
2025-Dec-25 12:05:06.126653
SERVICE_URL_MINIO=https://s3.hayataxi.online
2025-Dec-25 12:05:06.126653
SERVICE_FQDN_MINIO=s3.hayataxi.online
2025-Dec-25 12:05:06.126653
SERVICE_NAME_CONTROL-PLANE-DB=control-plane-db
2025-Dec-25 12:05:06.126653
SERVICE_NAME_API=api
2025-Dec-25 12:05:06.126653
SERVICE_NAME_DASHBOARD=dashboard
2025-Dec-25 12:05:06.126653
SERVICE_NAME_KEYCLOAK=keycloak
2025-Dec-25 12:05:06.126653
SERVICE_NAME_MINIO=minio
2025-Dec-25 12:05:06.126653
POSTGRES_USER=platform
2025-Dec-25 12:05:06.126653
POSTGRES_PASSWORD=platform
2025-Dec-25 12:05:06.126653
POSTGRES_DB=control_plane
2025-Dec-25 12:05:06.126653
KEYCLOAK_ADMIN_USER=admin
2025-Dec-25 12:05:06.126653
KEYCLOAK_ADMIN_PASSWORD=admin
2025-Dec-25 12:05:06.126653
MINIO_ROOT_USER=minioadmin
2025-Dec-25 12:05:06.126653
MINIO_ROOT_PASSWORD=minioadmin
2025-Dec-25 12:05:06.126653
URL=http://localhost:8000
2025-Dec-25 12:05:06.126653
NEXT_PUBLIC_API_URL=https://api.hayataxi.online
2025-Dec-25 12:05:06.126653
HOST=0.0.0.0
2025-Dec-25 12:05:06.467986
Removing old containers.
2025-Dec-25 12:05:07.342698
[CMD]: docker stop --time=30 dashboard-hck4w0k4ww8kk4gccw000ggg-115332739126
2025-Dec-25 12:05:07.342698
dashboard-hck4w0k4ww8kk4gccw000ggg-115332739126
2025-Dec-25 12:05:07.796175
[CMD]: docker rm -f dashboard-hck4w0k4ww8kk4gccw000ggg-115332739126
2025-Dec-25 12:05:07.796175
dashboard-hck4w0k4ww8kk4gccw000ggg-115332739126
2025-Dec-25 12:05:08.154365
[CMD]: docker stop --time=30 api-hck4w0k4ww8kk4gccw000ggg-115332724938
2025-Dec-25 12:05:08.154365
api-hck4w0k4ww8kk4gccw000ggg-115332724938
2025-Dec-25 12:05:08.520703
[CMD]: docker rm -f api-hck4w0k4ww8kk4gccw000ggg-115332724938
2025-Dec-25 12:05:08.520703
api-hck4w0k4ww8kk4gccw000ggg-115332724938
2025-Dec-25 12:05:09.069694
[CMD]: docker stop --time=30 keycloak-hck4w0k4ww8kk4gccw000ggg-115332748618
2025-Dec-25 12:05:09.069694
keycloak-hck4w0k4ww8kk4gccw000ggg-115332748618
2025-Dec-25 12:05:09.487719
[CMD]: docker rm -f keycloak-hck4w0k4ww8kk4gccw000ggg-115332748618
2025-Dec-25 12:05:09.487719
keycloak-hck4w0k4ww8kk4gccw000ggg-115332748618
2025-Dec-25 12:05:09.983018
[CMD]: docker stop --time=30 control-plane-db-hck4w0k4ww8kk4gccw000ggg-115332708621
2025-Dec-25 12:05:09.983018
control-plane-db-hck4w0k4ww8kk4gccw000ggg-115332708621
2025-Dec-25 12:05:10.347374
[CMD]: docker rm -f control-plane-db-hck4w0k4ww8kk4gccw000ggg-115332708621
2025-Dec-25 12:05:10.347374
control-plane-db-hck4w0k4ww8kk4gccw000ggg-115332708621
2025-Dec-25 12:05:10.870285
[CMD]: docker stop --time=30 minio-hck4w0k4ww8kk4gccw000ggg-115332758860
2025-Dec-25 12:05:10.870285
minio-hck4w0k4ww8kk4gccw000ggg-115332758860
2025-Dec-25 12:05:11.263324
[CMD]: docker rm -f minio-hck4w0k4ww8kk4gccw000ggg-115332758860
2025-Dec-25 12:05:11.263324
minio-hck4w0k4ww8kk4gccw000ggg-115332758860
2025-Dec-25 12:05:11.274696
Starting new application.
2025-Dec-25 12:05:12.564054
[CMD]: docker exec fg488844ckk48o4socc0kkog bash -c 'SOURCE_COMMIT=adfe8fa5a39b856c90990f4b611f7dd2c7068352 COOLIFY_BRANCH=main COOLIFY_RESOURCE_UUID=hck4w0k4ww8kk4gccw000ggg COOLIFY_CONTAINER_NAME=hck4w0k4ww8kk4gccw000ggg-120309019930  docker compose --env-file /artifacts/fg488844ckk48o4socc0kkog/.env --project-name hck4w0k4ww8kk4gccw000ggg --project-directory /artifacts/fg488844ckk48o4socc0kkog -f /artifacts/fg488844ckk48o4socc0kkog/docker-compose.coolify.yml up -d'
2025-Dec-25 12:05:12.564054
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-120329471929  Creating
2025-Dec-25 12:05:12.564054
Container minio-hck4w0k4ww8kk4gccw000ggg-120329522676  Creating
2025-Dec-25 12:05:12.620225
Container minio-hck4w0k4ww8kk4gccw000ggg-120329522676  Created
2025-Dec-25 12:05:12.620225
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-120329471929  Created
2025-Dec-25 12:05:12.620225
Container keycloak-hck4w0k4ww8kk4gccw000ggg-120329510169  Creating
2025-Dec-25 12:05:12.639218
Container keycloak-hck4w0k4ww8kk4gccw000ggg-120329510169  Created
2025-Dec-25 12:05:12.644418
Container api-hck4w0k4ww8kk4gccw000ggg-120329487149  Creating
2025-Dec-25 12:05:12.662783
Container api-hck4w0k4ww8kk4gccw000ggg-120329487149  Created
2025-Dec-25 12:05:12.668967
Container dashboard-hck4w0k4ww8kk4gccw000ggg-120329499269  Creating
2025-Dec-25 12:05:12.680457
Container dashboard-hck4w0k4ww8kk4gccw000ggg-120329499269  Created
2025-Dec-25 12:05:12.687593
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-120329471929  Starting
2025-Dec-25 12:05:12.687593
Container minio-hck4w0k4ww8kk4gccw000ggg-120329522676  Starting
2025-Dec-25 12:05:13.004210
Container minio-hck4w0k4ww8kk4gccw000ggg-120329522676  Started
2025-Dec-25 12:05:13.051870
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-120329471929  Started
2025-Dec-25 12:05:13.065823
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-120329471929  Waiting
2025-Dec-25 12:05:18.554540
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-120329471929  Healthy
2025-Dec-25 12:05:18.554540
Container keycloak-hck4w0k4ww8kk4gccw000ggg-120329510169  Starting
2025-Dec-25 12:05:18.760596
Container keycloak-hck4w0k4ww8kk4gccw000ggg-120329510169  Started
2025-Dec-25 12:05:18.760596
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-120329471929  Waiting
2025-Dec-25 12:05:19.265285
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-120329471929  Healthy
2025-Dec-25 12:05:19.265285
Container api-hck4w0k4ww8kk4gccw000ggg-120329487149  Starting
2025-Dec-25 12:05:19.578528
Container api-hck4w0k4ww8kk4gccw000ggg-120329487149  Started
2025-Dec-25 12:05:19.578528
Container dashboard-hck4w0k4ww8kk4gccw000ggg-120329499269  Starting
2025-Dec-25 12:05:19.915484
Container dashboard-hck4w0k4ww8kk4gccw000ggg-120329499269  Started
2025-Dec-25 12:05:22.246802
New container started.
2025-Dec-25 12:05:24.802995
Gracefully shutting down build container: fg488844ckk48o4socc0kkog
2025-Dec-25 12:05:25.425412
[CMD]: docker stop --time=30 fg488844ckk48o4socc0kkog
2025-Dec-25 12:05:25.425412
fg488844ckk48o4socc0kkog
2025-Dec-25 12:05:26.189856
[CMD]: docker rm -f fg488844ckk48o4socc0kkog
2025-Dec-25 12:05:26.189856
Error response from daemon: removal of container fg488844ckk48o4socc0kkog is already in progress