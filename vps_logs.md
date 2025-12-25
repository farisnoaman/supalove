Logs
Server: localhost
keycloak-hck4w0k4ww8kk4gccw000ggg-132202009031
Only Show Number of Lines
*
100
Refresh
Stream Logs
Include Timestamps

2025-12-25T13:24:19.584250432Z Updating the configuration and installing your custom providers, if any. Please wait.
2025-12-25T13:24:34.547212798Z 2025-12-25 13:24:34,544 INFO  [io.quarkus.deployment.QuarkusAugmentor] (main) Quarkus augmentation completed in 10898ms
2025-12-25T13:24:38.624405884Z 2025-12-25 13:24:36,511 INFO  [org.keycloak.quarkus.runtime.hostname.DefaultHostnameProvider] (main) Hostname settings: Base URL: <unset>, Hostname: <request>, Strict HTTPS: false, Path: <request>, Strict BackChannel: false, Admin URL: <unset>, Admin: <request>, Port: -1, Proxied: true
2025-12-25T13:24:39.036889247Z 2025-12-25 13:24:39,036 WARN  [io.quarkus.agroal.runtime.DataSources] (main) Datasource <default> enables XA but transaction recovery is not enabled. Please enable transaction recovery by setting quarkus.transaction-manager.enable-recovery=true, otherwise data may be lost if the application is terminated abruptly
2025-12-25T13:24:39.703050871Z 2025-12-25 13:24:39,702 WARN  [org.infinispan.PERSISTENCE] (keycloak-cache-init) ISPN000554: jboss-marshalling is deprecated and planned for removal
2025-12-25T13:24:39.809380536Z 2025-12-25 13:24:39,809 WARN  [org.infinispan.CONFIG] (keycloak-cache-init) ISPN000569: Unable to persist Infinispan internal caches as no global state enabled
2025-12-25T13:24:39.940657014Z 2025-12-25 13:24:39,940 INFO  [org.infinispan.CONTAINER] (keycloak-cache-init) ISPN000556: Starting user marshaller 'org.infinispan.jboss.marshalling.core.JBossUserMarshaller'
2025-12-25T13:24:40.753287675Z 2025-12-25 13:24:40,752 WARN  [io.quarkus.vertx.http.runtime.VertxHttpRecorder] (main) The X-Forwarded-* and Forwarded headers will be considered when determining the proxy address. This configuration can cause a security issue as clients can forge requests and send a forwarded header that is not overwritten by the proxy. Please consider use one of these headers just to forward the proxy address in requests.
2025-12-25T13:24:40.783907276Z 2025-12-25 13:24:40,783 INFO  [org.keycloak.connections.infinispan.DefaultInfinispanConnectionProviderFactory] (main) Node name: node_264346, Site name: null
2025-12-25T13:24:41.092993449Z 2025-12-25 13:24:41,092 INFO  [org.keycloak.broker.provider.AbstractIdentityProviderMapper] (main) Registering class org.keycloak.broker.provider.mappersync.ConfigSyncEventListener
2025-12-25T13:24:42.192371761Z 2025-12-25 13:24:42,191 INFO  [io.quarkus] (main) Keycloak 23.0.7 on JVM (powered by Quarkus 3.2.10.Final) started in 7.455s. Listening on: http://0.0.0.0:8080
2025-12-25T13:24:42.192668974Z 2025-12-25 13:24:42,192 INFO  [io.quarkus] (main) Profile dev activated. 
2025-12-25T13:24:42.192862376Z 2025-12-25 13:24:42,192 INFO  [io.quarkus] (main) Installed features: [agroal, cdi, hibernate-orm, jdbc-h2, jdbc-mariadb, jdbc-mssql, jdbc-mysql, jdbc-oracle, jdbc-postgresql, keycloak, logging-gelf, micrometer, narayana-jta, reactive-routes, resteasy-reactive, resteasy-reactive-jackson, smallrye-context-propagation, smallrye-health, vertx]
2025-12-25T13:24:42.292490933Z 2025-12-25 13:24:42,292 WARN  [org.keycloak.quarkus.runtime.KeycloakMain] (main) Running the server in development mode. DO NOT use this configuration in production.
minio-hck4w0k4ww8kk4gccw000ggg-132202024876
Only Show Number of Lines
*
100
Refresh
Stream Logs
Include Timestamps

2025-12-25T13:24:12.163744233Z MinIO Object Storage Server
2025-12-25T13:24:12.163803764Z Copyright: 2015-2025 MinIO, Inc.
2025-12-25T13:24:12.163808184Z License: GNU AGPLv3 - https://www.gnu.org/licenses/agpl-3.0.html
2025-12-25T13:24:12.163811184Z Version: RELEASE.2025-09-07T16-13-09Z (go1.24.6 linux/amd64)
2025-12-25T13:24:12.163813644Z 
2025-12-25T13:24:12.163816304Z API: http://10.0.2.4:9000  http://127.0.0.1:9000 
2025-12-25T13:24:12.163819054Z WebUI: http://10.0.2.4:9001 http://127.0.0.1:9001  
2025-12-25T13:24:12.163821024Z 
2025-12-25T13:24:12.163822894Z Docs: https://docs.min.io
2025-12-25T13:24:12.163824944Z WARN: Detected default credentials 'minioadmin:minioadmin', we recommend that you change these values with 'MINIO_ROOT_USER' and 'MINIO_ROOT_PASSWORD' environment variables
control-plane-db-hck4w0k4ww8kk4gccw000ggg-132201958859
Only Show Number of Lines
*
100
Refresh
Stream Logs
Include Timestamps

2025-12-25T13:24:11.491837779Z 
2025-12-25T13:24:11.491877140Z PostgreSQL Database directory appears to contain a database; Skipping initialization
2025-12-25T13:24:11.491880141Z 
2025-12-25T13:24:11.561548514Z 2025-12-25 13:24:11.561 UTC [1] LOG:  starting PostgreSQL 15.15 (Debian 15.15-1.pgdg13+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 14.2.0-19) 14.2.0, 64-bit
2025-12-25T13:24:11.564201976Z 2025-12-25 13:24:11.561 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
2025-12-25T13:24:11.564214656Z 2025-12-25 13:24:11.561 UTC [1] LOG:  listening on IPv6 address "::", port 5432
2025-12-25T13:24:11.564217476Z 2025-12-25 13:24:11.563 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
2025-12-25T13:24:11.585329896Z 2025-12-25 13:24:11.580 UTC [28] LOG:  database system was shut down at 2025-12-25 13:24:10 UTC
2025-12-25T13:24:11.614363333Z 2025-12-25 13:24:11.609 UTC [1] LOG:  database system is ready to accept connections
2025-12-25T13:29:11.673542068Z 2025-12-25 13:29:11.673 UTC [26] LOG:  checkpoint starting: time
2025-12-25T13:29:12.240225176Z 2025-12-25 13:29:12.240 UTC [26] LOG:  checkpoint complete: wrote 8 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.508 s, sync=0.004 s, total=0.567 s; sync files=6, longest=0.003 s, average=0.001 s; distance=0 kB, estimate=0 kB
------------------------
dashboard-hck4w0k4ww8kk4gccw000ggg-132201995907
Only Show Number of Lines
*
100
Refresh
Stream Logs
Include Timestamps

2025-12-25T13:24:19.897957584Z 
2025-12-25T13:24:19.898018944Z > dashboard@0.1.0 start
2025-12-25T13:24:19.898022445Z > next start
2025-12-25T13:24:19.898024695Z 
2025-12-25T13:24:21.085963983Z ▲ Next.js 16.1.0
2025-12-25T13:24:21.091135838Z - Local:         http://localhost:3000
2025-12-25T13:24:21.091167878Z - Network:       http://10.0.2.7:3000
2025-12-25T13:24:21.091172838Z 
2025-12-25T13:24:21.091177268Z ✓ Starting...
2025-12-25T13:24:21.459391064Z ✓ Ready in 1049ms
-----------------------
aapi-hck4w0k4ww8kk4gccw000ggg-133924664772
Only Show Number of Lines
*
1000
Refresh
Stream Logs
Include Timestamps

2025-12-25T13:41:53.492183099Z INFO:     Started server process [1]
2025-12-25T13:41:53.493963593Z INFO:     Waiting for application startup.
2025-12-25T13:41:53.558478622Z INFO:     Application startup complete.
2025-12-25T13:41:53.560322927Z INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
2025-12-25T13:48:00.192902292Z [Provisioning] Using Local Docker provider
2025-12-25T13:48:00.193343295Z [Scheduler] Starting background scheduler...
2025-12-25T13:48:00.193365695Z INFO:     10.0.2.2:46872 - "OPTIONS /api/v1/auth/register HTTP/1.1" 200 OK
2025-12-25T13:48:00.813295418Z INFO:     10.0.2.2:46872 - "POST /api/v1/auth/register HTTP/1.1" 200 OK
2025-12-25T13:48:02.861340194Z INFO:     10.0.2.2:46872 - "OPTIONS /api/v1/orgs HTTP/1.1" 200 OK
2025-12-25T13:48:03.075889420Z INFO:     10.0.2.2:46872 - "GET /api/v1/orgs HTTP/1.1" 200 OK
2025-12-25T13:48:04.901237785Z INFO:     10.0.2.2:46872 - "OPTIONS /api/v1/projects?org_id=858be0f1-ae98-42af-8c36-8dca45d3e58b HTTP/1.1" 200 OK
2025-12-25T13:48:05.115152795Z INFO:     10.0.2.2:46872 - "GET /api/v1/projects?org_id=858be0f1-ae98-42af-8c36-8dca45d3e58b HTTP/1.1" 200 OK
2025-12-25T13:48:23.153104586Z INFO:     10.0.2.2:51464 - "GET /api/v1/orgs HTTP/1.1" 200 OK
2025-12-25T13:48:26.789334647Z INFO:     10.0.2.2:51464 - "OPTIONS /api/v1/projects HTTP/1.1" 200 OK
2025-12-25T13:48:27.007105950Z DEBUG: Loading usage_service from /app/src/services/usage_service.py
2025-12-25T13:48:27.007127830Z DEBUG: usage_service.check_limit called for projects
2025-12-25T13:48:27.007132130Z INFO:     10.0.2.2:51464 - "POST /api/v1/projects HTTP/1.1" 500 Internal Server Error
2025-12-25T13:48:27.014509670Z ERROR:    Exception in ASGI application
2025-12-25T13:48:27.014530610Z Traceback (most recent call last):
2025-12-25T13:48:27.014569100Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/protocols/http/httptools_impl.py", line 416, in run_asgi
2025-12-25T13:48:27.014573581Z     result = await app(  # type: ignore[func-returns-value]
2025-12-25T13:48:27.014577291Z              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:48:27.014580561Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__
2025-12-25T13:48:27.014583881Z     return await self.app(scope, receive, send)
2025-12-25T13:48:27.014587022Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:48:27.014605601Z   File "/usr/local/lib/python3.12/site-packages/fastapi/applications.py", line 1135, in __call__
2025-12-25T13:48:27.014609071Z     await super().__call__(scope, receive, send)
2025-12-25T13:48:27.014612231Z   File "/usr/local/lib/python3.12/site-packages/starlette/applications.py", line 107, in __call__
2025-12-25T13:48:27.014868123Z     await self.middleware_stack(scope, receive, send)
2025-12-25T13:48:27.014877784Z   File "/usr/local/lib/python3.12/site-packages/starlette/middleware/errors.py", line 186, in __call__
2025-12-25T13:48:27.014894964Z     raise exc
2025-12-25T13:48:27.014897824Z   File "/usr/local/lib/python3.12/site-packages/starlette/middleware/errors.py", line 164, in __call__
2025-12-25T13:48:27.014909074Z     await self.app(scope, receive, _send)
2025-12-25T13:48:27.014911694Z   File "/usr/local/lib/python3.12/site-packages/starlette/middleware/base.py", line 191, in __call__
2025-12-25T13:48:27.014914474Z     with recv_stream, send_stream, collapse_excgroups():
2025-12-25T13:48:27.014916984Z                                    ^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:48:27.014919474Z   File "/usr/local/lib/python3.12/contextlib.py", line 158, in __exit__
2025-12-25T13:48:27.014922034Z     self.gen.throw(value)
2025-12-25T13:48:27.014924614Z   File "/usr/local/lib/python3.12/site-packages/starlette/_utils.py", line 85, in collapse_excgroups
2025-12-25T13:48:27.014927214Z     raise exc
2025-12-25T13:48:27.014929614Z   File "/usr/local/lib/python3.12/site-packages/starlette/middleware/base.py", line 193, in __call__
2025-12-25T13:48:27.014932194Z     response = await self.dispatch_func(request, call_next)
2025-12-25T13:48:27.014934794Z                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:48:27.014937344Z   File "/app/src/main.py", line 216, in track_requests
2025-12-25T13:48:27.014939784Z     response = await call_next(request)
2025-12-25T13:48:27.014942204Z                ^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:48:27.014944634Z   File "/usr/local/lib/python3.12/site-packages/starlette/middleware/base.py", line 168, in call_next
2025-12-25T13:48:27.014959114Z     raise app_exc from app_exc.__cause__ or app_exc.__context__
2025-12-25T13:48:27.014963244Z   File "/usr/local/lib/python3.12/site-packages/starlette/middleware/base.py", line 144, in coro
2025-12-25T13:48:27.014965924Z     await self.app(scope, receive_or_disconnect, send_no_error)
2025-12-25T13:48:27.014968464Z   File "/usr/local/lib/python3.12/site-packages/starlette/middleware/cors.py", line 93, in __call__
2025-12-25T13:48:27.014971374Z     await self.simple_response(scope, receive, send, request_headers=headers)
2025-12-25T13:48:27.014973944Z   File "/usr/local/lib/python3.12/site-packages/starlette/middleware/cors.py", line 144, in simple_response
2025-12-25T13:48:27.014976864Z     await self.app(scope, receive, send)
2025-12-25T13:48:27.014979544Z   File "/usr/local/lib/python3.12/site-packages/starlette/middleware/exceptions.py", line 63, in __call__
2025-12-25T13:48:27.014982354Z     await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
2025-12-25T13:48:27.014984994Z   File "/usr/local/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
2025-12-25T13:48:27.014987914Z     raise exc
2025-12-25T13:48:27.014990394Z   File "/usr/local/lib/python3.12/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
2025-12-25T13:48:27.014998384Z     await app(scope, receive, sender)
2025-12-25T13:48:27.015001274Z   File "/usr/local/lib/python3.12/site-packages/fastapi/middleware/asyncexitstack.py", line 18, in __call__
2025-12-25T13:48:27.015004114Z     await self.app(scope, receive, send)
2025-12-25T13:48:27.015006904Z   File "/usr/local/lib/python3.12/site-packages/starlette/routing.py", line 716, in __call__
2025-12-25T13:48:27.015009764Z     await self.middleware_stack(scope, receive, send)
2025-12-25T13:48:27.015012474Z   File "/usr/local/lib/python3.12/site-packages/starlette/routing.py", line 736, in app
2025-12-25T13:48:27.015015294Z     await route.handle(scope, receive, send)
2025-12-25T13:48:27.015018234Z   File "/usr/local/lib/python3.12/site-packages/starlette/routing.py", line 290, in handle
2025-12-25T13:48:27.015021195Z     await self.app(scope, receive, send)
2025-12-25T13:48:27.015023965Z   File "/usr/local/lib/python3.12/site-packages/fastapi/routing.py", line 119, in app
2025-12-25T13:48:27.015026945Z     await wrap_app_handling_exceptions(app, request)(scope, receive, send)
2025-12-25T13:48:27.015029775Z   File "/usr/local/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
2025-12-25T13:48:27.015032625Z     raise exc
2025-12-25T13:48:27.015035355Z   File "/usr/local/lib/python3.12/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
2025-12-25T13:48:27.015038255Z     await app(scope, receive, sender)
2025-12-25T13:48:27.015041205Z   File "/usr/local/lib/python3.12/site-packages/fastapi/routing.py", line 105, in app
2025-12-25T13:48:27.015044245Z     response = await f(request)
2025-12-25T13:48:27.015046885Z                ^^^^^^^^^^^^^^^^
2025-12-25T13:48:27.015050075Z   File "/usr/local/lib/python3.12/site-packages/fastapi/routing.py", line 426, in app
2025-12-25T13:48:27.015052935Z     raw_response = await run_endpoint_function(
2025-12-25T13:48:27.015055695Z                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:48:27.015058485Z   File "/usr/local/lib/python3.12/site-packages/fastapi/routing.py", line 314, in run_endpoint_function
2025-12-25T13:48:27.015061355Z     return await run_in_threadpool(dependant.call, **values)
2025-12-25T13:48:27.015064135Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:48:27.015066865Z   File "/usr/local/lib/python3.12/site-packages/starlette/concurrency.py", line 32, in run_in_threadpool
2025-12-25T13:48:27.015069735Z     return await anyio.to_thread.run_sync(func)
2025-12-25T13:48:27.015088145Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:48:27.015093505Z   File "/usr/local/lib/python3.12/site-packages/anyio/to_thread.py", line 61, in run_sync
2025-12-25T13:48:27.015096215Z     return await get_async_backend().run_sync_in_worker_thread(
2025-12-25T13:48:27.015098795Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:48:27.015106415Z   File "/usr/local/lib/python3.12/site-packages/anyio/_backends/_asyncio.py", line 2525, in run_sync_in_worker_thread
2025-12-25T13:48:27.015109045Z     return await future
2025-12-25T13:48:27.015111515Z            ^^^^^^^^^^^^
2025-12-25T13:48:27.015113855Z   File "/usr/local/lib/python3.12/site-packages/anyio/_backends/_asyncio.py", line 986, in run
2025-12-25T13:48:27.015116565Z     result = context.run(func, *args)
2025-12-25T13:48:27.015119165Z              ^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:48:27.015121515Z   File "/app/src/api/v1/projects.py", line 97, in create
2025-12-25T13:48:27.015124375Z     return create_project(db, custom_domain=custom_domain, name=name, org_id=target_org_id)
2025-12-25T13:48:27.015127045Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:48:27.015129435Z   File "/app/src/services/project_service.py", line 108, in create_project
2025-12-25T13:48:27.015131985Z     raise e
2025-12-25T13:48:27.015134295Z   File "/app/src/services/project_service.py", line 87, in create_project
2025-12-25T13:48:27.015136845Z     provision_output = provision_project(project_id, secrets, custom_domain=custom_domain)
2025-12-25T13:48:27.015139585Z                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:48:27.015142405Z   File "/app/src/services/provisioning_service.py", line 36, in provision_project
2025-12-25T13:48:27.015145115Z     return _provider.provision(project_id, secrets, custom_domain=custom_domain)
2025-12-25T13:48:27.015147555Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:48:27.015150605Z   File "/app/src/services/provisioning_local.py", line 50, in provision
2025-12-25T13:48:27.015153115Z     raise FileNotFoundError(f"Project template not found at {template_dir}")
2025-12-25T13:48:27.015155625Z FileNotFoundError: Project template not found at /app/data-plane/project-template