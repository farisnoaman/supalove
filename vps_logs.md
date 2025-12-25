Server: localhost
keycloak-hck4w0k4ww8kk4gccw000ggg-123454665242
Only Show Number of Lines
*
100
Refresh
Stream Logs
Include Timestamps

2025-12-25T12:36:49.982623600Z Updating the configuration and installing your custom providers, if any. Please wait.
2025-12-25T12:37:11.436583212Z 2025-12-25 12:37:11,433 INFO  [io.quarkus.deployment.QuarkusAugmentor] (main) Quarkus augmentation completed in 16799ms
2025-12-25T12:37:14.730217223Z 2025-12-25 12:37:13,206 INFO  [org.keycloak.quarkus.runtime.hostname.DefaultHostnameProvider] (main) Hostname settings: Base URL: <unset>, Hostname: <request>, Strict HTTPS: false, Path: <request>, Strict BackChannel: false, Admin URL: <unset>, Admin: <request>, Port: -1, Proxied: true
2025-12-25T12:37:14.985738446Z 2025-12-25 12:37:14,985 WARN  [io.quarkus.agroal.runtime.DataSources] (main) Datasource <default> enables XA but transaction recovery is not enabled. Please enable transaction recovery by setting quarkus.transaction-manager.enable-recovery=true, otherwise data may be lost if the application is terminated abruptly
2025-12-25T12:37:15.875948066Z 2025-12-25 12:37:15,875 WARN  [org.infinispan.PERSISTENCE] (keycloak-cache-init) ISPN000554: jboss-marshalling is deprecated and planned for removal
2025-12-25T12:37:16.044804105Z 2025-12-25 12:37:16,044 WARN  [org.infinispan.CONFIG] (keycloak-cache-init) ISPN000569: Unable to persist Infinispan internal caches as no global state enabled
2025-12-25T12:37:16.165789954Z 2025-12-25 12:37:16,165 INFO  [org.infinispan.CONTAINER] (keycloak-cache-init) ISPN000556: Starting user marshaller 'org.infinispan.jboss.marshalling.core.JBossUserMarshaller'
2025-12-25T12:37:17.174926918Z 2025-12-25 12:37:17,174 WARN  [io.quarkus.vertx.http.runtime.VertxHttpRecorder] (main) The X-Forwarded-* and Forwarded headers will be considered when determining the proxy address. This configuration can cause a security issue as clients can forge requests and send a forwarded header that is not overwritten by the proxy. Please consider use one of these headers just to forward the proxy address in requests.
2025-12-25T12:37:17.561712227Z 2025-12-25 12:37:17,561 INFO  [org.keycloak.connections.infinispan.DefaultInfinispanConnectionProviderFactory] (main) Node name: node_206669, Site name: null
2025-12-25T12:37:17.569280929Z 2025-12-25 12:37:17,568 INFO  [org.keycloak.broker.provider.AbstractIdentityProviderMapper] (main) Registering class org.keycloak.broker.provider.mappersync.ConfigSyncEventListener
2025-12-25T12:37:18.562102186Z 2025-12-25 12:37:18,561 INFO  [io.quarkus] (main) Keycloak 23.0.7 on JVM (powered by Quarkus 3.2.10.Final) started in 6.962s. Listening on: http://0.0.0.0:8080
2025-12-25T12:37:18.562478170Z 2025-12-25 12:37:18,562 INFO  [io.quarkus] (main) Profile dev activated. 
2025-12-25T12:37:18.563062545Z 2025-12-25 12:37:18,562 INFO  [io.quarkus] (main) Installed features: [agroal, cdi, hibernate-orm, jdbc-h2, jdbc-mariadb, jdbc-mssql, jdbc-mysql, jdbc-oracle, jdbc-postgresql, keycloak, logging-gelf, micrometer, narayana-jta, reactive-routes, resteasy-reactive, resteasy-reactive-jackson, smallrye-context-propagation, smallrye-health, vertx]
2025-12-25T12:37:18.640170968Z 2025-12-25 12:37:18,639 WARN  [org.keycloak.quarkus.runtime.KeycloakMain] (main) Running the server in development mode. DO NOT use this configuration in production.
minio-hck4w0k4ww8kk4gccw000ggg-123454680959
Only Show Number of Lines
*
100
Refresh
Stream Logs
Include Timestamps

2025-12-25T12:36:42.253213144Z MinIO Object Storage Server
2025-12-25T12:36:42.253256925Z Copyright: 2015-2025 MinIO, Inc.
2025-12-25T12:36:42.253260135Z License: GNU AGPLv3 - https://www.gnu.org/licenses/agpl-3.0.html
2025-12-25T12:36:42.253262635Z Version: RELEASE.2025-09-07T16-13-09Z (go1.24.6 linux/amd64)
2025-12-25T12:36:42.253264615Z 
2025-12-25T12:36:42.253275395Z API: http://10.0.2.3:9000  http://127.0.0.1:9000 
2025-12-25T12:36:42.253277695Z WebUI: http://10.0.2.3:9001 http://127.0.0.1:9001  
2025-12-25T12:36:42.253279675Z 
2025-12-25T12:36:42.253281545Z Docs: https://docs.min.io
2025-12-25T12:36:42.253283525Z WARN: Detected default credentials 'minioadmin:minioadmin', we recommend that you change these values with 'MINIO_ROOT_USER' and 'MINIO_ROOT_PASSWORD' environment variables
control-plane-db-hck4w0k4ww8kk4gccw000ggg-123454626379
Only Show Number of Lines
*
100
Refresh
Stream Logs
Include Timestamps

2025-12-25T12:36:41.898277542Z 
2025-12-25T12:36:41.898316772Z PostgreSQL Database directory appears to contain a database; Skipping initialization
2025-12-25T12:36:41.898320012Z 
2025-12-25T12:36:41.943978373Z 2025-12-25 12:36:41.943 UTC [1] LOG:  starting PostgreSQL 15.15 (Debian 15.15-1.pgdg13+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 14.2.0-19) 14.2.0, 64-bit
2025-12-25T12:36:41.944275256Z 2025-12-25 12:36:41.944 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
2025-12-25T12:36:41.944283526Z 2025-12-25 12:36:41.944 UTC [1] LOG:  listening on IPv6 address "::", port 5432
2025-12-25T12:36:41.945762538Z 2025-12-25 12:36:41.945 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
2025-12-25T12:36:41.950656438Z 2025-12-25 12:36:41.950 UTC [28] LOG:  database system was shut down at 2025-12-25 12:36:38 UTC
2025-12-25T12:36:41.957615437Z 2025-12-25 12:36:41.957 UTC [1] LOG:  database system is ready to accept connections
dashboard-hck4w0k4ww8kk4gccw000ggg-123454656284
Only Show Number of Lines
*
100
Refresh
Stream Logs
Include Timestamps

2025-12-25T12:36:50.380161527Z 
2025-12-25T12:36:50.380194287Z > dashboard@0.1.0 start
2025-12-25T12:36:50.380197739Z > next start
2025-12-25T12:36:50.380199939Z 
2025-12-25T12:36:51.554553380Z ▲ Next.js 16.1.0
2025-12-25T12:36:51.555064054Z - Local:         http://localhost:3000
2025-12-25T12:36:51.557729107Z - Network:       http://10.0.2.7:3000
2025-12-25T12:36:51.557764556Z 
2025-12-25T12:36:51.557769627Z ✓ Starting...
2025-12-25T12:36:52.012275341Z ✓ Ready in 1138ms
api-hck4w0k4ww8kk4gccw000ggg-123454642996
Only Show Number of Lines
*
30000
Refresh
Stream Logs
Include Timestamps

2025-12-25T12:36:50.420792977Z Traceback (most recent call last):
2025-12-25T12:36:50.423030205Z   File "/usr/local/bin/uvicorn", line 8, in <module>
2025-12-25T12:36:50.429245587Z     sys.exit(main())
2025-12-25T12:36:50.429268168Z              ^^^^^^
2025-12-25T12:36:50.429271608Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1485, in __call__
2025-12-25T12:36:50.429274788Z     return self.main(*args, **kwargs)
2025-12-25T12:36:50.429277598Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:36:50.429280348Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1406, in main
2025-12-25T12:36:50.429285178Z     rv = self.invoke(ctx)
2025-12-25T12:36:50.429289948Z          ^^^^^^^^^^^^^^^^
2025-12-25T12:36:50.429293048Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1269, in invoke
2025-12-25T12:36:50.429296338Z     return ctx.invoke(self.callback, **ctx.params)
2025-12-25T12:36:50.429299188Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:36:50.429301948Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 824, in invoke
2025-12-25T12:36:50.429304738Z     return callback(*args, **kwargs)
2025-12-25T12:36:50.429307208Z            ^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:36:50.429310048Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/main.py", line 424, in main
2025-12-25T12:36:50.429313058Z     run(
2025-12-25T12:36:50.429315908Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/main.py", line 594, in run
2025-12-25T12:36:50.429318678Z     server.run()
2025-12-25T12:36:50.429321338Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 67, in run
2025-12-25T12:36:50.429324448Z     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
2025-12-25T12:36:50.429327338Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:36:50.429330168Z   File "/usr/local/lib/python3.12/asyncio/runners.py", line 195, in run
2025-12-25T12:36:50.429332898Z     return runner.run(main)
2025-12-25T12:36:50.429335448Z            ^^^^^^^^^^^^^^^^
2025-12-25T12:36:50.429337908Z   File "/usr/local/lib/python3.12/asyncio/runners.py", line 118, in run
2025-12-25T12:36:50.429340628Z     return self._loop.run_until_complete(task)
2025-12-25T12:36:50.429343348Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:36:50.429345278Z   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
2025-12-25T12:36:50.429347248Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 71, in serve
2025-12-25T12:36:50.429349208Z     await self._serve(sockets)
2025-12-25T12:36:50.429351078Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 78, in _serve
2025-12-25T12:36:50.429366478Z     config.load()
2025-12-25T12:36:50.429368478Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/config.py", line 439, in load
2025-12-25T12:36:50.429370448Z     self.loaded_app = import_from_string(self.app)
2025-12-25T12:36:50.429372308Z                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:36:50.429374178Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/importer.py", line 19, in import_from_string
2025-12-25T12:36:50.429377558Z     module = importlib.import_module(module_str)
2025-12-25T12:36:50.429379488Z              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:36:50.429381428Z   File "/usr/local/lib/python3.12/importlib/__init__.py", line 90, in import_module
2025-12-25T12:36:50.429383408Z     return _bootstrap._gcd_import(name[level:], package, level)
2025-12-25T12:36:50.429385338Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:36:50.429387638Z   File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
2025-12-25T12:36:50.429390178Z   File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
2025-12-25T12:36:50.429392338Z   File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
2025-12-25T12:36:50.429394378Z   File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
2025-12-25T12:36:50.429396368Z   File "<frozen importlib._bootstrap_external>", line 999, in exec_module
2025-12-25T12:36:50.429398398Z   File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
2025-12-25T12:36:50.429400368Z   File "/app/src/main.py", line 19, in <module>
2025-12-25T12:36:50.429402478Z     from api.v1.projects import router as projects_router
2025-12-25T12:36:50.429404388Z   File "/app/src/api/v1/projects.py", line 3, in <module>
2025-12-25T12:36:50.432292333Z     from services.project_service import (
2025-12-25T12:36:50.432452374Z   File "/app/src/services/project_service.py", line 6, in <module>
2025-12-25T12:36:50.434500121Z     from services.secrets_service import generate_project_secrets
2025-12-25T12:36:50.434512851Z   File "/app/src/services/secrets_service.py", line 8, in <module>
2025-12-25T12:36:50.434516221Z     from services.provisioning_local import BASE_PROJECTS_DIR
2025-12-25T12:36:50.434518411Z   File "/app/src/services/provisioning_local.py", line 14, in <module>
2025-12-25T12:36:50.434520731Z     PROJECT_ROOT = Path(__file__).resolve().parents[4]
2025-12-25T12:36:50.434522631Z                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^
2025-12-25T12:36:50.434524551Z   File "/usr/local/lib/python3.12/pathlib.py", line 282, in __getitem__
2025-12-25T12:36:50.437175913Z     raise IndexError(idx)
2025-12-25T12:36:50.437188863Z IndexError: 4
2025-12-25T12:36:53.333745511Z Traceback (most recent call last):
2025-12-25T12:36:53.333841861Z   File "/usr/local/bin/uvicorn", line 8, in <module>
2025-12-25T12:36:53.333919452Z     sys.exit(main())
2025-12-25T12:36:53.334089703Z              ^^^^^^
2025-12-25T12:36:53.334115144Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1485, in __call__
2025-12-25T12:36:53.334405696Z     return self.main(*args, **kwargs)
2025-12-25T12:36:53.334480026Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:36:53.334528367Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1406, in main
2025-12-25T12:36:53.335362774Z     rv = self.invoke(ctx)
2025-12-25T12:36:53.335565465Z          ^^^^^^^^^^^^^^^^
2025-12-25T12:36:53.335662656Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1269, in invoke
2025-12-25T12:36:53.340233774Z     return ctx.invoke(self.callback, **ctx.params)
2025-12-25T12:36:53.340248174Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:36:53.340253584Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 824, in invoke
2025-12-25T12:36:53.340258455Z     return callback(*args, **kwargs)
2025-12-25T12:36:53.340262874Z            ^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:36:53.340267344Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/main.py", line 424, in main
2025-12-25T12:36:53.340271545Z     run(
2025-12-25T12:36:53.340294755Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/main.py", line 594, in run
2025-12-25T12:36:53.340298235Z     server.run()
2025-12-25T12:36:53.340301446Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 67, in run
2025-12-25T12:36:53.340304886Z     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
2025-12-25T12:36:53.340308355Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:36:53.340311656Z   File "/usr/local/lib/python3.12/asyncio/runners.py", line 195, in run
2025-12-25T12:36:53.340315016Z     return runner.run(main)
2025-12-25T12:36:53.340318195Z            ^^^^^^^^^^^^^^^^
2025-12-25T12:36:53.340322195Z   File "/usr/local/lib/python3.12/asyncio/runners.py", line 118, in run
2025-12-25T12:36:53.340326545Z     return self._loop.run_until_complete(task)
2025-12-25T12:36:53.340332726Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:36:53.340339825Z   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
2025-12-25T12:36:53.340344395Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 71, in serve
2025-12-25T12:36:53.340348355Z     await self._serve(sockets)
2025-12-25T12:36:53.340352056Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 78, in _serve
2025-12-25T12:36:53.340369446Z     config.load()
2025-12-25T12:36:53.340371976Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/config.py", line 439, in load
2025-12-25T12:36:53.340374466Z     self.loaded_app = import_from_string(self.app)
2025-12-25T12:36:53.340376846Z                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:36:53.340379286Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/importer.py", line 19, in import_from_string
2025-12-25T12:36:53.340381726Z     module = importlib.import_module(module_str)
2025-12-25T12:36:53.340384056Z              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:36:53.340386435Z   File "/usr/local/lib/python3.12/importlib/__init__.py", line 90, in import_module
2025-12-25T12:36:53.340388915Z     return _bootstrap._gcd_import(name[level:], package, level)
2025-12-25T12:36:53.340391376Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:36:53.340393835Z   File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
2025-12-25T12:36:53.340397155Z   File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
2025-12-25T12:36:53.340400056Z   File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
2025-12-25T12:36:53.340402986Z   File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
2025-12-25T12:36:53.340405926Z   File "<frozen importlib._bootstrap_external>", line 999, in exec_module
2025-12-25T12:36:53.340408826Z   File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
2025-12-25T12:36:53.340410906Z   File "/app/src/main.py", line 19, in <module>
2025-12-25T12:36:53.340412955Z     from api.v1.projects import router as projects_router
2025-12-25T12:36:53.340414896Z   File "/app/src/api/v1/projects.py", line 3, in <module>
2025-12-25T12:36:53.340416937Z     from services.project_service import (
2025-12-25T12:36:53.340418857Z   File "/app/src/services/project_service.py", line 6, in <module>
2025-12-25T12:36:53.340420876Z     from services.secrets_service import generate_project_secrets
2025-12-25T12:36:53.340422867Z   File "/app/src/services/secrets_service.py", line 8, in <module>
2025-12-25T12:36:53.340424897Z     from services.provisioning_local import BASE_PROJECTS_DIR
2025-12-25T12:36:53.340426827Z   File "/app/src/services/provisioning_local.py", line 14, in <module>
2025-12-25T12:36:53.340428857Z     PROJECT_ROOT = Path(__file__).resolve().parents[4]
2025-12-25T12:36:53.340430867Z                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^
2025-12-25T12:36:53.340432796Z   File "/usr/local/lib/python3.12/pathlib.py", line 282, in __getitem__
2025-12-25T12:36:53.340434807Z     raise IndexError(idx)
2025-12-25T12:36:53.340436716Z IndexError: 4
2025-12-25T12:36:55.427498487Z Traceback (most recent call last):
2025-12-25T12:36:55.427687968Z   File "/usr/local/bin/uvicorn", line 8, in <module>
2025-12-25T12:36:55.427697518Z     sys.exit(main())
2025-12-25T12:36:55.427702608Z              ^^^^^^
2025-12-25T12:36:55.427707218Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1485, in __call__
2025-12-25T12:36:55.427987431Z     return self.main(*args, **kwargs)
2025-12-25T12:36:55.427992931Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:36:55.427997711Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1406, in main
2025-12-25T12:36:55.428743357Z     rv = self.invoke(ctx)
2025-12-25T12:36:55.433223235Z          ^^^^^^^^^^^^^^^^
2025-12-25T12:36:55.433242935Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1269, in invoke
2025-12-25T12:36:55.433248205Z     return ctx.invoke(self.callback, **ctx.params)
2025-12-25T12:36:55.433252505Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:36:55.433256905Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 824, in invoke
2025-12-25T12:36:55.433261005Z     return callback(*args, **kwargs)
2025-12-25T12:36:55.433265135Z            ^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:36:55.433268945Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/main.py", line 424, in main
2025-12-25T12:36:55.433273275Z     run(
2025-12-25T12:36:55.433277475Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/main.py", line 594, in run
2025-12-25T12:36:55.433281515Z     server.run()
2025-12-25T12:36:55.433285745Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 67, in run
2025-12-25T12:36:55.433289825Z     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
2025-12-25T12:36:55.433293725Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:36:55.433297595Z   File "/usr/local/lib/python3.12/asyncio/runners.py", line 195, in run
2025-12-25T12:36:55.433301495Z     return runner.run(main)
2025-12-25T12:36:55.438350768Z            ^^^^^^^^^^^^^^^^
2025-12-25T12:36:55.438369408Z   File "/usr/local/lib/python3.12/asyncio/runners.py", line 118, in run
2025-12-25T12:36:55.438383888Z     return self._loop.run_until_complete(task)
2025-12-25T12:36:55.438387778Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:36:55.438391488Z   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
2025-12-25T12:36:55.438395848Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 71, in serve
2025-12-25T12:36:55.441928767Z     await self._serve(sockets)
2025-12-25T12:36:55.441954647Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 78, in _serve
2025-12-25T12:36:55.441969147Z     config.load()
2025-12-25T12:36:55.441972437Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/config.py", line 439, in load
2025-12-25T12:36:55.441975557Z     self.loaded_app = import_from_string(self.app)
2025-12-25T12:36:55.441978517Z                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:36:55.442829235Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/importer.py", line 19, in import_from_string
2025-12-25T12:36:55.442995626Z     module = importlib.import_module(module_str)
2025-12-25T12:36:55.443063517Z              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:36:55.443139997Z   File "/usr/local/lib/python3.12/importlib/__init__.py", line 90, in import_module
2025-12-25T12:36:55.443300658Z     return _bootstrap._gcd_import(name[level:], package, level)
2025-12-25T12:36:55.443498470Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:36:55.443710922Z   File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
2025-12-25T12:36:55.445697109Z   File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
2025-12-25T12:36:55.445712589Z   File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
2025-12-25T12:36:55.445716399Z   File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
2025-12-25T12:36:55.445719449Z   File "<frozen importlib._bootstrap_external>", line 999, in exec_module
2025-12-25T12:36:55.445722329Z   File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
2025-12-25T12:36:55.445725149Z   File "/app/src/main.py", line 19, in <module>
2025-12-25T12:36:55.445728099Z     from api.v1.projects import router as projects_router
2025-12-25T12:36:55.445731189Z   File "/app/src/api/v1/projects.py", line 3, in <module>
2025-12-25T12:36:55.445733869Z     from services.project_service import (
2025-12-25T12:36:55.445749249Z   File "/app/src/services/project_service.py", line 6, in <module>
2025-12-25T12:36:55.445752339Z     from services.secrets_service import generate_project_secrets
2025-12-25T12:36:55.445755049Z   File "/app/src/services/secrets_service.py", line 8, in <module>
2025-12-25T12:36:55.445757919Z     from services.provisioning_local import BASE_PROJECTS_DIR
2025-12-25T12:36:55.446161223Z   File "/app/src/services/provisioning_local.py", line 14, in <module>
2025-12-25T12:36:55.446171292Z     PROJECT_ROOT = Path(__file__).resolve().parents[4]
2025-12-25T12:36:55.446174273Z                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^
2025-12-25T12:36:55.446177103Z   File "/usr/local/lib/python3.12/pathlib.py", line 282, in __getitem__
2025-12-25T12:36:55.446180083Z     raise IndexError(idx)
2025-12-25T12:36:55.446284634Z IndexError: 4
2025-12-25T12:36:57.229657899Z Traceback (most recent call last):
2025-12-25T12:36:57.230282824Z   File "/usr/local/bin/uvicorn", line 8, in <module>
2025-12-25T12:36:57.230489836Z     sys.exit(main())
2025-12-25T12:36:57.230698118Z              ^^^^^^
2025-12-25T12:36:57.230712537Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1485, in __call__
2025-12-25T12:36:57.230978930Z     return self.main(*args, **kwargs)
2025-12-25T12:36:57.233181139Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:36:57.233194548Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1406, in main
2025-12-25T12:36:57.233198918Z     rv = self.invoke(ctx)
2025-12-25T12:36:57.233202398Z          ^^^^^^^^^^^^^^^^
2025-12-25T12:36:57.233217088Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1269, in invoke
2025-12-25T12:36:57.233221558Z     return ctx.invoke(self.callback, **ctx.params)
2025-12-25T12:36:57.233225688Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:36:57.233230029Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 824, in invoke
2025-12-25T12:36:57.233234349Z     return callback(*args, **kwargs)
2025-12-25T12:36:57.233238488Z            ^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:36:57.233242928Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/main.py", line 424, in main
2025-12-25T12:36:57.233247568Z     run(
2025-12-25T12:36:57.233251838Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/main.py", line 594, in run
2025-12-25T12:36:57.233415881Z     server.run()
2025-12-25T12:36:57.233438771Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 67, in run
2025-12-25T12:36:57.233590522Z     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
2025-12-25T12:36:57.233689432Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:36:57.233695742Z   File "/usr/local/lib/python3.12/asyncio/runners.py", line 195, in run
2025-12-25T12:36:57.234177657Z     return runner.run(main)
2025-12-25T12:36:57.234222307Z            ^^^^^^^^^^^^^^^^
2025-12-25T12:36:57.234259327Z   File "/usr/local/lib/python3.12/asyncio/runners.py", line 118, in run
2025-12-25T12:36:57.234386678Z     return self._loop.run_until_complete(task)
2025-12-25T12:36:57.234446419Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:36:57.234490619Z   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
2025-12-25T12:36:57.234670471Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 71, in serve
2025-12-25T12:36:57.234737311Z     await self._serve(sockets)
2025-12-25T12:36:57.235198535Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 78, in _serve
2025-12-25T12:36:57.235759380Z     config.load()
2025-12-25T12:36:57.235813510Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/config.py", line 439, in load
2025-12-25T12:36:57.235818041Z     self.loaded_app = import_from_string(self.app)
2025-12-25T12:36:57.235820241Z                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:36:57.235822230Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/importer.py", line 19, in import_from_string
2025-12-25T12:36:57.235824500Z     module = importlib.import_module(module_str)
2025-12-25T12:36:57.235826410Z              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:36:57.235828350Z   File "/usr/local/lib/python3.12/importlib/__init__.py", line 90, in import_module
2025-12-25T12:36:57.238159920Z     return _bootstrap._gcd_import(name[level:], package, level)
2025-12-25T12:36:57.238171980Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:36:57.238174630Z   File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
2025-12-25T12:36:57.238177290Z   File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
2025-12-25T12:36:57.238179580Z   File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
2025-12-25T12:36:57.238181700Z   File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
2025-12-25T12:36:57.238183690Z   File "<frozen importlib._bootstrap_external>", line 999, in exec_module
2025-12-25T12:36:57.238185770Z   File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
2025-12-25T12:36:57.238187790Z   File "/app/src/main.py", line 19, in <module>
2025-12-25T12:36:57.238189860Z     from api.v1.projects import router as projects_router
2025-12-25T12:36:57.238191800Z   File "/app/src/api/v1/projects.py", line 3, in <module>
2025-12-25T12:36:57.238193890Z     from services.project_service import (
2025-12-25T12:36:57.238195860Z   File "/app/src/services/project_service.py", line 6, in <module>
2025-12-25T12:36:57.238197930Z     from services.secrets_service import generate_project_secrets
2025-12-25T12:36:57.238199920Z   File "/app/src/services/secrets_service.py", line 8, in <module>
2025-12-25T12:36:57.238201920Z     from services.provisioning_local import BASE_PROJECTS_DIR
2025-12-25T12:36:57.238203860Z   File "/app/src/services/provisioning_local.py", line 14, in <module>
2025-12-25T12:36:57.238205860Z     PROJECT_ROOT = Path(__file__).resolve().parents[4]
2025-12-25T12:36:57.238207950Z                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^
2025-12-25T12:36:57.238209900Z   File "/usr/local/lib/python3.12/pathlib.py", line 282, in __getitem__
2025-12-25T12:36:57.238211910Z     raise IndexError(idx)
2025-12-25T12:36:57.238213780Z IndexError: 4
2025-12-25T12:37:00.037155412Z Traceback (most recent call last):
2025-12-25T12:37:00.037299074Z   File "/usr/local/bin/uvicorn", line 8, in <module>
2025-12-25T12:37:00.037522616Z     sys.exit(main())
2025-12-25T12:37:00.037636507Z              ^^^^^^
2025-12-25T12:37:00.037737247Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1485, in __call__
2025-12-25T12:37:00.038165861Z     return self.main(*args, **kwargs)
2025-12-25T12:37:00.038309272Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:00.038392413Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1406, in main
2025-12-25T12:37:00.038756226Z     rv = self.invoke(ctx)
2025-12-25T12:37:00.038849927Z          ^^^^^^^^^^^^^^^^
2025-12-25T12:37:00.040161048Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1269, in invoke
2025-12-25T12:37:00.040174168Z     return ctx.invoke(self.callback, **ctx.params)
2025-12-25T12:37:00.040178748Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:00.040182888Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 824, in invoke
2025-12-25T12:37:00.040187108Z     return callback(*args, **kwargs)
2025-12-25T12:37:00.040191098Z            ^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:00.040194918Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/main.py", line 424, in main
2025-12-25T12:37:00.040199068Z     run(
2025-12-25T12:37:00.040202958Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/main.py", line 594, in run
2025-12-25T12:37:00.040207038Z     server.run()
2025-12-25T12:37:00.040210918Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 67, in run
2025-12-25T12:37:00.040214918Z     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
2025-12-25T12:37:00.040218948Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:00.040222988Z   File "/usr/local/lib/python3.12/asyncio/runners.py", line 195, in run
2025-12-25T12:37:00.040226978Z     return runner.run(main)
2025-12-25T12:37:00.040230858Z            ^^^^^^^^^^^^^^^^
2025-12-25T12:37:00.040234718Z   File "/usr/local/lib/python3.12/asyncio/runners.py", line 118, in run
2025-12-25T12:37:00.040238728Z     return self._loop.run_until_complete(task)
2025-12-25T12:37:00.040242578Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:00.040246438Z   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
2025-12-25T12:37:00.040250418Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 71, in serve
2025-12-25T12:37:00.040397019Z     await self._serve(sockets)
2025-12-25T12:37:00.040511851Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 78, in _serve
2025-12-25T12:37:00.040700042Z     config.load()
2025-12-25T12:37:00.040816413Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/config.py", line 439, in load
2025-12-25T12:37:00.041043005Z     self.loaded_app = import_from_string(self.app)
2025-12-25T12:37:00.041186537Z                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:00.041275177Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/importer.py", line 19, in import_from_string
2025-12-25T12:37:00.041420588Z     module = importlib.import_module(module_str)
2025-12-25T12:37:00.041493119Z              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:00.041599299Z   File "/usr/local/lib/python3.12/importlib/__init__.py", line 90, in import_module
2025-12-25T12:37:00.041753151Z     return _bootstrap._gcd_import(name[level:], package, level)
2025-12-25T12:37:00.042169734Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:00.042180014Z   File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
2025-12-25T12:37:00.042183674Z   File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
2025-12-25T12:37:00.042186454Z   File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
2025-12-25T12:37:00.042189134Z   File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
2025-12-25T12:37:00.042191745Z   File "<frozen importlib._bootstrap_external>", line 999, in exec_module
2025-12-25T12:37:00.042194395Z   File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
2025-12-25T12:37:00.042197005Z   File "/app/src/main.py", line 19, in <module>
2025-12-25T12:37:00.042199635Z     from api.v1.projects import router as projects_router
2025-12-25T12:37:00.042202245Z   File "/app/src/api/v1/projects.py", line 3, in <module>
2025-12-25T12:37:00.042229185Z     from services.project_service import (
2025-12-25T12:37:00.042231845Z   File "/app/src/services/project_service.py", line 6, in <module>
2025-12-25T12:37:00.042361576Z     from services.secrets_service import generate_project_secrets
2025-12-25T12:37:00.042425446Z   File "/app/src/services/secrets_service.py", line 8, in <module>
2025-12-25T12:37:00.042572268Z     from services.provisioning_local import BASE_PROJECTS_DIR
2025-12-25T12:37:00.042691789Z   File "/app/src/services/provisioning_local.py", line 14, in <module>
2025-12-25T12:37:00.042795600Z     PROJECT_ROOT = Path(__file__).resolve().parents[4]
2025-12-25T12:37:00.044150341Z                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^
2025-12-25T12:37:00.044162281Z   File "/usr/local/lib/python3.12/pathlib.py", line 282, in __getitem__
2025-12-25T12:37:00.044165301Z     raise IndexError(idx)
2025-12-25T12:37:00.044167821Z IndexError: 4
2025-12-25T12:37:03.729374660Z Traceback (most recent call last):
2025-12-25T12:37:03.729501311Z   File "/usr/local/bin/uvicorn", line 8, in <module>
2025-12-25T12:37:03.729773744Z     sys.exit(main())
2025-12-25T12:37:03.729900025Z              ^^^^^^
2025-12-25T12:37:03.729977705Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1485, in __call__
2025-12-25T12:37:03.730400369Z     return self.main(*args, **kwargs)
2025-12-25T12:37:03.730532611Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:03.730638852Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1406, in main
2025-12-25T12:37:03.731004684Z     rv = self.invoke(ctx)
2025-12-25T12:37:03.731148345Z          ^^^^^^^^^^^^^^^^
2025-12-25T12:37:03.731219897Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1269, in invoke
2025-12-25T12:37:03.731571019Z     return ctx.invoke(self.callback, **ctx.params)
2025-12-25T12:37:03.731718120Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:03.731798491Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 824, in invoke
2025-12-25T12:37:03.732101954Z     return callback(*args, **kwargs)
2025-12-25T12:37:03.732229915Z            ^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:03.732266105Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/main.py", line 424, in main
2025-12-25T12:37:03.732461916Z     run(
2025-12-25T12:37:03.732523477Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/main.py", line 594, in run
2025-12-25T12:37:03.732782279Z     server.run()
2025-12-25T12:37:03.732887120Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 67, in run
2025-12-25T12:37:03.733118112Z     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
2025-12-25T12:37:03.733254524Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:03.733316004Z   File "/usr/local/lib/python3.12/asyncio/runners.py", line 195, in run
2025-12-25T12:37:03.734175611Z     return runner.run(main)
2025-12-25T12:37:03.734188361Z            ^^^^^^^^^^^^^^^^
2025-12-25T12:37:03.734192921Z   File "/usr/local/lib/python3.12/asyncio/runners.py", line 118, in run
2025-12-25T12:37:03.734197211Z     return self._loop.run_until_complete(task)
2025-12-25T12:37:03.734201141Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:03.734224881Z   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
2025-12-25T12:37:03.734229301Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 71, in serve
2025-12-25T12:37:03.734233571Z     await self._serve(sockets)
2025-12-25T12:37:03.734237731Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 78, in _serve
2025-12-25T12:37:03.734259562Z     config.load()
2025-12-25T12:37:03.734263302Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/config.py", line 439, in load
2025-12-25T12:37:03.734266162Z     self.loaded_app = import_from_string(self.app)
2025-12-25T12:37:03.734268802Z                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:03.734271292Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/importer.py", line 19, in import_from_string
2025-12-25T12:37:03.734390502Z     module = importlib.import_module(module_str)
2025-12-25T12:37:03.734503633Z              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:03.734584354Z   File "/usr/local/lib/python3.12/importlib/__init__.py", line 90, in import_module
2025-12-25T12:37:03.734764496Z     return _bootstrap._gcd_import(name[level:], package, level)
2025-12-25T12:37:03.734892807Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:03.734958697Z   File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
2025-12-25T12:37:03.735027478Z   File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
2025-12-25T12:37:03.735127198Z   File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
2025-12-25T12:37:03.735136099Z   File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
2025-12-25T12:37:03.735139199Z   File "<frozen importlib._bootstrap_external>", line 999, in exec_module
2025-12-25T12:37:03.735142019Z   File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
2025-12-25T12:37:03.735145179Z   File "/app/src/main.py", line 19, in <module>
2025-12-25T12:37:03.735335680Z     from api.v1.projects import router as projects_router
2025-12-25T12:37:03.735434472Z   File "/app/src/api/v1/projects.py", line 3, in <module>
2025-12-25T12:37:03.735583153Z     from services.project_service import (
2025-12-25T12:37:03.736137527Z   File "/app/src/services/project_service.py", line 6, in <module>
2025-12-25T12:37:03.736147207Z     from services.secrets_service import generate_project_secrets
2025-12-25T12:37:03.736149767Z   File "/app/src/services/secrets_service.py", line 8, in <module>
2025-12-25T12:37:03.736151927Z     from services.provisioning_local import BASE_PROJECTS_DIR
2025-12-25T12:37:03.736153927Z   File "/app/src/services/provisioning_local.py", line 14, in <module>
2025-12-25T12:37:03.736169388Z     PROJECT_ROOT = Path(__file__).resolve().parents[4]
2025-12-25T12:37:03.736171408Z                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^
2025-12-25T12:37:03.736173358Z   File "/usr/local/lib/python3.12/pathlib.py", line 282, in __getitem__
2025-12-25T12:37:03.736175568Z     raise IndexError(idx)
2025-12-25T12:37:03.736186538Z IndexError: 4
2025-12-25T12:37:08.587894124Z Traceback (most recent call last):
2025-12-25T12:37:08.588007965Z   File "/usr/local/bin/uvicorn", line 8, in <module>
2025-12-25T12:37:08.588205676Z     sys.exit(main())
2025-12-25T12:37:08.588298597Z              ^^^^^^
2025-12-25T12:37:08.588365617Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1485, in __call__
2025-12-25T12:37:08.588675811Z     return self.main(*args, **kwargs)
2025-12-25T12:37:08.588770981Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:08.588823102Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1406, in main
2025-12-25T12:37:08.589116634Z     rv = self.invoke(ctx)
2025-12-25T12:37:08.589227295Z          ^^^^^^^^^^^^^^^^
2025-12-25T12:37:08.589265106Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1269, in invoke
2025-12-25T12:37:08.589521877Z     return ctx.invoke(self.callback, **ctx.params)
2025-12-25T12:37:08.589615298Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:08.591166821Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 824, in invoke
2025-12-25T12:37:08.591177851Z     return callback(*args, **kwargs)
2025-12-25T12:37:08.591181811Z            ^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:08.591185342Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/main.py", line 424, in main
2025-12-25T12:37:08.591209972Z     run(
2025-12-25T12:37:08.591213702Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/main.py", line 594, in run
2025-12-25T12:37:08.591217092Z     server.run()
2025-12-25T12:37:08.591220322Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 67, in run
2025-12-25T12:37:08.591223702Z     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
2025-12-25T12:37:08.591226992Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:08.591230282Z   File "/usr/local/lib/python3.12/asyncio/runners.py", line 195, in run
2025-12-25T12:37:08.591233562Z     return runner.run(main)
2025-12-25T12:37:08.591236772Z            ^^^^^^^^^^^^^^^^
2025-12-25T12:37:08.591243832Z   File "/usr/local/lib/python3.12/asyncio/runners.py", line 118, in run
2025-12-25T12:37:08.591247192Z     return self._loop.run_until_complete(task)
2025-12-25T12:37:08.591250382Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:08.591253542Z   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
2025-12-25T12:37:08.591256802Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 71, in serve
2025-12-25T12:37:08.591260052Z     await self._serve(sockets)
2025-12-25T12:37:08.591278312Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 78, in _serve
2025-12-25T12:37:08.591281332Z     config.load()
2025-12-25T12:37:08.591283942Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/config.py", line 439, in load
2025-12-25T12:37:08.591286862Z     self.loaded_app = import_from_string(self.app)
2025-12-25T12:37:08.591289462Z                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:08.591292002Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/importer.py", line 19, in import_from_string
2025-12-25T12:37:08.591294682Z     module = importlib.import_module(module_str)
2025-12-25T12:37:08.591297322Z              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:08.591299962Z   File "/usr/local/lib/python3.12/importlib/__init__.py", line 90, in import_module
2025-12-25T12:37:08.591302662Z     return _bootstrap._gcd_import(name[level:], package, level)
2025-12-25T12:37:08.591305402Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:08.591308322Z   File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
2025-12-25T12:37:08.591311192Z   File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
2025-12-25T12:37:08.591313402Z   File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
2025-12-25T12:37:08.591315832Z   File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
2025-12-25T12:37:08.591317842Z   File "<frozen importlib._bootstrap_external>", line 999, in exec_module
2025-12-25T12:37:08.591319972Z   File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
2025-12-25T12:37:08.591321982Z   File "/app/src/main.py", line 19, in <module>
2025-12-25T12:37:08.591324293Z     from api.v1.projects import router as projects_router
2025-12-25T12:37:08.591326253Z   File "/app/src/api/v1/projects.py", line 3, in <module>
2025-12-25T12:37:08.591328313Z     from services.project_service import (
2025-12-25T12:37:08.591330253Z   File "/app/src/services/project_service.py", line 6, in <module>
2025-12-25T12:37:08.591332263Z     from services.secrets_service import generate_project_secrets
2025-12-25T12:37:08.591334263Z   File "/app/src/services/secrets_service.py", line 8, in <module>
2025-12-25T12:37:08.591336273Z     from services.provisioning_local import BASE_PROJECTS_DIR
2025-12-25T12:37:08.591338203Z   File "/app/src/services/provisioning_local.py", line 14, in <module>
2025-12-25T12:37:08.591383693Z     PROJECT_ROOT = Path(__file__).resolve().parents[4]
2025-12-25T12:37:08.591487484Z                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^
2025-12-25T12:37:08.591516754Z   File "/usr/local/lib/python3.12/pathlib.py", line 282, in __getitem__
2025-12-25T12:37:08.591682116Z     raise IndexError(idx)
2025-12-25T12:37:08.591760466Z IndexError: 4
2025-12-25T12:37:16.475062886Z Traceback (most recent call last):
2025-12-25T12:37:16.475127617Z   File "/usr/local/bin/uvicorn", line 8, in <module>
2025-12-25T12:37:16.475241808Z     sys.exit(main())
2025-12-25T12:37:16.475290889Z              ^^^^^^
2025-12-25T12:37:16.475302609Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1485, in __call__
2025-12-25T12:37:16.475646531Z     return self.main(*args, **kwargs)
2025-12-25T12:37:16.475693331Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:16.475767572Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1406, in main
2025-12-25T12:37:16.476413417Z     rv = self.invoke(ctx)
2025-12-25T12:37:16.476466079Z          ^^^^^^^^^^^^^^^^
2025-12-25T12:37:16.476506418Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1269, in invoke
2025-12-25T12:37:16.476836581Z     return ctx.invoke(self.callback, **ctx.params)
2025-12-25T12:37:16.476904202Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:16.476946812Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 824, in invoke
2025-12-25T12:37:16.477266575Z     return callback(*args, **kwargs)
2025-12-25T12:37:16.477407896Z            ^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:16.477423616Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/main.py", line 424, in main
2025-12-25T12:37:16.478274893Z     run(
2025-12-25T12:37:16.478295073Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/main.py", line 594, in run
2025-12-25T12:37:16.478536596Z     server.run()
2025-12-25T12:37:16.478616056Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 67, in run
2025-12-25T12:37:16.479177351Z     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
2025-12-25T12:37:16.479190141Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:16.479195381Z   File "/usr/local/lib/python3.12/asyncio/runners.py", line 195, in run
2025-12-25T12:37:16.479200121Z     return runner.run(main)
2025-12-25T12:37:16.479204591Z            ^^^^^^^^^^^^^^^^
2025-12-25T12:37:16.479209210Z   File "/usr/local/lib/python3.12/asyncio/runners.py", line 118, in run
2025-12-25T12:37:16.479213901Z     return self._loop.run_until_complete(task)
2025-12-25T12:37:16.479218481Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:16.479223041Z   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
2025-12-25T12:37:16.479350412Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 71, in serve
2025-12-25T12:37:16.480290391Z     await self._serve(sockets)
2025-12-25T12:37:16.480323120Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 78, in _serve
2025-12-25T12:37:16.480328210Z     config.load()
2025-12-25T12:37:16.480331050Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/config.py", line 439, in load
2025-12-25T12:37:16.480333881Z     self.loaded_app = import_from_string(self.app)
2025-12-25T12:37:16.480336610Z                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:16.480339511Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/importer.py", line 19, in import_from_string
2025-12-25T12:37:16.480342740Z     module = importlib.import_module(module_str)
2025-12-25T12:37:16.480345290Z              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:16.480347881Z   File "/usr/local/lib/python3.12/importlib/__init__.py", line 90, in import_module
2025-12-25T12:37:16.480350391Z     return _bootstrap._gcd_import(name[level:], package, level)
2025-12-25T12:37:16.480352751Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:16.480355191Z   File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
2025-12-25T12:37:16.480358071Z   File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
2025-12-25T12:37:16.480360671Z   File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
2025-12-25T12:37:16.480363300Z   File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
2025-12-25T12:37:16.480365820Z   File "<frozen importlib._bootstrap_external>", line 999, in exec_module
2025-12-25T12:37:16.480368450Z   File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
2025-12-25T12:37:16.480371231Z   File "/app/src/main.py", line 19, in <module>
2025-12-25T12:37:16.480374041Z     from api.v1.projects import router as projects_router
2025-12-25T12:37:16.480376530Z   File "/app/src/api/v1/projects.py", line 3, in <module>
2025-12-25T12:37:16.480379321Z     from services.project_service import (
2025-12-25T12:37:16.480381980Z   File "/app/src/services/project_service.py", line 6, in <module>
2025-12-25T12:37:16.480384660Z     from services.secrets_service import generate_project_secrets
2025-12-25T12:37:16.480387210Z   File "/app/src/services/secrets_service.py", line 8, in <module>
2025-12-25T12:37:16.480389810Z     from services.provisioning_local import BASE_PROJECTS_DIR
2025-12-25T12:37:16.480392551Z   File "/app/src/services/provisioning_local.py", line 14, in <module>
2025-12-25T12:37:16.480395450Z     PROJECT_ROOT = Path(__file__).resolve().parents[4]
2025-12-25T12:37:16.480398210Z                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^
2025-12-25T12:37:16.480401020Z   File "/usr/local/lib/python3.12/pathlib.py", line 282, in __getitem__
2025-12-25T12:37:16.481521350Z     raise IndexError(idx)
2025-12-25T12:37:16.481725763Z IndexError: 4
2025-12-25T12:37:30.496575920Z Traceback (most recent call last):
2025-12-25T12:37:30.496606251Z   File "/usr/local/bin/uvicorn", line 8, in <module>
2025-12-25T12:37:30.496612162Z     sys.exit(main())
2025-12-25T12:37:30.496688392Z              ^^^^^^
2025-12-25T12:37:30.496694992Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1485, in __call__
2025-12-25T12:37:30.496830883Z     return self.main(*args, **kwargs)
2025-12-25T12:37:30.496839843Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:30.496892403Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1406, in main
2025-12-25T12:37:30.497109485Z     rv = self.invoke(ctx)
2025-12-25T12:37:30.497119005Z          ^^^^^^^^^^^^^^^^
2025-12-25T12:37:30.497123106Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1269, in invoke
2025-12-25T12:37:30.497296147Z     return ctx.invoke(self.callback, **ctx.params)
2025-12-25T12:37:30.497301776Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:30.497305136Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 824, in invoke
2025-12-25T12:37:30.497410198Z     return callback(*args, **kwargs)
2025-12-25T12:37:30.497414888Z            ^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:30.497418158Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/main.py", line 424, in main
2025-12-25T12:37:30.497525709Z     run(
2025-12-25T12:37:30.497531249Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/main.py", line 594, in run
2025-12-25T12:37:30.497638490Z     server.run()
2025-12-25T12:37:30.497691080Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 67, in run
2025-12-25T12:37:30.497782141Z     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
2025-12-25T12:37:30.497816202Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:30.497824282Z   File "/usr/local/lib/python3.12/asyncio/runners.py", line 195, in run
2025-12-25T12:37:30.497888762Z     return runner.run(main)
2025-12-25T12:37:30.497975193Z            ^^^^^^^^^^^^^^^^
2025-12-25T12:37:30.497978902Z   File "/usr/local/lib/python3.12/asyncio/runners.py", line 118, in run
2025-12-25T12:37:30.497982213Z     return self._loop.run_until_complete(task)
2025-12-25T12:37:30.498000693Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:30.498004093Z   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
2025-12-25T12:37:30.498134644Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 71, in serve
2025-12-25T12:37:30.498243495Z     await self._serve(sockets)
2025-12-25T12:37:30.498260415Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 78, in _serve
2025-12-25T12:37:30.498315595Z     config.load()
2025-12-25T12:37:30.498321895Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/config.py", line 439, in load
2025-12-25T12:37:30.498483957Z     self.loaded_app = import_from_string(self.app)
2025-12-25T12:37:30.498589298Z                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:30.498593088Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/importer.py", line 19, in import_from_string
2025-12-25T12:37:30.498595867Z     module = importlib.import_module(module_str)
2025-12-25T12:37:30.498598387Z              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:30.498600968Z   File "/usr/local/lib/python3.12/importlib/__init__.py", line 90, in import_module
2025-12-25T12:37:30.498689909Z     return _bootstrap._gcd_import(name[level:], package, level)
2025-12-25T12:37:30.498767869Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:30.498771469Z   File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
2025-12-25T12:37:30.498773869Z   File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
2025-12-25T12:37:30.498776089Z   File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
2025-12-25T12:37:30.498778149Z   File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
2025-12-25T12:37:30.498780139Z   File "<frozen importlib._bootstrap_external>", line 999, in exec_module
2025-12-25T12:37:30.498782169Z   File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
2025-12-25T12:37:30.498784179Z   File "/app/src/main.py", line 19, in <module>
2025-12-25T12:37:30.498860050Z     from api.v1.projects import router as projects_router
2025-12-25T12:37:30.498864160Z   File "/app/src/api/v1/projects.py", line 3, in <module>
2025-12-25T12:37:30.498938360Z     from services.project_service import (
2025-12-25T12:37:30.498942730Z   File "/app/src/services/project_service.py", line 6, in <module>
2025-12-25T12:37:30.498969731Z     from services.secrets_service import generate_project_secrets
2025-12-25T12:37:30.498972171Z   File "/app/src/services/secrets_service.py", line 8, in <module>
2025-12-25T12:37:30.499049711Z     from services.provisioning_local import BASE_PROJECTS_DIR
2025-12-25T12:37:30.499053341Z   File "/app/src/services/provisioning_local.py", line 14, in <module>
2025-12-25T12:37:30.499163093Z     PROJECT_ROOT = Path(__file__).resolve().parents[4]
2025-12-25T12:37:30.499190683Z                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^
2025-12-25T12:37:30.499193403Z   File "/usr/local/lib/python3.12/pathlib.py", line 282, in __getitem__
2025-12-25T12:37:30.499310924Z     raise IndexError(idx)
2025-12-25T12:37:30.499325284Z IndexError: 4
2025-12-25T12:37:57.040954483Z Traceback (most recent call last):
2025-12-25T12:37:57.041005383Z   File "/usr/local/bin/uvicorn", line 8, in <module>
2025-12-25T12:37:57.041138374Z     sys.exit(main())
2025-12-25T12:37:57.041151114Z              ^^^^^^
2025-12-25T12:37:57.041155544Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1485, in __call__
2025-12-25T12:37:57.041264495Z     return self.main(*args, **kwargs)
2025-12-25T12:37:57.041271215Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:57.041275426Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1406, in main
2025-12-25T12:37:57.041537918Z     rv = self.invoke(ctx)
2025-12-25T12:37:57.041556128Z          ^^^^^^^^^^^^^^^^
2025-12-25T12:37:57.041560268Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1269, in invoke
2025-12-25T12:37:57.041805510Z     return ctx.invoke(self.callback, **ctx.params)
2025-12-25T12:37:57.041814660Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:57.041819250Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 824, in invoke
2025-12-25T12:37:57.041982202Z     return callback(*args, **kwargs)
2025-12-25T12:37:57.041990661Z            ^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:57.042038101Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/main.py", line 424, in main
2025-12-25T12:37:57.042117702Z     run(
2025-12-25T12:37:57.042125053Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/main.py", line 594, in run
2025-12-25T12:37:57.042284244Z     server.run()
2025-12-25T12:37:57.042295324Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 67, in run
2025-12-25T12:37:57.042346134Z     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
2025-12-25T12:37:57.042517806Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:57.042613416Z   File "/usr/local/lib/python3.12/asyncio/runners.py", line 195, in run
2025-12-25T12:37:57.042619007Z     return runner.run(main)
2025-12-25T12:37:57.042622706Z            ^^^^^^^^^^^^^^^^
2025-12-25T12:37:57.042625967Z   File "/usr/local/lib/python3.12/asyncio/runners.py", line 118, in run
2025-12-25T12:37:57.042629706Z     return self._loop.run_until_complete(task)
2025-12-25T12:37:57.042633167Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:57.042636357Z   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
2025-12-25T12:37:57.042735958Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 71, in serve
2025-12-25T12:37:57.042805358Z     await self._serve(sockets)
2025-12-25T12:37:57.042893239Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 78, in _serve
2025-12-25T12:37:57.042897879Z     config.load()
2025-12-25T12:37:57.042912469Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/config.py", line 439, in load
2025-12-25T12:37:57.043012670Z     self.loaded_app = import_from_string(self.app)
2025-12-25T12:37:57.043017660Z                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:57.043020320Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/importer.py", line 19, in import_from_string
2025-12-25T12:37:57.043071420Z     module = importlib.import_module(module_str)
2025-12-25T12:37:57.043145631Z              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:57.043148611Z   File "/usr/local/lib/python3.12/importlib/__init__.py", line 90, in import_module
2025-12-25T12:37:57.043263293Z     return _bootstrap._gcd_import(name[level:], package, level)
2025-12-25T12:37:57.043268662Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:37:57.043270923Z   File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
2025-12-25T12:37:57.043273363Z   File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
2025-12-25T12:37:57.043275582Z   File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
2025-12-25T12:37:57.043278472Z   File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
2025-12-25T12:37:57.043281213Z   File "<frozen importlib._bootstrap_external>", line 999, in exec_module
2025-12-25T12:37:57.043284043Z   File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
2025-12-25T12:37:57.043406264Z   File "/app/src/main.py", line 19, in <module>
2025-12-25T12:37:57.043410304Z     from api.v1.projects import router as projects_router
2025-12-25T12:37:57.043412414Z   File "/app/src/api/v1/projects.py", line 3, in <module>
2025-12-25T12:37:57.043493324Z     from services.project_service import (
2025-12-25T12:37:57.043497724Z   File "/app/src/services/project_service.py", line 6, in <module>
2025-12-25T12:37:57.043571225Z     from services.secrets_service import generate_project_secrets
2025-12-25T12:37:57.043622965Z   File "/app/src/services/secrets_service.py", line 8, in <module>
2025-12-25T12:37:57.043626765Z     from services.provisioning_local import BASE_PROJECTS_DIR
2025-12-25T12:37:57.043629375Z   File "/app/src/services/provisioning_local.py", line 14, in <module>
2025-12-25T12:37:57.043729926Z     PROJECT_ROOT = Path(__file__).resolve().parents[4]
2025-12-25T12:37:57.043735766Z                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^
2025-12-25T12:37:57.043738836Z   File "/usr/local/lib/python3.12/pathlib.py", line 282, in __getitem__
2025-12-25T12:37:57.043813826Z     raise IndexError(idx)
2025-12-25T12:37:57.043826626Z IndexError: 4
2025-12-25T12:38:49.311520986Z Traceback (most recent call last):
2025-12-25T12:38:49.311582247Z   File "/usr/local/bin/uvicorn", line 8, in <module>
2025-12-25T12:38:49.311587837Z     sys.exit(main())
2025-12-25T12:38:49.311664777Z              ^^^^^^
2025-12-25T12:38:49.311700807Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1485, in __call__
2025-12-25T12:38:49.311845628Z     return self.main(*args, **kwargs)
2025-12-25T12:38:49.311851388Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:38:49.311855569Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1406, in main
2025-12-25T12:38:49.312141521Z     rv = self.invoke(ctx)
2025-12-25T12:38:49.312185642Z          ^^^^^^^^^^^^^^^^
2025-12-25T12:38:49.312217102Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1269, in invoke
2025-12-25T12:38:49.312400903Z     return ctx.invoke(self.callback, **ctx.params)
2025-12-25T12:38:49.312446633Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:38:49.312450903Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 824, in invoke
2025-12-25T12:38:49.312623046Z     return callback(*args, **kwargs)
2025-12-25T12:38:49.312628606Z            ^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:38:49.312632616Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/main.py", line 424, in main
2025-12-25T12:38:49.312747137Z     run(
2025-12-25T12:38:49.312752477Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/main.py", line 594, in run
2025-12-25T12:38:49.312893368Z     server.run()
2025-12-25T12:38:49.312898598Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 67, in run
2025-12-25T12:38:49.312922078Z     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
2025-12-25T12:38:49.312984169Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:38:49.312988798Z   File "/usr/local/lib/python3.12/asyncio/runners.py", line 195, in run
2025-12-25T12:38:49.313132130Z     return runner.run(main)
2025-12-25T12:38:49.313138519Z            ^^^^^^^^^^^^^^^^
2025-12-25T12:38:49.313170850Z   File "/usr/local/lib/python3.12/asyncio/runners.py", line 118, in run
2025-12-25T12:38:49.313205611Z     return self._loop.run_until_complete(task)
2025-12-25T12:38:49.313255841Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:38:49.313260171Z   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
2025-12-25T12:38:49.313402312Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 71, in serve
2025-12-25T12:38:49.313481262Z     await self._serve(sockets)
2025-12-25T12:38:49.313501263Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 78, in _serve
2025-12-25T12:38:49.313579453Z     config.load()
2025-12-25T12:38:49.313582393Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/config.py", line 439, in load
2025-12-25T12:38:49.313698864Z     self.loaded_app = import_from_string(self.app)
2025-12-25T12:38:49.313702304Z                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:38:49.313704874Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/importer.py", line 19, in import_from_string
2025-12-25T12:38:49.313830276Z     module = importlib.import_module(module_str)
2025-12-25T12:38:49.313833236Z              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:38:49.313835736Z   File "/usr/local/lib/python3.12/importlib/__init__.py", line 90, in import_module
2025-12-25T12:38:49.313863676Z     return _bootstrap._gcd_import(name[level:], package, level)
2025-12-25T12:38:49.313912296Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:38:49.313915036Z   File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
2025-12-25T12:38:49.313917766Z   File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
2025-12-25T12:38:49.313920496Z   File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
2025-12-25T12:38:49.313923097Z   File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
2025-12-25T12:38:49.313925627Z   File "<frozen importlib._bootstrap_external>", line 999, in exec_module
2025-12-25T12:38:49.313958647Z   File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
2025-12-25T12:38:49.313961357Z   File "/app/src/main.py", line 19, in <module>
2025-12-25T12:38:49.314011757Z     from api.v1.projects import router as projects_router
2025-12-25T12:38:49.314036027Z   File "/app/src/api/v1/projects.py", line 3, in <module>
2025-12-25T12:38:49.314096658Z     from services.project_service import (
2025-12-25T12:38:49.314102448Z   File "/app/src/services/project_service.py", line 6, in <module>
2025-12-25T12:38:49.314215308Z     from services.secrets_service import generate_project_secrets
2025-12-25T12:38:49.314218279Z   File "/app/src/services/secrets_service.py", line 8, in <module>
2025-12-25T12:38:49.314257249Z     from services.provisioning_local import BASE_PROJECTS_DIR
2025-12-25T12:38:49.314259919Z   File "/app/src/services/provisioning_local.py", line 14, in <module>
2025-12-25T12:38:49.314321269Z     PROJECT_ROOT = Path(__file__).resolve().parents[4]
2025-12-25T12:38:49.314374101Z                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^
2025-12-25T12:38:49.314376890Z   File "/usr/local/lib/python3.12/pathlib.py", line 282, in __getitem__
2025-12-25T12:38:49.314461311Z     raise IndexError(idx)
2025-12-25T12:38:49.314464201Z IndexError: 4
2025-12-25T12:39:50.340651149Z Traceback (most recent call last):
2025-12-25T12:39:50.340734001Z   File "/usr/local/bin/uvicorn", line 8, in <module>
2025-12-25T12:39:50.340816260Z     sys.exit(main())
2025-12-25T12:39:50.340932292Z              ^^^^^^
2025-12-25T12:39:50.340938862Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1485, in __call__
2025-12-25T12:39:50.341326935Z     return self.main(*args, **kwargs)
2025-12-25T12:39:50.341465706Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:39:50.341527857Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1406, in main
2025-12-25T12:39:50.343190781Z     rv = self.invoke(ctx)
2025-12-25T12:39:50.343206351Z          ^^^^^^^^^^^^^^^^
2025-12-25T12:39:50.343211371Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1269, in invoke
2025-12-25T12:39:50.343215931Z     return ctx.invoke(self.callback, **ctx.params)
2025-12-25T12:39:50.343220071Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:39:50.343235501Z   File "/usr/local/lib/python3.12/site-packages/click/core.py", line 824, in invoke
2025-12-25T12:39:50.343239781Z     return callback(*args, **kwargs)
2025-12-25T12:39:50.343243791Z            ^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:39:50.343252621Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/main.py", line 424, in main
2025-12-25T12:39:50.343256941Z     run(
2025-12-25T12:39:50.343261431Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/main.py", line 594, in run
2025-12-25T12:39:50.343265581Z     server.run()
2025-12-25T12:39:50.343269641Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 67, in run
2025-12-25T12:39:50.343273971Z     return asyncio_run(self.serve(sockets=sockets), loop_factory=self.config.get_loop_factory())
2025-12-25T12:39:50.343278201Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:39:50.343282551Z   File "/usr/local/lib/python3.12/asyncio/runners.py", line 195, in run
2025-12-25T12:39:50.343286831Z     return runner.run(main)
2025-12-25T12:39:50.343290702Z            ^^^^^^^^^^^^^^^^
2025-12-25T12:39:50.343294391Z   File "/usr/local/lib/python3.12/asyncio/runners.py", line 118, in run
2025-12-25T12:39:50.343298211Z     return self._loop.run_until_complete(task)
2025-12-25T12:39:50.343301931Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:39:50.343305721Z   File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
2025-12-25T12:39:50.343315062Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 71, in serve
2025-12-25T12:39:50.343425892Z     await self._serve(sockets)
2025-12-25T12:39:50.343564304Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 78, in _serve
2025-12-25T12:39:50.343720815Z     config.load()
2025-12-25T12:39:50.343812326Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/config.py", line 439, in load
2025-12-25T12:39:50.344050628Z     self.loaded_app = import_from_string(self.app)
2025-12-25T12:39:50.344178089Z                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:39:50.344257990Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/importer.py", line 19, in import_from_string
2025-12-25T12:39:50.344392311Z     module = importlib.import_module(module_str)
2025-12-25T12:39:50.344511092Z              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:39:50.344610242Z   File "/usr/local/lib/python3.12/importlib/__init__.py", line 90, in import_module
2025-12-25T12:39:50.344765213Z     return _bootstrap._gcd_import(name[level:], package, level)
2025-12-25T12:39:50.344868105Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T12:39:50.344927905Z   File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
2025-12-25T12:39:50.344986546Z   File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
2025-12-25T12:39:50.344989716Z   File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
2025-12-25T12:39:50.344992406Z   File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
2025-12-25T12:39:50.344995046Z   File "<frozen importlib._bootstrap_external>", line 999, in exec_module
2025-12-25T12:39:50.344997616Z   File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
2025-12-25T12:39:50.346162246Z   File "/app/src/main.py", line 19, in <module>
2025-12-25T12:39:50.346188876Z     from api.v1.projects import router as projects_router
2025-12-25T12:39:50.346191806Z   File "/app/src/api/v1/projects.py", line 3, in <module>
2025-12-25T12:39:50.346194096Z     from services.project_service import (
2025-12-25T12:39:50.346196096Z   File "/app/src/services/project_service.py", line 6, in <module>
2025-12-25T12:39:50.346198106Z     from services.secrets_service import generate_project_secrets
2025-12-25T12:39:50.346200076Z   File "/app/src/services/secrets_service.py", line 8, in <module>
2025-12-25T12:39:50.346202086Z     from services.provisioning_local import BASE_PROJECTS_DIR
2025-12-25T12:39:50.346204136Z   File "/app/src/services/provisioning_local.py", line 14, in <module>
2025-12-25T12:39:50.346206186Z     PROJECT_ROOT = Path(__file__).resolve().parents[4]
2025-12-25T12:39:50.346208096Z                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^
2025-12-25T12:39:50.346210006Z   File "/usr/local/lib/python3.12/pathlib.py", line 282, in __getitem__
2025-12-25T12:39:50.346221296Z     raise IndexError(idx)
2025-12-25T12:39:50.346223326Z IndexError: 4