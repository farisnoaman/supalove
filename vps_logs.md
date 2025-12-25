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
api-hck4w0k4ww8kk4gccw000ggg-132201978563
Only Show Number of Lines
*
2000
Refresh
Stream Logs
Include Timestamps

2025-12-25T13:24:22.903401194Z INFO:     Started server process [1]
2025-12-25T13:24:22.903494714Z INFO:     Waiting for application startup.
2025-12-25T13:24:22.936575336Z INFO:     Application startup complete.
2025-12-25T13:24:22.938688094Z INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
2025-12-25T13:26:34.743515378Z [Provisioning] Using Local Docker provider
2025-12-25T13:26:34.743583718Z [Scheduler] Starting background scheduler...
2025-12-25T13:26:34.743590258Z INFO:     10.0.2.2:33246 - "OPTIONS /api/v1/auth/register HTTP/1.1" 200 OK
2025-12-25T13:26:34.989973295Z (trapped) error reading bcrypt version
2025-12-25T13:26:34.990001026Z Traceback (most recent call last):
2025-12-25T13:26:34.990006106Z   File "/usr/local/lib/python3.12/site-packages/passlib/handlers/bcrypt.py", line 620, in _load_backend_mixin
2025-12-25T13:26:34.990011056Z     version = _bcrypt.__about__.__version__
2025-12-25T13:26:34.990015556Z               ^^^^^^^^^^^^^^^^^
2025-12-25T13:26:34.990020096Z AttributeError: module 'bcrypt' has no attribute '__about__'
2025-12-25T13:26:34.998059504Z INFO:     10.0.2.2:33246 - "POST /api/v1/auth/register HTTP/1.1" 500 Internal Server Error
2025-12-25T13:26:35.010663621Z ERROR:    Exception in ASGI application
2025-12-25T13:26:35.010688741Z Traceback (most recent call last):
2025-12-25T13:26:35.010692741Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/protocols/http/httptools_impl.py", line 416, in run_asgi
2025-12-25T13:26:35.010696362Z     result = await app(  # type: ignore[func-returns-value]
2025-12-25T13:26:35.010699602Z              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:26:35.010702941Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__
2025-12-25T13:26:35.010706301Z     return await self.app(scope, receive, send)
2025-12-25T13:26:35.010709432Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:26:35.010712581Z   File "/usr/local/lib/python3.12/site-packages/fastapi/applications.py", line 1135, in __call__
2025-12-25T13:26:35.010715872Z     await super().__call__(scope, receive, send)
2025-12-25T13:26:35.010719012Z   File "/usr/local/lib/python3.12/site-packages/starlette/applications.py", line 107, in __call__
2025-12-25T13:26:35.010819793Z     await self.middleware_stack(scope, receive, send)
2025-12-25T13:26:35.010826803Z   File "/usr/local/lib/python3.12/site-packages/starlette/middleware/errors.py", line 186, in __call__
2025-12-25T13:26:35.010830503Z     raise exc
2025-12-25T13:26:35.010833743Z   File "/usr/local/lib/python3.12/site-packages/starlette/middleware/errors.py", line 164, in __call__
2025-12-25T13:26:35.010837033Z     await self.app(scope, receive, _send)
2025-12-25T13:26:35.010840183Z   File "/usr/local/lib/python3.12/site-packages/starlette/middleware/base.py", line 191, in __call__
2025-12-25T13:26:35.010853133Z     with recv_stream, send_stream, collapse_excgroups():
2025-12-25T13:26:35.010855233Z                                    ^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:26:35.010857183Z   File "/usr/local/lib/python3.12/contextlib.py", line 158, in __exit__
2025-12-25T13:26:35.010859213Z     self.gen.throw(value)
2025-12-25T13:26:35.010861073Z   File "/usr/local/lib/python3.12/site-packages/starlette/_utils.py", line 85, in collapse_excgroups
2025-12-25T13:26:35.010863113Z     raise exc
2025-12-25T13:26:35.010865123Z   File "/usr/local/lib/python3.12/site-packages/starlette/middleware/base.py", line 193, in __call__
2025-12-25T13:26:35.010867113Z     response = await self.dispatch_func(request, call_next)
2025-12-25T13:26:35.010869023Z                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:26:35.010870923Z   File "/app/src/main.py", line 216, in track_requests
2025-12-25T13:26:35.010872833Z     response = await call_next(request)
2025-12-25T13:26:35.010874693Z                ^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:26:35.010876573Z   File "/usr/local/lib/python3.12/site-packages/starlette/middleware/base.py", line 168, in call_next
2025-12-25T13:26:35.010878573Z     raise app_exc from app_exc.__cause__ or app_exc.__context__
2025-12-25T13:26:35.010881983Z   File "/usr/local/lib/python3.12/site-packages/starlette/middleware/base.py", line 144, in coro
2025-12-25T13:26:35.010884033Z     await self.app(scope, receive_or_disconnect, send_no_error)
2025-12-25T13:26:35.010885953Z   File "/usr/local/lib/python3.12/site-packages/starlette/middleware/cors.py", line 93, in __call__
2025-12-25T13:26:35.010887933Z     await self.simple_response(scope, receive, send, request_headers=headers)
2025-12-25T13:26:35.010889863Z   File "/usr/local/lib/python3.12/site-packages/starlette/middleware/cors.py", line 144, in simple_response
2025-12-25T13:26:35.010891843Z     await self.app(scope, receive, send)
2025-12-25T13:26:35.010893713Z   File "/usr/local/lib/python3.12/site-packages/starlette/middleware/exceptions.py", line 63, in __call__
2025-12-25T13:26:35.010895723Z     await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
2025-12-25T13:26:35.010897633Z   File "/usr/local/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
2025-12-25T13:26:35.010899623Z     raise exc
2025-12-25T13:26:35.010901463Z   File "/usr/local/lib/python3.12/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
2025-12-25T13:26:35.010903463Z     await app(scope, receive, sender)
2025-12-25T13:26:35.010905323Z   File "/usr/local/lib/python3.12/site-packages/fastapi/middleware/asyncexitstack.py", line 18, in __call__
2025-12-25T13:26:35.010907703Z     await self.app(scope, receive, send)
2025-12-25T13:26:35.010910353Z   File "/usr/local/lib/python3.12/site-packages/starlette/routing.py", line 716, in __call__
2025-12-25T13:26:35.010917723Z     await self.middleware_stack(scope, receive, send)
2025-12-25T13:26:35.010920493Z   File "/usr/local/lib/python3.12/site-packages/starlette/routing.py", line 736, in app
2025-12-25T13:26:35.010923433Z     await route.handle(scope, receive, send)
2025-12-25T13:26:35.010926103Z   File "/usr/local/lib/python3.12/site-packages/starlette/routing.py", line 290, in handle
2025-12-25T13:26:35.010929003Z     await self.app(scope, receive, send)
2025-12-25T13:26:35.010931643Z   File "/usr/local/lib/python3.12/site-packages/fastapi/routing.py", line 119, in app
2025-12-25T13:26:35.010934313Z     await wrap_app_handling_exceptions(app, request)(scope, receive, send)
2025-12-25T13:26:35.010936903Z   File "/usr/local/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
2025-12-25T13:26:35.010950744Z     raise exc
2025-12-25T13:26:35.010953324Z   File "/usr/local/lib/python3.12/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
2025-12-25T13:26:35.010956154Z     await app(scope, receive, sender)
2025-12-25T13:26:35.010958094Z   File "/usr/local/lib/python3.12/site-packages/fastapi/routing.py", line 105, in app
2025-12-25T13:26:35.010960124Z     response = await f(request)
2025-12-25T13:26:35.010962024Z                ^^^^^^^^^^^^^^^^
2025-12-25T13:26:35.010964254Z   File "/usr/local/lib/python3.12/site-packages/fastapi/routing.py", line 426, in app
2025-12-25T13:26:35.010966244Z     raw_response = await run_endpoint_function(
2025-12-25T13:26:35.010968214Z                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:26:35.010970124Z   File "/usr/local/lib/python3.12/site-packages/fastapi/routing.py", line 314, in run_endpoint_function
2025-12-25T13:26:35.010972104Z     return await run_in_threadpool(dependant.call, **values)
2025-12-25T13:26:35.010974004Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:26:35.010975914Z   File "/usr/local/lib/python3.12/site-packages/starlette/concurrency.py", line 32, in run_in_threadpool
2025-12-25T13:26:35.010977894Z     return await anyio.to_thread.run_sync(func)
2025-12-25T13:26:35.010979784Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:26:35.010982084Z   File "/usr/local/lib/python3.12/site-packages/anyio/to_thread.py", line 61, in run_sync
2025-12-25T13:26:35.010984504Z     return await get_async_backend().run_sync_in_worker_thread(
2025-12-25T13:26:35.010986414Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:26:35.010988324Z   File "/usr/local/lib/python3.12/site-packages/anyio/_backends/_asyncio.py", line 2525, in run_sync_in_worker_thread
2025-12-25T13:26:35.010990344Z     return await future
2025-12-25T13:26:35.010992184Z            ^^^^^^^^^^^^
2025-12-25T13:26:35.010994064Z   File "/usr/local/lib/python3.12/site-packages/anyio/_backends/_asyncio.py", line 986, in run
2025-12-25T13:26:35.011002804Z     result = context.run(func, *args)
2025-12-25T13:26:35.011004804Z              ^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:26:35.011006694Z   File "/app/src/api/v1/auth.py", line 52, in register
2025-12-25T13:26:35.011008644Z     hashed_password = AuthService.get_password_hash(user_in.password)
2025-12-25T13:26:35.011010584Z                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:26:35.011012524Z   File "/app/src/services/auth_service.py", line 21, in get_password_hash
2025-12-25T13:26:35.011014474Z     return pwd_context.hash(password)
2025-12-25T13:26:35.011016324Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:26:35.011018174Z   File "/usr/local/lib/python3.12/site-packages/passlib/context.py", line 2258, in hash
2025-12-25T13:26:35.011020134Z     return record.hash(secret, **kwds)
2025-12-25T13:26:35.011022014Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:26:35.011024834Z   File "/usr/local/lib/python3.12/site-packages/passlib/utils/handlers.py", line 779, in hash
2025-12-25T13:26:35.011027654Z     self.checksum = self._calc_checksum(secret)
2025-12-25T13:26:35.011030404Z                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:26:35.011033074Z   File "/usr/local/lib/python3.12/site-packages/passlib/handlers/bcrypt.py", line 591, in _calc_checksum
2025-12-25T13:26:35.011035844Z     self._stub_requires_backend()
2025-12-25T13:26:35.011039104Z   File "/usr/local/lib/python3.12/site-packages/passlib/utils/handlers.py", line 2254, in _stub_requires_backend
2025-12-25T13:26:35.011041794Z     cls.set_backend()
2025-12-25T13:26:35.011043734Z   File "/usr/local/lib/python3.12/site-packages/passlib/utils/handlers.py", line 2156, in set_backend
2025-12-25T13:26:35.011045774Z     return owner.set_backend(name, dryrun=dryrun)
2025-12-25T13:26:35.011047754Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:26:35.011049664Z   File "/usr/local/lib/python3.12/site-packages/passlib/utils/handlers.py", line 2163, in set_backend
2025-12-25T13:26:35.011051624Z     return cls.set_backend(name, dryrun=dryrun)
2025-12-25T13:26:35.011053494Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:26:35.011055394Z   File "/usr/local/lib/python3.12/site-packages/passlib/utils/handlers.py", line 2188, in set_backend
2025-12-25T13:26:35.011057364Z     cls._set_backend(name, dryrun)
2025-12-25T13:26:35.011059274Z   File "/usr/local/lib/python3.12/site-packages/passlib/utils/handlers.py", line 2311, in _set_backend
2025-12-25T13:26:35.011061264Z     super(SubclassBackendMixin, cls)._set_backend(name, dryrun)
2025-12-25T13:26:35.011063184Z   File "/usr/local/lib/python3.12/site-packages/passlib/utils/handlers.py", line 2224, in _set_backend
2025-12-25T13:26:35.011065164Z     ok = loader(**kwds)
2025-12-25T13:26:35.011066994Z          ^^^^^^^^^^^^^^
2025-12-25T13:26:35.011082984Z   File "/usr/local/lib/python3.12/site-packages/passlib/handlers/bcrypt.py", line 626, in _load_backend_mixin
2025-12-25T13:26:35.011087225Z     return mixin_cls._finalize_backend_mixin(name, dryrun)
2025-12-25T13:26:35.011089225Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:26:35.011091155Z   File "/usr/local/lib/python3.12/site-packages/passlib/handlers/bcrypt.py", line 421, in _finalize_backend_mixin
2025-12-25T13:26:35.011093255Z     if detect_wrap_bug(IDENT_2A):
2025-12-25T13:26:35.011095125Z        ^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:26:35.011096985Z   File "/usr/local/lib/python3.12/site-packages/passlib/handlers/bcrypt.py", line 380, in detect_wrap_bug
2025-12-25T13:26:35.011098955Z     if verify(secret, bug_hash):
2025-12-25T13:26:35.011100815Z        ^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:26:35.011102685Z   File "/usr/local/lib/python3.12/site-packages/passlib/utils/handlers.py", line 792, in verify
2025-12-25T13:26:35.011104655Z     return consteq(self._calc_checksum(secret), chk)
2025-12-25T13:26:35.011106595Z                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:26:35.011108525Z   File "/usr/local/lib/python3.12/site-packages/passlib/handlers/bcrypt.py", line 655, in _calc_checksum
2025-12-25T13:26:35.011110505Z     hash = _bcrypt.hashpw(secret, config)
2025-12-25T13:26:35.011112375Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:26:35.011114275Z ValueError: password cannot be longer than 72 bytes, truncate manually if necessary (e.g. my_password[:72])
2025-12-25T13:27:08.284763915Z INFO:     10.0.2.2:38000 - "OPTIONS /api/v1/auth/register HTTP/1.1" 200 OK
2025-12-25T13:27:08.537153962Z (trapped) error reading bcrypt version
2025-12-25T13:27:08.537181593Z Traceback (most recent call last):
2025-12-25T13:27:08.537185962Z   File "/usr/local/lib/python3.12/site-packages/passlib/handlers/bcrypt.py", line 620, in _load_backend_mixin
2025-12-25T13:27:08.537189602Z     version = _bcrypt.__about__.__version__
2025-12-25T13:27:08.537193012Z               ^^^^^^^^^^^^^^^^^
2025-12-25T13:27:08.537196193Z AttributeError: module 'bcrypt' has no attribute '__about__'
2025-12-25T13:27:08.543446806Z INFO:     10.0.2.2:38000 - "POST /api/v1/auth/register HTTP/1.1" 500 Internal Server Error
2025-12-25T13:27:08.545921327Z ERROR:    Exception in ASGI application
2025-12-25T13:27:08.545960298Z Traceback (most recent call last):
2025-12-25T13:27:08.545964548Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/protocols/http/httptools_impl.py", line 416, in run_asgi
2025-12-25T13:27:08.545968648Z     result = await app(  # type: ignore[func-returns-value]
2025-12-25T13:27:08.545971978Z              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:27:08.545975278Z   File "/usr/local/lib/python3.12/site-packages/uvicorn/middleware/proxy_headers.py", line 60, in __call__
2025-12-25T13:27:08.545986338Z     return await self.app(scope, receive, send)
2025-12-25T13:27:08.545988718Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:27:08.545990658Z   File "/usr/local/lib/python3.12/site-packages/fastapi/applications.py", line 1135, in __call__
2025-12-25T13:27:08.545992668Z     await super().__call__(scope, receive, send)
2025-12-25T13:27:08.545994558Z   File "/usr/local/lib/python3.12/site-packages/starlette/applications.py", line 107, in __call__
2025-12-25T13:27:08.545996668Z     await self.middleware_stack(scope, receive, send)
2025-12-25T13:27:08.545998578Z   File "/usr/local/lib/python3.12/site-packages/starlette/middleware/errors.py", line 186, in __call__
2025-12-25T13:27:08.546000598Z     raise exc
2025-12-25T13:27:08.546002478Z   File "/usr/local/lib/python3.12/site-packages/starlette/middleware/errors.py", line 164, in __call__
2025-12-25T13:27:08.546004478Z     await self.app(scope, receive, _send)
2025-12-25T13:27:08.546006408Z   File "/usr/local/lib/python3.12/site-packages/starlette/middleware/base.py", line 191, in __call__
2025-12-25T13:27:08.546008788Z     with recv_stream, send_stream, collapse_excgroups():
2025-12-25T13:27:08.546010698Z                                    ^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:27:08.546012638Z   File "/usr/local/lib/python3.12/contextlib.py", line 158, in __exit__
2025-12-25T13:27:08.546014608Z     self.gen.throw(value)
2025-12-25T13:27:08.546016488Z   File "/usr/local/lib/python3.12/site-packages/starlette/_utils.py", line 85, in collapse_excgroups
2025-12-25T13:27:08.546104099Z     raise exc
2025-12-25T13:27:08.546108729Z   File "/usr/local/lib/python3.12/site-packages/starlette/middleware/base.py", line 193, in __call__
2025-12-25T13:27:08.546110899Z     response = await self.dispatch_func(request, call_next)
2025-12-25T13:27:08.546112859Z                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:27:08.546115309Z   File "/app/src/main.py", line 216, in track_requests
2025-12-25T13:27:08.546117379Z     response = await call_next(request)
2025-12-25T13:27:08.546119269Z                ^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:27:08.546121299Z   File "/usr/local/lib/python3.12/site-packages/starlette/middleware/base.py", line 168, in call_next
2025-12-25T13:27:08.546123349Z     raise app_exc from app_exc.__cause__ or app_exc.__context__
2025-12-25T13:27:08.546126419Z   File "/usr/local/lib/python3.12/site-packages/starlette/middleware/base.py", line 144, in coro
2025-12-25T13:27:08.546128489Z     await self.app(scope, receive_or_disconnect, send_no_error)
2025-12-25T13:27:08.546130459Z   File "/usr/local/lib/python3.12/site-packages/starlette/middleware/cors.py", line 93, in __call__
2025-12-25T13:27:08.546132519Z     await self.simple_response(scope, receive, send, request_headers=headers)
2025-12-25T13:27:08.546134529Z   File "/usr/local/lib/python3.12/site-packages/starlette/middleware/cors.py", line 144, in simple_response
2025-12-25T13:27:08.546141459Z     await self.app(scope, receive, send)
2025-12-25T13:27:08.546143479Z   File "/usr/local/lib/python3.12/site-packages/starlette/middleware/exceptions.py", line 63, in __call__
2025-12-25T13:27:08.546145499Z     await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
2025-12-25T13:27:08.546147459Z   File "/usr/local/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
2025-12-25T13:27:08.546149459Z     raise exc
2025-12-25T13:27:08.546151289Z   File "/usr/local/lib/python3.12/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
2025-12-25T13:27:08.546153359Z     await app(scope, receive, sender)
2025-12-25T13:27:08.546155279Z   File "/usr/local/lib/python3.12/site-packages/fastapi/middleware/asyncexitstack.py", line 18, in __call__
2025-12-25T13:27:08.546157269Z     await self.app(scope, receive, send)
2025-12-25T13:27:08.546159149Z   File "/usr/local/lib/python3.12/site-packages/starlette/routing.py", line 716, in __call__
2025-12-25T13:27:08.546161209Z     await self.middleware_stack(scope, receive, send)
2025-12-25T13:27:08.546163089Z   File "/usr/local/lib/python3.12/site-packages/starlette/routing.py", line 736, in app
2025-12-25T13:27:08.546173300Z     await route.handle(scope, receive, send)
2025-12-25T13:27:08.546175309Z   File "/usr/local/lib/python3.12/site-packages/starlette/routing.py", line 290, in handle
2025-12-25T13:27:08.546177329Z     await self.app(scope, receive, send)
2025-12-25T13:27:08.546179260Z   File "/usr/local/lib/python3.12/site-packages/fastapi/routing.py", line 119, in app
2025-12-25T13:27:08.546181229Z     await wrap_app_handling_exceptions(app, request)(scope, receive, send)
2025-12-25T13:27:08.546183159Z   File "/usr/local/lib/python3.12/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
2025-12-25T13:27:08.546185119Z     raise exc
2025-12-25T13:27:08.546186949Z   File "/usr/local/lib/python3.12/site-packages/starlette/_exception_handler.py", line 42, in wrapped_app
2025-12-25T13:27:08.546188909Z     await app(scope, receive, sender)
2025-12-25T13:27:08.546190769Z   File "/usr/local/lib/python3.12/site-packages/fastapi/routing.py", line 105, in app
2025-12-25T13:27:08.546192740Z     response = await f(request)
2025-12-25T13:27:08.546194639Z                ^^^^^^^^^^^^^^^^
2025-12-25T13:27:08.546196759Z   File "/usr/local/lib/python3.12/site-packages/fastapi/routing.py", line 426, in app
2025-12-25T13:27:08.546198719Z     raw_response = await run_endpoint_function(
2025-12-25T13:27:08.546200639Z                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:27:08.546202519Z   File "/usr/local/lib/python3.12/site-packages/fastapi/routing.py", line 314, in run_endpoint_function
2025-12-25T13:27:08.546204500Z     return await run_in_threadpool(dependant.call, **values)
2025-12-25T13:27:08.546210029Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:27:08.546212049Z   File "/usr/local/lib/python3.12/site-packages/starlette/concurrency.py", line 32, in run_in_threadpool
2025-12-25T13:27:08.546214109Z     return await anyio.to_thread.run_sync(func)
2025-12-25T13:27:08.546215989Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:27:08.546217900Z   File "/usr/local/lib/python3.12/site-packages/anyio/to_thread.py", line 61, in run_sync
2025-12-25T13:27:08.546219879Z     return await get_async_backend().run_sync_in_worker_thread(
2025-12-25T13:27:08.546221919Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:27:08.546223839Z   File "/usr/local/lib/python3.12/site-packages/anyio/_backends/_asyncio.py", line 2525, in run_sync_in_worker_thread
2025-12-25T13:27:08.546225869Z     return await future
2025-12-25T13:27:08.546227719Z            ^^^^^^^^^^^^
2025-12-25T13:27:08.546229629Z   File "/usr/local/lib/python3.12/site-packages/anyio/_backends/_asyncio.py", line 986, in run
2025-12-25T13:27:08.546231620Z     result = context.run(func, *args)
2025-12-25T13:27:08.546233519Z              ^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:27:08.546235389Z   File "/app/src/api/v1/auth.py", line 52, in register
2025-12-25T13:27:08.546237341Z     hashed_password = AuthService.get_password_hash(user_in.password)
2025-12-25T13:27:08.546239280Z                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:27:08.546241250Z   File "/app/src/services/auth_service.py", line 21, in get_password_hash
2025-12-25T13:27:08.546243200Z     return pwd_context.hash(password)
2025-12-25T13:27:08.546245101Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:27:08.546247030Z   File "/usr/local/lib/python3.12/site-packages/passlib/context.py", line 2258, in hash
2025-12-25T13:27:08.546248990Z     return record.hash(secret, **kwds)
2025-12-25T13:27:08.546250861Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:27:08.546252730Z   File "/usr/local/lib/python3.12/site-packages/passlib/utils/handlers.py", line 779, in hash
2025-12-25T13:27:08.546254701Z     self.checksum = self._calc_checksum(secret)
2025-12-25T13:27:08.546256581Z                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:27:08.546258490Z   File "/usr/local/lib/python3.12/site-packages/passlib/handlers/bcrypt.py", line 591, in _calc_checksum
2025-12-25T13:27:08.546260520Z     self._stub_requires_backend()
2025-12-25T13:27:08.546262730Z   File "/usr/local/lib/python3.12/site-packages/passlib/utils/handlers.py", line 2254, in _stub_requires_backend
2025-12-25T13:27:08.546264840Z     cls.set_backend()
2025-12-25T13:27:08.546266730Z   File "/usr/local/lib/python3.12/site-packages/passlib/utils/handlers.py", line 2156, in set_backend
2025-12-25T13:27:08.546268720Z     return owner.set_backend(name, dryrun=dryrun)
2025-12-25T13:27:08.546273901Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:27:08.546275890Z   File "/usr/local/lib/python3.12/site-packages/passlib/utils/handlers.py", line 2163, in set_backend
2025-12-25T13:27:08.546277880Z     return cls.set_backend(name, dryrun=dryrun)
2025-12-25T13:27:08.546279781Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:27:08.546281640Z   File "/usr/local/lib/python3.12/site-packages/passlib/utils/handlers.py", line 2188, in set_backend
2025-12-25T13:27:08.546283600Z     cls._set_backend(name, dryrun)
2025-12-25T13:27:08.546285471Z   File "/usr/local/lib/python3.12/site-packages/passlib/utils/handlers.py", line 2311, in _set_backend
2025-12-25T13:27:08.546287440Z     super(SubclassBackendMixin, cls)._set_backend(name, dryrun)
2025-12-25T13:27:08.546289341Z   File "/usr/local/lib/python3.12/site-packages/passlib/utils/handlers.py", line 2224, in _set_backend
2025-12-25T13:27:08.546291320Z     ok = loader(**kwds)
2025-12-25T13:27:08.546293181Z          ^^^^^^^^^^^^^^
2025-12-25T13:27:08.546295061Z   File "/usr/local/lib/python3.12/site-packages/passlib/handlers/bcrypt.py", line 626, in _load_backend_mixin
2025-12-25T13:27:08.546297050Z     return mixin_cls._finalize_backend_mixin(name, dryrun)
2025-12-25T13:27:08.546298930Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:27:08.546300840Z   File "/usr/local/lib/python3.12/site-packages/passlib/handlers/bcrypt.py", line 421, in _finalize_backend_mixin
2025-12-25T13:27:08.546302800Z     if detect_wrap_bug(IDENT_2A):
2025-12-25T13:27:08.546304680Z        ^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:27:08.546306551Z   File "/usr/local/lib/python3.12/site-packages/passlib/handlers/bcrypt.py", line 380, in detect_wrap_bug
2025-12-25T13:27:08.546308530Z     if verify(secret, bug_hash):
2025-12-25T13:27:08.546310431Z        ^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:27:08.546312280Z   File "/usr/local/lib/python3.12/site-packages/passlib/utils/handlers.py", line 792, in verify
2025-12-25T13:27:08.546314240Z     return consteq(self._calc_checksum(secret), chk)
2025-12-25T13:27:08.546316130Z                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:27:08.546318021Z   File "/usr/local/lib/python3.12/site-packages/passlib/handlers/bcrypt.py", line 655, in _calc_checksum
2025-12-25T13:27:08.546320000Z     hash = _bcrypt.hashpw(secret, config)
2025-12-25T13:27:08.546321880Z            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2025-12-25T13:27:08.546323770Z ValueError: password cannot be longer than 72 bytes, truncate manually if necessary (e.g. my_password[:72])