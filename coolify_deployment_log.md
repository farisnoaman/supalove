2025-Dec-25 10:45:32.574901
Starting deployment of supalove to localhost.
2025-Dec-25 10:45:33.236276
Preparing container with helper image: ghcr.io/coollabsio/coolify-helper:1.0.12
2025-Dec-25 10:45:33.568211
[CMD]: docker stop --time=30 rogwc4s4s0cwwkoscgg00go8
2025-Dec-25 10:45:33.568211
Error response from daemon: No such container: rogwc4s4s0cwwkoscgg00go8
2025-Dec-25 10:45:33.900842
[CMD]: docker rm -f rogwc4s4s0cwwkoscgg00go8
2025-Dec-25 10:45:33.900842
Error response from daemon: No such container: rogwc4s4s0cwwkoscgg00go8
2025-Dec-25 10:45:34.272236
[CMD]: docker run -d --network coolify --name rogwc4s4s0cwwkoscgg00go8  --rm -v /var/run/docker.sock:/var/run/docker.sock ghcr.io/coollabsio/coolify-helper:1.0.12
2025-Dec-25 10:45:34.272236
c8f2bb3f52e399c958c49944bb6419f6f28be7b1c5f0642b57e4724a092d8ca4
2025-Dec-25 10:45:35.561826
[CMD]: docker exec rogwc4s4s0cwwkoscgg00go8 bash -c 'GIT_SSH_COMMAND="ssh -o ConnectTimeout=30 -p 22 -o Port=22 -o LogLevel=ERROR -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" git ls-remote https://github.com/farisnoaman/supalove refs/heads/main'
2025-Dec-25 10:45:35.561826
d74b420205cdec807791ed43c25e610c4e16482e	refs/heads/main
2025-Dec-25 10:45:35.582277
----------------------------------------
2025-Dec-25 10:45:35.587909
Importing farisnoaman/supalove:main (commit sha d74b420205cdec807791ed43c25e610c4e16482e) to /artifacts/rogwc4s4s0cwwkoscgg00go8.
2025-Dec-25 10:45:35.954932
[CMD]: docker exec rogwc4s4s0cwwkoscgg00go8 bash -c 'git clone --depth=1 --recurse-submodules --shallow-submodules -b 'main' 'https://github.com/farisnoaman/supalove' '/artifacts/rogwc4s4s0cwwkoscgg00go8' && cd '/artifacts/rogwc4s4s0cwwkoscgg00go8' && if [ -f .gitmodules ]; then sed -i "s#git@\(.*\):#https://\1/#g" '/artifacts/rogwc4s4s0cwwkoscgg00go8'/.gitmodules || true && git submodule sync && GIT_SSH_COMMAND="ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" git submodule update --init --recursive --depth=1; fi && cd '/artifacts/rogwc4s4s0cwwkoscgg00go8' && GIT_SSH_COMMAND="ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" git lfs pull'
2025-Dec-25 10:45:35.954932
Cloning into '/artifacts/rogwc4s4s0cwwkoscgg00go8'...
2025-Dec-25 10:45:42.414972
Updating files:  26% (3955/15083)
2025-Dec-25 10:45:42.438190
Updating files:  27% (4073/15083)
2025-Dec-25 10:45:42.465864
Updating files:  28% (4224/15083)
2025-Dec-25 10:45:42.485676
Updating files:  29% (4375/15083)
2025-Dec-25 10:45:42.503484
Updating files:  30% (4525/15083)
2025-Dec-25 10:45:42.515179
Updating files:  31% (4676/15083)
2025-Dec-25 10:45:42.529183
Updating files:  32% (4827/15083)
2025-Dec-25 10:45:42.544033
Updating files:  33% (4978/15083)
2025-Dec-25 10:45:42.580541
Updating files:  34% (5129/15083)
2025-Dec-25 10:45:42.612891
Updating files:  35% (5280/15083)
2025-Dec-25 10:45:42.655998
Updating files:  36% (5430/15083)
2025-Dec-25 10:45:42.696533
Updating files:  37% (5581/15083)
2025-Dec-25 10:45:42.714714
Updating files:  38% (5732/15083)
2025-Dec-25 10:45:42.732778
Updating files:  39% (5883/15083)
2025-Dec-25 10:45:42.750357
Updating files:  40% (6034/15083)
2025-Dec-25 10:45:42.768163
Updating files:  41% (6185/15083)
2025-Dec-25 10:45:42.784714
Updating files:  42% (6335/15083)
2025-Dec-25 10:45:42.796702
Updating files:  43% (6486/15083)
2025-Dec-25 10:45:42.809194
Updating files:  44% (6637/15083)
2025-Dec-25 10:45:42.820853
Updating files:  45% (6788/15083)
2025-Dec-25 10:45:42.834338
Updating files:  46% (6939/15083)
2025-Dec-25 10:45:42.847817
Updating files:  47% (7090/15083)
2025-Dec-25 10:45:42.863581
Updating files:  48% (7240/15083)
2025-Dec-25 10:45:42.875859
Updating files:  49% (7391/15083)
2025-Dec-25 10:45:42.891545
Updating files:  50% (7542/15083)
2025-Dec-25 10:45:42.901649
Updating files:  51% (7693/15083)
2025-Dec-25 10:45:42.918387
Updating files:  52% (7844/15083)
2025-Dec-25 10:45:42.937211
Updating files:  53% (7994/15083)
2025-Dec-25 10:45:42.959039
Updating files:  54% (8145/15083)
2025-Dec-25 10:45:43.054986
Updating files:  55% (8296/15083)
2025-Dec-25 10:45:43.096617
Updating files:  56% (8447/15083)
2025-Dec-25 10:45:43.108155
Updating files:  57% (8598/15083)
2025-Dec-25 10:45:43.125266
Updating files:  58% (8749/15083)
2025-Dec-25 10:45:43.147954
Updating files:  59% (8899/15083)
2025-Dec-25 10:45:43.161807
Updating files:  60% (9050/15083)
2025-Dec-25 10:45:43.180693
Updating files:  61% (9201/15083)
2025-Dec-25 10:45:43.196938
Updating files:  62% (9352/15083)
2025-Dec-25 10:45:43.209974
Updating files:  63% (9503/15083)
2025-Dec-25 10:45:43.223430
Updating files:  64% (9654/15083)
2025-Dec-25 10:45:43.296604
Updating files:  65% (9804/15083)
2025-Dec-25 10:45:43.309641
Updating files:  66% (9955/15083)
2025-Dec-25 10:45:43.324658
Updating files:  67% (10106/15083)
2025-Dec-25 10:45:43.343155
Updating files:  68% (10257/15083)
2025-Dec-25 10:45:43.362198
Updating files:  69% (10408/15083)
2025-Dec-25 10:45:43.379737
Updating files:  70% (10559/15083)
2025-Dec-25 10:45:43.391670
Updating files:  70% (10694/15083)
2025-Dec-25 10:45:43.394979
Updating files:  71% (10709/15083)
2025-Dec-25 10:45:43.411195
Updating files:  72% (10860/15083)
2025-Dec-25 10:45:43.425762
Updating files:  73% (11011/15083)
2025-Dec-25 10:45:43.438891
Updating files:  74% (11162/15083)
2025-Dec-25 10:45:43.455860
Updating files:  75% (11313/15083)
2025-Dec-25 10:45:43.470995
Updating files:  76% (11464/15083)
2025-Dec-25 10:45:43.484903
Updating files:  77% (11614/15083)
2025-Dec-25 10:45:43.496957
Updating files:  78% (11765/15083)
2025-Dec-25 10:45:43.511982
Updating files:  79% (11916/15083)
2025-Dec-25 10:45:43.583143
Updating files:  80% (12067/15083)
2025-Dec-25 10:45:43.596375
Updating files:  81% (12218/15083)
2025-Dec-25 10:45:43.635208
Updating files:  82% (12369/15083)
2025-Dec-25 10:45:43.645772
Updating files:  83% (12519/15083)
2025-Dec-25 10:45:43.661035
Updating files:  84% (12670/15083)
2025-Dec-25 10:45:43.681841
Updating files:  85% (12821/15083)
2025-Dec-25 10:45:43.693210
Updating files:  86% (12972/15083)
2025-Dec-25 10:45:43.705209
Updating files:  87% (13123/15083)
2025-Dec-25 10:45:43.740122
Updating files:  88% (13274/15083)
2025-Dec-25 10:45:43.759860
Updating files:  89% (13424/15083)
2025-Dec-25 10:45:43.783268
Updating files:  90% (13575/15083)
2025-Dec-25 10:45:43.805696
Updating files:  91% (13726/15083)
2025-Dec-25 10:45:43.817365
Updating files:  92% (13877/15083)
2025-Dec-25 10:45:43.829058
Updating files:  93% (14028/15083)
2025-Dec-25 10:45:43.910586
Updating files:  94% (14179/15083)
2025-Dec-25 10:45:43.939391
Updating files:  95% (14329/15083)
2025-Dec-25 10:45:43.960637
Updating files:  96% (14480/15083)
2025-Dec-25 10:45:43.979832
Updating files:  97% (14631/15083)
2025-Dec-25 10:45:43.994580
Updating files:  98% (14782/15083)
2025-Dec-25 10:45:44.017010
Updating files:  99% (14933/15083)
2025-Dec-25 10:45:44.032158
Updating files: 100% (15083/15083)
Updating files: 100% (15083/15083), done.
2025-Dec-25 10:45:45.229962
[CMD]: docker exec rogwc4s4s0cwwkoscgg00go8 bash -c 'cd /artifacts/rogwc4s4s0cwwkoscgg00go8 && git log -1 d74b420205cdec807791ed43c25e610c4e16482e --pretty=%B'
2025-Dec-25 10:45:45.229962
feat: Upgrade Node.js to v20 and configure `NEXT_PUBLIC_API_URL` as a build argument for the dashboard service.
2025-Dec-25 10:45:53.250662
[CMD]: docker exec rogwc4s4s0cwwkoscgg00go8 bash -c 'test -f /artifacts/rogwc4s4s0cwwkoscgg00go8/control-plane/api/Dockerfile && echo 'exists' || echo 'not found''
2025-Dec-25 10:45:53.250662
exists
2025-Dec-25 10:45:53.682158
[CMD]: docker exec rogwc4s4s0cwwkoscgg00go8 bash -c 'cat /artifacts/rogwc4s4s0cwwkoscgg00go8/control-plane/api/Dockerfile'
2025-Dec-25 10:45:53.682158
FROM python:3.12-slim
2025-Dec-25 10:45:53.682158
WORKDIR /app
2025-Dec-25 10:45:53.682158
COPY requirements.txt .
2025-Dec-25 10:45:53.682158
RUN pip install -r requirements.txt
2025-Dec-25 10:45:53.682158
COPY . .
2025-Dec-25 10:45:53.682158
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
2025-Dec-25 10:45:54.149503
Added 20 ARG declarations to Dockerfile for service api.
2025-Dec-25 10:45:54.552926
[CMD]: docker exec rogwc4s4s0cwwkoscgg00go8 bash -c 'test -f /artifacts/rogwc4s4s0cwwkoscgg00go8/dashboard/Dockerfile && echo 'exists' || echo 'not found''
2025-Dec-25 10:45:54.552926
exists
2025-Dec-25 10:45:55.008683
[CMD]: docker exec rogwc4s4s0cwwkoscgg00go8 bash -c 'cat /artifacts/rogwc4s4s0cwwkoscgg00go8/dashboard/Dockerfile'
2025-Dec-25 10:45:55.008683
# Stage 1: Dependencies
2025-Dec-25 10:45:55.008683
FROM node:20-alpine AS deps
2025-Dec-25 10:45:55.008683
WORKDIR /app
2025-Dec-25 10:45:55.008683
COPY package*.json ./
2025-Dec-25 10:45:55.008683
RUN npm install
2025-Dec-25 10:45:55.008683
2025-Dec-25 10:45:55.008683
# Stage 2: Builder
2025-Dec-25 10:45:55.008683
FROM node:20-alpine AS builder
2025-Dec-25 10:45:55.008683
WORKDIR /app
2025-Dec-25 10:45:55.008683
COPY --from=deps /app/node_modules ./node_modules
2025-Dec-25 10:45:55.008683
COPY . .
2025-Dec-25 10:45:55.008683
# Set environment variables for build if needed (e.g. backend URL)
2025-Dec-25 10:45:55.008683
# For Next.js client-side fetch, it might need to know the URL at build time if pre-rendering,
2025-Dec-25 10:45:55.008683
# but we are using "use client" so it's fine.
2025-Dec-25 10:45:55.008683
ARG NEXT_PUBLIC_API_URL
2025-Dec-25 10:45:55.008683
ENV NEXT_PUBLIC_API_URL=${NEXT_PUBLIC_API_URL}
2025-Dec-25 10:45:55.008683
RUN npm run build
2025-Dec-25 10:45:55.008683
2025-Dec-25 10:45:55.008683
# Stage 3: Runner
2025-Dec-25 10:45:55.008683
FROM node:20-alpine AS runner
2025-Dec-25 10:45:55.008683
WORKDIR /app
2025-Dec-25 10:45:55.008683
ENV NODE_ENV=production
2025-Dec-25 10:45:55.008683
COPY --from=builder /app/public ./public
2025-Dec-25 10:45:55.008683
COPY --from=builder /app/.next ./.next
2025-Dec-25 10:45:55.008683
COPY --from=builder /app/node_modules ./node_modules
2025-Dec-25 10:45:55.008683
COPY --from=builder /app/package.json ./package.json
2025-Dec-25 10:45:55.008683
2025-Dec-25 10:45:55.008683
EXPOSE 3000
2025-Dec-25 10:45:55.008683
CMD ["npm", "start"]
2025-Dec-25 10:45:55.434730
Added 60 ARG declarations to Dockerfile for service dashboard (multi-stage build, added to 3 stages).
2025-Dec-25 10:45:55.442492
Pulling & building required images.
2025-Dec-25 10:45:55.475043
Creating build-time .env file in /artifacts (outside Docker context).
2025-Dec-25 10:45:56.237911
[CMD]: docker exec rogwc4s4s0cwwkoscgg00go8 bash -c 'cat /artifacts/build-time.env'
2025-Dec-25 10:45:56.237911
SOURCE_COMMIT='d74b420205cdec807791ed43c25e610c4e16482e'
2025-Dec-25 10:45:56.237911
COOLIFY_URL=''
2025-Dec-25 10:45:56.237911
COOLIFY_FQDN=''
2025-Dec-25 10:45:56.237911
SERVICE_NAME_CONTROL-PLANE-DB='control-plane-db'
2025-Dec-25 10:45:56.237911
SERVICE_NAME_API='api'
2025-Dec-25 10:45:56.237911
SERVICE_NAME_DASHBOARD='dashboard'
2025-Dec-25 10:45:56.237911
SERVICE_NAME_KEYCLOAK='keycloak'
2025-Dec-25 10:45:56.237911
SERVICE_NAME_MINIO='minio'
2025-Dec-25 10:45:56.237911
SERVICE_URL_DASHBOARD='https://supalove.hayataxi.online'
2025-Dec-25 10:45:56.237911
SERVICE_FQDN_DASHBOARD='supalove.hayataxi.online'
2025-Dec-25 10:45:56.237911
SERVICE_URL_API='https://api.supalove.hayataxi.online'
2025-Dec-25 10:45:56.237911
SERVICE_FQDN_API='api.supalove.hayataxi.online'
2025-Dec-25 10:45:56.237911
SERVICE_URL_KEYCLOAK='https://auth.supalove.hayataxi.online'
2025-Dec-25 10:45:56.237911
SERVICE_FQDN_KEYCLOAK='auth.supalove.hayataxi.online'
2025-Dec-25 10:45:56.237911
SERVICE_URL_MINIO='https://s3.supalove.hayataxi.online'
2025-Dec-25 10:45:56.237911
SERVICE_FQDN_MINIO='s3.supalove.hayataxi.online'
2025-Dec-25 10:45:56.237911
KEYCLOAK_ADMIN_PASSWORD="admin"
2025-Dec-25 10:45:56.237911
KEYCLOAK_ADMIN_USER="admin"
2025-Dec-25 10:45:56.237911
MINIO_ROOT_PASSWORD="minioadmin"
2025-Dec-25 10:45:56.237911
MINIO_ROOT_USER="minioadmin"
2025-Dec-25 10:45:56.237911
NEXT_PUBLIC_API_URL="https://api.supalove.hayataxi.online"
2025-Dec-25 10:45:56.237911
POSTGRES_DB="control_plane"
2025-Dec-25 10:45:56.237911
POSTGRES_PASSWORD="platform"
2025-Dec-25 10:45:56.237911
POSTGRES_USER="platform"
2025-Dec-25 10:45:56.237911
URL="http://localhost:8000"
2025-Dec-25 10:45:56.246479
Adding build arguments to Docker Compose build command.
2025-Dec-25 10:45:56.767904
[CMD]: docker exec rogwc4s4s0cwwkoscgg00go8 bash -c 'SOURCE_COMMIT=d74b420205cdec807791ed43c25e610c4e16482e COOLIFY_BRANCH=main COOLIFY_RESOURCE_UUID=hck4w0k4ww8kk4gccw000ggg COOLIFY_CONTAINER_NAME=hck4w0k4ww8kk4gccw000ggg-104529203943  docker compose --env-file /artifacts/build-time.env --project-name hck4w0k4ww8kk4gccw000ggg --project-directory /artifacts/rogwc4s4s0cwwkoscgg00go8 -f /artifacts/rogwc4s4s0cwwkoscgg00go8/docker-compose.coolify.yml build --pull --build-arg SOURCE_COMMIT --build-arg COOLIFY_URL --build-arg COOLIFY_FQDN --build-arg SERVICE_FQDN_API --build-arg SERVICE_FQDN_DASHBOARD --build-arg SERVICE_FQDN_KEYCLOAK --build-arg SERVICE_FQDN_MINIO --build-arg SERVICE_URL_API --build-arg SERVICE_URL_DASHBOARD --build-arg SERVICE_URL_KEYCLOAK --build-arg SERVICE_URL_MINIO --build-arg KEYCLOAK_ADMIN_PASSWORD --build-arg KEYCLOAK_ADMIN_USER --build-arg MINIO_ROOT_PASSWORD --build-arg MINIO_ROOT_USER --build-arg NEXT_PUBLIC_API_URL --build-arg POSTGRES_DB --build-arg POSTGRES_PASSWORD --build-arg POSTGRES_USER --build-arg URL --build-arg COOLIFY_BUILD_SECRETS_HASH=8741b702dbcb7a6fcb27448ca4e743836a13d67f0c8c5e545a1fcdab705c7637'
2025-Dec-25 10:45:56.767904
#1 [internal] load local bake definitions
2025-Dec-25 10:45:57.009177
#1 reading from stdin 3.15kB done
2025-Dec-25 10:45:57.009177
#1 DONE 0.0s
2025-Dec-25 10:45:57.009177
2025-Dec-25 10:45:57.009177
#2 [api internal] load build definition from Dockerfile
2025-Dec-25 10:45:57.009177
#2 transferring dockerfile: 638B done
2025-Dec-25 10:45:57.009177
#2 DONE 0.0s
2025-Dec-25 10:45:57.009177
2025-Dec-25 10:45:57.009177
#3 [dashboard internal] load build definition from Dockerfile
2025-Dec-25 10:45:57.009177
#3 transferring dockerfile: 2.14kB done
2025-Dec-25 10:45:57.009177
#3 DONE 0.0s
2025-Dec-25 10:45:57.009177
2025-Dec-25 10:45:57.009177
#4 [dashboard internal] load metadata for docker.io/library/node:20-alpine
2025-Dec-25 10:45:57.484316
#4 ...
2025-Dec-25 10:45:57.484316
2025-Dec-25 10:45:57.484316
#5 [api internal] load metadata for docker.io/library/python:3.12-slim
2025-Dec-25 10:45:57.484316
#5 DONE 0.6s
2025-Dec-25 10:45:57.624578
#6 [api internal] load .dockerignore
2025-Dec-25 10:45:57.624578
#6 transferring context: 2B done
2025-Dec-25 10:45:57.624578
#6 DONE 0.0s
2025-Dec-25 10:45:57.624578
2025-Dec-25 10:45:57.624578
#7 [api 1/5] FROM docker.io/library/python:3.12-slim@sha256:fa48eefe2146644c2308b909d6bb7651a768178f84fc9550dcd495e4d6d84d01
2025-Dec-25 10:45:57.624578
#7 DONE 0.0s
2025-Dec-25 10:45:57.624578
2025-Dec-25 10:45:57.624578
#8 [api internal] load build context
2025-Dec-25 10:45:58.333695
#8 ...
2025-Dec-25 10:45:58.333695
2025-Dec-25 10:45:58.333695
#4 [dashboard internal] load metadata for docker.io/library/node:20-alpine
2025-Dec-25 10:45:58.333695
#4 DONE 1.4s
2025-Dec-25 10:45:58.333695
2025-Dec-25 10:45:58.333695
#9 [dashboard internal] load .dockerignore
2025-Dec-25 10:45:58.333695
#9 transferring context: 2B done
2025-Dec-25 10:45:58.333695
#9 DONE 0.0s
2025-Dec-25 10:45:58.333695
2025-Dec-25 10:45:58.333695
#8 [api internal] load build context
2025-Dec-25 10:45:58.435007
#8 ...
2025-Dec-25 10:45:58.435007
2025-Dec-25 10:45:58.435007
#10 [dashboard internal] load build context
2025-Dec-25 10:45:58.435007
#10 transferring context: 837.63kB 0.1s done
2025-Dec-25 10:45:58.435007
#10 DONE 0.1s
2025-Dec-25 10:45:58.435007
2025-Dec-25 10:45:58.435007
#8 [api internal] load build context
2025-Dec-25 10:46:03.491567
#8 transferring context: 281.92MB 5.9s
2025-Dec-25 10:46:04.257325
#8 transferring context: 330.52MB 6.7s done
2025-Dec-25 10:46:04.257325
#8 DONE 6.8s
2025-Dec-25 10:46:04.257325
2025-Dec-25 10:46:04.257325
#11 [dashboard deps 1/4] FROM docker.io/library/node:20-alpine@sha256:658d0f63e501824d6c23e06d4bb95c71e7d704537c9d9272f488ac03a370d448
2025-Dec-25 10:46:04.257325
#11 resolve docker.io/library/node:20-alpine@sha256:658d0f63e501824d6c23e06d4bb95c71e7d704537c9d9272f488ac03a370d448 done
2025-Dec-25 10:46:04.257325
#11 sha256:658d0f63e501824d6c23e06d4bb95c71e7d704537c9d9272f488ac03a370d448 7.67kB / 7.67kB done
2025-Dec-25 10:46:04.257325
#11 sha256:fcbb8f7d018707c656a4da2eea8a15f2893d2258093fea9ff2ea5ea1cba82112 1.72kB / 1.72kB done
2025-Dec-25 10:46:04.257325
#11 sha256:e80b0510ba947015cacddea3d23dcdc761e399971c074a1bf32eea7e44510524 6.52kB / 6.52kB done
2025-Dec-25 10:46:04.257325
#11 sha256:1074353eec0db2c1d81d5af2671e56e00cf5738486f5762609ea33d606f88612 3.86MB / 3.86MB 0.3s done
2025-Dec-25 10:46:04.257325
#11 sha256:8d06ba6946d1f299d8f962e37906c77006df33d47050430a57f7893ec35af697 42.78MB / 42.78MB 1.4s done
2025-Dec-25 10:46:04.257325
#11 sha256:cb3325e64457574e24f92246e3da3376946e473d636209e1390eac47b50b26a3 1.26MB / 1.26MB 0.5s done
2025-Dec-25 10:46:04.257325
#11 extracting sha256:1074353eec0db2c1d81d5af2671e56e00cf5738486f5762609ea33d606f88612 0.3s done
2025-Dec-25 10:46:04.257325
#11 sha256:fd1849a5c548bc65ee47a64498951bda5d40e87d08efe9dca69b5c8cdedc7a52 443B / 443B 0.6s done
2025-Dec-25 10:46:04.257325
#11 extracting sha256:8d06ba6946d1f299d8f962e37906c77006df33d47050430a57f7893ec35af697 4.4s
2025-Dec-25 10:46:04.492163
#11 ...
2025-Dec-25 10:46:04.492163
2025-Dec-25 10:46:04.492163
#12 [api 2/5] WORKDIR /app
2025-Dec-25 10:46:04.492163
#12 CACHED
2025-Dec-25 10:46:04.492163
2025-Dec-25 10:46:04.492163
#13 [api 3/5] COPY requirements.txt .
2025-Dec-25 10:46:04.492163
#13 CACHED
2025-Dec-25 10:46:04.492163
2025-Dec-25 10:46:04.492163
#11 [dashboard deps 1/4] FROM docker.io/library/node:20-alpine@sha256:658d0f63e501824d6c23e06d4bb95c71e7d704537c9d9272f488ac03a370d448
2025-Dec-25 10:46:04.492163
#11 ...
2025-Dec-25 10:46:04.492163
2025-Dec-25 10:46:04.492163
#14 [api 4/5] RUN pip install -r requirements.txt
2025-Dec-25 10:46:05.516855
#14 ...
2025-Dec-25 10:46:05.516855
2025-Dec-25 10:46:05.516855
#11 [dashboard deps 1/4] FROM docker.io/library/node:20-alpine@sha256:658d0f63e501824d6c23e06d4bb95c71e7d704537c9d9272f488ac03a370d448
2025-Dec-25 10:46:05.516855
#11 extracting sha256:8d06ba6946d1f299d8f962e37906c77006df33d47050430a57f7893ec35af697 5.4s done
2025-Dec-25 10:46:05.516855
#11 extracting sha256:cb3325e64457574e24f92246e3da3376946e473d636209e1390eac47b50b26a3 0.0s done
2025-Dec-25 10:46:05.516855
#11 extracting sha256:fd1849a5c548bc65ee47a64498951bda5d40e87d08efe9dca69b5c8cdedc7a52 done
2025-Dec-25 10:46:05.516855
#11 DONE 7.1s
2025-Dec-25 10:46:05.586060
#15 [dashboard deps 2/4] WORKDIR /app
2025-Dec-25 10:46:05.586060
#15 DONE 0.2s
2025-Dec-25 10:46:05.594360
#14 [api 4/5] RUN pip install -r requirements.txt
2025-Dec-25 10:46:05.774566
#14 ...
2025-Dec-25 10:46:05.774566
2025-Dec-25 10:46:05.774566
#16 [dashboard deps 3/4] COPY package*.json ./
2025-Dec-25 10:46:05.774566
#16 DONE 0.0s
2025-Dec-25 10:46:05.924550
#17 [dashboard deps 4/4] RUN npm install
2025-Dec-25 10:46:10.734587
#17 ...
2025-Dec-25 10:46:10.734587
2025-Dec-25 10:46:10.734587
#14 [api 4/5] RUN pip install -r requirements.txt
2025-Dec-25 10:46:10.734587
#14 2.459 Collecting fastapi (from -r requirements.txt (line 1))
2025-Dec-25 10:46:10.734587
#14 2.484   Downloading fastapi-0.127.0-py3-none-any.whl.metadata (30 kB)
2025-Dec-25 10:46:10.734587
#14 2.779 Collecting sqlalchemy (from -r requirements.txt (line 3))
2025-Dec-25 10:46:10.734587
#14 2.787   Downloading sqlalchemy-2.0.45-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (9.5 kB)
2025-Dec-25 10:46:10.734587
#14 2.875 Collecting psycopg2-binary (from -r requirements.txt (line 4))
2025-Dec-25 10:46:10.734587
#14 2.879   Downloading psycopg2_binary-2.9.11-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (4.9 kB)
2025-Dec-25 10:46:10.734587
#14 2.904 Collecting httpx (from -r requirements.txt (line 5))
2025-Dec-25 10:46:10.734587
#14 2.908   Downloading httpx-0.28.1-py3-none-any.whl.metadata (7.1 kB)
2025-Dec-25 10:46:10.734587
#14 2.954 Collecting python-keycloak (from -r requirements.txt (line 6))
2025-Dec-25 10:46:10.734587
#14 2.959   Downloading python_keycloak-5.8.1-py3-none-any.whl.metadata (6.0 kB)
2025-Dec-25 10:46:10.734587
#14 3.045 Collecting minio (from -r requirements.txt (line 7))
2025-Dec-25 10:46:10.734587
#14 3.051   Downloading minio-7.2.20-py3-none-any.whl.metadata (6.5 kB)
2025-Dec-25 10:46:10.734587
#14 3.084 Collecting requests (from -r requirements.txt (line 8))
2025-Dec-25 10:46:10.734587
#14 3.091   Downloading requests-2.32.5-py3-none-any.whl.metadata (4.9 kB)
2025-Dec-25 10:46:10.734587
#14 3.117 Collecting python-dotenv (from -r requirements.txt (line 9))
2025-Dec-25 10:46:10.734587
#14 3.128   Downloading python_dotenv-1.2.1-py3-none-any.whl.metadata (25 kB)
2025-Dec-25 10:46:10.734587
#14 3.175 Collecting uvicorn[standard] (from -r requirements.txt (line 2))
2025-Dec-25 10:46:10.734587
#14 3.177   Downloading uvicorn-0.40.0-py3-none-any.whl.metadata (6.7 kB)
2025-Dec-25 10:46:10.734587
#14 3.196 Collecting passlib[bcrypt] (from -r requirements.txt (line 10))
2025-Dec-25 10:46:10.734587
#14 3.202   Downloading passlib-1.7.4-py2.py3-none-any.whl.metadata (1.7 kB)
2025-Dec-25 10:46:10.734587
#14 3.221 Collecting python-jose[cryptography] (from -r requirements.txt (line 11))
2025-Dec-25 10:46:10.734587
#14 3.230   Downloading python_jose-3.5.0-py2.py3-none-any.whl.metadata (5.5 kB)
2025-Dec-25 10:46:10.734587
#14 3.272 Collecting starlette<0.51.0,>=0.40.0 (from fastapi->-r requirements.txt (line 1))
2025-Dec-25 10:46:10.734587
#14 3.276   Downloading starlette-0.50.0-py3-none-any.whl.metadata (6.3 kB)
2025-Dec-25 10:46:10.734587
#14 3.398 Collecting pydantic>=2.7.0 (from fastapi->-r requirements.txt (line 1))
2025-Dec-25 10:46:10.734587
#14 3.405   Downloading pydantic-2.12.5-py3-none-any.whl.metadata (90 kB)
2025-Dec-25 10:46:10.734587
#14 3.440 Collecting typing-extensions>=4.8.0 (from fastapi->-r requirements.txt (line 1))
2025-Dec-25 10:46:10.734587
#14 3.446   Downloading typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
2025-Dec-25 10:46:10.734587
#14 3.462 Collecting annotated-doc>=0.0.2 (from fastapi->-r requirements.txt (line 1))
2025-Dec-25 10:46:10.734587
#14 3.467   Downloading annotated_doc-0.0.4-py3-none-any.whl.metadata (6.6 kB)
2025-Dec-25 10:46:10.734587
#14 3.501 Collecting click>=7.0 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 10:46:10.734587
#14 3.506   Downloading click-8.3.1-py3-none-any.whl.metadata (2.6 kB)
2025-Dec-25 10:46:10.734587
#14 3.528 Collecting h11>=0.8 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 10:46:10.734587
#14 3.530   Downloading h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
2025-Dec-25 10:46:10.734587
#14 3.577 Collecting httptools>=0.6.3 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 10:46:10.734587
#14 3.583   Downloading httptools-0.7.1-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (3.5 kB)
2025-Dec-25 10:46:10.734587
#14 3.622 Collecting pyyaml>=5.1 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 10:46:10.734587
#14 3.628   Downloading pyyaml-6.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.4 kB)
2025-Dec-25 10:46:10.734587
#14 3.679 Collecting uvloop>=0.15.1 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 10:46:10.734587
#14 3.684   Downloading uvloop-0.22.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (4.9 kB)
2025-Dec-25 10:46:10.734587
#14 3.789 Collecting watchfiles>=0.13 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 10:46:10.734587
#14 3.801   Downloading watchfiles-1.1.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.9 kB)
2025-Dec-25 10:46:10.734587
#14 3.914 Collecting websockets>=10.4 (from uvicorn[standard]->-r requirements.txt (line 2))
2025-Dec-25 10:46:10.734587
#14 3.928   Downloading websockets-15.0.1-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.8 kB)
2025-Dec-25 10:46:10.734587
#14 4.128 Collecting greenlet>=1 (from sqlalchemy->-r requirements.txt (line 3))
2025-Dec-25 10:46:10.734587
#14 4.136   Downloading greenlet-3.3.0-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (4.1 kB)
2025-Dec-25 10:46:10.734587
#14 4.192 Collecting anyio (from httpx->-r requirements.txt (line 5))
2025-Dec-25 10:46:10.734587
#14 4.197   Downloading anyio-4.12.0-py3-none-any.whl.metadata (4.3 kB)
2025-Dec-25 10:46:10.734587
#14 4.235 Collecting certifi (from httpx->-r requirements.txt (line 5))
2025-Dec-25 10:46:10.734587
#14 4.245   Downloading certifi-2025.11.12-py3-none-any.whl.metadata (2.5 kB)
2025-Dec-25 10:46:10.734587
#14 4.276 Collecting httpcore==1.* (from httpx->-r requirements.txt (line 5))
2025-Dec-25 10:46:10.734587
#14 4.283   Downloading httpcore-1.0.9-py3-none-any.whl.metadata (21 kB)
2025-Dec-25 10:46:10.734587
#14 4.310 Collecting idna (from httpx->-r requirements.txt (line 5))
2025-Dec-25 10:46:10.734587
#14 4.314   Downloading idna-3.11-py3-none-any.whl.metadata (8.4 kB)
2025-Dec-25 10:46:10.734587
#14 4.340 Collecting aiofiles>=24.1.0 (from python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 10:46:10.734587
#14 4.348   Downloading aiofiles-25.1.0-py3-none-any.whl.metadata (6.3 kB)
2025-Dec-25 10:46:10.734587
#14 4.369 Collecting async-property>=0.2.2 (from python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 10:46:10.734587
#14 4.382   Downloading async_property-0.2.2-py2.py3-none-any.whl.metadata (5.3 kB)
2025-Dec-25 10:46:10.734587
#14 4.403 Collecting deprecation>=2.1.0 (from python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 10:46:10.734587
#14 4.408   Downloading deprecation-2.1.0-py2.py3-none-any.whl.metadata (4.6 kB)
2025-Dec-25 10:46:10.734587
#14 4.433 Collecting jwcrypto>=1.5.4 (from python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 10:46:10.734587
#14 4.454   Downloading jwcrypto-1.5.6-py3-none-any.whl.metadata (3.1 kB)
2025-Dec-25 10:46:10.734587
#14 4.485 Collecting requests-toolbelt>=0.6.0 (from python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 10:46:10.734587
#14 4.489   Downloading requests_toolbelt-1.0.0-py2.py3-none-any.whl.metadata (14 kB)
2025-Dec-25 10:46:10.734587
#14 4.528 Collecting argon2-cffi (from minio->-r requirements.txt (line 7))
2025-Dec-25 10:46:10.734587
#14 4.533   Downloading argon2_cffi-25.1.0-py3-none-any.whl.metadata (4.1 kB)
2025-Dec-25 10:46:10.734587
#14 4.613 Collecting pycryptodome (from minio->-r requirements.txt (line 7))
2025-Dec-25 10:46:10.734587
#14 4.616   Downloading pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (3.4 kB)
2025-Dec-25 10:46:10.734587
#14 4.657 Collecting urllib3 (from minio->-r requirements.txt (line 7))
2025-Dec-25 10:46:10.734587
#14 4.669   Downloading urllib3-2.6.2-py3-none-any.whl.metadata (6.6 kB)
2025-Dec-25 10:46:10.734587
#14 4.812 Collecting charset_normalizer<4,>=2 (from requests->-r requirements.txt (line 8))
2025-Dec-25 10:46:10.734587
#14 4.818   Downloading charset_normalizer-3.4.4-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (37 kB)
2025-Dec-25 10:46:10.734587
#14 4.903 Collecting bcrypt>=3.1.0 (from passlib[bcrypt]->-r requirements.txt (line 10))
2025-Dec-25 10:46:10.734587
#14 4.919   Downloading bcrypt-5.0.0-cp39-abi3-manylinux_2_34_x86_64.whl.metadata (10 kB)
2025-Dec-25 10:46:10.734587
#14 4.956 Collecting ecdsa!=0.15 (from python-jose[cryptography]->-r requirements.txt (line 11))
2025-Dec-25 10:46:10.734587
#14 4.976   Downloading ecdsa-0.19.1-py2.py3-none-any.whl.metadata (29 kB)
2025-Dec-25 10:46:10.734587
#14 5.047 Collecting rsa!=4.1.1,!=4.4,<5.0,>=4.0 (from python-jose[cryptography]->-r requirements.txt (line 11))
2025-Dec-25 10:46:10.734587
#14 5.059   Downloading rsa-4.9.1-py3-none-any.whl.metadata (5.6 kB)
2025-Dec-25 10:46:10.734587
#14 5.124 Collecting pyasn1>=0.5.0 (from python-jose[cryptography]->-r requirements.txt (line 11))
2025-Dec-25 10:46:10.734587
#14 5.131   Downloading pyasn1-0.6.1-py3-none-any.whl.metadata (8.4 kB)
2025-Dec-25 10:46:10.734587
#14 5.352 Collecting cryptography>=3.4.0 (from python-jose[cryptography]->-r requirements.txt (line 11))
2025-Dec-25 10:46:10.734587
#14 5.362   Downloading cryptography-46.0.3-cp311-abi3-manylinux_2_34_x86_64.whl.metadata (5.7 kB)
2025-Dec-25 10:46:10.734587
#14 5.591 Collecting cffi>=2.0.0 (from cryptography>=3.4.0->python-jose[cryptography]->-r requirements.txt (line 11))
2025-Dec-25 10:46:10.734587
#14 5.603   Downloading cffi-2.0.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (2.6 kB)
2025-Dec-25 10:46:10.734587
#14 5.674 Collecting packaging (from deprecation>=2.1.0->python-keycloak->-r requirements.txt (line 6))
2025-Dec-25 10:46:10.734587
#14 5.691   Downloading packaging-25.0-py3-none-any.whl.metadata (3.3 kB)
2025-Dec-25 10:46:10.734587
#14 5.754 Collecting six>=1.9.0 (from ecdsa!=0.15->python-jose[cryptography]->-r requirements.txt (line 11))
2025-Dec-25 10:46:10.734587
#14 5.766   Downloading six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
2025-Dec-25 10:46:10.734587
#14 5.849 Collecting annotated-types>=0.6.0 (from pydantic>=2.7.0->fastapi->-r requirements.txt (line 1))
2025-Dec-25 10:46:10.734587
#14 5.865   Downloading annotated_types-0.7.0-py3-none-any.whl.metadata (15 kB)
2025-Dec-25 10:46:10.955515
#14 6.684 Collecting pydantic-core==2.41.5 (from pydantic>=2.7.0->fastapi->-r requirements.txt (line 1))
2025-Dec-25 10:46:11.097244
#14 6.690   Downloading pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (7.3 kB)
2025-Dec-25 10:46:11.097244
#14 6.728 Collecting typing-inspection>=0.4.2 (from pydantic>=2.7.0->fastapi->-r requirements.txt (line 1))
2025-Dec-25 10:46:11.114986
#14 6.735   Downloading typing_inspection-0.4.2-py3-none-any.whl.metadata (2.6 kB)
2025-Dec-25 10:46:11.114986
#14 6.830 Collecting argon2-cffi-bindings (from argon2-cffi->minio->-r requirements.txt (line 7))
2025-Dec-25 10:46:11.202225
#14 6.837   Downloading argon2_cffi_bindings-25.1.0-cp39-abi3-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl.metadata (7.4 kB)
2025-Dec-25 10:46:11.202225
#14 6.883 Collecting pycparser (from cffi>=2.0.0->cryptography>=3.4.0->python-jose[cryptography]->-r requirements.txt (line 11))
2025-Dec-25 10:46:11.202225
#14 6.890   Downloading pycparser-2.23-py3-none-any.whl.metadata (993 bytes)
2025-Dec-25 10:46:11.202225
#14 6.935 Downloading fastapi-0.127.0-py3-none-any.whl (112 kB)
2025-Dec-25 10:46:11.343318
#14 6.950 Downloading sqlalchemy-2.0.45-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (3.3 MB)
2025-Dec-25 10:46:11.343318
#14 7.000    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.3/3.3 MB 74.6 MB/s eta 0:00:00
2025-Dec-25 10:46:11.343318
#14 7.013 Downloading psycopg2_binary-2.9.11-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (4.2 MB)
2025-Dec-25 10:46:11.343318
#14 7.077    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.2/4.2 MB 66.2 MB/s eta 0:00:00
2025-Dec-25 10:46:11.445987
#14 7.084 Downloading httpx-0.28.1-py3-none-any.whl (73 kB)
2025-Dec-25 10:46:11.445987
#14 7.097 Downloading httpcore-1.0.9-py3-none-any.whl (78 kB)
2025-Dec-25 10:46:11.445987
#14 7.113 Downloading python_keycloak-5.8.1-py3-none-any.whl (77 kB)
2025-Dec-25 10:46:11.445987
#14 7.128 Downloading minio-7.2.20-py3-none-any.whl (93 kB)
2025-Dec-25 10:46:11.445987
#14 7.137 Downloading requests-2.32.5-py3-none-any.whl (64 kB)
2025-Dec-25 10:46:11.445987
#14 7.147 Downloading python_dotenv-1.2.1-py3-none-any.whl (21 kB)
2025-Dec-25 10:46:11.445987
#14 7.158 Downloading aiofiles-25.1.0-py3-none-any.whl (14 kB)
2025-Dec-25 10:46:11.445987
#14 7.166 Downloading annotated_doc-0.0.4-py3-none-any.whl (5.3 kB)
2025-Dec-25 10:46:11.445987
#14 7.177 Downloading async_property-0.2.2-py2.py3-none-any.whl (9.5 kB)
2025-Dec-25 10:46:11.574009
#14 7.192 Downloading bcrypt-5.0.0-cp39-abi3-manylinux_2_34_x86_64.whl (278 kB)
2025-Dec-25 10:46:11.574009
#14 7.208 Downloading certifi-2025.11.12-py3-none-any.whl (159 kB)
2025-Dec-25 10:46:11.574009
#14 7.216 Downloading charset_normalizer-3.4.4-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (153 kB)
2025-Dec-25 10:46:11.574009
#14 7.229 Downloading click-8.3.1-py3-none-any.whl (108 kB)
2025-Dec-25 10:46:11.574009
#14 7.238 Downloading cryptography-46.0.3-cp311-abi3-manylinux_2_34_x86_64.whl (4.5 MB)
2025-Dec-25 10:46:11.574009
#14 7.307    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.5/4.5 MB 68.4 MB/s eta 0:00:00
2025-Dec-25 10:46:11.675128
#14 7.316 Downloading deprecation-2.1.0-py2.py3-none-any.whl (11 kB)
2025-Dec-25 10:46:11.675128
#14 7.324 Downloading ecdsa-0.19.1-py2.py3-none-any.whl (150 kB)
2025-Dec-25 10:46:11.675128
#14 7.338 Downloading greenlet-3.3.0-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (609 kB)
2025-Dec-25 10:46:11.675128
#14 7.352    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 609.9/609.9 kB 53.8 MB/s eta 0:00:00
2025-Dec-25 10:46:11.675128
#14 7.358 Downloading h11-0.16.0-py3-none-any.whl (37 kB)
2025-Dec-25 10:46:11.675128
#14 7.369 Downloading httptools-0.7.1-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (517 kB)
2025-Dec-25 10:46:11.675128
#14 7.386 Downloading idna-3.11-py3-none-any.whl (71 kB)
2025-Dec-25 10:46:11.675128
#14 7.394 Downloading jwcrypto-1.5.6-py3-none-any.whl (92 kB)
2025-Dec-25 10:46:11.675128
#14 7.406 Downloading pyasn1-0.6.1-py3-none-any.whl (83 kB)
2025-Dec-25 10:46:11.783263
#14 7.419 Downloading pydantic-2.12.5-py3-none-any.whl (463 kB)
2025-Dec-25 10:46:11.783263
#14 7.439 Downloading pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.1 MB)
2025-Dec-25 10:46:11.783263
#14 7.487    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 56.8 MB/s eta 0:00:00
2025-Dec-25 10:46:11.783263
#14 7.493 Downloading pyyaml-6.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (807 kB)
2025-Dec-25 10:46:11.783263
#14 7.516    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 807.9/807.9 kB 34.4 MB/s eta 0:00:00
2025-Dec-25 10:46:11.961604
#14 7.526 Downloading requests_toolbelt-1.0.0-py2.py3-none-any.whl (54 kB)
2025-Dec-25 10:46:11.961604
#14 7.536 Downloading rsa-4.9.1-py3-none-any.whl (34 kB)
2025-Dec-25 10:46:11.961604
#14 7.549 Downloading starlette-0.50.0-py3-none-any.whl (74 kB)
2025-Dec-25 10:46:11.961604
#14 7.561 Downloading anyio-4.12.0-py3-none-any.whl (113 kB)
2025-Dec-25 10:46:11.961604
#14 7.573 Downloading typing_extensions-4.15.0-py3-none-any.whl (44 kB)
2025-Dec-25 10:46:11.961604
#14 7.583 Downloading urllib3-2.6.2-py3-none-any.whl (131 kB)
2025-Dec-25 10:46:11.961604
#14 7.615 Downloading uvloop-0.22.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (4.4 MB)
2025-Dec-25 10:46:11.961604
#14 7.694    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.4/4.4 MB 60.8 MB/s eta 0:00:00
2025-Dec-25 10:46:12.073178
#14 7.704 Downloading watchfiles-1.1.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (456 kB)
2025-Dec-25 10:46:12.073178
#14 7.727 Downloading websockets-15.0.1-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (182 kB)
2025-Dec-25 10:46:12.073178
#14 7.745 Downloading argon2_cffi-25.1.0-py3-none-any.whl (14 kB)
2025-Dec-25 10:46:12.073178
#14 7.765 Downloading passlib-1.7.4-py2.py3-none-any.whl (525 kB)
2025-Dec-25 10:46:12.073178
#14 7.790    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 525.6/525.6 kB 18.3 MB/s eta 0:00:00
2025-Dec-25 10:46:12.073178
#14 7.803 Downloading pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.3 MB)
2025-Dec-25 10:46:12.183097
#14 7.866    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.3/2.3 MB 38.2 MB/s eta 0:00:00
2025-Dec-25 10:46:12.183097
#14 7.871 Downloading python_jose-3.5.0-py2.py3-none-any.whl (34 kB)
2025-Dec-25 10:46:12.183097
#14 7.889 Downloading uvicorn-0.40.0-py3-none-any.whl (68 kB)
2025-Dec-25 10:46:12.183097
#14 7.901 Downloading annotated_types-0.7.0-py3-none-any.whl (13 kB)
2025-Dec-25 10:46:12.183097
#14 7.914 Downloading cffi-2.0.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (219 kB)
2025-Dec-25 10:46:12.414772
#14 7.933 Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
2025-Dec-25 10:46:12.414772
#14 7.946 Downloading typing_inspection-0.4.2-py3-none-any.whl (14 kB)
2025-Dec-25 10:46:12.414772
#14 7.957 Downloading argon2_cffi_bindings-25.1.0-cp39-abi3-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl (87 kB)
2025-Dec-25 10:46:12.414772
#14 7.972 Downloading packaging-25.0-py3-none-any.whl (66 kB)
2025-Dec-25 10:46:12.414772
#14 7.997 Downloading pycparser-2.23-py3-none-any.whl (118 kB)
2025-Dec-25 10:46:12.520685
#14 8.252 Installing collected packages: passlib, async-property, websockets, uvloop, urllib3, typing-extensions, six, pyyaml, python-dotenv, pycryptodome, pycparser, pyasn1, psycopg2-binary, packaging, idna, httptools, h11, greenlet, click, charset_normalizer, certifi, bcrypt, annotated-types, annotated-doc, aiofiles, uvicorn, typing-inspection, sqlalchemy, rsa, requests, pydantic-core, httpcore, ecdsa, deprecation, cffi, anyio, watchfiles, starlette, requests-toolbelt, python-jose, pydantic, httpx, cryptography, argon2-cffi-bindings, jwcrypto, fastapi, argon2-cffi, python-keycloak, minio
2025-Dec-25 10:46:18.609441
#14 14.34 Successfully installed aiofiles-25.1.0 annotated-doc-0.0.4 annotated-types-0.7.0 anyio-4.12.0 argon2-cffi-25.1.0 argon2-cffi-bindings-25.1.0 async-property-0.2.2 bcrypt-5.0.0 certifi-2025.11.12 cffi-2.0.0 charset_normalizer-3.4.4 click-8.3.1 cryptography-46.0.3 deprecation-2.1.0 ecdsa-0.19.1 fastapi-0.127.0 greenlet-3.3.0 h11-0.16.0 httpcore-1.0.9 httptools-0.7.1 httpx-0.28.1 idna-3.11 jwcrypto-1.5.6 minio-7.2.20 packaging-25.0 passlib-1.7.4 psycopg2-binary-2.9.11 pyasn1-0.6.1 pycparser-2.23 pycryptodome-3.23.0 pydantic-2.12.5 pydantic-core-2.41.5 python-dotenv-1.2.1 python-jose-3.5.0 python-keycloak-5.8.1 pyyaml-6.0.3 requests-2.32.5 requests-toolbelt-1.0.0 rsa-4.9.1 six-1.17.0 sqlalchemy-2.0.45 starlette-0.50.0 typing-extensions-4.15.0 typing-inspection-0.4.2 urllib3-2.6.2 uvicorn-0.40.0 uvloop-0.22.1 watchfiles-1.1.1 websockets-15.0.1
2025-Dec-25 10:46:18.840507
#14 14.34 WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager, possibly rendering your system unusable. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv. Use the --root-user-action option if you know what you are doing and want to suppress this warning.
2025-Dec-25 10:46:18.840507
#14 14.42
2025-Dec-25 10:46:18.840507
#14 14.42 [notice] A new release of pip is available: 25.0.1 -> 25.3
2025-Dec-25 10:46:18.840507
#14 14.42 [notice] To update, run: pip install --upgrade pip
2025-Dec-25 10:46:19.387650
#14 DONE 15.1s
2025-Dec-25 10:46:19.387650
2025-Dec-25 10:46:19.387650
#17 [dashboard deps 4/4] RUN npm install
2025-Dec-25 10:46:19.541658
#17 ...
2025-Dec-25 10:46:19.541658
2025-Dec-25 10:46:19.541658
#18 [api 5/5] COPY . .
2025-Dec-25 10:46:25.581187
#18 DONE 6.2s
2025-Dec-25 10:46:25.581187
2025-Dec-25 10:46:25.581187
#17 [dashboard deps 4/4] RUN npm install
2025-Dec-25 10:46:25.732929
#17 ...
2025-Dec-25 10:46:25.732929
2025-Dec-25 10:46:25.732929
#19 [api] exporting to image
2025-Dec-25 10:46:25.732929
#19 exporting layers
2025-Dec-25 10:46:30.445590
#19 exporting layers 4.9s done
2025-Dec-25 10:46:30.638910
#19 writing image sha256:0d331e1a20d41efd22eac9cd607c09b32812bea5ef47dd091e84eadc87cb00a9 done
2025-Dec-25 10:46:30.638910
#19 naming to docker.io/library/hck4w0k4ww8kk4gccw000ggg-api done
2025-Dec-25 10:46:30.638910
#19 DONE 4.9s
2025-Dec-25 10:46:30.638910
2025-Dec-25 10:46:30.638910
#20 [api] resolving provenance for metadata file
2025-Dec-25 10:46:30.638910
#20 DONE 0.0s
2025-Dec-25 10:46:30.638910
2025-Dec-25 10:46:30.638910
#17 [dashboard deps 4/4] RUN npm install
2025-Dec-25 10:46:31.623208
#17 26.00
2025-Dec-25 10:46:31.623208
#17 26.00 added 473 packages, and audited 474 packages in 26s
2025-Dec-25 10:46:31.623208
#17 26.00
2025-Dec-25 10:46:31.623208
#17 26.00 154 packages are looking for funding
2025-Dec-25 10:46:31.623208
#17 26.00   run `npm fund` for details
2025-Dec-25 10:46:31.781530
#17 26.00
2025-Dec-25 10:46:31.781530
#17 26.00 found 0 vulnerabilities
2025-Dec-25 10:46:31.781530
#17 26.01 npm notice
2025-Dec-25 10:46:31.781530
#17 26.01 npm notice New major version of npm available! 10.8.2 -> 11.7.0
2025-Dec-25 10:46:31.781530
#17 26.01 npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.7.0
2025-Dec-25 10:46:31.781530
#17 26.01 npm notice To update run: npm install -g npm@11.7.0
2025-Dec-25 10:46:31.781530
#17 26.01 npm notice
2025-Dec-25 10:46:32.013100
#17 DONE 26.4s
2025-Dec-25 10:46:38.582382
2025-Dec-25 10:46:38.588320
#21 [dashboard builder 3/5] COPY --from=deps /app/node_modules ./node_modules
2025-Dec-25 10:46:48.487386
#21 DONE 9.9s
2025-Dec-25 10:46:48.689365
#22 [dashboard builder 4/5] COPY . .
2025-Dec-25 10:46:48.689365
#22 DONE 0.0s
2025-Dec-25 10:46:48.689365
2025-Dec-25 10:46:48.689365
#23 [dashboard builder 5/5] RUN npm run build
2025-Dec-25 10:46:49.161977
#23 0.622
2025-Dec-25 10:46:49.161977
#23 0.622 > dashboard@0.1.0 build
2025-Dec-25 10:46:49.161977
#23 0.622 > next build
2025-Dec-25 10:46:49.161977
#23 0.622
2025-Dec-25 10:46:49.974063
#23 1.432 Attention: Next.js now collects completely anonymous telemetry regarding usage.
2025-Dec-25 10:46:50.100773
#23 1.434 This information is used to shape Next.js' roadmap and prioritize features.
2025-Dec-25 10:46:50.105846
#23 1.434 You can learn more, including how to opt-out if you'd not like to participate in this anonymous program, by visiting the following URL:
2025-Dec-25 10:46:50.105846
#23 1.434 https://nextjs.org/telemetry
2025-Dec-25 10:46:50.105846
#23 1.434
2025-Dec-25 10:46:50.105846
#23 1.448 ▲ Next.js 16.1.0 (Turbopack)
2025-Dec-25 10:46:50.105846
#23 1.448
2025-Dec-25 10:46:50.105846
#23 1.562   Creating an optimized production build ...
2025-Dec-25 10:47:10.017276
#23 21.48 ✓ Compiled successfully in 19.5s
2025-Dec-25 10:47:10.218777
#23 21.53   Running TypeScript ...
2025-Dec-25 10:47:19.430559
#23 30.89   Collecting page data using 1 worker ...
2025-Dec-25 10:47:20.033467
#23 31.49   Generating static pages using 1 worker (0/11) ...
2025-Dec-25 10:47:20.329571
#23 31.79   Generating static pages using 1 worker (2/11)
2025-Dec-25 10:47:20.336481
2025-Dec-25 10:47:20.548449
#23 31.79   Generating static pages using 1 worker (5/11)
2025-Dec-25 10:47:20.548449
#23 31.79   Generating static pages using 1 worker (8/11)
2025-Dec-25 10:47:20.548449
#23 31.85 ✓ Generating static pages using 1 worker (11/11) in 351.1ms
2025-Dec-25 10:47:20.548449
#23 31.85   Finalizing page optimization ...
2025-Dec-25 10:47:20.548449
#23 31.86
2025-Dec-25 10:47:20.548449
#23 31.86 Route (app)
2025-Dec-25 10:47:20.548449
#23 31.86 ┌ ○ /
2025-Dec-25 10:47:20.548449
#23 31.86 ├ ○ /_not-found
2025-Dec-25 10:47:20.548449
#23 31.86 ├ ○ /login
2025-Dec-25 10:47:20.548449
#23 31.86 ├ ○ /org
2025-Dec-25 10:47:20.548449
#23 31.86 ├ ƒ /org/[orgId]/billing
2025-Dec-25 10:47:20.548449
#23 31.86 ├ ƒ /org/[orgId]/projects
2025-Dec-25 10:47:20.548449
#23 31.86 ├ ƒ /org/[orgId]/projects/new
2025-Dec-25 10:47:20.548449
#23 31.86 ├ ƒ /org/[orgId]/settings
2025-Dec-25 10:47:20.548449
#23 31.86 ├ ƒ /org/[orgId]/team
2025-Dec-25 10:47:20.548449
#23 31.86 ├ ○ /projects
2025-Dec-25 10:47:20.548449
#23 31.86 ├ ƒ /projects/[id]
2025-Dec-25 10:47:20.548449
#23 31.86 ├ ƒ /projects/[id]/auth
2025-Dec-25 10:47:20.548449
#23 31.86 ├ ƒ /projects/[id]/backups
2025-Dec-25 10:47:20.548449
#23 31.86 ├ ƒ /projects/[id]/database
2025-Dec-25 10:47:20.548449
#23 31.86 ├ ƒ /projects/[id]/database/[table]
2025-Dec-25 10:47:20.548449
#23 31.86 ├ ƒ /projects/[id]/edge-functions
2025-Dec-25 10:47:20.548449
#23 31.86 ├ ƒ /projects/[id]/logs
2025-Dec-25 10:47:20.548449
#23 31.86 ├ ƒ /projects/[id]/realtime
2025-Dec-25 10:47:20.548449
#23 31.86 ├ ƒ /projects/[id]/secrets
2025-Dec-25 10:47:20.553641
#23 31.86 ├ ƒ /projects/[id]/settings
2025-Dec-25 10:47:20.553641
#23 31.86 ├ ƒ /projects/[id]/settings/deployment
2025-Dec-25 10:47:20.553641
#23 31.86 ├ ƒ /projects/[id]/sql
2025-Dec-25 10:47:20.553641
#23 31.86 ├ ƒ /projects/[id]/storage
2025-Dec-25 10:47:20.553641
#23 31.86 ├ ○ /projects/new
2025-Dec-25 10:47:20.553641
#23 31.86 ├ ○ /settings/organization
2025-Dec-25 10:47:20.553641
#23 31.86 ├ ƒ /settings/organization/[id]
2025-Dec-25 10:47:20.553641
#23 31.86 ├ ○ /settings/profile
2025-Dec-25 10:47:20.553641
#23 31.86 └ ○ /signup
2025-Dec-25 10:47:20.553641
#23 31.86
2025-Dec-25 10:47:20.553641
#23 31.86
2025-Dec-25 10:47:20.553641
#23 31.86 ○  (Static)   prerendered as static content
2025-Dec-25 10:47:20.553641
#23 31.86 ƒ  (Dynamic)  server-rendered on demand
2025-Dec-25 10:47:20.553641
#23 31.86
2025-Dec-25 10:47:20.600305
#23 32.06 npm notice
2025-Dec-25 10:47:20.600305
#23 32.06 npm notice New major version of npm available! 10.8.2 -> 11.7.0
2025-Dec-25 10:47:20.600305
#23 32.06 npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.7.0
2025-Dec-25 10:47:20.600305
#23 32.06 npm notice To update run: npm install -g npm@11.7.0
2025-Dec-25 10:47:20.600305
#23 32.06 npm notice
2025-Dec-25 10:47:20.814724
#23 DONE 32.1s
2025-Dec-25 10:47:30.304600
#24 [dashboard runner 3/6] COPY --from=builder /app/public ./public
2025-Dec-25 10:47:30.477780
#24 DONE 0.0s
2025-Dec-25 10:47:30.477780
2025-Dec-25 10:47:30.477780
#25 [dashboard runner 4/6] COPY --from=builder /app/.next ./.next
2025-Dec-25 10:47:30.515903
#25 DONE 0.2s
2025-Dec-25 10:47:30.669519
#26 [dashboard runner 5/6] COPY --from=builder /app/node_modules ./node_modules
2025-Dec-25 10:47:43.240781
#26 DONE 12.7s
2025-Dec-25 10:47:43.429696
#27 [dashboard runner 6/6] COPY --from=builder /app/package.json ./package.json
2025-Dec-25 10:47:43.429696
#27 DONE 0.0s
2025-Dec-25 10:47:43.429696
2025-Dec-25 10:47:43.429696
#28 [dashboard] exporting to image
2025-Dec-25 10:47:43.429696
#28 exporting layers
2025-Dec-25 10:47:55.245125
#28 exporting layers 12.0s done
2025-Dec-25 10:47:55.298830
#28 writing image sha256:f4417c5bd7dcded4fdb953ebc0cb2ab88641d9bc4d1d30c709d637b4c0a7e560 done
2025-Dec-25 10:47:55.298830
#28 naming to docker.io/library/hck4w0k4ww8kk4gccw000ggg-dashboard done
2025-Dec-25 10:47:55.298830
#28 DONE 12.0s
2025-Dec-25 10:47:55.298830
2025-Dec-25 10:47:55.298830
#29 [dashboard] resolving provenance for metadata file
2025-Dec-25 10:47:55.298830
#29 DONE 0.0s
2025-Dec-25 10:47:55.313855
dashboard  Built
2025-Dec-25 10:47:55.313855
api  Built
2025-Dec-25 10:47:55.360027
Creating .env file with runtime variables for build phase.
2025-Dec-25 10:47:56.138195
[CMD]: docker exec rogwc4s4s0cwwkoscgg00go8 bash -c 'cat /artifacts/rogwc4s4s0cwwkoscgg00go8/.env'
2025-Dec-25 10:47:56.138195
SOURCE_COMMIT=d74b420205cdec807791ed43c25e610c4e16482e
2025-Dec-25 10:47:56.138195
COOLIFY_URL=
2025-Dec-25 10:47:56.138195
COOLIFY_FQDN=
2025-Dec-25 10:47:56.138195
SERVICE_URL_DASHBOARD=https://supalove.hayataxi.online
2025-Dec-25 10:47:56.138195
SERVICE_FQDN_DASHBOARD=supalove.hayataxi.online
2025-Dec-25 10:47:56.138195
SERVICE_URL_API=https://api.supalove.hayataxi.online
2025-Dec-25 10:47:56.138195
SERVICE_FQDN_API=api.supalove.hayataxi.online
2025-Dec-25 10:47:56.138195
SERVICE_URL_KEYCLOAK=https://auth.supalove.hayataxi.online
2025-Dec-25 10:47:56.138195
SERVICE_FQDN_KEYCLOAK=auth.supalove.hayataxi.online
2025-Dec-25 10:47:56.138195
SERVICE_URL_MINIO=https://s3.supalove.hayataxi.online
2025-Dec-25 10:47:56.138195
SERVICE_FQDN_MINIO=s3.supalove.hayataxi.online
2025-Dec-25 10:47:56.138195
SERVICE_NAME_CONTROL-PLANE-DB=control-plane-db
2025-Dec-25 10:47:56.138195
SERVICE_NAME_API=api
2025-Dec-25 10:47:56.138195
SERVICE_NAME_DASHBOARD=dashboard
2025-Dec-25 10:47:56.138195
SERVICE_NAME_KEYCLOAK=keycloak
2025-Dec-25 10:47:56.138195
SERVICE_NAME_MINIO=minio
2025-Dec-25 10:47:56.138195
POSTGRES_USER=platform
2025-Dec-25 10:47:56.138195
POSTGRES_PASSWORD=platform
2025-Dec-25 10:47:56.138195
POSTGRES_DB=control_plane
2025-Dec-25 10:47:56.138195
KEYCLOAK_ADMIN_USER=admin
2025-Dec-25 10:47:56.138195
KEYCLOAK_ADMIN_PASSWORD=admin
2025-Dec-25 10:47:56.138195
MINIO_ROOT_USER=minioadmin
2025-Dec-25 10:47:56.138195
MINIO_ROOT_PASSWORD=minioadmin
2025-Dec-25 10:47:56.138195
URL=http://localhost:8000
2025-Dec-25 10:47:56.138195
NEXT_PUBLIC_API_URL=https://api.supalove.hayataxi.online
2025-Dec-25 10:47:56.138195
HOST=0.0.0.0
2025-Dec-25 10:47:56.462638
Removing old containers.
2025-Dec-25 10:47:56.814849
Starting new application.
2025-Dec-25 10:47:58.181040
[CMD]: docker exec rogwc4s4s0cwwkoscgg00go8 bash -c 'SOURCE_COMMIT=d74b420205cdec807791ed43c25e610c4e16482e COOLIFY_BRANCH=main COOLIFY_RESOURCE_UUID=hck4w0k4ww8kk4gccw000ggg COOLIFY_CONTAINER_NAME=hck4w0k4ww8kk4gccw000ggg-104529203943  docker compose --env-file /artifacts/rogwc4s4s0cwwkoscgg00go8/.env --project-name hck4w0k4ww8kk4gccw000ggg --project-directory /artifacts/rogwc4s4s0cwwkoscgg00go8 -f /artifacts/rogwc4s4s0cwwkoscgg00go8/docker-compose.coolify.yml up -d'
2025-Dec-25 10:47:58.181040
minio Pulling
2025-Dec-25 10:47:58.181040
control-plane-db Pulling
2025-Dec-25 10:47:58.188680
keycloak Pulling
2025-Dec-25 10:47:59.752681
b83ce1c86227 Pulling fs layer
2025-Dec-25 10:47:59.752681
f94d28849fa3 Pulling fs layer
2025-Dec-25 10:47:59.752681
81260b173076 Pulling fs layer
2025-Dec-25 10:47:59.752681
f9c0805c25ee Pulling fs layer
2025-Dec-25 10:47:59.752681
1008deaf6ec4 Pulling fs layer
2025-Dec-25 10:47:59.752681
71e9fc939447 Pulling fs layer
2025-Dec-25 10:47:59.752681
c1bc68842c41 Pulling fs layer
2025-Dec-25 10:47:59.752681
0288b5a0d7e7 Pulling fs layer
2025-Dec-25 10:47:59.752681
34013573f278 Pulling fs layer
2025-Dec-25 10:47:59.752681
1008deaf6ec4 Waiting
2025-Dec-25 10:47:59.759247
71e9fc939447 Waiting
2025-Dec-25 10:47:59.759247
c1bc68842c41 Waiting
2025-Dec-25 10:47:59.759247
0288b5a0d7e7 Waiting
2025-Dec-25 10:47:59.759247
34013573f278 Waiting
2025-Dec-25 10:47:59.759247
f9c0805c25ee Waiting
2025-Dec-25 10:47:59.766009
1733a4cd5954 Already exists
2025-Dec-25 10:47:59.772841
66fe66faf896 Pulling fs layer
2025-Dec-25 10:47:59.772841
c94f51fe9236 Pulling fs layer
2025-Dec-25 10:47:59.772841
9602d06b4e70 Pulling fs layer
2025-Dec-25 10:47:59.772841
fab6e4443d8a Pulling fs layer
2025-Dec-25 10:47:59.772841
f2a9e5883151 Pulling fs layer
2025-Dec-25 10:47:59.772841
8d363c2df07a Pulling fs layer
2025-Dec-25 10:47:59.772841
5cdd56139991 Pulling fs layer
2025-Dec-25 10:47:59.772841
aa55ead71133 Pulling fs layer
2025-Dec-25 10:47:59.772841
758ebfa119db Pulling fs layer
2025-Dec-25 10:47:59.772841
798e92f9757e Pulling fs layer
2025-Dec-25 10:47:59.772841
ada9fa789fdc Pulling fs layer
2025-Dec-25 10:47:59.772841
3e738c3a66c8 Pulling fs layer
2025-Dec-25 10:47:59.772841
687b178dca38 Pulling fs layer
2025-Dec-25 10:47:59.772841
66fe66faf896 Waiting
2025-Dec-25 10:47:59.772841
c94f51fe9236 Waiting
2025-Dec-25 10:47:59.772841
9602d06b4e70 Waiting
2025-Dec-25 10:47:59.772841
fab6e4443d8a Waiting
2025-Dec-25 10:47:59.772841
f2a9e5883151 Waiting
2025-Dec-25 10:47:59.772841
8d363c2df07a Waiting
2025-Dec-25 10:47:59.772841
5cdd56139991 Waiting
2025-Dec-25 10:47:59.772841
aa55ead71133 Waiting
2025-Dec-25 10:47:59.772841
758ebfa119db Waiting
2025-Dec-25 10:47:59.772841
798e92f9757e Waiting
2025-Dec-25 10:47:59.772841
ada9fa789fdc Waiting
2025-Dec-25 10:47:59.772841
3e738c3a66c8 Waiting
2025-Dec-25 10:47:59.772841
687b178dca38 Waiting
2025-Dec-25 10:47:59.983584
ea29d36b883e Pulling fs layer
2025-Dec-25 10:47:59.983584
a9bb58c3bdd8 Pulling fs layer
2025-Dec-25 10:47:59.983584
393f8747e4b4 Pulling fs layer
2025-Dec-25 10:47:59.983584
20b69ee379c9 Pulling fs layer
2025-Dec-25 10:47:59.983584
ea29d36b883e Waiting
2025-Dec-25 10:47:59.983584
a9bb58c3bdd8 Waiting
2025-Dec-25 10:47:59.983584
393f8747e4b4 Waiting
2025-Dec-25 10:47:59.983584
20b69ee379c9 Waiting
2025-Dec-25 10:48:00.073351
f94d28849fa3 Downloading [>                                                  ]  17.36kB/1.637MB
2025-Dec-25 10:48:00.092384
81260b173076 Downloading [>                                                  ]  2.301kB/122.7kB
2025-Dec-25 10:48:00.092384
81260b173076 Verifying Checksum
2025-Dec-25 10:48:00.092384
81260b173076 Download complete
2025-Dec-25 10:48:00.108570
b83ce1c86227 Downloading [>                                                  ]  75.84kB/7.241MB
2025-Dec-25 10:48:00.123436
f94d28849fa3 Verifying Checksum
2025-Dec-25 10:48:00.123436
f94d28849fa3 Download complete
2025-Dec-25 10:48:00.165549
b83ce1c86227 Verifying Checksum
2025-Dec-25 10:48:00.174031
b83ce1c86227 Download complete
2025-Dec-25 10:48:00.174031
b83ce1c86227 Extracting [>                                                  ]   98.3kB/7.241MB
2025-Dec-25 10:48:00.280974
b83ce1c86227 Extracting [==============>                                    ]  2.064MB/7.241MB
2025-Dec-25 10:48:00.379862
b83ce1c86227 Extracting [===================================>               ]  5.112MB/7.241MB
2025-Dec-25 10:48:00.453283
1008deaf6ec4 Downloading [>                                                  ]    114kB/11.19MB
2025-Dec-25 10:48:00.480968
71e9fc939447 Downloading [>                                                  ]  24.61kB/2.402MB
2025-Dec-25 10:48:00.523616
f9c0805c25ee Downloading [>                                                  ]    409kB/39.45MB
2025-Dec-25 10:48:00.538545
b83ce1c86227 Extracting [============================================>      ]  6.488MB/7.241MB
2025-Dec-25 10:48:00.555307
1008deaf6ec4 Downloading [===============================>                   ]  7.066MB/11.19MB
2025-Dec-25 10:48:00.568561
71e9fc939447 Downloading [==================================================>]  2.402MB/2.402MB
2025-Dec-25 10:48:00.568561
71e9fc939447 Verifying Checksum
2025-Dec-25 10:48:00.568561
71e9fc939447 Download complete
2025-Dec-25 10:48:00.611154
1008deaf6ec4 Verifying Checksum
2025-Dec-25 10:48:00.611154
1008deaf6ec4 Download complete
2025-Dec-25 10:48:00.632429
f9c0805c25ee Downloading [=====>                                             ]  4.044MB/39.45MB
2025-Dec-25 10:48:00.675332
b83ce1c86227 Extracting [==============================================>    ]  6.685MB/7.241MB
2025-Dec-25 10:48:00.714515
b83ce1c86227 Extracting [==================================================>]  7.241MB/7.241MB
2025-Dec-25 10:48:00.727063
f9c0805c25ee Downloading [====================>                              ]  15.79MB/39.45MB
2025-Dec-25 10:48:00.757980
b83ce1c86227 Pull complete
2025-Dec-25 10:48:00.769985
f94d28849fa3 Extracting [=>                                                 ]  32.77kB/1.637MB
2025-Dec-25 10:48:00.824591
f9c0805c25ee Downloading [===================================>               ]  27.98MB/39.45MB
2025-Dec-25 10:48:00.868122
f94d28849fa3 Extracting [================================================>  ]  1.573MB/1.637MB
2025-Dec-25 10:48:00.883963
f94d28849fa3 Extracting [==================================================>]  1.637MB/1.637MB
2025-Dec-25 10:48:00.893122
f94d28849fa3 Extracting [==================================================>]  1.637MB/1.637MB
2025-Dec-25 10:48:00.912540
c1bc68842c41 Downloading [>                                                  ]  2.301kB/180.3kB
2025-Dec-25 10:48:00.927121
c1bc68842c41 Downloading [==================================================>]  180.3kB/180.3kB
2025-Dec-25 10:48:00.927121
c1bc68842c41 Verifying Checksum
2025-Dec-25 10:48:00.927121
c1bc68842c41 Download complete
2025-Dec-25 10:48:00.941312
f9c0805c25ee Downloading [=================================================> ]  38.97MB/39.45MB
2025-Dec-25 10:48:00.941312
f9c0805c25ee Verifying Checksum
2025-Dec-25 10:48:00.941312
f9c0805c25ee Download complete
2025-Dec-25 10:48:00.952785
f94d28849fa3 Pull complete
2025-Dec-25 10:48:00.961353
81260b173076 Extracting [=============>                                     ]  32.77kB/122.7kB
2025-Dec-25 10:48:00.961353
81260b173076 Extracting [==================================================>]  122.7kB/122.7kB
2025-Dec-25 10:48:00.961353
81260b173076 Extracting [==================================================>]  122.7kB/122.7kB
2025-Dec-25 10:48:00.981919
0288b5a0d7e7 Downloading [===>                                               ]     933B/11.88kB
2025-Dec-25 10:48:00.981919
0288b5a0d7e7 Downloading [==================================================>]  11.88kB/11.88kB
2025-Dec-25 10:48:00.981919
0288b5a0d7e7 Verifying Checksum
2025-Dec-25 10:48:00.981919
0288b5a0d7e7 Download complete
2025-Dec-25 10:48:01.002863
81260b173076 Pull complete
2025-Dec-25 10:48:01.030873
f9c0805c25ee Extracting [>                                                  ]    426kB/39.45MB
2025-Dec-25 10:48:01.137456
f9c0805c25ee Extracting [===>                                               ]  2.982MB/39.45MB
2025-Dec-25 10:48:01.244334
f9c0805c25ee Extracting [=======>                                           ]  5.964MB/39.45MB
2025-Dec-25 10:48:01.273503
34013573f278 Downloading [==================================================>]     496B/496B
2025-Dec-25 10:48:01.273503
34013573f278 Verifying Checksum
2025-Dec-25 10:48:01.273503
34013573f278 Download complete
2025-Dec-25 10:48:01.352135
f9c0805c25ee Extracting [===========>                                       ]  8.946MB/39.45MB
2025-Dec-25 10:48:01.399319
66fe66faf896 Downloading [========================================>          ]     953B/1.165kB
2025-Dec-25 10:48:01.418992
66fe66faf896 Downloading [==================================================>]  1.165kB/1.165kB
2025-Dec-25 10:48:01.418992
66fe66faf896 Verifying Checksum
2025-Dec-25 10:48:01.418992
66fe66faf896 Download complete
2025-Dec-25 10:48:01.418992
66fe66faf896 Extracting [==================================================>]  1.165kB/1.165kB
2025-Dec-25 10:48:01.418992
66fe66faf896 Extracting [==================================================>]  1.165kB/1.165kB
2025-Dec-25 10:48:01.439720
c94f51fe9236 Downloading [>                                                  ]  67.45kB/6.437MB
2025-Dec-25 10:48:01.478050
f9c0805c25ee Extracting [==============>                                    ]  11.08MB/39.45MB
2025-Dec-25 10:48:01.516997
66fe66faf896 Pull complete
2025-Dec-25 10:48:01.545204
c94f51fe9236 Downloading [===========================================>       ]   5.55MB/6.437MB
2025-Dec-25 10:48:01.565019
c94f51fe9236 Verifying Checksum
2025-Dec-25 10:48:01.565019
c94f51fe9236 Download complete
2025-Dec-25 10:48:01.565019
c94f51fe9236 Extracting [>                                                  ]  65.54kB/6.437MB
2025-Dec-25 10:48:01.611679
f9c0805c25ee Extracting [===============>                                   ]  12.35MB/39.45MB
2025-Dec-25 10:48:01.650786
c94f51fe9236 Extracting [=========>                                         ]   1.18MB/6.437MB
2025-Dec-25 10:48:01.711548
f9c0805c25ee Extracting [=================>                                 ]  14.06MB/39.45MB
2025-Dec-25 10:48:01.751609
c94f51fe9236 Extracting [===================>                               ]   2.49MB/6.437MB
2025-Dec-25 10:48:01.782347
9602d06b4e70 Downloading [>                                                  ]  13.69kB/1.257MB
2025-Dec-25 10:48:01.821765
f9c0805c25ee Extracting [===================>                               ]  15.34MB/39.45MB
2025-Dec-25 10:48:01.821765
9602d06b4e70 Verifying Checksum
2025-Dec-25 10:48:01.821765
9602d06b4e70 Download complete
2025-Dec-25 10:48:01.855377
c94f51fe9236 Extracting [============================>                      ]   3.67MB/6.437MB
2025-Dec-25 10:48:01.917804
fab6e4443d8a Downloading [>                                                  ]  84.36kB/8.204MB
2025-Dec-25 10:48:01.956752
f9c0805c25ee Extracting [====================>                              ]  16.19MB/39.45MB
2025-Dec-25 10:48:01.977713
c94f51fe9236 Extracting [===================================>               ]  4.522MB/6.437MB
2025-Dec-25 10:48:01.999912
fab6e4443d8a Verifying Checksum
2025-Dec-25 10:48:01.999912
fab6e4443d8a Download complete
2025-Dec-25 10:48:02.027194
f2a9e5883151 Downloading [>                                                  ]  13.69kB/1.312MB
2025-Dec-25 10:48:02.091468
f2a9e5883151 Verifying Checksum
2025-Dec-25 10:48:02.091468
f2a9e5883151 Download complete
2025-Dec-25 10:48:02.123360
c94f51fe9236 Extracting [=======================================>           ]  5.046MB/6.437MB
2025-Dec-25 10:48:02.183374
f9c0805c25ee Extracting [=====================>                             ]  17.04MB/39.45MB
2025-Dec-25 10:48:02.215151
c94f51fe9236 Extracting [==========================================>        ]  5.505MB/6.437MB
2025-Dec-25 10:48:02.314523
c94f51fe9236 Extracting [=================================================> ]  6.357MB/6.437MB
2025-Dec-25 10:48:02.314523
f9c0805c25ee Extracting [======================>                            ]  17.89MB/39.45MB
2025-Dec-25 10:48:02.347659
c94f51fe9236 Extracting [==================================================>]  6.437MB/6.437MB
2025-Dec-25 10:48:02.369876
8d363c2df07a Downloading [==================================================>]     116B/116B
2025-Dec-25 10:48:02.369876
8d363c2df07a Verifying Checksum
2025-Dec-25 10:48:02.369876
8d363c2df07a Download complete
2025-Dec-25 10:48:02.424320
f9c0805c25ee Extracting [==========================>                        ]   21.3MB/39.45MB
2025-Dec-25 10:48:02.469983
c94f51fe9236 Pull complete
2025-Dec-25 10:48:02.488037
9602d06b4e70 Extracting [=>                                                 ]  32.77kB/1.257MB
2025-Dec-25 10:48:02.533045
5cdd56139991 Downloading [===============>                                   ]     953B/3.144kB
2025-Dec-25 10:48:02.550144
5cdd56139991 Downloading [==================================================>]  3.144kB/3.144kB
2025-Dec-25 10:48:02.550144
5cdd56139991 Verifying Checksum
2025-Dec-25 10:48:02.550144
5cdd56139991 Download complete
2025-Dec-25 10:48:02.563356
f9c0805c25ee Extracting [=============================>                     ]     23MB/39.45MB
2025-Dec-25 10:48:02.578818
9602d06b4e70 Extracting [==================================================>]  1.257MB/1.257MB
2025-Dec-25 10:48:02.590714
aa55ead71133 Downloading [>                                                  ]  540.7kB/111MB
2025-Dec-25 10:48:02.619620
9602d06b4e70 Pull complete
2025-Dec-25 10:48:02.653426
fab6e4443d8a Extracting [>                                                  ]   98.3kB/8.204MB
2025-Dec-25 10:48:02.676008
f9c0805c25ee Extracting [==============================>                    ]  24.28MB/39.45MB
2025-Dec-25 10:48:02.707579
aa55ead71133 Downloading [===>                                               ]  6.955MB/111MB
2025-Dec-25 10:48:02.741602
fab6e4443d8a Extracting [====>                                              ]  688.1kB/8.204MB
2025-Dec-25 10:48:02.793451
f9c0805c25ee Extracting [==================================>                ]  26.84MB/39.45MB
2025-Dec-25 10:48:02.816632
aa55ead71133 Downloading [=======>                                           ]  17.15MB/111MB
2025-Dec-25 10:48:02.869817
fab6e4443d8a Extracting [========>                                          ]  1.475MB/8.204MB
2025-Dec-25 10:48:02.884569
758ebfa119db Downloading [====>                                              ]     953B/9.879kB
2025-Dec-25 10:48:02.884569
758ebfa119db Downloading [==================================================>]  9.879kB/9.879kB
2025-Dec-25 10:48:02.884569
758ebfa119db Verifying Checksum
2025-Dec-25 10:48:02.884569
758ebfa119db Download complete
2025-Dec-25 10:48:02.907155
f9c0805c25ee Extracting [====================================>              ]  28.54MB/39.45MB
2025-Dec-25 10:48:02.925537
aa55ead71133 Downloading [===========>                                       ]  25.73MB/111MB
2025-Dec-25 10:48:02.955314
fab6e4443d8a Extracting [===================>                               ]  3.146MB/8.204MB
2025-Dec-25 10:48:03.030191
aa55ead71133 Downloading [===============>                                   ]  34.28MB/111MB
2025-Dec-25 10:48:03.030191
f9c0805c25ee Extracting [======================================>            ]  30.24MB/39.45MB
2025-Dec-25 10:48:03.057464
fab6e4443d8a Extracting [=========================>                         ]  4.227MB/8.204MB
2025-Dec-25 10:48:03.099795
798e92f9757e Downloading [==================================================>]     128B/128B
2025-Dec-25 10:48:03.099795
798e92f9757e Verifying Checksum
2025-Dec-25 10:48:03.099795
798e92f9757e Download complete
2025-Dec-25 10:48:03.128713
f9c0805c25ee Extracting [=========================================>         ]   32.8MB/39.45MB
2025-Dec-25 10:48:03.143253
aa55ead71133 Downloading [====================>                              ]  44.45MB/111MB
2025-Dec-25 10:48:03.155436
fab6e4443d8a Extracting [=============================>                     ]  4.915MB/8.204MB
2025-Dec-25 10:48:03.236621
aa55ead71133 Downloading [========================>                          ]  53.59MB/111MB
2025-Dec-25 10:48:03.256845
f9c0805c25ee Extracting [==============================================>    ]  36.63MB/39.45MB
2025-Dec-25 10:48:03.256845
fab6e4443d8a Extracting [===================================>               ]  5.898MB/8.204MB
2025-Dec-25 10:48:03.338751
aa55ead71133 Downloading [============================>                      ]  62.71MB/111MB
2025-Dec-25 10:48:03.356885
f9c0805c25ee Extracting [================================================>  ]  38.34MB/39.45MB
2025-Dec-25 10:48:03.372211
ada9fa789fdc Downloading [==================================================>]     168B/168B
2025-Dec-25 10:48:03.372211
ada9fa789fdc Verifying Checksum
2025-Dec-25 10:48:03.372211
ada9fa789fdc Download complete
2025-Dec-25 10:48:03.383053
fab6e4443d8a Extracting [=========================================>         ]  6.783MB/8.204MB
2025-Dec-25 10:48:03.437908
f9c0805c25ee Extracting [==================================================>]  39.45MB/39.45MB
2025-Dec-25 10:48:03.465653
aa55ead71133 Downloading [===============================>                   ]  70.71MB/111MB
2025-Dec-25 10:48:03.482531
fab6e4443d8a Extracting [==============================================>    ]  7.668MB/8.204MB
2025-Dec-25 10:48:03.482531
f9c0805c25ee Pull complete
2025-Dec-25 10:48:03.495648
1008deaf6ec4 Extracting [>                                                  ]  131.1kB/11.19MB
2025-Dec-25 10:48:03.546802
aa55ead71133 Downloading [====================================>              ]  80.38MB/111MB
2025-Dec-25 10:48:03.563197
fab6e4443d8a Extracting [==================================================>]  8.204MB/8.204MB
2025-Dec-25 10:48:03.573630
3e738c3a66c8 Downloading [========>                                          ]     953B/5.837kB
2025-Dec-25 10:48:03.573630
3e738c3a66c8 Downloading [==================================================>]  5.837kB/5.837kB
2025-Dec-25 10:48:03.573630
3e738c3a66c8 Verifying Checksum
2025-Dec-25 10:48:03.573630
3e738c3a66c8 Download complete
2025-Dec-25 10:48:03.592536
1008deaf6ec4 Extracting [========>                                          ]  1.966MB/11.19MB
2025-Dec-25 10:48:03.603985
fab6e4443d8a Pull complete
2025-Dec-25 10:48:03.617631
f2a9e5883151 Extracting [=>                                                 ]  32.77kB/1.312MB
2025-Dec-25 10:48:03.650349
aa55ead71133 Downloading [=======================================>           ]   88.4MB/111MB
2025-Dec-25 10:48:03.697875
1008deaf6ec4 Extracting [===================>                               ]  4.456MB/11.19MB
2025-Dec-25 10:48:03.719157
f2a9e5883151 Extracting [==================================================>]  1.312MB/1.312MB
2025-Dec-25 10:48:03.749961
f2a9e5883151 Pull complete
2025-Dec-25 10:48:03.762183
aa55ead71133 Downloading [============================================>      ]  98.03MB/111MB
2025-Dec-25 10:48:03.776129
8d363c2df07a Extracting [==================================================>]     116B/116B
2025-Dec-25 10:48:03.776129
8d363c2df07a Extracting [==================================================>]     116B/116B
2025-Dec-25 10:48:03.793901
8d363c2df07a Pull complete
2025-Dec-25 10:48:03.793901
5cdd56139991 Extracting [==================================================>]  3.144kB/3.144kB
2025-Dec-25 10:48:03.815999
1008deaf6ec4 Extracting [=============================>                     ]  6.554MB/11.19MB
2025-Dec-25 10:48:03.815999
5cdd56139991 Extracting [==================================================>]  3.144kB/3.144kB
2025-Dec-25 10:48:03.841844
5cdd56139991 Pull complete
2025-Dec-25 10:48:03.868788
aa55ead71133 Downloading [===============================================>   ]  106.1MB/111MB
2025-Dec-25 10:48:03.868788
687b178dca38 Downloading [==================================================>]     185B/185B
2025-Dec-25 10:48:03.868788
687b178dca38 Verifying Checksum
2025-Dec-25 10:48:03.868788
687b178dca38 Download complete
2025-Dec-25 10:48:03.909602
1008deaf6ec4 Extracting [==================================>                ]  7.733MB/11.19MB
2025-Dec-25 10:48:03.930429
aa55ead71133 Verifying Checksum
2025-Dec-25 10:48:03.930429
aa55ead71133 Download complete
2025-Dec-25 10:48:03.984459
ea29d36b883e Downloading [>                                                  ]  74.57kB/7.221MB
2025-Dec-25 10:48:04.052290
1008deaf6ec4 Extracting [========================================>          ]  9.044MB/11.19MB
2025-Dec-25 10:48:04.089679
aa55ead71133 Extracting [>                                                  ]  557.1kB/111MB
2025-Dec-25 10:48:04.120104
ea29d36b883e Downloading [==================================>                ]  5.022MB/7.221MB
2025-Dec-25 10:48:04.134506
ea29d36b883e Verifying Checksum
2025-Dec-25 10:48:04.134506
ea29d36b883e Download complete
2025-Dec-25 10:48:04.134506
ea29d36b883e Extracting [>                                                  ]   98.3kB/7.221MB
2025-Dec-25 10:48:04.151565
1008deaf6ec4 Extracting [===========================================>       ]   9.83MB/11.19MB
2025-Dec-25 10:48:04.215576
aa55ead71133 Extracting [>                                                  ]  1.671MB/111MB
2025-Dec-25 10:48:04.234803
ea29d36b883e Extracting [======>                                            ]    983kB/7.221MB
2025-Dec-25 10:48:04.253461
1008deaf6ec4 Extracting [================================================>  ]  10.88MB/11.19MB
2025-Dec-25 10:48:04.272895
1008deaf6ec4 Extracting [==================================================>]  11.19MB/11.19MB
2025-Dec-25 10:48:04.286818
a9bb58c3bdd8 Downloading [>                                                  ]  528.4kB/77.15MB
2025-Dec-25 10:48:04.325070
1008deaf6ec4 Pull complete
2025-Dec-25 10:48:04.325070
71e9fc939447 Extracting [>                                                  ]  32.77kB/2.402MB
2025-Dec-25 10:48:04.350839
393f8747e4b4 Downloading [>                                                  ]  532.5kB/177.9MB
2025-Dec-25 10:48:04.372223
aa55ead71133 Extracting [=>                                                 ]  3.342MB/111MB
2025-Dec-25 10:48:04.397413
a9bb58c3bdd8 Downloading [=====>                                             ]  8.469MB/77.15MB
2025-Dec-25 10:48:04.421498
71e9fc939447 Extracting [==========================>                        ]  1.278MB/2.402MB
2025-Dec-25 10:48:04.421498
ea29d36b883e Extracting [==============>                                    ]  2.064MB/7.221MB
2025-Dec-25 10:48:04.457615
393f8747e4b4 Downloading [=>                                                 ]   6.93MB/177.9MB
2025-Dec-25 10:48:04.489646
aa55ead71133 Extracting [==>                                                ]  4.456MB/111MB
2025-Dec-25 10:48:04.502849
a9bb58c3bdd8 Downloading [==========>                                        ]  15.89MB/77.15MB
2025-Dec-25 10:48:04.527950
71e9fc939447 Extracting [===============================================>   ]  2.294MB/2.402MB
2025-Dec-25 10:48:04.542060
ea29d36b883e Extracting [===============>                                   ]  2.261MB/7.221MB
2025-Dec-25 10:48:04.542060
71e9fc939447 Extracting [==================================================>]  2.402MB/2.402MB
2025-Dec-25 10:48:04.555801
393f8747e4b4 Downloading [===>                                               ]  13.31MB/177.9MB
2025-Dec-25 10:48:04.580448
71e9fc939447 Pull complete
2025-Dec-25 10:48:04.597055
20b69ee379c9 Downloading [==================================================>]     551B/551B
2025-Dec-25 10:48:04.597055
20b69ee379c9 Verifying Checksum
2025-Dec-25 10:48:04.597055
20b69ee379c9 Download complete
2025-Dec-25 10:48:04.597055
c1bc68842c41 Extracting [=========>                                         ]  32.77kB/180.3kB
2025-Dec-25 10:48:04.597055
a9bb58c3bdd8 Downloading [==============>                                    ]  22.23MB/77.15MB
2025-Dec-25 10:48:04.613279
c1bc68842c41 Extracting [==================================================>]  180.3kB/180.3kB
2025-Dec-25 10:48:04.631448
aa55ead71133 Extracting [==>                                                ]  6.128MB/111MB
2025-Dec-25 10:48:04.631448
ea29d36b883e Extracting [=======================>                           ]  3.342MB/7.221MB
2025-Dec-25 10:48:04.653971
c1bc68842c41 Extracting [==================================================>]  180.3kB/180.3kB
2025-Dec-25 10:48:04.666206
393f8747e4b4 Downloading [=====>                                             ]  18.64MB/177.9MB
2025-Dec-25 10:48:04.686935
c1bc68842c41 Pull complete
2025-Dec-25 10:48:04.698436
0288b5a0d7e7 Extracting [==================================================>]  11.88kB/11.88kB
2025-Dec-25 10:48:04.698436
0288b5a0d7e7 Extracting [==================================================>]  11.88kB/11.88kB
2025-Dec-25 10:48:04.708698
a9bb58c3bdd8 Downloading [===================>                               ]  29.61MB/77.15MB
2025-Dec-25 10:48:04.726482
0288b5a0d7e7 Pull complete
2025-Dec-25 10:48:04.738737
aa55ead71133 Extracting [===>                                               ]  7.242MB/111MB
2025-Dec-25 10:48:04.749538
34013573f278 Extracting [==================================================>]     496B/496B
2025-Dec-25 10:48:04.749538
34013573f278 Extracting [==================================================>]     496B/496B
2025-Dec-25 10:48:04.749538
ea29d36b883e Extracting [==============================>                    ]  4.424MB/7.221MB
2025-Dec-25 10:48:04.764696
393f8747e4b4 Downloading [======>                                            ]  23.45MB/177.9MB
2025-Dec-25 10:48:04.774108
34013573f278 Pull complete
2025-Dec-25 10:48:04.805695
a9bb58c3bdd8 Downloading [========================>                          ]  37.56MB/77.15MB
2025-Dec-25 10:48:04.852550
minio Pulled
2025-Dec-25 10:48:04.852550
aa55ead71133 Extracting [===>                                               ]  7.799MB/111MB
2025-Dec-25 10:48:04.870806
ea29d36b883e Extracting [====================================>              ]   5.21MB/7.221MB
2025-Dec-25 10:48:04.870806
393f8747e4b4 Downloading [========>                                          ]  29.35MB/177.9MB
2025-Dec-25 10:48:04.920367
a9bb58c3bdd8 Downloading [===========================>                       ]  42.32MB/77.15MB
2025-Dec-25 10:48:04.972448
393f8747e4b4 Downloading [=========>                                         ]  35.24MB/177.9MB
2025-Dec-25 10:48:04.986730
aa55ead71133 Extracting [====>                                              ]  8.913MB/111MB
2025-Dec-25 10:48:05.021053
a9bb58c3bdd8 Downloading [================================>                  ]  50.78MB/77.15MB
2025-Dec-25 10:48:05.038636
ea29d36b883e Extracting [============================================>      ]   6.39MB/7.221MB
2025-Dec-25 10:48:05.080532
393f8747e4b4 Downloading [===========>                                       ]  41.62MB/177.9MB
2025-Dec-25 10:48:05.119490
aa55ead71133 Extracting [====>                                              ]  10.58MB/111MB
2025-Dec-25 10:48:05.145808
a9bb58c3bdd8 Downloading [=====================================>             ]  57.65MB/77.15MB
2025-Dec-25 10:48:05.176780
ea29d36b883e Extracting [===============================================>   ]  6.881MB/7.221MB
2025-Dec-25 10:48:05.207121
393f8747e4b4 Downloading [=============>                                     ]  47.51MB/177.9MB
2025-Dec-25 10:48:05.234592
ea29d36b883e Extracting [==================================================>]  7.221MB/7.221MB
2025-Dec-25 10:48:05.252855
aa55ead71133 Extracting [=====>                                             ]   11.7MB/111MB
2025-Dec-25 10:48:05.252855
a9bb58c3bdd8 Downloading [==========================================>        ]  65.08MB/77.15MB
2025-Dec-25 10:48:05.277481
ea29d36b883e Pull complete
2025-Dec-25 10:48:05.291823
393f8747e4b4 Downloading [===============>                                   ]   53.4MB/177.9MB
2025-Dec-25 10:48:05.341627
a9bb58c3bdd8 Downloading [===============================================>   ]  73.56MB/77.15MB
2025-Dec-25 10:48:05.373858
aa55ead71133 Extracting [======>                                            ]  13.93MB/111MB
2025-Dec-25 10:48:05.404713
393f8747e4b4 Downloading [================>                                  ]  58.75MB/177.9MB
2025-Dec-25 10:48:05.404713
a9bb58c3bdd8 Verifying Checksum
2025-Dec-25 10:48:05.404713
a9bb58c3bdd8 Download complete
2025-Dec-25 10:48:05.460066
a9bb58c3bdd8 Extracting [>                                                  ]  557.1kB/77.15MB
2025-Dec-25 10:48:05.500487
aa55ead71133 Extracting [=======>                                           ]   15.6MB/111MB
2025-Dec-25 10:48:05.500487
393f8747e4b4 Downloading [==================>                                ]  66.72MB/177.9MB
2025-Dec-25 10:48:05.604022
a9bb58c3bdd8 Extracting [=>                                                 ]  2.228MB/77.15MB
2025-Dec-25 10:48:05.604022
393f8747e4b4 Downloading [=====================>                             ]  75.72MB/177.9MB
2025-Dec-25 10:48:05.625185
aa55ead71133 Extracting [========>                                          ]  17.83MB/111MB
2025-Dec-25 10:48:05.705891
393f8747e4b4 Downloading [=======================>                           ]  84.19MB/177.9MB
2025-Dec-25 10:48:05.705891
a9bb58c3bdd8 Extracting [==>                                                ]  4.456MB/77.15MB
2025-Dec-25 10:48:05.752116
aa55ead71133 Extracting [=========>                                         ]  20.05MB/111MB
2025-Dec-25 10:48:05.817488
a9bb58c3bdd8 Extracting [====>                                              ]  6.685MB/77.15MB
2025-Dec-25 10:48:05.817488
393f8747e4b4 Downloading [==========================>                        ]  92.62MB/177.9MB
2025-Dec-25 10:48:05.881399
aa55ead71133 Extracting [==========>                                        ]  22.28MB/111MB
2025-Dec-25 10:48:05.919880
393f8747e4b4 Downloading [============================>                      ]  100.5MB/177.9MB
2025-Dec-25 10:48:05.952446
a9bb58c3bdd8 Extracting [=====>                                             ]  8.356MB/77.15MB
2025-Dec-25 10:48:06.021753
aa55ead71133 Extracting [==========>                                        ]   23.4MB/111MB
2025-Dec-25 10:48:06.021753
393f8747e4b4 Downloading [==============================>                    ]  109.5MB/177.9MB
2025-Dec-25 10:48:06.065486
a9bb58c3bdd8 Extracting [======>                                            ]  10.58MB/77.15MB
2025-Dec-25 10:48:06.122172
393f8747e4b4 Downloading [=================================>                 ]  119.1MB/177.9MB
2025-Dec-25 10:48:06.141970
aa55ead71133 Extracting [===========>                                       ]  25.62MB/111MB
2025-Dec-25 10:48:06.170728
a9bb58c3bdd8 Extracting [========>                                          ]  12.81MB/77.15MB
2025-Dec-25 10:48:06.221972
393f8747e4b4 Downloading [====================================>              ]  129.1MB/177.9MB
2025-Dec-25 10:48:06.234568
aa55ead71133 Extracting [============>                                      ]  28.41MB/111MB
2025-Dec-25 10:48:06.280983
a9bb58c3bdd8 Extracting [==========>                                        ]   15.6MB/77.15MB
2025-Dec-25 10:48:06.339854
393f8747e4b4 Downloading [======================================>            ]  138.6MB/177.9MB
2025-Dec-25 10:48:06.380450
aa55ead71133 Extracting [==============>                                    ]   31.2MB/111MB
2025-Dec-25 10:48:06.441297
393f8747e4b4 Downloading [========================================>          ]  145.5MB/177.9MB
2025-Dec-25 10:48:06.470899
a9bb58c3bdd8 Extracting [===========>                                       ]  17.27MB/77.15MB
2025-Dec-25 10:48:06.492584
aa55ead71133 Extracting [==============>                                    ]  31.75MB/111MB
2025-Dec-25 10:48:06.543932
393f8747e4b4 Downloading [============================================>      ]  157.1MB/177.9MB
2025-Dec-25 10:48:06.573883
a9bb58c3bdd8 Extracting [===========>                                       ]  18.38MB/77.15MB
2025-Dec-25 10:48:06.612346
aa55ead71133 Extracting [===============>                                   ]  33.42MB/111MB
2025-Dec-25 10:48:06.642455
393f8747e4b4 Downloading [===============================================>   ]  168.2MB/177.9MB
2025-Dec-25 10:48:06.680601
a9bb58c3bdd8 Extracting [============>                                      ]  20.05MB/77.15MB
2025-Dec-25 10:48:06.717802
aa55ead71133 Extracting [================>                                  ]  35.65MB/111MB
2025-Dec-25 10:48:06.745910
393f8747e4b4 Downloading [=================================================> ]  176.7MB/177.9MB
2025-Dec-25 10:48:06.757922
393f8747e4b4 Verifying Checksum
2025-Dec-25 10:48:06.757922
393f8747e4b4 Download complete
2025-Dec-25 10:48:06.782667
a9bb58c3bdd8 Extracting [==============>                                    ]  22.28MB/77.15MB
2025-Dec-25 10:48:06.829820
aa55ead71133 Extracting [=================>                                 ]  38.99MB/111MB
2025-Dec-25 10:48:06.892840
a9bb58c3bdd8 Extracting [================>                                  ]  26.18MB/77.15MB
2025-Dec-25 10:48:06.940021
aa55ead71133 Extracting [===================>                               ]  42.89MB/111MB
2025-Dec-25 10:48:07.005861
a9bb58c3bdd8 Extracting [==================>                                ]  28.97MB/77.15MB
2025-Dec-25 10:48:07.048495
aa55ead71133 Extracting [====================>                              ]  45.12MB/111MB
2025-Dec-25 10:48:07.126813
a9bb58c3bdd8 Extracting [====================>                              ]   31.2MB/77.15MB
2025-Dec-25 10:48:07.165769
aa55ead71133 Extracting [=====================>                             ]  47.91MB/111MB
2025-Dec-25 10:48:07.228183
a9bb58c3bdd8 Extracting [======================>                            ]  34.54MB/77.15MB
2025-Dec-25 10:48:07.268652
aa55ead71133 Extracting [=======================>                           ]  51.25MB/111MB
2025-Dec-25 10:48:07.329949
a9bb58c3bdd8 Extracting [=======================>                           ]  36.21MB/77.15MB
2025-Dec-25 10:48:07.385567
aa55ead71133 Extracting [=======================>                           ]  52.92MB/111MB
2025-Dec-25 10:48:07.437506
a9bb58c3bdd8 Extracting [=========================>                         ]  39.55MB/77.15MB
2025-Dec-25 10:48:07.501448
aa55ead71133 Extracting [========================>                          ]  54.59MB/111MB
2025-Dec-25 10:48:07.548216
a9bb58c3bdd8 Extracting [===========================>                       ]  42.34MB/77.15MB
2025-Dec-25 10:48:07.615698
aa55ead71133 Extracting [=========================>                         ]  56.82MB/111MB
2025-Dec-25 10:48:07.658805
a9bb58c3bdd8 Extracting [=============================>                     ]  45.68MB/77.15MB
2025-Dec-25 10:48:07.717426
aa55ead71133 Extracting [==========================>                        ]   59.6MB/111MB
2025-Dec-25 10:48:07.770623
a9bb58c3bdd8 Extracting [================================>                  ]  49.58MB/77.15MB
2025-Dec-25 10:48:07.819747
aa55ead71133 Extracting [============================>                      ]  62.39MB/111MB
2025-Dec-25 10:48:07.879490
a9bb58c3bdd8 Extracting [=================================>                 ]  51.25MB/77.15MB
2025-Dec-25 10:48:07.936346
aa55ead71133 Extracting [=============================>                     ]  66.29MB/111MB
2025-Dec-25 10:48:07.983948
a9bb58c3bdd8 Extracting [==================================>                ]  53.48MB/77.15MB
2025-Dec-25 10:48:08.044831
aa55ead71133 Extracting [===============================>                   ]  70.75MB/111MB
2025-Dec-25 10:48:08.090089
a9bb58c3bdd8 Extracting [====================================>              ]  56.26MB/77.15MB
2025-Dec-25 10:48:08.153003
aa55ead71133 Extracting [=================================>                 ]  74.09MB/111MB
2025-Dec-25 10:48:08.210944
a9bb58c3bdd8 Extracting [======================================>            ]   59.6MB/77.15MB
2025-Dec-25 10:48:08.254841
aa55ead71133 Extracting [==================================>                ]  76.32MB/111MB
2025-Dec-25 10:48:08.316922
a9bb58c3bdd8 Extracting [========================================>          ]  61.83MB/77.15MB
2025-Dec-25 10:48:08.358156
aa55ead71133 Extracting [===================================>               ]  78.54MB/111MB
2025-Dec-25 10:48:08.431520
a9bb58c3bdd8 Extracting [==========================================>        ]  65.18MB/77.15MB
2025-Dec-25 10:48:08.462362
aa55ead71133 Extracting [====================================>              ]  81.89MB/111MB
2025-Dec-25 10:48:08.552725
a9bb58c3bdd8 Extracting [===========================================>       ]   67.4MB/77.15MB
2025-Dec-25 10:48:08.567541
aa55ead71133 Extracting [======================================>            ]  84.67MB/111MB
2025-Dec-25 10:48:08.674041
aa55ead71133 Extracting [======================================>            ]  86.34MB/111MB
2025-Dec-25 10:48:08.687124
a9bb58c3bdd8 Extracting [============================================>      ]  68.52MB/77.15MB
2025-Dec-25 10:48:08.780474
aa55ead71133 Extracting [=========================================>         ]  91.36MB/111MB
2025-Dec-25 10:48:08.861991
a9bb58c3bdd8 Extracting [=============================================>     ]  70.75MB/77.15MB
2025-Dec-25 10:48:08.906242
aa55ead71133 Extracting [==========================================>        ]   94.7MB/111MB
2025-Dec-25 10:48:09.003745
a9bb58c3bdd8 Extracting [==============================================>    ]  72.42MB/77.15MB
2025-Dec-25 10:48:09.047505
aa55ead71133 Extracting [===========================================>       ]  95.81MB/111MB
2025-Dec-25 10:48:09.147070
aa55ead71133 Extracting [===========================================>       ]  96.93MB/111MB
2025-Dec-25 10:48:09.188147
a9bb58c3bdd8 Extracting [===============================================>   ]  73.53MB/77.15MB
2025-Dec-25 10:48:09.300673
aa55ead71133 Extracting [============================================>      ]   98.6MB/111MB
2025-Dec-25 10:48:09.357642
a9bb58c3bdd8 Extracting [================================================>  ]  74.09MB/77.15MB
2025-Dec-25 10:48:09.420097
aa55ead71133 Extracting [============================================>      ]  99.71MB/111MB
2025-Dec-25 10:48:09.557504
aa55ead71133 Extracting [=============================================>     ]  100.8MB/111MB
2025-Dec-25 10:48:09.656806
aa55ead71133 Extracting [=============================================>     ]  101.9MB/111MB
2025-Dec-25 10:48:09.754267
aa55ead71133 Extracting [==============================================>    ]  104.2MB/111MB
2025-Dec-25 10:48:09.894701
a9bb58c3bdd8 Extracting [================================================>  ]   75.2MB/77.15MB
2025-Dec-25 10:48:09.960298
aa55ead71133 Extracting [===============================================>   ]  105.8MB/111MB
2025-Dec-25 10:48:10.028780
a9bb58c3bdd8 Extracting [=================================================> ]  76.32MB/77.15MB
2025-Dec-25 10:48:10.104945
a9bb58c3bdd8 Extracting [==================================================>]  77.15MB/77.15MB
2025-Dec-25 10:48:10.116733
aa55ead71133 Extracting [================================================>  ]    107MB/111MB
2025-Dec-25 10:48:10.143741
a9bb58c3bdd8 Pull complete
2025-Dec-25 10:48:10.163581
393f8747e4b4 Extracting [>                                                  ]  557.1kB/177.9MB
2025-Dec-25 10:48:10.267020
393f8747e4b4 Extracting [==>                                                ]  10.58MB/177.9MB
2025-Dec-25 10:48:10.278250
aa55ead71133 Extracting [================================================>  ]  108.1MB/111MB
2025-Dec-25 10:48:10.370837
393f8747e4b4 Extracting [=====>                                             ]  18.38MB/177.9MB
2025-Dec-25 10:48:10.382517
aa55ead71133 Extracting [=================================================> ]  109.2MB/111MB
2025-Dec-25 10:48:10.472977
393f8747e4b4 Extracting [=======>                                           ]  28.41MB/177.9MB
2025-Dec-25 10:48:10.591395
393f8747e4b4 Extracting [=========>                                         ]  34.54MB/177.9MB
2025-Dec-25 10:48:10.685823
aa55ead71133 Extracting [=================================================> ]  109.7MB/111MB
2025-Dec-25 10:48:10.697549
393f8747e4b4 Extracting [===========>                                       ]  40.11MB/177.9MB
2025-Dec-25 10:48:10.801819
393f8747e4b4 Extracting [==============>                                    ]  50.14MB/177.9MB
2025-Dec-25 10:48:10.801819
aa55ead71133 Extracting [=================================================> ]  110.9MB/111MB
2025-Dec-25 10:48:10.885258
aa55ead71133 Extracting [==================================================>]    111MB/111MB
2025-Dec-25 10:48:10.902267
393f8747e4b4 Extracting [===============>                                   ]  55.15MB/177.9MB
2025-Dec-25 10:48:10.965630
aa55ead71133 Pull complete
2025-Dec-25 10:48:10.998914
758ebfa119db Extracting [==================================================>]  9.879kB/9.879kB
2025-Dec-25 10:48:10.998914
758ebfa119db Extracting [==================================================>]  9.879kB/9.879kB
2025-Dec-25 10:48:11.034296
758ebfa119db Pull complete
2025-Dec-25 10:48:11.034296
798e92f9757e Extracting [==================================================>]     128B/128B
2025-Dec-25 10:48:11.034296
798e92f9757e Extracting [==================================================>]     128B/128B
2025-Dec-25 10:48:11.034296
393f8747e4b4 Extracting [================>                                  ]  60.16MB/177.9MB
2025-Dec-25 10:48:11.057450
798e92f9757e Pull complete
2025-Dec-25 10:48:11.057450
ada9fa789fdc Extracting [==================================================>]     168B/168B
2025-Dec-25 10:48:11.057450
ada9fa789fdc Extracting [==================================================>]     168B/168B
2025-Dec-25 10:48:11.072681
ada9fa789fdc Pull complete
2025-Dec-25 10:48:11.072681
3e738c3a66c8 Extracting [==================================================>]  5.837kB/5.837kB
2025-Dec-25 10:48:11.072681
3e738c3a66c8 Extracting [==================================================>]  5.837kB/5.837kB
2025-Dec-25 10:48:11.094019
3e738c3a66c8 Pull complete
2025-Dec-25 10:48:11.111823
687b178dca38 Extracting [==================================================>]     185B/185B
2025-Dec-25 10:48:11.111823
687b178dca38 Extracting [==================================================>]     185B/185B
2025-Dec-25 10:48:11.123321
687b178dca38 Pull complete
2025-Dec-25 10:48:11.148979
control-plane-db Pulled
2025-Dec-25 10:48:11.148979
393f8747e4b4 Extracting [==================>                                ]  64.06MB/177.9MB
2025-Dec-25 10:48:11.240502
393f8747e4b4 Extracting [=====================>                             ]  76.32MB/177.9MB
2025-Dec-25 10:48:11.354551
393f8747e4b4 Extracting [========================>                          ]  88.57MB/177.9MB
2025-Dec-25 10:48:11.457735
393f8747e4b4 Extracting [==========================>                        ]  95.26MB/177.9MB
2025-Dec-25 10:48:11.557924
393f8747e4b4 Extracting [=============================>                     ]  105.3MB/177.9MB
2025-Dec-25 10:48:11.660947
393f8747e4b4 Extracting [================================>                  ]  115.3MB/177.9MB
2025-Dec-25 10:48:11.763216
393f8747e4b4 Extracting [===================================>               ]  127.6MB/177.9MB
2025-Dec-25 10:48:11.864748
393f8747e4b4 Extracting [========================================>          ]  143.7MB/177.9MB
2025-Dec-25 10:48:11.978720
393f8747e4b4 Extracting [=============================================>     ]  162.1MB/177.9MB
2025-Dec-25 10:48:12.082292
393f8747e4b4 Extracting [================================================>  ]  173.8MB/177.9MB
2025-Dec-25 10:48:12.148900
393f8747e4b4 Extracting [==================================================>]  177.9MB/177.9MB
2025-Dec-25 10:48:12.168043
393f8747e4b4 Pull complete
2025-Dec-25 10:48:12.181398
20b69ee379c9 Extracting [==================================================>]     551B/551B
2025-Dec-25 10:48:12.181398
20b69ee379c9 Extracting [==================================================>]     551B/551B
2025-Dec-25 10:48:12.191736
20b69ee379c9 Pull complete
2025-Dec-25 10:48:12.202693
keycloak Pulled
2025-Dec-25 10:48:12.213716
Volume "hck4w0k4ww8kk4gccw000ggg_minio-data"  Creating
2025-Dec-25 10:48:12.226831
Volume "hck4w0k4ww8kk4gccw000ggg_minio-data"  Created
2025-Dec-25 10:48:12.226831
Volume "hck4w0k4ww8kk4gccw000ggg_control-plane-data"  Creating
2025-Dec-25 10:48:12.226831
Volume "hck4w0k4ww8kk4gccw000ggg_control-plane-data"  Created
2025-Dec-25 10:48:12.226831
Container minio-hck4w0k4ww8kk4gccw000ggg-104552416742  Creating
2025-Dec-25 10:48:12.226831
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-104552360220  Creating
2025-Dec-25 10:48:12.444723
Container minio-hck4w0k4ww8kk4gccw000ggg-104552416742  Created
2025-Dec-25 10:48:12.464934
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-104552360220  Created
2025-Dec-25 10:48:12.464934
Container keycloak-hck4w0k4ww8kk4gccw000ggg-104552403645  Creating
2025-Dec-25 10:48:12.508424
Container keycloak-hck4w0k4ww8kk4gccw000ggg-104552403645  Created
2025-Dec-25 10:48:12.508424
Container api-hck4w0k4ww8kk4gccw000ggg-104552377562  Creating
2025-Dec-25 10:48:12.508424
Container api-hck4w0k4ww8kk4gccw000ggg-104552377562  Created
2025-Dec-25 10:48:12.508424
Container dashboard-hck4w0k4ww8kk4gccw000ggg-104552392826  Creating
2025-Dec-25 10:48:12.524617
Container dashboard-hck4w0k4ww8kk4gccw000ggg-104552392826  Created
2025-Dec-25 10:48:12.539586
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-104552360220  Starting
2025-Dec-25 10:48:12.539586
Container minio-hck4w0k4ww8kk4gccw000ggg-104552416742  Starting
2025-Dec-25 10:48:12.784756
Container minio-hck4w0k4ww8kk4gccw000ggg-104552416742  Started
2025-Dec-25 10:48:12.823977
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-104552360220  Started
2025-Dec-25 10:48:12.823977
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-104552360220  Waiting
2025-Dec-25 10:48:18.326648
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-104552360220  Healthy
2025-Dec-25 10:48:18.326648
Container keycloak-hck4w0k4ww8kk4gccw000ggg-104552403645  Starting
2025-Dec-25 10:48:18.563041
Container keycloak-hck4w0k4ww8kk4gccw000ggg-104552403645  Started
2025-Dec-25 10:48:18.582645
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-104552360220  Waiting
2025-Dec-25 10:48:19.065756
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-104552360220  Healthy
2025-Dec-25 10:48:19.117982
Container api-hck4w0k4ww8kk4gccw000ggg-104552377562  Starting
2025-Dec-25 10:48:19.388208
Container api-hck4w0k4ww8kk4gccw000ggg-104552377562  Started
2025-Dec-25 10:48:19.388208
Container dashboard-hck4w0k4ww8kk4gccw000ggg-104552392826  Starting
2025-Dec-25 10:48:19.445556
Error response from daemon: driver failed programming external connectivity on endpoint dashboard-hck4w0k4ww8kk4gccw000ggg-104552392826 (054e93aa21485b0724dad3a5cfe1597c0fe0da902583fcb145c3d187271dc85d): Bind for 0.0.0.0:3000 failed: port is already allocated
2025-Dec-25 10:48:19.476434
exit status 1
2025-Dec-25 10:48:19.555495
Oops something is not okay, are you okay? 😢
2025-Dec-25 10:48:19.580030
minio Pulling
2025-Dec-25 10:48:19.580030
control-plane-db Pulling
2025-Dec-25 10:48:19.580030
keycloak Pulling
2025-Dec-25 10:48:19.580030
b83ce1c86227 Pulling fs layer
2025-Dec-25 10:48:19.580030
f94d28849fa3 Pulling fs layer
2025-Dec-25 10:48:19.580030
81260b173076 Pulling fs layer
2025-Dec-25 10:48:19.580030
f9c0805c25ee Pulling fs layer
2025-Dec-25 10:48:19.580030
1008deaf6ec4 Pulling fs layer
2025-Dec-25 10:48:19.580030
71e9fc939447 Pulling fs layer
2025-Dec-25 10:48:19.580030
c1bc68842c41 Pulling fs layer
2025-Dec-25 10:48:19.580030
0288b5a0d7e7 Pulling fs layer
2025-Dec-25 10:48:19.580030
34013573f278 Pulling fs layer
2025-Dec-25 10:48:19.580030
1008deaf6ec4 Waiting
2025-Dec-25 10:48:19.580030
71e9fc939447 Waiting
2025-Dec-25 10:48:19.580030
c1bc68842c41 Waiting
2025-Dec-25 10:48:19.580030
0288b5a0d7e7 Waiting
2025-Dec-25 10:48:19.580030
34013573f278 Waiting
2025-Dec-25 10:48:19.580030
f9c0805c25ee Waiting
2025-Dec-25 10:48:19.580030
1733a4cd5954 Already exists
2025-Dec-25 10:48:19.580030
66fe66faf896 Pulling fs layer
2025-Dec-25 10:48:19.580030
c94f51fe9236 Pulling fs layer
2025-Dec-25 10:48:19.580030
9602d06b4e70 Pulling fs layer
2025-Dec-25 10:48:19.580030
fab6e4443d8a Pulling fs layer
2025-Dec-25 10:48:19.580030
f2a9e5883151 Pulling fs layer
2025-Dec-25 10:48:19.580030
8d363c2df07a Pulling fs layer
2025-Dec-25 10:48:19.580030
5cdd56139991 Pulling fs layer
2025-Dec-25 10:48:19.580030
aa55ead71133 Pulling fs layer
2025-Dec-25 10:48:19.580030
758ebfa119db Pulling fs layer
2025-Dec-25 10:48:19.580030
798e92f9757e Pulling fs layer
2025-Dec-25 10:48:19.580030
ada9fa789fdc Pulling fs layer
2025-Dec-25 10:48:19.580030
3e738c3a66c8 Pulling fs layer
2025-Dec-25 10:48:19.580030
687b178dca38 Pulling fs layer
2025-Dec-25 10:48:19.580030
66fe66faf896 Waiting
2025-Dec-25 10:48:19.580030
c94f51fe9236 Waiting
2025-Dec-25 10:48:19.580030
9602d06b4e70 Waiting
2025-Dec-25 10:48:19.580030
fab6e4443d8a Waiting
2025-Dec-25 10:48:19.580030
f2a9e5883151 Waiting
2025-Dec-25 10:48:19.580030
8d363c2df07a Waiting
2025-Dec-25 10:48:19.580030
5cdd56139991 Waiting
2025-Dec-25 10:48:19.580030
aa55ead71133 Waiting
2025-Dec-25 10:48:19.580030
758ebfa119db Waiting
2025-Dec-25 10:48:19.580030
798e92f9757e Waiting
2025-Dec-25 10:48:19.580030
ada9fa789fdc Waiting
2025-Dec-25 10:48:19.580030
3e738c3a66c8 Waiting
2025-Dec-25 10:48:19.580030
687b178dca38 Waiting
2025-Dec-25 10:48:19.580030
ea29d36b883e Pulling fs layer
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Pulling fs layer
2025-Dec-25 10:48:19.580030
393f8747e4b4 Pulling fs layer
2025-Dec-25 10:48:19.580030
20b69ee379c9 Pulling fs layer
2025-Dec-25 10:48:19.580030
ea29d36b883e Waiting
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Waiting
2025-Dec-25 10:48:19.580030
393f8747e4b4 Waiting
2025-Dec-25 10:48:19.580030
20b69ee379c9 Waiting
2025-Dec-25 10:48:19.580030
f94d28849fa3 Downloading [>                                                  ]  17.36kB/1.637MB
2025-Dec-25 10:48:19.580030
81260b173076 Downloading [>                                                  ]  2.301kB/122.7kB
2025-Dec-25 10:48:19.580030
81260b173076 Verifying Checksum
2025-Dec-25 10:48:19.580030
81260b173076 Download complete
2025-Dec-25 10:48:19.580030
b83ce1c86227 Downloading [>                                                  ]  75.84kB/7.241MB
2025-Dec-25 10:48:19.580030
f94d28849fa3 Verifying Checksum
2025-Dec-25 10:48:19.580030
f94d28849fa3 Download complete
2025-Dec-25 10:48:19.580030
b83ce1c86227 Verifying Checksum
2025-Dec-25 10:48:19.580030
b83ce1c86227 Download complete
2025-Dec-25 10:48:19.580030
b83ce1c86227 Extracting [>                                                  ]   98.3kB/7.241MB
2025-Dec-25 10:48:19.580030
b83ce1c86227 Extracting [==============>                                    ]  2.064MB/7.241MB
2025-Dec-25 10:48:19.580030
b83ce1c86227 Extracting [===================================>               ]  5.112MB/7.241MB
2025-Dec-25 10:48:19.580030
1008deaf6ec4 Downloading [>                                                  ]    114kB/11.19MB
2025-Dec-25 10:48:19.580030
71e9fc939447 Downloading [>                                                  ]  24.61kB/2.402MB
2025-Dec-25 10:48:19.580030
f9c0805c25ee Downloading [>                                                  ]    409kB/39.45MB
2025-Dec-25 10:48:19.580030
b83ce1c86227 Extracting [============================================>      ]  6.488MB/7.241MB
2025-Dec-25 10:48:19.580030
1008deaf6ec4 Downloading [===============================>                   ]  7.066MB/11.19MB
2025-Dec-25 10:48:19.580030
71e9fc939447 Downloading [==================================================>]  2.402MB/2.402MB
2025-Dec-25 10:48:19.580030
71e9fc939447 Verifying Checksum
2025-Dec-25 10:48:19.580030
71e9fc939447 Download complete
2025-Dec-25 10:48:19.580030
1008deaf6ec4 Verifying Checksum
2025-Dec-25 10:48:19.580030
1008deaf6ec4 Download complete
2025-Dec-25 10:48:19.580030
f9c0805c25ee Downloading [=====>                                             ]  4.044MB/39.45MB
2025-Dec-25 10:48:19.580030
b83ce1c86227 Extracting [==============================================>    ]  6.685MB/7.241MB
2025-Dec-25 10:48:19.580030
b83ce1c86227 Extracting [==================================================>]  7.241MB/7.241MB
2025-Dec-25 10:48:19.580030
f9c0805c25ee Downloading [====================>                              ]  15.79MB/39.45MB
2025-Dec-25 10:48:19.580030
b83ce1c86227 Pull complete
2025-Dec-25 10:48:19.580030
f94d28849fa3 Extracting [=>                                                 ]  32.77kB/1.637MB
2025-Dec-25 10:48:19.580030
f9c0805c25ee Downloading [===================================>               ]  27.98MB/39.45MB
2025-Dec-25 10:48:19.580030
f94d28849fa3 Extracting [================================================>  ]  1.573MB/1.637MB
2025-Dec-25 10:48:19.580030
f94d28849fa3 Extracting [==================================================>]  1.637MB/1.637MB
2025-Dec-25 10:48:19.580030
f94d28849fa3 Extracting [==================================================>]  1.637MB/1.637MB
2025-Dec-25 10:48:19.580030
c1bc68842c41 Downloading [>                                                  ]  2.301kB/180.3kB
2025-Dec-25 10:48:19.580030
c1bc68842c41 Downloading [==================================================>]  180.3kB/180.3kB
2025-Dec-25 10:48:19.580030
c1bc68842c41 Verifying Checksum
2025-Dec-25 10:48:19.580030
c1bc68842c41 Download complete
2025-Dec-25 10:48:19.580030
f9c0805c25ee Downloading [=================================================> ]  38.97MB/39.45MB
2025-Dec-25 10:48:19.580030
f9c0805c25ee Verifying Checksum
2025-Dec-25 10:48:19.580030
f9c0805c25ee Download complete
2025-Dec-25 10:48:19.580030
f94d28849fa3 Pull complete
2025-Dec-25 10:48:19.580030
81260b173076 Extracting [=============>                                     ]  32.77kB/122.7kB
2025-Dec-25 10:48:19.580030
81260b173076 Extracting [==================================================>]  122.7kB/122.7kB
2025-Dec-25 10:48:19.580030
81260b173076 Extracting [==================================================>]  122.7kB/122.7kB
2025-Dec-25 10:48:19.580030
0288b5a0d7e7 Downloading [===>                                               ]     933B/11.88kB
2025-Dec-25 10:48:19.580030
0288b5a0d7e7 Downloading [==================================================>]  11.88kB/11.88kB
2025-Dec-25 10:48:19.580030
0288b5a0d7e7 Verifying Checksum
2025-Dec-25 10:48:19.580030
0288b5a0d7e7 Download complete
2025-Dec-25 10:48:19.580030
81260b173076 Pull complete
2025-Dec-25 10:48:19.580030
f9c0805c25ee Extracting [>                                                  ]    426kB/39.45MB
2025-Dec-25 10:48:19.580030
f9c0805c25ee Extracting [===>                                               ]  2.982MB/39.45MB
2025-Dec-25 10:48:19.580030
f9c0805c25ee Extracting [=======>                                           ]  5.964MB/39.45MB
2025-Dec-25 10:48:19.580030
34013573f278 Downloading [==================================================>]     496B/496B
2025-Dec-25 10:48:19.580030
34013573f278 Verifying Checksum
2025-Dec-25 10:48:19.580030
34013573f278 Download complete
2025-Dec-25 10:48:19.580030
f9c0805c25ee Extracting [===========>                                       ]  8.946MB/39.45MB
2025-Dec-25 10:48:19.580030
66fe66faf896 Downloading [========================================>          ]     953B/1.165kB
2025-Dec-25 10:48:19.580030
66fe66faf896 Downloading [==================================================>]  1.165kB/1.165kB
2025-Dec-25 10:48:19.580030
66fe66faf896 Verifying Checksum
2025-Dec-25 10:48:19.580030
66fe66faf896 Download complete
2025-Dec-25 10:48:19.580030
66fe66faf896 Extracting [==================================================>]  1.165kB/1.165kB
2025-Dec-25 10:48:19.580030
66fe66faf896 Extracting [==================================================>]  1.165kB/1.165kB
2025-Dec-25 10:48:19.580030
c94f51fe9236 Downloading [>                                                  ]  67.45kB/6.437MB
2025-Dec-25 10:48:19.580030
f9c0805c25ee Extracting [==============>                                    ]  11.08MB/39.45MB
2025-Dec-25 10:48:19.580030
66fe66faf896 Pull complete
2025-Dec-25 10:48:19.580030
c94f51fe9236 Downloading [===========================================>       ]   5.55MB/6.437MB
2025-Dec-25 10:48:19.580030
c94f51fe9236 Verifying Checksum
2025-Dec-25 10:48:19.580030
c94f51fe9236 Download complete
2025-Dec-25 10:48:19.580030
c94f51fe9236 Extracting [>                                                  ]  65.54kB/6.437MB
2025-Dec-25 10:48:19.580030
f9c0805c25ee Extracting [===============>                                   ]  12.35MB/39.45MB
2025-Dec-25 10:48:19.580030
c94f51fe9236 Extracting [=========>                                         ]   1.18MB/6.437MB
2025-Dec-25 10:48:19.580030
f9c0805c25ee Extracting [=================>                                 ]  14.06MB/39.45MB
2025-Dec-25 10:48:19.580030
c94f51fe9236 Extracting [===================>                               ]   2.49MB/6.437MB
2025-Dec-25 10:48:19.580030
9602d06b4e70 Downloading [>                                                  ]  13.69kB/1.257MB
2025-Dec-25 10:48:19.580030
f9c0805c25ee Extracting [===================>                               ]  15.34MB/39.45MB
2025-Dec-25 10:48:19.580030
9602d06b4e70 Verifying Checksum
2025-Dec-25 10:48:19.580030
9602d06b4e70 Download complete
2025-Dec-25 10:48:19.580030
c94f51fe9236 Extracting [============================>                      ]   3.67MB/6.437MB
2025-Dec-25 10:48:19.580030
fab6e4443d8a Downloading [>                                                  ]  84.36kB/8.204MB
2025-Dec-25 10:48:19.580030
f9c0805c25ee Extracting [====================>                              ]  16.19MB/39.45MB
2025-Dec-25 10:48:19.580030
c94f51fe9236 Extracting [===================================>               ]  4.522MB/6.437MB
2025-Dec-25 10:48:19.580030
fab6e4443d8a Verifying Checksum
2025-Dec-25 10:48:19.580030
fab6e4443d8a Download complete
2025-Dec-25 10:48:19.580030
f2a9e5883151 Downloading [>                                                  ]  13.69kB/1.312MB
2025-Dec-25 10:48:19.580030
f2a9e5883151 Verifying Checksum
2025-Dec-25 10:48:19.580030
f2a9e5883151 Download complete
2025-Dec-25 10:48:19.580030
c94f51fe9236 Extracting [=======================================>           ]  5.046MB/6.437MB
2025-Dec-25 10:48:19.580030
f9c0805c25ee Extracting [=====================>                             ]  17.04MB/39.45MB
2025-Dec-25 10:48:19.580030
c94f51fe9236 Extracting [==========================================>        ]  5.505MB/6.437MB
2025-Dec-25 10:48:19.580030
c94f51fe9236 Extracting [=================================================> ]  6.357MB/6.437MB
2025-Dec-25 10:48:19.580030
f9c0805c25ee Extracting [======================>                            ]  17.89MB/39.45MB
2025-Dec-25 10:48:19.580030
c94f51fe9236 Extracting [==================================================>]  6.437MB/6.437MB
2025-Dec-25 10:48:19.580030
8d363c2df07a Downloading [==================================================>]     116B/116B
2025-Dec-25 10:48:19.580030
8d363c2df07a Verifying Checksum
2025-Dec-25 10:48:19.580030
8d363c2df07a Download complete
2025-Dec-25 10:48:19.580030
f9c0805c25ee Extracting [==========================>                        ]   21.3MB/39.45MB
2025-Dec-25 10:48:19.580030
c94f51fe9236 Pull complete
2025-Dec-25 10:48:19.580030
9602d06b4e70 Extracting [=>                                                 ]  32.77kB/1.257MB
2025-Dec-25 10:48:19.580030
5cdd56139991 Downloading [===============>                                   ]     953B/3.144kB
2025-Dec-25 10:48:19.580030
5cdd56139991 Downloading [==================================================>]  3.144kB/3.144kB
2025-Dec-25 10:48:19.580030
5cdd56139991 Verifying Checksum
2025-Dec-25 10:48:19.580030
5cdd56139991 Download complete
2025-Dec-25 10:48:19.580030
f9c0805c25ee Extracting [=============================>                     ]     23MB/39.45MB
2025-Dec-25 10:48:19.580030
9602d06b4e70 Extracting [==================================================>]  1.257MB/1.257MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Downloading [>                                                  ]  540.7kB/111MB
2025-Dec-25 10:48:19.580030
9602d06b4e70 Pull complete
2025-Dec-25 10:48:19.580030
fab6e4443d8a Extracting [>                                                  ]   98.3kB/8.204MB
2025-Dec-25 10:48:19.580030
f9c0805c25ee Extracting [==============================>                    ]  24.28MB/39.45MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Downloading [===>                                               ]  6.955MB/111MB
2025-Dec-25 10:48:19.580030
fab6e4443d8a Extracting [====>                                              ]  688.1kB/8.204MB
2025-Dec-25 10:48:19.580030
f9c0805c25ee Extracting [==================================>                ]  26.84MB/39.45MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Downloading [=======>                                           ]  17.15MB/111MB
2025-Dec-25 10:48:19.580030
fab6e4443d8a Extracting [========>                                          ]  1.475MB/8.204MB
2025-Dec-25 10:48:19.580030
758ebfa119db Downloading [====>                                              ]     953B/9.879kB
2025-Dec-25 10:48:19.580030
758ebfa119db Downloading [==================================================>]  9.879kB/9.879kB
2025-Dec-25 10:48:19.580030
758ebfa119db Verifying Checksum
2025-Dec-25 10:48:19.580030
758ebfa119db Download complete
2025-Dec-25 10:48:19.580030
f9c0805c25ee Extracting [====================================>              ]  28.54MB/39.45MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Downloading [===========>                                       ]  25.73MB/111MB
2025-Dec-25 10:48:19.580030
fab6e4443d8a Extracting [===================>                               ]  3.146MB/8.204MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Downloading [===============>                                   ]  34.28MB/111MB
2025-Dec-25 10:48:19.580030
f9c0805c25ee Extracting [======================================>            ]  30.24MB/39.45MB
2025-Dec-25 10:48:19.580030
fab6e4443d8a Extracting [=========================>                         ]  4.227MB/8.204MB
2025-Dec-25 10:48:19.580030
798e92f9757e Downloading [==================================================>]     128B/128B
2025-Dec-25 10:48:19.580030
798e92f9757e Verifying Checksum
2025-Dec-25 10:48:19.580030
798e92f9757e Download complete
2025-Dec-25 10:48:19.580030
f9c0805c25ee Extracting [=========================================>         ]   32.8MB/39.45MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Downloading [====================>                              ]  44.45MB/111MB
2025-Dec-25 10:48:19.580030
fab6e4443d8a Extracting [=============================>                     ]  4.915MB/8.204MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Downloading [========================>                          ]  53.59MB/111MB
2025-Dec-25 10:48:19.580030
f9c0805c25ee Extracting [==============================================>    ]  36.63MB/39.45MB
2025-Dec-25 10:48:19.580030
fab6e4443d8a Extracting [===================================>               ]  5.898MB/8.204MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Downloading [============================>                      ]  62.71MB/111MB
2025-Dec-25 10:48:19.580030
f9c0805c25ee Extracting [================================================>  ]  38.34MB/39.45MB
2025-Dec-25 10:48:19.580030
ada9fa789fdc Downloading [==================================================>]     168B/168B
2025-Dec-25 10:48:19.580030
ada9fa789fdc Verifying Checksum
2025-Dec-25 10:48:19.580030
ada9fa789fdc Download complete
2025-Dec-25 10:48:19.580030
fab6e4443d8a Extracting [=========================================>         ]  6.783MB/8.204MB
2025-Dec-25 10:48:19.580030
f9c0805c25ee Extracting [==================================================>]  39.45MB/39.45MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Downloading [===============================>                   ]  70.71MB/111MB
2025-Dec-25 10:48:19.580030
fab6e4443d8a Extracting [==============================================>    ]  7.668MB/8.204MB
2025-Dec-25 10:48:19.580030
f9c0805c25ee Pull complete
2025-Dec-25 10:48:19.580030
1008deaf6ec4 Extracting [>                                                  ]  131.1kB/11.19MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Downloading [====================================>              ]  80.38MB/111MB
2025-Dec-25 10:48:19.580030
fab6e4443d8a Extracting [==================================================>]  8.204MB/8.204MB
2025-Dec-25 10:48:19.580030
3e738c3a66c8 Downloading [========>                                          ]     953B/5.837kB
2025-Dec-25 10:48:19.580030
3e738c3a66c8 Downloading [==================================================>]  5.837kB/5.837kB
2025-Dec-25 10:48:19.580030
3e738c3a66c8 Verifying Checksum
2025-Dec-25 10:48:19.580030
3e738c3a66c8 Download complete
2025-Dec-25 10:48:19.580030
1008deaf6ec4 Extracting [========>                                          ]  1.966MB/11.19MB
2025-Dec-25 10:48:19.580030
fab6e4443d8a Pull complete
2025-Dec-25 10:48:19.580030
f2a9e5883151 Extracting [=>                                                 ]  32.77kB/1.312MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Downloading [=======================================>           ]   88.4MB/111MB
2025-Dec-25 10:48:19.580030
1008deaf6ec4 Extracting [===================>                               ]  4.456MB/11.19MB
2025-Dec-25 10:48:19.580030
f2a9e5883151 Extracting [==================================================>]  1.312MB/1.312MB
2025-Dec-25 10:48:19.580030
f2a9e5883151 Pull complete
2025-Dec-25 10:48:19.580030
aa55ead71133 Downloading [============================================>      ]  98.03MB/111MB
2025-Dec-25 10:48:19.580030
8d363c2df07a Extracting [==================================================>]     116B/116B
2025-Dec-25 10:48:19.580030
8d363c2df07a Extracting [==================================================>]     116B/116B
2025-Dec-25 10:48:19.580030
8d363c2df07a Pull complete
2025-Dec-25 10:48:19.580030
5cdd56139991 Extracting [==================================================>]  3.144kB/3.144kB
2025-Dec-25 10:48:19.580030
1008deaf6ec4 Extracting [=============================>                     ]  6.554MB/11.19MB
2025-Dec-25 10:48:19.580030
5cdd56139991 Extracting [==================================================>]  3.144kB/3.144kB
2025-Dec-25 10:48:19.580030
5cdd56139991 Pull complete
2025-Dec-25 10:48:19.580030
aa55ead71133 Downloading [===============================================>   ]  106.1MB/111MB
2025-Dec-25 10:48:19.580030
687b178dca38 Downloading [==================================================>]     185B/185B
2025-Dec-25 10:48:19.580030
687b178dca38 Verifying Checksum
2025-Dec-25 10:48:19.580030
687b178dca38 Download complete
2025-Dec-25 10:48:19.580030
1008deaf6ec4 Extracting [==================================>                ]  7.733MB/11.19MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Verifying Checksum
2025-Dec-25 10:48:19.580030
aa55ead71133 Download complete
2025-Dec-25 10:48:19.580030
ea29d36b883e Downloading [>                                                  ]  74.57kB/7.221MB
2025-Dec-25 10:48:19.580030
1008deaf6ec4 Extracting [========================================>          ]  9.044MB/11.19MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [>                                                  ]  557.1kB/111MB
2025-Dec-25 10:48:19.580030
ea29d36b883e Downloading [==================================>                ]  5.022MB/7.221MB
2025-Dec-25 10:48:19.580030
ea29d36b883e Verifying Checksum
2025-Dec-25 10:48:19.580030
ea29d36b883e Download complete
2025-Dec-25 10:48:19.580030
ea29d36b883e Extracting [>                                                  ]   98.3kB/7.221MB
2025-Dec-25 10:48:19.580030
1008deaf6ec4 Extracting [===========================================>       ]   9.83MB/11.19MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [>                                                  ]  1.671MB/111MB
2025-Dec-25 10:48:19.580030
ea29d36b883e Extracting [======>                                            ]    983kB/7.221MB
2025-Dec-25 10:48:19.580030
1008deaf6ec4 Extracting [================================================>  ]  10.88MB/11.19MB
2025-Dec-25 10:48:19.580030
1008deaf6ec4 Extracting [==================================================>]  11.19MB/11.19MB
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Downloading [>                                                  ]  528.4kB/77.15MB
2025-Dec-25 10:48:19.580030
1008deaf6ec4 Pull complete
2025-Dec-25 10:48:19.580030
71e9fc939447 Extracting [>                                                  ]  32.77kB/2.402MB
2025-Dec-25 10:48:19.580030
393f8747e4b4 Downloading [>                                                  ]  532.5kB/177.9MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [=>                                                 ]  3.342MB/111MB
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Downloading [=====>                                             ]  8.469MB/77.15MB
2025-Dec-25 10:48:19.580030
71e9fc939447 Extracting [==========================>                        ]  1.278MB/2.402MB
2025-Dec-25 10:48:19.580030
ea29d36b883e Extracting [==============>                                    ]  2.064MB/7.221MB
2025-Dec-25 10:48:19.580030
393f8747e4b4 Downloading [=>                                                 ]   6.93MB/177.9MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [==>                                                ]  4.456MB/111MB
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Downloading [==========>                                        ]  15.89MB/77.15MB
2025-Dec-25 10:48:19.580030
71e9fc939447 Extracting [===============================================>   ]  2.294MB/2.402MB
2025-Dec-25 10:48:19.580030
ea29d36b883e Extracting [===============>                                   ]  2.261MB/7.221MB
2025-Dec-25 10:48:19.580030
71e9fc939447 Extracting [==================================================>]  2.402MB/2.402MB
2025-Dec-25 10:48:19.580030
393f8747e4b4 Downloading [===>                                               ]  13.31MB/177.9MB
2025-Dec-25 10:48:19.580030
71e9fc939447 Pull complete
2025-Dec-25 10:48:19.580030
20b69ee379c9 Downloading [==================================================>]     551B/551B
2025-Dec-25 10:48:19.580030
20b69ee379c9 Verifying Checksum
2025-Dec-25 10:48:19.580030
20b69ee379c9 Download complete
2025-Dec-25 10:48:19.580030
c1bc68842c41 Extracting [=========>                                         ]  32.77kB/180.3kB
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Downloading [==============>                                    ]  22.23MB/77.15MB
2025-Dec-25 10:48:19.580030
c1bc68842c41 Extracting [==================================================>]  180.3kB/180.3kB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [==>                                                ]  6.128MB/111MB
2025-Dec-25 10:48:19.580030
ea29d36b883e Extracting [=======================>                           ]  3.342MB/7.221MB
2025-Dec-25 10:48:19.580030
c1bc68842c41 Extracting [==================================================>]  180.3kB/180.3kB
2025-Dec-25 10:48:19.580030
393f8747e4b4 Downloading [=====>                                             ]  18.64MB/177.9MB
2025-Dec-25 10:48:19.580030
c1bc68842c41 Pull complete
2025-Dec-25 10:48:19.580030
0288b5a0d7e7 Extracting [==================================================>]  11.88kB/11.88kB
2025-Dec-25 10:48:19.580030
0288b5a0d7e7 Extracting [==================================================>]  11.88kB/11.88kB
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Downloading [===================>                               ]  29.61MB/77.15MB
2025-Dec-25 10:48:19.580030
0288b5a0d7e7 Pull complete
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [===>                                               ]  7.242MB/111MB
2025-Dec-25 10:48:19.580030
34013573f278 Extracting [==================================================>]     496B/496B
2025-Dec-25 10:48:19.580030
34013573f278 Extracting [==================================================>]     496B/496B
2025-Dec-25 10:48:19.580030
ea29d36b883e Extracting [==============================>                    ]  4.424MB/7.221MB
2025-Dec-25 10:48:19.580030
393f8747e4b4 Downloading [======>                                            ]  23.45MB/177.9MB
2025-Dec-25 10:48:19.580030
34013573f278 Pull complete
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Downloading [========================>                          ]  37.56MB/77.15MB
2025-Dec-25 10:48:19.580030
minio Pulled
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [===>                                               ]  7.799MB/111MB
2025-Dec-25 10:48:19.580030
ea29d36b883e Extracting [====================================>              ]   5.21MB/7.221MB
2025-Dec-25 10:48:19.580030
393f8747e4b4 Downloading [========>                                          ]  29.35MB/177.9MB
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Downloading [===========================>                       ]  42.32MB/77.15MB
2025-Dec-25 10:48:19.580030
393f8747e4b4 Downloading [=========>                                         ]  35.24MB/177.9MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [====>                                              ]  8.913MB/111MB
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Downloading [================================>                  ]  50.78MB/77.15MB
2025-Dec-25 10:48:19.580030
ea29d36b883e Extracting [============================================>      ]   6.39MB/7.221MB
2025-Dec-25 10:48:19.580030
393f8747e4b4 Downloading [===========>                                       ]  41.62MB/177.9MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [====>                                              ]  10.58MB/111MB
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Downloading [=====================================>             ]  57.65MB/77.15MB
2025-Dec-25 10:48:19.580030
ea29d36b883e Extracting [===============================================>   ]  6.881MB/7.221MB
2025-Dec-25 10:48:19.580030
393f8747e4b4 Downloading [=============>                                     ]  47.51MB/177.9MB
2025-Dec-25 10:48:19.580030
ea29d36b883e Extracting [==================================================>]  7.221MB/7.221MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [=====>                                             ]   11.7MB/111MB
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Downloading [==========================================>        ]  65.08MB/77.15MB
2025-Dec-25 10:48:19.580030
ea29d36b883e Pull complete
2025-Dec-25 10:48:19.580030
393f8747e4b4 Downloading [===============>                                   ]   53.4MB/177.9MB
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Downloading [===============================================>   ]  73.56MB/77.15MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [======>                                            ]  13.93MB/111MB
2025-Dec-25 10:48:19.580030
393f8747e4b4 Downloading [================>                                  ]  58.75MB/177.9MB
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Verifying Checksum
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Download complete
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Extracting [>                                                  ]  557.1kB/77.15MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [=======>                                           ]   15.6MB/111MB
2025-Dec-25 10:48:19.580030
393f8747e4b4 Downloading [==================>                                ]  66.72MB/177.9MB
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Extracting [=>                                                 ]  2.228MB/77.15MB
2025-Dec-25 10:48:19.580030
393f8747e4b4 Downloading [=====================>                             ]  75.72MB/177.9MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [========>                                          ]  17.83MB/111MB
2025-Dec-25 10:48:19.580030
393f8747e4b4 Downloading [=======================>                           ]  84.19MB/177.9MB
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Extracting [==>                                                ]  4.456MB/77.15MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [=========>                                         ]  20.05MB/111MB
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Extracting [====>                                              ]  6.685MB/77.15MB
2025-Dec-25 10:48:19.580030
393f8747e4b4 Downloading [==========================>                        ]  92.62MB/177.9MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [==========>                                        ]  22.28MB/111MB
2025-Dec-25 10:48:19.580030
393f8747e4b4 Downloading [============================>                      ]  100.5MB/177.9MB
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Extracting [=====>                                             ]  8.356MB/77.15MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [==========>                                        ]   23.4MB/111MB
2025-Dec-25 10:48:19.580030
393f8747e4b4 Downloading [==============================>                    ]  109.5MB/177.9MB
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Extracting [======>                                            ]  10.58MB/77.15MB
2025-Dec-25 10:48:19.580030
393f8747e4b4 Downloading [=================================>                 ]  119.1MB/177.9MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [===========>                                       ]  25.62MB/111MB
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Extracting [========>                                          ]  12.81MB/77.15MB
2025-Dec-25 10:48:19.580030
393f8747e4b4 Downloading [====================================>              ]  129.1MB/177.9MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [============>                                      ]  28.41MB/111MB
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Extracting [==========>                                        ]   15.6MB/77.15MB
2025-Dec-25 10:48:19.580030
393f8747e4b4 Downloading [======================================>            ]  138.6MB/177.9MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [==============>                                    ]   31.2MB/111MB
2025-Dec-25 10:48:19.580030
393f8747e4b4 Downloading [========================================>          ]  145.5MB/177.9MB
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Extracting [===========>                                       ]  17.27MB/77.15MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [==============>                                    ]  31.75MB/111MB
2025-Dec-25 10:48:19.580030
393f8747e4b4 Downloading [============================================>      ]  157.1MB/177.9MB
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Extracting [===========>                                       ]  18.38MB/77.15MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [===============>                                   ]  33.42MB/111MB
2025-Dec-25 10:48:19.580030
393f8747e4b4 Downloading [===============================================>   ]  168.2MB/177.9MB
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Extracting [============>                                      ]  20.05MB/77.15MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [================>                                  ]  35.65MB/111MB
2025-Dec-25 10:48:19.580030
393f8747e4b4 Downloading [=================================================> ]  176.7MB/177.9MB
2025-Dec-25 10:48:19.580030
393f8747e4b4 Verifying Checksum
2025-Dec-25 10:48:19.580030
393f8747e4b4 Download complete
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Extracting [==============>                                    ]  22.28MB/77.15MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [=================>                                 ]  38.99MB/111MB
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Extracting [================>                                  ]  26.18MB/77.15MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [===================>                               ]  42.89MB/111MB
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Extracting [==================>                                ]  28.97MB/77.15MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [====================>                              ]  45.12MB/111MB
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Extracting [====================>                              ]   31.2MB/77.15MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [=====================>                             ]  47.91MB/111MB
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Extracting [======================>                            ]  34.54MB/77.15MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [=======================>                           ]  51.25MB/111MB
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Extracting [=======================>                           ]  36.21MB/77.15MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [=======================>                           ]  52.92MB/111MB
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Extracting [=========================>                         ]  39.55MB/77.15MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [========================>                          ]  54.59MB/111MB
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Extracting [===========================>                       ]  42.34MB/77.15MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [=========================>                         ]  56.82MB/111MB
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Extracting [=============================>                     ]  45.68MB/77.15MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [==========================>                        ]   59.6MB/111MB
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Extracting [================================>                  ]  49.58MB/77.15MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [============================>                      ]  62.39MB/111MB
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Extracting [=================================>                 ]  51.25MB/77.15MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [=============================>                     ]  66.29MB/111MB
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Extracting [==================================>                ]  53.48MB/77.15MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [===============================>                   ]  70.75MB/111MB
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Extracting [====================================>              ]  56.26MB/77.15MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [=================================>                 ]  74.09MB/111MB
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Extracting [======================================>            ]   59.6MB/77.15MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [==================================>                ]  76.32MB/111MB
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Extracting [========================================>          ]  61.83MB/77.15MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [===================================>               ]  78.54MB/111MB
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Extracting [==========================================>        ]  65.18MB/77.15MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [====================================>              ]  81.89MB/111MB
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Extracting [===========================================>       ]   67.4MB/77.15MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [======================================>            ]  84.67MB/111MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [======================================>            ]  86.34MB/111MB
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Extracting [============================================>      ]  68.52MB/77.15MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [=========================================>         ]  91.36MB/111MB
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Extracting [=============================================>     ]  70.75MB/77.15MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [==========================================>        ]   94.7MB/111MB
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Extracting [==============================================>    ]  72.42MB/77.15MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [===========================================>       ]  95.81MB/111MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [===========================================>       ]  96.93MB/111MB
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Extracting [===============================================>   ]  73.53MB/77.15MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [============================================>      ]   98.6MB/111MB
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Extracting [================================================>  ]  74.09MB/77.15MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [============================================>      ]  99.71MB/111MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [=============================================>     ]  100.8MB/111MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [=============================================>     ]  101.9MB/111MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [==============================================>    ]  104.2MB/111MB
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Extracting [================================================>  ]   75.2MB/77.15MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [===============================================>   ]  105.8MB/111MB
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Extracting [=================================================> ]  76.32MB/77.15MB
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Extracting [==================================================>]  77.15MB/77.15MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [================================================>  ]    107MB/111MB
2025-Dec-25 10:48:19.580030
a9bb58c3bdd8 Pull complete
2025-Dec-25 10:48:19.580030
393f8747e4b4 Extracting [>                                                  ]  557.1kB/177.9MB
2025-Dec-25 10:48:19.580030
393f8747e4b4 Extracting [==>                                                ]  10.58MB/177.9MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [================================================>  ]  108.1MB/111MB
2025-Dec-25 10:48:19.580030
393f8747e4b4 Extracting [=====>                                             ]  18.38MB/177.9MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [=================================================> ]  109.2MB/111MB
2025-Dec-25 10:48:19.580030
393f8747e4b4 Extracting [=======>                                           ]  28.41MB/177.9MB
2025-Dec-25 10:48:19.580030
393f8747e4b4 Extracting [=========>                                         ]  34.54MB/177.9MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [=================================================> ]  109.7MB/111MB
2025-Dec-25 10:48:19.580030
393f8747e4b4 Extracting [===========>                                       ]  40.11MB/177.9MB
2025-Dec-25 10:48:19.580030
393f8747e4b4 Extracting [==============>                                    ]  50.14MB/177.9MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [=================================================> ]  110.9MB/111MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Extracting [==================================================>]    111MB/111MB
2025-Dec-25 10:48:19.580030
393f8747e4b4 Extracting [===============>                                   ]  55.15MB/177.9MB
2025-Dec-25 10:48:19.580030
aa55ead71133 Pull complete
2025-Dec-25 10:48:19.580030
758ebfa119db Extracting [==================================================>]  9.879kB/9.879kB
2025-Dec-25 10:48:19.580030
758ebfa119db Extracting [==================================================>]  9.879kB/9.879kB
2025-Dec-25 10:48:19.580030
758ebfa119db Pull complete
2025-Dec-25 10:48:19.580030
798e92f9757e Extracting [==================================================>]     128B/128B
2025-Dec-25 10:48:19.580030
798e92f9757e Extracting [==================================================>]     128B/128B
2025-Dec-25 10:48:19.580030
393f8747e4b4 Extracting [================>                                  ]  60.16MB/177.9MB
2025-Dec-25 10:48:19.580030
798e92f9757e Pull complete
2025-Dec-25 10:48:19.580030
ada9fa789fdc Extracting [==================================================>]     168B/168B
2025-Dec-25 10:48:19.580030
ada9fa789fdc Extracting [==================================================>]     168B/168B
2025-Dec-25 10:48:19.580030
ada9fa789fdc Pull complete
2025-Dec-25 10:48:19.580030
3e738c3a66c8 Extracting [==================================================>]  5.837kB/5.837kB
2025-Dec-25 10:48:19.580030
3e738c3a66c8 Extracting [==================================================>]  5.837kB/5.837kB
2025-Dec-25 10:48:19.580030
3e738c3a66c8 Pull complete
2025-Dec-25 10:48:19.580030
687b178dca38 Extracting [==================================================>]     185B/185B
2025-Dec-25 10:48:19.580030
687b178dca38 Extracting [==================================================>]     185B/185B
2025-Dec-25 10:48:19.580030
687b178dca38 Pull complete
2025-Dec-25 10:48:19.580030
control-plane-db Pulled
2025-Dec-25 10:48:19.580030
393f8747e4b4 Extracting [==================>                                ]  64.06MB/177.9MB
2025-Dec-25 10:48:19.580030
393f8747e4b4 Extracting [=====================>                             ]  76.32MB/177.9MB
2025-Dec-25 10:48:19.580030
393f8747e4b4 Extracting [========================>                          ]  88.57MB/177.9MB
2025-Dec-25 10:48:19.580030
393f8747e4b4 Extracting [==========================>                        ]  95.26MB/177.9MB
2025-Dec-25 10:48:19.580030
393f8747e4b4 Extracting [=============================>                     ]  105.3MB/177.9MB
2025-Dec-25 10:48:19.580030
393f8747e4b4 Extracting [================================>                  ]  115.3MB/177.9MB
2025-Dec-25 10:48:19.580030
393f8747e4b4 Extracting [===================================>               ]  127.6MB/177.9MB
2025-Dec-25 10:48:19.580030
393f8747e4b4 Extracting [========================================>          ]  143.7MB/177.9MB
2025-Dec-25 10:48:19.580030
393f8747e4b4 Extracting [=============================================>     ]  162.1MB/177.9MB
2025-Dec-25 10:48:19.580030
393f8747e4b4 Extracting [================================================>  ]  173.8MB/177.9MB
2025-Dec-25 10:48:19.580030
393f8747e4b4 Extracting [==================================================>]  177.9MB/177.9MB
2025-Dec-25 10:48:19.580030
393f8747e4b4 Pull complete
2025-Dec-25 10:48:19.580030
20b69ee379c9 Extracting [==================================================>]     551B/551B
2025-Dec-25 10:48:19.580030
20b69ee379c9 Extracting [==================================================>]     551B/551B
2025-Dec-25 10:48:19.580030
20b69ee379c9 Pull complete
2025-Dec-25 10:48:19.580030
keycloak Pulled
2025-Dec-25 10:48:19.580030
Volume "hck4w0k4ww8kk4gccw000ggg_minio-data"  Creating
2025-Dec-25 10:48:19.580030
Volume "hck4w0k4ww8kk4gccw000ggg_minio-data"  Created
2025-Dec-25 10:48:19.580030
Volume "hck4w0k4ww8kk4gccw000ggg_control-plane-data"  Creating
2025-Dec-25 10:48:19.580030
Volume "hck4w0k4ww8kk4gccw000ggg_control-plane-data"  Created
2025-Dec-25 10:48:19.580030
Container minio-hck4w0k4ww8kk4gccw000ggg-104552416742  Creating
2025-Dec-25 10:48:19.580030
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-104552360220  Creating
2025-Dec-25 10:48:19.580030
Container minio-hck4w0k4ww8kk4gccw000ggg-104552416742  Created
2025-Dec-25 10:48:19.580030
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-104552360220  Created
2025-Dec-25 10:48:19.580030
Container keycloak-hck4w0k4ww8kk4gccw000ggg-104552403645  Creating
2025-Dec-25 10:48:19.580030
Container keycloak-hck4w0k4ww8kk4gccw000ggg-104552403645  Created
2025-Dec-25 10:48:19.580030
Container api-hck4w0k4ww8kk4gccw000ggg-104552377562  Creating
2025-Dec-25 10:48:19.580030
Container api-hck4w0k4ww8kk4gccw000ggg-104552377562  Created
2025-Dec-25 10:48:19.580030
Container dashboard-hck4w0k4ww8kk4gccw000ggg-104552392826  Creating
2025-Dec-25 10:48:19.580030
Container dashboard-hck4w0k4ww8kk4gccw000ggg-104552392826  Created
2025-Dec-25 10:48:19.580030
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-104552360220  Starting
2025-Dec-25 10:48:19.580030
Container minio-hck4w0k4ww8kk4gccw000ggg-104552416742  Starting
2025-Dec-25 10:48:19.580030
Container minio-hck4w0k4ww8kk4gccw000ggg-104552416742  Started
2025-Dec-25 10:48:19.580030
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-104552360220  Started
2025-Dec-25 10:48:19.580030
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-104552360220  Waiting
2025-Dec-25 10:48:19.580030
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-104552360220  Healthy
2025-Dec-25 10:48:19.580030
Container keycloak-hck4w0k4ww8kk4gccw000ggg-104552403645  Starting
2025-Dec-25 10:48:19.580030
Container keycloak-hck4w0k4ww8kk4gccw000ggg-104552403645  Started
2025-Dec-25 10:48:19.580030
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-104552360220  Waiting
2025-Dec-25 10:48:19.580030
Container control-plane-db-hck4w0k4ww8kk4gccw000ggg-104552360220  Healthy
2025-Dec-25 10:48:19.580030
Container api-hck4w0k4ww8kk4gccw000ggg-104552377562  Starting
2025-Dec-25 10:48:19.580030
Container api-hck4w0k4ww8kk4gccw000ggg-104552377562  Started
2025-Dec-25 10:48:19.580030
Container dashboard-hck4w0k4ww8kk4gccw000ggg-104552392826  Starting
2025-Dec-25 10:48:19.580030
Error response from daemon: driver failed programming external connectivity on endpoint dashboard-hck4w0k4ww8kk4gccw000ggg-104552392826 (054e93aa21485b0724dad3a5cfe1597c0fe0da902583fcb145c3d187271dc85d): Bind for 0.0.0.0:3000 failed: port is already allocated
2025-Dec-25 10:48:19.580030
exit status 1
2025-Dec-25 10:48:21.820828
Gracefully shutting down build container: rogwc4s4s0cwwkoscgg00go8
2025-Dec-25 10:48:23.020274
[CMD]: docker stop --time=30 rogwc4s4s0cwwkoscgg00go8
2025-Dec-25 10:48:23.020274
rogwc4s4s0cwwkoscgg00go8
2025-Dec-25 10:48:23.837221
[CMD]: docker rm -f rogwc4s4s0cwwkoscgg00go8
2025-Dec-25 10:48:23.837221
Error response from daemon: removal of container rogwc4s4s0cwwkoscgg00go8 is already in progress