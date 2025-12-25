Deployment is Finished.


2025-Dec-25 11:36:22.298754
Starting deployment of supalove to localhost.
2025-Dec-25 11:36:22.489472
Preparing container with helper image: ghcr.io/coollabsio/coolify-helper:1.0.12
2025-Dec-25 11:36:22.595722
[CMD]: docker stop --time=30 u04wc8c0cogswcwso8cs08wc
2025-Dec-25 11:36:22.595722
Error response from daemon: No such container: u04wc8c0cogswcwso8cs08wc
2025-Dec-25 11:36:22.702648
[CMD]: docker rm -f u04wc8c0cogswcwso8cs08wc
2025-Dec-25 11:36:22.702648
Error response from daemon: No such container: u04wc8c0cogswcwso8cs08wc
2025-Dec-25 11:36:22.854466
[CMD]: docker run -d --network coolify --name u04wc8c0cogswcwso8cs08wc  --rm -v /var/run/docker.sock:/var/run/docker.sock ghcr.io/coollabsio/coolify-helper:1.0.12
2025-Dec-25 11:36:22.854466
2ba625be19f2347deed5610ba9122c0db80c9ff8ecc0ee17c67ad9c3161439c7
2025-Dec-25 11:36:23.751888
[CMD]: docker exec u04wc8c0cogswcwso8cs08wc bash -c 'GIT_SSH_COMMAND="ssh -o ConnectTimeout=30 -p 22 -o Port=22 -o LogLevel=ERROR -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" git ls-remote https://github.com/farisnoaman/supalove refs/heads/main'
2025-Dec-25 11:36:23.751888
adfe8fa5a39b856c90990f4b611f7dd2c7068352	refs/heads/main
2025-Dec-25 11:36:23.767426
----------------------------------------
2025-Dec-25 11:36:23.773610
Importing farisnoaman/supalove:main (commit sha adfe8fa5a39b856c90990f4b611f7dd2c7068352) to /artifacts/u04wc8c0cogswcwso8cs08wc.
2025-Dec-25 11:36:23.924722
[CMD]: docker exec u04wc8c0cogswcwso8cs08wc bash -c 'git clone --depth=1 --recurse-submodules --shallow-submodules -b 'main' 'https://github.com/farisnoaman/supalove' '/artifacts/u04wc8c0cogswcwso8cs08wc' && cd '/artifacts/u04wc8c0cogswcwso8cs08wc' && if [ -f .gitmodules ]; then sed -i "s#git@\(.*\):#https://\1/#g" '/artifacts/u04wc8c0cogswcwso8cs08wc'/.gitmodules || true && git submodule sync && GIT_SSH_COMMAND="ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" git submodule update --init --recursive --depth=1; fi && cd '/artifacts/u04wc8c0cogswcwso8cs08wc' && GIT_SSH_COMMAND="ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" git lfs pull'
2025-Dec-25 11:36:23.924722
Cloning into '/artifacts/u04wc8c0cogswcwso8cs08wc'...
2025-Dec-25 11:36:30.045471
Updating files:  23% (3601/15084)
2025-Dec-25 11:36:30.061437
Updating files:  24% (3621/15084)
2025-Dec-25 11:36:30.097392
Updating files:  25% (3771/15084)
2025-Dec-25 11:36:30.124602
Updating files:  26% (3922/15084)
2025-Dec-25 11:36:30.177748
Updating files:  27% (4073/15084)
2025-Dec-25 11:36:30.210325
Updating files:  28% (4224/15084)
2025-Dec-25 11:36:30.234538
Updating files:  29% (4375/15084)
2025-Dec-25 11:36:30.252289
Updating files:  30% (4526/15084)
2025-Dec-25 11:36:30.266497
Updating files:  31% (4677/15084)
2025-Dec-25 11:36:30.282919
Updating files:  32% (4827/15084)
2025-Dec-25 11:36:30.299946
Updating files:  33% (4978/15084)
2025-Dec-25 11:36:30.340489
Updating files:  34% (5129/15084)
2025-Dec-25 11:36:30.374100
Updating files:  35% (5280/15084)
2025-Dec-25 11:36:30.421427
Updating files:  36% (5431/15084)
2025-Dec-25 11:36:30.461830
Updating files:  37% (5582/15084)
2025-Dec-25 11:36:30.479439
Updating files:  38% (5732/15084)
2025-Dec-25 11:36:30.496439
Updating files:  39% (5883/15084)
2025-Dec-25 11:36:30.513944
Updating files:  40% (6034/15084)
2025-Dec-25 11:36:30.531765
Updating files:  41% (6185/15084)
2025-Dec-25 11:36:30.548024
Updating files:  42% (6336/15084)
2025-Dec-25 11:36:30.558666
Updating files:  43% (6487/15084)
2025-Dec-25 11:36:30.569321
Updating files:  44% (6637/15084)
2025-Dec-25 11:36:30.579420
Updating files:  45% (6788/15084)
2025-Dec-25 11:36:30.593019
Updating files:  46% (6939/15084)
2025-Dec-25 11:36:30.605708
Updating files:  47% (7090/15084)
2025-Dec-25 11:36:30.617365
Updating files:  48% (7241/15084)
2025-Dec-25 11:36:30.628577
Updating files:  49% (7392/15084)
2025-Dec-25 11:36:30.642396
Updating files:  50% (7542/15084)
2025-Dec-25 11:36:30.652384
Updating files:  51% (7693/15084)
2025-Dec-25 11:36:30.665511
Updating files:  52% (7844/15084)
2025-Dec-25 11:36:30.681703
Updating files:  53% (7995/15084)
2025-Dec-25 11:36:30.701157
Updating files:  54% (8146/15084)
2025-Dec-25 11:36:30.791758
Updating files:  55% (8297/15084)
2025-Dec-25 11:36:30.826789
Updating files:  56% (8448/15084)
2025-Dec-25 11:36:30.838176
Updating files:  57% (8598/15084)
2025-Dec-25 11:36:30.852227
Updating files:  58% (8749/15084)
2025-Dec-25 11:36:30.874867
Updating files:  59% (8900/15084)
2025-Dec-25 11:36:30.889806
Updating files:  60% (9051/15084)
2025-Dec-25 11:36:30.906904
Updating files:  61% (9202/15084)
2025-Dec-25 11:36:30.925674
Updating files:  62% (9353/15084)
2025-Dec-25 11:36:30.938901
Updating files:  63% (9503/15084)
2025-Dec-25 11:36:30.962192
Updating files:  64% (9654/15084)
2025-Dec-25 11:36:31.039446
Updating files:  65% (9805/15084)
2025-Dec-25 11:36:31.042388
Updating files:  65% (9820/15084)
2025-Dec-25 11:36:31.052740
Updating files:  66% (9956/15084)
2025-Dec-25 11:36:31.067390
Updating files:  67% (10107/15084)
2025-Dec-25 11:36:31.087182
Updating files:  68% (10258/15084)
2025-Dec-25 11:36:31.108197
Updating files:  69% (10408/15084)
2025-Dec-25 11:36:31.125111
Updating files:  70% (10559/15084)
2025-Dec-25 11:36:31.139686
Updating files:  71% (10710/15084)
2025-Dec-25 11:36:31.156205
Updating files:  72% (10861/15084)
2025-Dec-25 11:36:31.168790
Updating files:  73% (11012/15084)
2025-Dec-25 11:36:31.181241
Updating files:  74% (11163/15084)
2025-Dec-25 11:36:31.199507
Updating files:  75% (11313/15084)
2025-Dec-25 11:36:31.220694
Updating files:  76% (11464/15084)
2025-Dec-25 11:36:31.246597
Updating files:  77% (11615/15084)
2025-Dec-25 11:36:31.265791
Updating files:  78% (11766/15084)
2025-Dec-25 11:36:31.284871
Updating files:  79% (11917/15084)
2025-Dec-25 11:36:31.354281
Updating files:  80% (12068/15084)
2025-Dec-25 11:36:31.369190
Updating files:  81% (12219/15084)
2025-Dec-25 11:36:31.416439
Updating files:  82% (12369/15084)
2025-Dec-25 11:36:31.428569
Updating files:  83% (12520/15084)
2025-Dec-25 11:36:31.448918
Updating files:  84% (12671/15084)
2025-Dec-25 11:36:31.467723
Updating files:  85% (12822/15084)
2025-Dec-25 11:36:31.478645
Updating files:  86% (12973/15084)
2025-Dec-25 11:36:31.494242
Updating files:  87% (13124/15084)
2025-Dec-25 11:36:31.537506
Updating files:  88% (13274/15084)
2025-Dec-25 11:36:31.560647
Updating files:  89% (13425/15084)
2025-Dec-25 11:36:31.602018
Updating files:  90% (13576/15084)
2025-Dec-25 11:36:31.637570
Updating files:  91% (13727/15084)
2025-Dec-25 11:36:31.645831
Updating files:  92% (13878/15084)
2025-Dec-25 11:36:31.659158
Updating files:  93% (14029/15084)
2025-Dec-25 11:36:31.771967
Updating files:  94% (14179/15084)
2025-Dec-25 11:36:31.801673
Updating files:  95% (14330/15084)
2025-Dec-25 11:36:31.828232
Updating files:  96% (14481/15084)
2025-Dec-25 11:36:31.852666
Updating files:  97% (14632/15084)
2025-Dec-25 11:36:31.873856
Updating files:  98% (14783/15084)
2025-Dec-25 11:36:31.908333
Updating files:  99% (14934/15084)
2025-Dec-25 11:36:31.930359
Updating files: 100% (15084/15084)
Updating files: 100% (15084/15084), done.
2025-Dec-25 11:36:32.607261
[CMD]: docker exec u04wc8c0cogswcwso8cs08wc bash -c 'cd /artifacts/u04wc8c0cogswcwso8cs08wc && git log -1 adfe8fa5a39b856c90990f4b611f7dd2c7068352 --pretty=%B'
2025-Dec-25 11:36:32.607261
feat: Add service `expose` configurations to docker-compose and create `coolify_deployment_log.md`.
2025-Dec-25 11:36:39.013483
[CMD]: docker exec u04wc8c0cogswcwso8cs08wc bash -c 'test -f /artifacts/u04wc8c0cogswcwso8cs08wc/control-plane/api/Dockerfile && echo 'exists' || echo 'not found''
2025-Dec-25 11:36:39.013483
exists
2025-Dec-25 11:36:39.168188
[CMD]: docker exec u04wc8c0cogswcwso8cs08wc bash -c 'cat /artifacts/u04wc8c0cogswcwso8cs08wc/control-plane/api/Dockerfile'
2025-Dec-25 11:36:39.168188
FROM python:3.12-slim
2025-Dec-25 11:36:39.168188
WORKDIR /app
2025-Dec-25 11:36:39.168188
COPY requirements.txt .
2025-Dec-25 11:36:39.168188
RUN pip install -r requirements.txt
2025-Dec-25 11:36:39.168188
COPY . .
2025-Dec-25 11:36:39.168188
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
2025-Dec-25 11:36:39.336399
Added 20 ARG declarations to Dockerfile for service api.
2025-Dec-25 11:36:39.577760
[CMD]: docker exec u04wc8c0cogswcwso8cs08wc bash -c 'test -f /artifacts/u04wc8c0cogswcwso8cs08wc/dashboard/Dockerfile && echo 'exists' || echo 'not found''
2025-Dec-25 11:36:39.577760
exists
2025-Dec-25 11:36:39.956456
[CMD]: docker exec u04wc8c0cogswcwso8cs08wc bash -c 'cat /artifacts/u04wc8c0cogswcwso8cs08wc/dashboard/Dockerfile'
2025-Dec-25 11:36:39.956456
# Stage 1: Dependencies
2025-Dec-25 11:36:39.956456
FROM node:20-alpine AS deps
2025-Dec-25 11:36:39.956456
WORKDIR /app
2025-Dec-25 11:36:39.956456
COPY package*.json ./
2025-Dec-25 11:36:39.956456
RUN npm install
2025-Dec-25 11:36:39.956456
2025-Dec-25 11:36:39.956456
# Stage 2: Builder
2025-Dec-25 11:36:39.956456
FROM node:20-alpine AS builder
2025-Dec-25 11:36:39.956456
WORKDIR /app
2025-Dec-25 11:36:39.956456
COPY --from=deps /app/node_modules ./node_modules
2025-Dec-25 11:36:39.956456
COPY . .
2025-Dec-25 11:36:39.956456
# Set environment variables for build if needed (e.g. backend URL)
2025-Dec-25 11:36:39.956456
# For Next.js client-side fetch, it might need to know the URL at build time if pre-rendering,
2025-Dec-25 11:36:39.956456
# but we are using "use client" so it's fine.
2025-Dec-25 11:36:39.956456
ARG NEXT_PUBLIC_API_URL
2025-Dec-25 11:36:39.956456
ENV NEXT_PUBLIC_API_URL=${NEXT_PUBLIC_API_URL}
2025-Dec-25 11:36:39.956456
RUN npm run build
2025-Dec-25 11:36:39.956456
2025-Dec-25 11:36:39.956456
# Stage 3: Runner
2025-Dec-25 11:36:39.956456
FROM node:20-alpine AS runner
2025-Dec-25 11:36:39.956456
WORKDIR /app
2025-Dec-25 11:36:39.956456
ENV NODE_ENV=production
2025-Dec-25 11:36:39.956456
COPY --from=builder /app/public ./public
2025-Dec-25 11:36:39.956456
COPY --from=builder /app/.next ./.next
2025-Dec-25 11:36:39.956456
COPY --from=builder /app/node_modules ./node_modules
2025-Dec-25 11:36:39.956456
COPY --from=builder /app/package.json ./package.json
2025-Dec-25 11:36:39.956456
2025-Dec-25 11:36:39.956456
EXPOSE 3000
2025-Dec-25 11:36:39.956456
CMD ["npm", "start"]
2025-Dec-25 11:36:40.284371
Added 60 ARG declarations to Dockerfile for service dashboard (multi-stage build, added to 3 stages).
2025-Dec-25 11:36:40.299018
Pulling & building required images.
2025-Dec-25 11:36:40.368656
Creating build-time .env file in /artifacts (outside Docker context).
2025-Dec-25 11:36:40.879486
[CMD]: docker exec u04wc8c0cogswcwso8cs08wc bash -c 'cat /artifacts/build-time.env'
2025-Dec-25 11:36:40.879486
SOURCE_COMMIT='adfe8fa5a39b856c90990f4b611f7dd2c7068352'
2025-Dec-25 11:36:40.879486
COOLIFY_URL=''
2025-Dec-25 11:36:40.879486
COOLIFY_FQDN=''
2025-Dec-25 11:36:40.879486
SERVICE_NAME_CONTROL-PLANE-DB='control-plane-db'
2025-Dec-25 11:36:40.879486
SERVICE_NAME_API='api'
2025-Dec-25 11:36:40.879486
SERVICE_NAME_DASHBOARD='dashboard'
2025-Dec-25 11:36:40.879486
SERVICE_NAME_KEYCLOAK='keycloak'
2025-Dec-25 11:36:40.879486
SERVICE_NAME_MINIO='minio'
2025-Dec-25 11:36:40.879486
SERVICE_URL_DASHBOARD='https://supalove.hayataxi.online'
2025-Dec-25 11:36:40.879486
SERVICE_FQDN_DASHBOARD='supalove.hayataxi.online'
2025-Dec-25 11:36:40.879486
SERVICE_URL_API='https://api.hayataxi.online'
2025-Dec-25 11:36:40.879486
SERVICE_FQDN_API='api.hayataxi.online'
2025-Dec-25 11:36:40.879486
SERVICE_URL_KEYCLOAK='https://auth.hayataxi.online'
2025-Dec-25 11:36:40.879486
SERVICE_FQDN_KEYCLOAK='auth.hayataxi.online'
2025-Dec-25 11:36:40.879486
SERVICE_URL_MINIO='https://s3.hayataxi.online'
2025-Dec-25 11:36:40.879486
SERVICE_FQDN_MINIO='s3.hayataxi.online'
2025-Dec-25 11:36:40.879486
KEYCLOAK_ADMIN_PASSWORD="admin"
2025-Dec-25 11:36:40.879486
KEYCLOAK_ADMIN_USER="admin"
2025-Dec-25 11:36:40.879486
MINIO_ROOT_PASSWORD="minioadmin"
2025-Dec-25 11:36:40.879486
MINIO_ROOT_USER="minioadmin"
2025-Dec-25 11:36:40.879486
NEXT_PUBLIC_API_URL="https://api.hayataxi.online"
2025-Dec-25 11:36:40.879486
POSTGRES_DB="control_plane"
2025-Dec-25 11:36:40.879486
POSTGRES_PASSWORD="platform"
2025-Dec-25 11:36:40.879486
POSTGRES_USER="platform"
2025-Dec-25 11:36:40.879486
URL="http://localhost:8000"
2025-Dec-25 11:36:40.892515
Adding build arguments to Docker Compose build command.
2025-Dec-25 11:36:41.257808
[CMD]: docker exec u04wc8c0cogswcwso8cs08wc bash -c 'SOURCE_COMMIT=adfe8fa5a39b856c90990f4b611f7dd2c7068352 COOLIFY_BRANCH=main COOLIFY_RESOURCE_UUID=hck4w0k4ww8kk4gccw000ggg COOLIFY_CONTAINER_NAME=hck4w0k4ww8kk4gccw000ggg-113620930993  docker compose --env-file /artifacts/build-time.env --project-name hck4w0k4ww8kk4gccw000ggg --project-directory /artifacts/u04wc8c0cogswcwso8cs08wc -f /artifacts/u04wc8c0cogswcwso8cs08wc/docker-compose.coolify.yml build --pull --build-arg SOURCE_COMMIT --build-arg COOLIFY_URL --build-arg COOLIFY_FQDN --build-arg SERVICE_FQDN_API --build-arg SERVICE_FQDN_DASHBOARD --build-arg SERVICE_FQDN_KEYCLOAK --build-arg SERVICE_FQDN_MINIO --build-arg SERVICE_URL_API --build-arg SERVICE_URL_DASHBOARD --build-arg SERVICE_URL_KEYCLOAK --build-arg SERVICE_URL_MINIO --build-arg KEYCLOAK_ADMIN_PASSWORD --build-arg KEYCLOAK_ADMIN_USER --build-arg MINIO_ROOT_PASSWORD --build-arg MINIO_ROOT_USER --build-arg NEXT_PUBLIC_API_URL --build-arg POSTGRES_DB --build-arg POSTGRES_PASSWORD --build-arg POSTGRES_USER --build-arg URL --build-arg COOLIFY_BUILD_SECRETS_HASH=c876791ca260c934a139f5632932ce9776c810759b50594b2764e52b42180172'
2025-Dec-25 11:36:41.257808
#1 [internal] load local bake definitions
2025-Dec-25 11:36:41.500447
#1 reading from stdin 3.02kB done
2025-Dec-25 11:36:41.500447
#1 DONE 0.0s
2025-Dec-25 11:36:41.500447
2025-Dec-25 11:36:41.500447
#2 [dashboard internal] load build definition from Dockerfile
2025-Dec-25 11:36:41.500447
#2 transferring dockerfile: 2.14kB done
2025-Dec-25 11:36:41.500447
#2 DONE 0.0s
2025-Dec-25 11:36:41.500447
2025-Dec-25 11:36:41.500447
#3 [api internal] load build definition from Dockerfile
2025-Dec-25 11:36:41.500447
#3 transferring dockerfile: 638B done
2025-Dec-25 11:36:41.500447
#3 DONE 0.0s
2025-Dec-25 11:36:41.500447
2025-Dec-25 11:36:41.500447
#4 [dashboard internal] load metadata for docker.io/library/node:20-alpine
2025-Dec-25 11:36:42.090409
#4 ...
2025-Dec-25 11:36:42.090409
2025-Dec-25 11:36:42.090409
#5 [api internal] load metadata for docker.io/library/python:3.12-slim
2025-Dec-25 11:36:42.090409
#5 DONE 0.7s
2025-Dec-25 11:36:42.198700
#6 [api internal] load .dockerignore
2025-Dec-25 11:36:42.198700
#6 transferring context: 2B done
2025-Dec-25 11:36:42.198700
#6 DONE 0.0s
2025-Dec-25 11:36:42.198700
2025-Dec-25 11:36:42.198700
#7 [api 1/5] FROM docker.io/library/python:3.12-slim@sha256:fa48eefe2146644c2308b909d6bb7651a768178f84fc9550dcd495e4d6d84d01
2025-Dec-25 11:36:42.198700
#7 DONE 0.0s
2025-Dec-25 11:36:42.198700
2025-Dec-25 11:36:42.198700
#4 [dashboard internal] load metadata for docker.io/library/node:20-alpine
2025-Dec-25 11:36:42.198700
#4 DONE 0.8s
2025-Dec-25 11:36:42.198700
2025-Dec-25 11:36:42.198700
#8 [dashboard internal] load .dockerignore
2025-Dec-25 11:36:42.198700
#8 transferring context: 2B done
2025-Dec-25 11:36:42.198700
#8 DONE 0.0s
2025-Dec-25 11:36:42.198700
2025-Dec-25 11:36:42.198700
#9 [api internal] load build context
2025-Dec-25 11:36:42.323386
#9 ...
2025-Dec-25 11:36:42.323386
2025-Dec-25 11:36:42.323386
#10 [dashboard deps 1/4] FROM docker.io/library/node:20-alpine@sha256:658d0f63e501824d6c23e06d4bb95c71e7d704537c9d9272f488ac03a370d448
2025-Dec-25 11:36:42.323386
#10 DONE 0.0s
2025-Dec-25 11:36:42.323386
2025-Dec-25 11:36:42.323386
#11 [dashboard internal] load build context
2025-Dec-25 11:36:42.323386
#11 transferring context: 837.63kB 0.1s done
2025-Dec-25 11:36:42.323386
#11 DONE 0.1s
2025-Dec-25 11:36:42.323386
2025-Dec-25 11:36:42.323386
#12 [dashboard deps 2/4] WORKDIR /app
2025-Dec-25 11:36:42.323386
#12 CACHED
2025-Dec-25 11:36:42.323386
2025-Dec-25 11:36:42.323386
#13 [dashboard deps 3/4] COPY package*.json ./
2025-Dec-25 11:36:42.323386
#13 CACHED
2025-Dec-25 11:36:42.323386
2025-Dec-25 11:36:42.323386
#9 [api internal] load build context
2025-Dec-25 11:36:47.452642
#9 transferring context: 219.06MB 5.3s
2025-Dec-25 11:36:49.076056
#9 transferring context: 330.52MB 7.0s done
2025-Dec-25 11:36:49.195225
#9 DONE 7.0s
2025-Dec-25 11:36:49.195225
2025-Dec-25 11:36:49.195225
#14 [api 2/5] WORKDIR /app
2025-Dec-25 11:36:49.195225
#14 CACHED
2025-Dec-25 11:36:49.195225
2025-Dec-25 11:36:49.195225
#15 [api 3/5] COPY requirements.txt .
2025-Dec-25 11:36:49.195225
#15 CACHED
2025-Dec-25 11:36:49.195225
2025-Dec-25 11:36:49.195225
#16 [dashboard deps 4/4] RUN npm install
2025-Dec-25 11:36:49.346606
#16 ...
2025-Dec-25 11:36:49.346606
2025-Dec-25 11:36:49.346606
#17 [api 4/5] RUN pip install -r requirements.txt
2025-Dec-25 11:36:52.217709
#17 3.022 Collecting fastapi (from -r requirements.txt (line 1))
2025-Dec-25 11:36:52.223528
2025-Dec-25 11:36:52.401670
#17 3.054   Downloading fastapi-0.127.0-py3-none-any.whl.metadata (30 kB)
2025-Dec-25 11:36:52.412618
2025-Dec-25 11:36:52.540313
#17 3.344 Collecting sqlalchemy (from -r requirements.txt (line 3))
2025-Dec-25 11:36:52.649328
#17 3.351   Downloading sqlalchemy-2.0.45-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (9.5 kB)
2025-Dec-25 11:36:52.658776
#17 3.454 Collecting psycopg2-binary (from -r requirements.txt (line 4))
2025-Dec-25 11:36:52.753005
#17 3.460   Downloading psycopg2_binary-2.9.11-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (4.9 kB)
2025-Dec-25 11:36:52.753005
#17 3.501 Collecting httpx (from -r requirements.txt (line 5))
2025-Dec-25 11:36:52.753005
#17 3.508   Downloading httpx-0.28.1-py3-none-any.whl.metadata (7.1 kB)
2025-Dec-25 11:36:52.753005
#17 3.557 Collecting python-keycloak (from -r requirements.txt (line 6))
2025-Dec-25 11:36:52.858190
#17 3.566   Downloading python_keycloak-5.8.1-py3-none-any.whl.metadata (6.0 kB)
2025-Dec-25 11:36:52.892064
#17 3.599 Collecting minio (from -r requirements.txt (line 7))
2025-Dec-25 11:36:52.892064
#17 3.607   Downloading minio-7.2.20-py3-none-any.whl.metadata (6.5 kB)
2025-Dec-25 11:36:52.892064
#17 3.654 Collecting requests (from -r requirements.txt (line 8))
2025-Dec-25 11:36:52.892064
#17 3.663   Downloading requests-2.32.5-py3-none-any.whl.metadata (4.9 kB)
2025-Dec-25 11:36:52.982750
#17 3.709 Collecting python-dotenv (from -r requirements.txt (line 9))
2025-Dec-25 11:36:52.982750
#17 3.717   Downloading python_dotenv-1.2.1-py3-none-any.whl.metadata (25 kB)
2025-Dec-25 11:36:52.982750
#17 3.787 Collecting uvicorn[standard] (from -r requirements.txt (line 2))
2025-Dec-25 11:36:53.096523
#17 3.792   Downloading uvicorn-0.40.0-py3-none-any.whl.metadata (6.7 kB)
2025-Dec-25 11:36:53.108665
#17 3.825 Collecting passlib[bcrypt] (from -r requirements.txt (line 10))
2025-Dec-25 11:36:53.108665
#17 3.830   Downloading passlib-1.7.4-py2.py3-none-any.whl.metadata (1.7 kB)
2025-Dec-25 11:36:53.108665
#17 3.854 Collecting python-jose[cryptography] (from -r requirements.txt (line 11))
2025-Dec-25 11:36:53.108665
#17 3.858   Downloading python_jose-3.5.0-py2.py3-none-any.whl.metadata (5.5 kB)
2025-Dec-25 11:36:53.108665
#17 3.901 Collecting starlette<0.51.0,>=0.40.0 (from fastapi->-r requirements.txt (line 1))
2025-Dec-25 11:36:53.257564
#17 3.908   Downloading starlette-0.50.0-py3-none-any.whl.metadata (6.3 kB)
2025-Dec-25 11:36:53.430243
#17 4.233 Collecting pydantic>=2.7.0 (from fastapi->-r requirements.txt (line 1))
2025-Dec-25 11:36:53.547100
#17 4.241   Downloading pydantic-2.12.5-py3-none-any.whl.metadata (90 kB)
2025-Dec-25 11:36:53.547100
#17 4.279 Collecting typing-extensions>=4.8.0 (from fastapi->-r requirements.txt (line 1))
2025-Dec-25 11:36:53.547100
#17 4.283   Downloading typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
2025-Dec-25 11:36:53.547100
#17 4.305 Collecting annotated-doc>=0.0.2 (from fastapi->-r requirements.txt (line 1))
2025-Dec-25 11:36:53.547100
#17 4.312   Downloading annotated_doc-0.0.4-py3-none-any.whl.metadata (6.6 kB)
2025-Dec-25 11:36:53.547100
#17 4.349 Collecting click>=7.0 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 11:36:53.681742
#17 4.355   Downloading click-8.3.1-py3-none-any.whl.metadata (2.6 kB)
2025-Dec-25 11:36:53.681742
#17 4.390 Collecting h11>=0.8 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 11:36:53.681742
#17 4.398   Downloading h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
2025-Dec-25 11:36:53.681742
#17 4.476 Collecting httptools>=0.6.3 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 11:36:53.781835
#17 4.485   Downloading httptools-0.7.1-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (3.5 kB)
2025-Dec-25 11:36:53.781835
#17 4.576 Collecting pyyaml>=5.1 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 11:36:53.781835
#17 4.586   Downloading pyyaml-6.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.4 kB)
2025-Dec-25 11:36:53.944934
#17 4.628 Collecting uvloop>=0.15.1 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 11:36:53.944934
#17 4.634   Downloading uvloop-0.22.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (4.9 kB)
2025-Dec-25 11:36:53.944934
#17 4.740 Collecting watchfiles>=0.13 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 11:36:54.184597
#17 4.747   Downloading watchfiles-1.1.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.9 kB)
2025-Dec-25 11:36:54.184597
#17 4.834 Collecting websockets>=10.4 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 11:36:54.184597
#17 4.838   Downloading websockets-15.0.1-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.8 kB)
2025-Dec-25 11:36:54.244657
#17 5.045 Collecting greenlet>=1 (from sqlalchemy->-r requirements.txt (line 3))
2025-Dec-25 11:36:54.365002
#17 5.053   Downloading greenlet-3.3.0-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (4.1 kB)
2025-Dec-25 11:36:54.365002
#17 5.129 Collecting anyio (from httpx->-r requirements.txt (line 5))
2025-Dec-25 11:36:54.365002
#17 5.134   Downloading anyio-4.12.0-py3-none-any.whl.metadata (4.3 kB)
2025-Dec-25 11:36:54.365002
#17 5.169 Collecting certifi (from httpx->-r requirements.txt (line 5))
2025-Dec-25 11:36:54.472618
#17 5.173   Downloading certifi-2025.11.12-py3-none-any.whl.metadata (2.5 kB)
2025-Dec-25 11:36:54.472618
#17 5.201 Collecting httpcore==1.* (from httpx->-r requirements.txt (line 5))
2025-Dec-25 11:36:54.472618
#17 5.207   Downloading httpcore-1.0.9-py3-none-any.whl.metadata (21 kB)
2025-Dec-25 11:36:54.472618
#17 5.227 Collecting idna (from httpx->-r requirements.txt (line 5))
2025-Dec-25 11:36:54.472618
#17 5.230   Downloading idna-3.11-py3-none-any.whl.metadata (8.4 kB)
2025-Dec-25 11:36:54.472618
#17 5.254 Collecting aiofiles>=24.1.0 (from python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 11:36:54.472618
#17 5.257   Downloading aiofiles-25.1.0-py3-none-any.whl.metadata (6.3 kB)
2025-Dec-25 11:36:54.472618
#17 5.276 Collecting async-property>=0.2.2 (from python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 11:36:54.575270
#17 5.282   Downloading async_property-0.2.2-py2.py3-none-any.whl.metadata (5.3 kB)
2025-Dec-25 11:36:54.575270
#17 5.300 Collecting deprecation>=2.1.0 (from python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 11:36:54.575270
#17 5.304   Downloading deprecation-2.1.0-py2.py3-none-any.whl.metadata (4.6 kB)
2025-Dec-25 11:36:54.575270
#17 5.328 Collecting jwcrypto>=1.5.4 (from python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 11:36:54.575270
#17 5.340   Downloading jwcrypto-1.5.6-py3-none-any.whl.metadata (3.1 kB)
2025-Dec-25 11:36:54.575270
#17 5.373 Collecting requests-toolbelt>=0.6.0 (from python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 11:36:54.575270
#17 5.379   Downloading requests_toolbelt-1.0.0-py2.py3-none-any.whl.metadata (14 kB)
2025-Dec-25 11:36:54.764629
#17 5.423 Collecting argon2-cffi (from minio->-r requirements.txt (line 7))
2025-Dec-25 11:36:54.764629
#17 5.436   Downloading argon2_cffi-25.1.0-py3-none-any.whl.metadata (4.1 kB)
2025-Dec-25 11:36:54.764629
#17 5.568 Collecting pycryptodome (from minio->-r requirements.txt (line 7))
2025-Dec-25 11:36:54.885408
#17 5.578   Downloading pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (3.4 kB)
2025-Dec-25 11:36:54.898301
#17 5.619 Collecting urllib3 (from minio->-r requirements.txt (line 7))
2025-Dec-25 11:36:54.898301
#17 5.622   Downloading urllib3-2.6.2-py3-none-any.whl.metadata (6.6 kB)
2025-Dec-25 11:36:54.898301
#17 5.690 Collecting charset_normalizer<4,>=2 (from requests->-r requirements.txt (line 8))
2025-Dec-25 11:36:54.988578
#17 5.696   Downloading charset_normalizer-3.4.4-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (37 kB)
2025-Dec-25 11:36:54.988578
#17 5.781 Collecting bcrypt>=3.1.0 (from passlib[bcrypt]->-r requirements.txt (line 10))
2025-Dec-25 11:36:54.988578
#17 5.791   Downloading bcrypt-5.0.0-cp39-abi3-manylinux_2_34_x86_64.whl.metadata (10 kB)
2025-Dec-25 11:36:55.090694
#17 5.839 Collecting ecdsa!=0.15 (from python-jose[cryptography]->-r requirements.txt (line 11))
2025-Dec-25 11:36:55.090694
#17 5.848   Downloading ecdsa-0.19.1-py2.py3-none-any.whl.metadata (29 kB)
2025-Dec-25 11:36:55.090694
#17 5.895 Collecting rsa!=4.1.1,!=4.4,<5.0,>=4.0 (from python-jose[cryptography]->-r requirements.txt (line 11))
2025-Dec-25 11:36:55.302062
#17 5.899   Downloading rsa-4.9.1-py3-none-any.whl.metadata (5.6 kB)
2025-Dec-25 11:36:55.302062
#17 5.949 Collecting pyasn1>=0.5.0 (from python-jose[cryptography]->-r requirements.txt (line 11))
2025-Dec-25 11:36:55.302062
#17 5.953   Downloading pyasn1-0.6.1-py3-none-any.whl.metadata (8.4 kB)
2025-Dec-25 11:36:55.312259
#17 6.106 Collecting cryptography>=3.4.0 (from python-jose[cryptography]->-r requirements.txt (line 11))
2025-Dec-25 11:36:55.433909
#17 6.112   Downloading cryptography-46.0.3-cp311-abi3-manylinux_2_34_x86_64.whl.metadata (5.7 kB)
2025-Dec-25 11:36:55.433909
#17 6.237 Collecting cffi>=2.0.0 (from cryptography>=3.4.0->python-jose[cryptography]->-r requirements.txt (line 11))
2025-Dec-25 11:36:55.550846
#17 6.242   Downloading cffi-2.0.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (2.6 kB)
2025-Dec-25 11:36:55.550846
#17 6.276 Collecting packaging (from deprecation>=2.1.0->python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 11:36:55.550846
#17 6.282   Downloading packaging-25.0-py3-none-any.whl.metadata (3.3 kB)
2025-Dec-25 11:36:55.550846
#17 6.317 Collecting six>=1.9.0 (from ecdsa!=0.15->python-jose[cryptography]->-r requirements.txt (line 11))
2025-Dec-25 11:36:55.550846
#17 6.323   Downloading six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
2025-Dec-25 11:36:55.550846
#17 6.353 Collecting annotated-types>=0.6.0 (from pydantic>=2.7.0->fastapi->-r requirements.txt (line 1))
2025-Dec-25 11:36:55.703915
#17 6.356   Downloading annotated_types-0.7.0-py3-none-any.whl.metadata (15 kB)
2025-Dec-25 11:36:56.228247
#17 7.032 Collecting pydantic-core==2.41.5 (from pydantic>=2.7.0->fastapi->-r requirements.txt (line 1))
2025-Dec-25 11:36:56.239197
2025-Dec-25 11:36:56.350871
#17 7.037   Downloading pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (7.3 kB)
2025-Dec-25 11:36:56.357398
#17 7.073 Collecting typing-inspection>=0.4.2 (from pydantic>=2.7.0->fastapi->-r requirements.txt (line 1))
2025-Dec-25 11:36:56.357398
#17 7.079   Downloading typing_inspection-0.4.2-py3-none-any.whl.metadata (2.6 kB)
2025-Dec-25 11:36:56.357398
#17 7.155 Collecting argon2-cffi-bindings (from argon2-cffi->minio->-r requirements.txt (line 7))
2025-Dec-25 11:36:56.528215
#17 7.164   Downloading argon2_cffi_bindings-25.1.0-cp39-abi3-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl.metadata (7.4 kB)
2025-Dec-25 11:36:56.528215
#17 7.200 Collecting pycparser (from cffi>=2.0.0->cryptography>=3.4.0->python-jose[cryptography]->-r requirements.txt (line 11))
2025-Dec-25 11:36:56.528215
#17 7.204   Downloading pycparser-2.23-py3-none-any.whl.metadata (993 bytes)
2025-Dec-25 11:36:56.528215
#17 7.229 Downloading fastapi-0.127.0-py3-none-any.whl (112 kB)
2025-Dec-25 11:36:56.528215
#17 7.248 Downloading sqlalchemy-2.0.45-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (3.3 MB)
2025-Dec-25 11:36:56.528215
#17 7.333    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.3/3.3 MB 40.2 MB/s eta 0:00:00
2025-Dec-25 11:36:56.630885
2025-Dec-25 11:36:56.637593
#17 7.344 Downloading psycopg2_binary-2.9.11-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (4.2 MB)
2025-Dec-25 11:36:56.637593
#17 7.434    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.2/4.2 MB 47.0 MB/s eta 0:00:00
2025-Dec-25 11:36:56.734993
#17 7.443 Downloading httpx-0.28.1-py3-none-any.whl (73 kB)
2025-Dec-25 11:36:56.734993
#17 7.452 Downloading httpcore-1.0.9-py3-none-any.whl (78 kB)
2025-Dec-25 11:36:56.734993
#17 7.462 Downloading python_keycloak-5.8.1-py3-none-any.whl (77 kB)
2025-Dec-25 11:36:56.734993
#17 7.470 Downloading minio-7.2.20-py3-none-any.whl (93 kB)
2025-Dec-25 11:36:56.734993
#17 7.486 Downloading requests-2.32.5-py3-none-any.whl (64 kB)
2025-Dec-25 11:36:56.742674
#17 7.494 Downloading python_dotenv-1.2.1-py3-none-any.whl (21 kB)
2025-Dec-25 11:36:56.742674
#17 7.501 Downloading aiofiles-25.1.0-py3-none-any.whl (14 kB)
2025-Dec-25 11:36:56.742674
#17 7.507 Downloading annotated_doc-0.0.4-py3-none-any.whl (5.3 kB)
2025-Dec-25 11:36:56.742674
#17 7.518 Downloading async_property-0.2.2-py2.py3-none-any.whl (9.5 kB)
2025-Dec-25 11:36:56.742674
#17 7.525 Downloading bcrypt-5.0.0-cp39-abi3-manylinux_2_34_x86_64.whl (278 kB)
2025-Dec-25 11:36:56.742674
#17 7.540 Downloading certifi-2025.11.12-py3-none-any.whl (159 kB)
2025-Dec-25 11:36:56.875332
#17 7.558 Downloading charset_normalizer-3.4.4-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (153 kB)
2025-Dec-25 11:36:56.875332
#17 7.572 Downloading click-8.3.1-py3-none-any.whl (108 kB)
2025-Dec-25 11:36:56.875332
#17 7.586 Downloading cryptography-46.0.3-cp311-abi3-manylinux_2_34_x86_64.whl (4.5 MB)
2025-Dec-25 11:36:56.875332
#17 7.680    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.5/4.5 MB 49.3 MB/s eta 0:00:00
2025-Dec-25 11:36:56.977314
2025-Dec-25 11:36:56.986551
#17 7.692 Downloading deprecation-2.1.0-py2.py3-none-any.whl (11 kB)
2025-Dec-25 11:36:56.986551
#17 7.698 Downloading ecdsa-0.19.1-py2.py3-none-any.whl (150 kB)
2025-Dec-25 11:36:56.986551
#17 7.724 Downloading greenlet-3.3.0-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (609 kB)
2025-Dec-25 11:36:56.986551
#17 7.738    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 609.9/609.9 kB 30.9 MB/s eta 0:00:00
2025-Dec-25 11:36:56.986551
#17 7.744 Downloading h11-0.16.0-py3-none-any.whl (37 kB)
2025-Dec-25 11:36:56.986551
#17 7.758 Downloading httptools-0.7.1-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (517 kB)
2025-Dec-25 11:36:56.986551
#17 7.771 Downloading idna-3.11-py3-none-any.whl (71 kB)
2025-Dec-25 11:36:56.986551
#17 7.781 Downloading jwcrypto-1.5.6-py3-none-any.whl (92 kB)
2025-Dec-25 11:36:57.097689
#17 7.795 Downloading pyasn1-0.6.1-py3-none-any.whl (83 kB)
2025-Dec-25 11:36:57.097689
#17 7.802 Downloading pydantic-2.12.5-py3-none-any.whl (463 kB)
2025-Dec-25 11:36:57.097689
#17 7.821 Downloading pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.1 MB)
2025-Dec-25 11:36:57.097689
#17 7.868    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 53.4 MB/s eta 0:00:00
2025-Dec-25 11:36:57.097689
#17 7.876 Downloading pyyaml-6.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (807 kB)
2025-Dec-25 11:36:57.097689
#17 7.900    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 807.9/807.9 kB 42.4 MB/s eta 0:00:00
2025-Dec-25 11:36:57.239564
#17 7.906 Downloading requests_toolbelt-1.0.0-py2.py3-none-any.whl (54 kB)
2025-Dec-25 11:36:57.239564
#17 7.912 Downloading rsa-4.9.1-py3-none-any.whl (34 kB)
2025-Dec-25 11:36:57.239564
#17 7.921 Downloading starlette-0.50.0-py3-none-any.whl (74 kB)
2025-Dec-25 11:36:57.239564
#17 7.934 Downloading anyio-4.12.0-py3-none-any.whl (113 kB)
2025-Dec-25 11:36:57.239564
#17 7.944 Downloading typing_extensions-4.15.0-py3-none-any.whl (44 kB)
2025-Dec-25 11:36:57.239564
#17 7.952 Downloading urllib3-2.6.2-py3-none-any.whl (131 kB)
2025-Dec-25 11:36:57.239564
#17 7.960 Downloading uvloop-0.22.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (4.4 MB)
2025-Dec-25 11:36:57.239564
#17 8.043    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.4/4.4 MB 56.6 MB/s eta 0:00:00
2025-Dec-25 11:36:57.347183
#17 8.048 Downloading watchfiles-1.1.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (456 kB)
2025-Dec-25 11:36:57.347183
#17 8.067 Downloading websockets-15.0.1-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (182 kB)
2025-Dec-25 11:36:57.347183
#17 8.078 Downloading argon2_cffi-25.1.0-py3-none-any.whl (14 kB)
2025-Dec-25 11:36:57.347183
#17 8.085 Downloading passlib-1.7.4-py2.py3-none-any.whl (525 kB)
2025-Dec-25 11:36:57.347183
#17 8.097    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 525.6/525.6 kB 41.8 MB/s eta 0:00:00
2025-Dec-25 11:36:57.347183
#17 8.106 Downloading pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.3 MB)
2025-Dec-25 11:36:57.347183
#17 8.152    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.3/2.3 MB 48.7 MB/s eta 0:00:00
2025-Dec-25 11:36:57.582425
#17 8.157 Downloading python_jose-3.5.0-py2.py3-none-any.whl (34 kB)
2025-Dec-25 11:36:57.582425
#17 8.165 Downloading uvicorn-0.40.0-py3-none-any.whl (68 kB)
2025-Dec-25 11:36:57.582425
#17 8.174 Downloading annotated_types-0.7.0-py3-none-any.whl (13 kB)
2025-Dec-25 11:36:57.592798
#17 8.184 Downloading cffi-2.0.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (219 kB)
2025-Dec-25 11:36:57.592798
#17 8.195 Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
2025-Dec-25 11:36:57.592798
#17 8.203 Downloading typing_inspection-0.4.2-py3-none-any.whl (14 kB)
2025-Dec-25 11:36:57.592798
#17 8.214 Downloading argon2_cffi_bindings-25.1.0-cp39-abi3-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl (87 kB)
2025-Dec-25 11:36:57.592798
#17 8.224 Downloading packaging-25.0-py3-none-any.whl (66 kB)
2025-Dec-25 11:36:57.592798
#17 8.234 Downloading pycparser-2.23-py3-none-any.whl (118 kB)
2025-Dec-25 11:36:57.592798
#17 8.397 Installing collected packages: passlib, async-property, websockets, uvloop, urllib3, typing-extensions, six, pyyaml, python-dotenv, pycryptodome, pycparser, pyasn1, psycopg2-binary, packaging, idna, httptools, h11, greenlet, click, charset_normalizer, certifi, bcrypt, annotated-types, annotated-doc, aiofiles, uvicorn, typing-inspection, sqlalchemy, rsa, requests, pydantic-core, httpcore, ecdsa, deprecation, cffi, anyio, watchfiles, starlette, requests-toolbelt, python-jose, pydantic, httpx, cryptography, argon2-cffi-bindings, jwcrypto, fastapi, argon2-cffi, python-keycloak, minio
2025-Dec-25 11:37:04.881497
#17 15.68 Successfully installed aiofiles-25.1.0 annotated-doc-0.0.4 annotated-types-0.7.0 anyio-4.12.0 argon2-cffi-25.1.0 argon2-cffi-bindings-25.1.0 async-property-0.2.2 bcrypt-5.0.0 certifi-2025.11.12 cffi-2.0.0 charset_normalizer-3.4.4 click-8.3.1 cryptography-46.0.3 deprecation-2.1.0 ecdsa-0.19.1 fastapi-0.127.0 greenlet-3.3.0 h11-0.16.0 httpcore-1.0.9 httptools-0.7.1 httpx-0.28.1 idna-3.11 jwcrypto-1.5.6 minio-7.2.20 packaging-25.0 passlib-1.7.4 psycopg2-binary-2.9.11 pyasn1-0.6.1 pycparser-2.23 pycryptodome-3.23.0 pydantic-2.12.5 pydantic-core-2.41.5 python-dotenv-1.2.1 python-jose-3.5.0 python-keycloak-5.8.1 pyyaml-6.0.3 requests-2.32.5 requests-toolbelt-1.0.0 rsa-4.9.1 six-1.17.0 sqlalchemy-2.0.45 starlette-0.50.0 typing-extensions-4.15.0 typing-inspection-0.4.2 urllib3-2.6.2 uvicorn-0.40.0 uvloop-0.22.1 watchfiles-1.1.1 websockets-15.0.1
2025-Dec-25 11:37:05.118431
#17 15.69 WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager, possibly rendering your system unusable. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv. Use the --root-user-action option if you know what you are doing and want to suppress this warning.
2025-Dec-25 11:37:05.118431
#17 15.77
2025-Dec-25 11:37:05.118431
#17 15.77 [notice] A new release of pip is available: 25.0.1 -> 25.3
2025-Dec-25 11:37:05.118431
#17 15.77 [notice] To update, run: pip install --upgrade pip
2025-Dec-25 11:37:06.024024
#17 DONE 16.8s
2025-Dec-25 11:37:06.024024
2025-Dec-25 11:37:06.024024
#16 [dashboard deps 4/4] RUN npm install
2025-Dec-25 11:37:06.179737
#16 ...
2025-Dec-25 11:37:06.179737
2025-Dec-25 11:37:06.179737
#18 [api 5/5] COPY . .
2025-Dec-25 11:37:11.301352
#18 ...
2025-Dec-25 11:37:11.301352
2025-Dec-25 11:37:11.301352
#16 [dashboard deps 4/4] RUN npm install
2025-Dec-25 11:37:11.301352
#16 29.02
2025-Dec-25 11:37:11.301352
#16 29.02 added 473 packages, and audited 474 packages in 29s
2025-Dec-25 11:37:11.457489
#16 29.02
2025-Dec-25 11:37:11.457489
#16 29.02 154 packages are looking for funding
2025-Dec-25 11:37:11.457489
#16 29.02   run `npm fund` for details
2025-Dec-25 11:37:11.457489
#16 29.03
2025-Dec-25 11:37:11.457489
#16 29.03 found 0 vulnerabilities
2025-Dec-25 11:37:11.457489
#16 29.03 npm notice
2025-Dec-25 11:37:11.457489
#16 29.03 npm notice New major version of npm available! 10.8.2 -> 11.7.0
2025-Dec-25 11:37:11.457489
#16 29.03 npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.7.0
2025-Dec-25 11:37:11.457489
#16 29.03 npm notice To update run: npm install -g npm@11.7.0
2025-Dec-25 11:37:11.457489
#16 29.03 npm notice
2025-Dec-25 11:37:11.757740
#16 DONE 29.5s
2025-Dec-25 11:37:11.757740
2025-Dec-25 11:37:11.757740
#18 [api 5/5] COPY . .
2025-Dec-25 11:37:15.604314
#18 DONE 9.6s
2025-Dec-25 11:37:15.760767
#19 [api] exporting to image
2025-Dec-25 11:37:15.760767
#19 exporting layers
2025-Dec-25 11:37:15.863504
#19 ...
2025-Dec-25 11:37:15.863504
2025-Dec-25 11:37:15.863504
#20 [dashboard builder 3/5] COPY --from=deps /app/node_modules ./node_modules
2025-Dec-25 11:37:15.863504
#20 CACHED
2025-Dec-25 11:37:15.863504
2025-Dec-25 11:37:15.863504
#21 [dashboard builder 4/5] COPY . .
2025-Dec-25 11:37:15.863504
#21 CACHED
2025-Dec-25 11:37:16.031784
#22 [dashboard builder 5/5] RUN npm run build
2025-Dec-25 11:37:16.675695
#22 0.872
2025-Dec-25 11:37:16.675695
#22 0.872 > dashboard@0.1.0 build
2025-Dec-25 11:37:16.675695
#22 0.872 > next build
2025-Dec-25 11:37:16.675695
#22 0.872
2025-Dec-25 11:37:18.009693
#22 2.209 Attention: Next.js now collects completely anonymous telemetry regarding usage.
2025-Dec-25 11:37:18.177291
#22 2.210 This information is used to shape Next.js' roadmap and prioritize features.
2025-Dec-25 11:37:18.177291
#22 2.212 You can learn more, including how to opt-out if you'd not like to participate in this anonymous program, by visiting the following URL:
2025-Dec-25 11:37:18.177291
#22 2.212 https://nextjs.org/telemetry
2025-Dec-25 11:37:18.177291
#22 2.212
2025-Dec-25 11:37:18.177291
#22 2.233 ▲ Next.js 16.1.0 (Turbopack)
2025-Dec-25 11:37:18.177291
#22 2.234
2025-Dec-25 11:37:18.177291
#22 2.377   Creating an optimized production build ...
2025-Dec-25 11:37:19.962253
#22 ...
2025-Dec-25 11:37:19.962253
2025-Dec-25 11:37:19.962253
#19 [api] exporting to image
2025-Dec-25 11:37:19.962253
#19 exporting layers 4.2s done
2025-Dec-25 11:37:19.962253
#19 writing image sha256:04ee52ebe21213cfb609395e4b4d3f570929ee3e71dad17c641f3a76f7edd2a0 done
2025-Dec-25 11:37:19.962253
#19 naming to docker.io/library/hck4w0k4ww8kk4gccw000ggg-api done
2025-Dec-25 11:37:19.962253
#19 DONE 4.2s
2025-Dec-25 11:37:19.962253
2025-Dec-25 11:37:19.962253
#23 [api] resolving provenance for metadata file
2025-Dec-25 11:37:19.962253
#23 DONE 0.0s
2025-Dec-25 11:37:20.109004
#22 [dashboard builder 5/5] RUN npm run build
2025-Dec-25 11:37:35.121809
#22 19.32 ✓ Compiled successfully in 16.3s
2025-Dec-25 11:37:35.293253
#22 19.34   Running TypeScript ...
2025-Dec-25 11:37:44.953709
#22 29.15   Collecting page data using 1 worker ...
2025-Dec-25 11:37:45.564178
#22 29.76   Generating static pages using 1 worker (0/11) ...
2025-Dec-25 11:37:45.881610
#22 30.08   Generating static pages using 1 worker (2/11)
2025-Dec-25 11:37:45.881610
#22 30.08   Generating static pages using 1 worker (5/11)
2025-Dec-25 11:37:46.104788
#22 30.08   Generating static pages using 1 worker (8/11)
2025-Dec-25 11:37:46.104788
#22 30.14 ✓ Generating static pages using 1 worker (11/11) in 374.0ms
2025-Dec-25 11:37:46.104788
#22 30.14   Finalizing page optimization ...
2025-Dec-25 11:37:46.104788
#22 30.15
2025-Dec-25 11:37:46.104788
#22 30.15 Route (app)
2025-Dec-25 11:37:46.104788
#22 30.15 ┌ ○ /
2025-Dec-25 11:37:46.104788
#22 30.15 ├ ○ /_not-found
2025-Dec-25 11:37:46.104788
#22 30.15 ├ ○ /login
2025-Dec-25 11:37:46.104788
#22 30.15 ├ ○ /org
2025-Dec-25 11:37:46.104788
#22 30.15 ├ ƒ /org/[orgId]/billing
2025-Dec-25 11:37:46.104788
#22 30.15 ├ ƒ /org/[orgId]/projects
2025-Dec-25 11:37:46.104788
#22 30.15 ├ ƒ /org/[orgId]/projects/new
2025-Dec-25 11:37:46.104788
#22 30.15 ├ ƒ /org/[orgId]/settings
2025-Dec-25 11:37:46.104788
#22 30.15 ├ ƒ /org/[orgId]/team
2025-Dec-25 11:37:46.104788
#22 30.15 ├ ○ /projects
2025-Dec-25 11:37:46.104788
#22 30.15 ├ ƒ /projects/[id]
2025-Dec-25 11:37:46.104788
#22 30.15 ├ ƒ /projects/[id]/auth
2025-Dec-25 11:37:46.104788
#22 30.15 ├ ƒ /projects/[id]/backups
2025-Dec-25 11:37:46.104788
#22 30.15 ├ ƒ /projects/[id]/database
2025-Dec-25 11:37:46.104788
#22 30.15 ├ ƒ /projects/[id]/database/[table]
2025-Dec-25 11:37:46.104788
#22 30.15 ├ ƒ /projects/[id]/edge-functions
2025-Dec-25 11:37:46.104788
#22 30.15 ├ ƒ /projects/[id]/logs
2025-Dec-25 11:37:46.104788
#22 30.15 ├ ƒ /projects/[id]/realtime
2025-Dec-25 11:37:46.104788
#22 30.15 ├ ƒ /projects/[id]/secrets
2025-Dec-25 11:37:46.104788
#22 30.15 ├ ƒ /projects/[id]/settings
2025-Dec-25 11:37:46.104788
#22 30.15 ├ ƒ /projects/[id]/settings/deployment
2025-Dec-25 11:37:46.104788
#22 30.15 ├ ƒ /projects/[id]/sql
2025-Dec-25 11:37:46.104788
#22 30.15 ├ ƒ /projects/[id]/storage
2025-Dec-25 11:37:46.104788
#22 30.15 ├ ○ /projects/new
2025-Dec-25 11:37:46.104788
#22 30.15 ├ ○ /settings/organization
2025-Dec-25 11:37:46.104788
#22 30.15 ├ ƒ /settings/organization/[id]
2025-Dec-25 11:37:46.104788
#22 30.15 ├ ○ /settings/profile
2025-Dec-25 11:37:46.104788
#22 30.15 └ ○ /signup
2025-Dec-25 11:37:46.104788
#22 30.15
2025-Dec-25 11:37:46.104788
#22 30.15
2025-Dec-25 11:37:46.104788
#22 30.15 ○  (Static)   prerendered as static content
2025-Dec-25 11:37:46.104788
#22 30.15 ƒ  (Dynamic)  server-rendered on demand
2025-Dec-25 11:37:46.104788
#22 30.15
2025-Dec-25 11:37:46.180559
#22 30.38 npm notice
2025-Dec-25 11:37:46.180559
#22 30.38 npm notice New major version of npm available! 10.8.2 -> 11.7.0
2025-Dec-25 11:37:46.180559
#22 30.38 npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.7.0
2025-Dec-25 11:37:46.180559
#22 30.38 npm notice To update run: npm install -g npm@11.7.0
2025-Dec-25 11:37:46.180559
#22 30.38 npm notice
2025-Dec-25 11:37:46.283701
#22 DONE 30.5s
2025-Dec-25 11:37:47.498484
2025-Dec-25 11:37:47.524441
#24 [dashboard runner 3/6] COPY --from=builder /app/public ./public
2025-Dec-25 11:37:47.524441
#24 CACHED
2025-Dec-25 11:37:47.524441
2025-Dec-25 11:37:47.524441
#25 [dashboard runner 4/6] COPY --from=builder /app/.next ./.next
2025-Dec-25 11:37:47.806933
#25 DONE 0.3s
2025-Dec-25 11:37:53.572138
#26 [dashboard runner 5/6] COPY --from=builder /app/node_modules ./node_modules
2025-Dec-25 11:38:02.264026
#26 DONE 8.7s
2025-Dec-25 11:38:02.465433
#27 [dashboard runner 6/6] COPY --from=builder /app/package.json ./package.json
2025-Dec-25 11:38:02.465433
#27 DONE 0.0s
2025-Dec-25 11:38:02.465433
2025-Dec-25 11:38:02.465433
#28 [dashboard] exporting to image
2025-Dec-25 11:38:02.465433
#28 exporting layers
2025-Dec-25 11:38:06.099935
#28 exporting layers 3.8s done
2025-Dec-25 11:38:06.175421
#28 writing image sha256:a93b4f6e7d4a47247dd2ea21faafe370ba13453c946dcca62f77d57919e41a1b done
2025-Dec-25 11:38:06.175421
#28 naming to docker.io/library/hck4w0k4ww8kk4gccw000ggg-dashboard done
2025-Dec-25 11:38:06.175421
#28 DONE 3.8s
2025-Dec-25 11:38:06.175421
2025-Dec-25 11:38:06.175421
#29 [dashboard] resolving provenance for metadata file
2025-Dec-25 11:38:06.175421
#29 DONE 0.0s
2025-Dec-25 11:38:06.182055
api  Built
2025-Dec-25 11:38:06.182055
dashboard  Built
2025-Dec-25 11:38:06.226043
Creating .env file with runtime variables for build phase.
2025-Dec-25 11:38:06.559213
[CMD]: docker exec u04wc8c0cogswcwso8cs08wc bash -c 'cat /artifacts/u04wc8c0cogswcwso8cs08wc/.env'
2025-Dec-25 11:38:06.559213
SOURCE_COMMIT=adfe8fa5a39b856c90990f4b611f7dd2c7068352
2025-Dec-25 11:38:06.559213
COOLIFY_URL=
2025-Dec-25 11:38:06.559213
COOLIFY_FQDN=
2025-Dec-25 11:38:06.559213
SERVICE_URL_DASHBOARD=https://supalove.hayataxi.online
2025-Dec-25 11:38:06.559213
SERVICE_FQDN_DASHBOARD=supalove.hayataxi.online
2025-Dec-25 11:38:06.559213
SERVICE_URL_API=https://api.hayataxi.online
2025-Dec-25 11:38:06.559213
SERVICE_FQDN_API=api.hayataxi.online
2025-Dec-25 11:38:06.559213
SERVICE_URL_KEYCLOAK=https://auth.hayataxi.online
2025-Dec-25 11:38:06.559213
SERVICE_FQDN_KEYCLOAK=auth.hayataxi.online
2025-Dec-25 11:38:06.559213
SERVICE_URL_MINIO=https://s3.hayataxi.online
2025-Dec-25 11:38:06.559213
SERVICE_FQDN_MINIO=s3.hayataxi.online
2025-Dec-25 11:38:06.559213
SERVICE_NAME_CONTROL-PLANE-DB=control-plane-db
2025-Dec-25 11:38:06.559213
SERVICE_NAME_API=api
2025-Dec-25 11:38:06.559213
SERVICE_NAME_DASHBOARD=dashboard
2025-Dec-25 11:38:06.559213
SERVICE_NAME_KEYCLOAK=keycloak
2025-Dec-25 11:38:06.559213
SERVICE_NAME_MINIO=minio
2025-Dec-25 11:38:06.559213
POSTGRES_USER=platform
2025-Dec-25 11:38:06.559213
POSTGRES_PASSWORD=platform
2025-Dec-25 11:38:06.559213
POSTGRES_DB=control_plane
2025-Dec-25 11:38:06.559213
KEYCLOAK_ADMIN_USER=admin
2025-Dec-25 11:38:06.559213
KEYCLOAK_ADMIN_PASSWORD=admin
2025-Dec-25 11:38:06.559213
MINIO_ROOT_USER=minioadmin
2025-Dec-25 11:38:06.559213
MINIO_ROOT_PASSWORD=minioadmin
2025-Dec-25 11:38:06.559213
URL=http://localhost:8000
2025-Dec-25 11:38:06.559213
NEXT_PUBLIC_API_URL=https://api.hayataxi.online
2025-Dec-25 11:38:06.559213
HOST=0.0.0.0
2025-Dec-25 11:38:06.691983
Removing old containers.
2025-Dec-25 11:38:07.087539
[CMD]: docker stop --time=30 dashboard-hck4w0k4ww8kk4gccw000ggg-111416808698
2025-Dec-25 11:38:07.087539
dashboard-hck4w0k4ww8kk4gccw000ggg-111416808698
2025-Dec-25 11:38:07.221388
[CMD]: docker rm -f dashboard-hck4w0k4ww8kk4gccw000ggg-111416808698
2025-Dec-25 11:38:07.221388
dashboard-hck4w0k4ww8kk4gccw000ggg-111416808698
2025-Dec-25 11:38:07.340614
[CMD]: docker stop --time=30 api-hck4w0k4ww8kk4gccw000ggg-111416796282
2025-Dec-25 11:38:07.340614
api-hck4w0k4ww8kk4gccw000ggg-111416796282
2025-Dec-25 11:38:07.471265
[CMD]: docker rm -f api-hck4w0k4ww8kk4gccw000ggg-111416796282
2025-Dec-25 11:38:07.471265
api-hck4w0k4ww8kk4gccw000ggg-111416796282
2025-Dec-25 11:38:07.789952
[CMD]: docker stop --time=30 keycloak-hck4w0k4ww8kk4gccw000ggg-111416818698
2025-Dec-25 11:38:07.789952
keycloak-hck4w0k4ww8kk4gccw000ggg-111416818698
2025-Dec-25 11:38:07.955252
[CMD]: docker rm -f keycloak-hck4w0k4ww8kk4gccw000ggg-111416818698
2025-Dec-25 11:38:07.955252
keycloak-hck4w0k4ww8kk4gccw000ggg-111416818698
2025-Dec-25 11:38:08.215349
[CMD]: docker stop --time=30 control-plane-db-hck4w0k4ww8kk4gccw000ggg-111416780961
2025-Dec-25 11:38:08.215349
control-plane-db-hck4w0k4ww8kk4gccw000ggg-111416780961
2025-Dec-25 11:38:08.350835
[CMD]: docker rm -f control-plane-db-hck4w0k4ww8kk4gccw000ggg-111416780961
2025-Dec-25 11:38:08.350835
control-plane-db-hck4w0k4ww8kk4gccw000ggg-111416780961
2025-Dec-25 11:38:08.618006
[CMD]: docker stop --time=30 minio-hck4w0k4ww8kk4gccw000ggg-111416831360
2025-Dec-25 11:38:08.618006
minio-hck4w0k4ww8kk4gccw000ggg-111416831360
2025-Dec-25 11:38:08.737347
[CMD]: docker rm -f minio-hck4w0k4ww8kk4gccw000ggg-111416831360
2025-Dec-25 11:38:08.737347
minio-hck4w0k4ww8kk4gccw000ggg-111416831360
2025-Dec-25 11:38:08.744675
Starting new application.
2025-Dec-25 11:38:09.374314
[CMD]: docker exec u04wc8c0cogswcwso8cs08wc bash -c 'SOURCE_COMMIT=adfe8fa5a39b856c90990f4b611f7dd2c7068352 COOLIFY_BRANCH=main COOLIFY_RESOURCE_UUID=hck4w0k4ww8kk4gccw000ggg COOLIFY_CONTAINER_NAME=hck4w0k4ww8kk4gccw000ggg-113620930993  docker compose --env-file /artifacts/u04wc8c0cogswcwso8cs08wc/.env --project-name hck4w0k4ww8kk4gccw000ggg --project-directory /artifacts/u04wc8c0cogswcwso8cs08wc -f /artifacts/u04wc8c0cogswcwso8cs08wc/docker-compose.coolify.yml up -d'
2025-Dec-25 11:38:09.374314
Container minio-hck4w0k4ww8kk4gccw000ggg-113638649957  Creating
2025-Dec-25 11:38:09.374314
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-113638601013  Creating
2025-Dec-25 11:38:09.423339
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-113638601013  Created
2025-Dec-25 11:38:09.423339
Container keycloak-hck4w0k4ww8kk4gccw000ggg-113638637738  Creating
2025-Dec-25 11:38:09.423339
Container minio-hck4w0k4ww8kk4gccw000ggg-113638649957  Created
2025-Dec-25 11:38:09.446531
Container keycloak-hck4w0k4ww8kk4gccw000ggg-113638637738  Created
2025-Dec-25 11:38:09.446531
Container api-hck4w0k4ww8kk4gccw000ggg-113638615535  Creating
2025-Dec-25 11:38:09.464433
Container api-hck4w0k4ww8kk4gccw000ggg-113638615535  Created
2025-Dec-25 11:38:09.471842
Container dashboard-hck4w0k4ww8kk4gccw000ggg-113638628690  Creating
2025-Dec-25 11:38:09.481732
Container dashboard-hck4w0k4ww8kk4gccw000ggg-113638628690  Created
2025-Dec-25 11:38:09.488391
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-113638601013  Starting
2025-Dec-25 11:38:09.488391
Container minio-hck4w0k4ww8kk4gccw000ggg-113638649957  Starting
2025-Dec-25 11:38:09.784472
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-113638601013  Started
2025-Dec-25 11:38:09.784472
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-113638601013  Waiting
2025-Dec-25 11:38:09.850648
Container minio-hck4w0k4ww8kk4gccw000ggg-113638649957  Started
2025-Dec-25 11:38:15.286448
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-113638601013  Healthy
2025-Dec-25 11:38:15.286448
Container keycloak-hck4w0k4ww8kk4gccw000ggg-113638637738  Starting
2025-Dec-25 11:38:15.500066
Container keycloak-hck4w0k4ww8kk4gccw000ggg-113638637738  Started
2025-Dec-25 11:38:15.500066
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-113638601013  Waiting
2025-Dec-25 11:38:16.006833
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-113638601013  Healthy
2025-Dec-25 11:38:16.006833
Container api-hck4w0k4ww8kk4gccw000ggg-113638615535  Starting
2025-Dec-25 11:38:16.336503
Container api-hck4w0k4ww8kk4gccw000ggg-113638615535  Started
2025-Dec-25 11:38:16.336503
Container dashboard-hck4w0k4ww8kk4gccw000ggg-113638628690  Starting
2025-Dec-25 11:38:16.713711
Container dashboard-hck4w0k4ww8kk4gccw000ggg-113638628690  Started
2025-Dec-25 11:38:17.576646
New container started.
2025-Dec-25 11:38:18.781223
Gracefully shutting down build container: u04wc8c0cogswcwso8cs08wc
2025-Dec-25 11:38:19.856506
[CMD]: docker stop --time=30 u04wc8c0cogswcwso8cs08wc
2025-Dec-25 11:38:19.856506
u04wc8c0cogswcwso8cs08wc
2025-Dec-25 11:38:20.141095
[CMD]: docker rm -f u04wc8c0cogswcwso8cs08wc
2025-Dec-25 11:38:20.141095
Error response from daemon: removal of container u04wc8c0cogswcwso8cs08wc is already in progress