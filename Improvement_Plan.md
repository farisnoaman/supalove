# Supalove: Scaling & Improvement Plan (1,000+ Projects)

To evolve Supalove from a single-node prototype to a production-grade platform capable of hosting 1,000+ concurrent projects, we must shift from a **local Docker orchestration** model to a **cloud-native, distributed architecture**.

---

## 1. Infrastructure Architecture
### Shift to Kubernetes (K8s)
The current `LocalStorageProvisioner` is bound to a single host. To scale, we must move to Kubernetes.
- **Node Pools**: Separate "Control Plane" nodes (API, Dashboard, Keycloak) from "Data Plane" nodes (Tenant projects).
- **Custom Resource Definitions (CRDs)**: Create a `SupaloveProject` CRD. Instead of running `docker-compose`, the API will create K8s objects (Deployments, Services, ConfigMaps).
- **Isolation**: Use **Kubernetes Namespaces** per project for network and resource isolation.

### Distributed Compute
- **Provisioning Engine**: Use a **Worker Pattern** (e.g., Celery + Redis). Provisioning a project takes time; it should be handled by background workers to keep the API responsive.
- **Auto-scaling**: Implement K8s Cluster Autoscaler to spin up more worker nodes as project demand increases.

---

## 2. Platform Performance & Scaling
### Intelligent Routing
- **Global Gateway**: Replace host-port mapping with an **Ingress Controller** (e.g., Traefik or Nginx Ingress).
- **Subdomain Routing**: Projects should be accessible via `[project-id].supalove.cloud` rather than `:port`.
- **Dynamic Re-routing**: Use a dynamic discovery mechanism (like Consul or K8s Service Discovery) so the gateway always knows which node a project is running on.

### Database Strategy
- **Connection Pooling**: At 1,000+ projects, the number of open connections will crash the DB. Mandate **PgBouncer** or **Supavisor** for every project.
- **Shared vs. Dedicated**:
    - **Free Tier**: Shared large Postgres clusters with logical database isolation.
    - **Pro Tier**: Dedicated K8s StatefulSets with guaranteed CPU/RAM.

---

## 3. Security Enhancements
### Multi-Tenant Isolation
- **Micro-VMs**: Use **gVisor** or **Kata Containers** for project runtimes to prevent container escape attacks.
- **Network Policies**: Strictly enforce K8s `NetworkPolicies` to ensure Project A cannot talk to Project B.
- **Resource Quotas**: Set hard limits on Memory/CPU/IOPS per project to prevent "noisy neighbor" issues.

### Secrets Management
- **Vault Integration**: Move project secrets from the metadata DB to a dedicated secret manager like **HashiCorp Vault**.
- **Least Privilege**: The Control Plane API should only have access to provisioning interfaces, not the raw data inside tenant databases.

---

## 4. Reliability & Maintenance
### Automated Backups
- **Continuous Archiving**: Use **WAL-G** or **Barman** to stream Postgres WAL segments to S3 (MinIO/AWS).
- **Point-in-Time Recovery (PITR)**: Enable users to restore their database to any second in the last 7 days.

### Observability
- **Centralized Logs**: Ship project logs (Auth, DB, PostgREST) to an ELK or Grafana Loki stack.
- **Metrics**: Export metrics Using **Prometheus** and visualize platform health with **Grafana**. 
- **Health Checks**: Automate project restarts if the Gateway detects a DOWN status.

---

## 5. Implementation Roadmap

| Phase | Focus | Key Deliverable |
|-------|-------|-----------------|
| **Phase 1** | **Async Ops** | Implement Task Queue (Celery) for project lifecycle. |
| **Phase 2** | **Networking** | Implement Subdomain routing with Traefik/Nginx. |
| **Phase 3** | **Orchestration** | Migrate `provisioning_local.py` to `provisioning_k8s.py`. |
| **Phase 4** | **Observability** | Deploy Prometheus/Grafana monitoring. |
| **Phase 5** | **Hardening** | Implement gVisor isolation and Resource Quotas. |

---

> [!IMPORTANT]
> Scaling to 1,000 projects on a single VPS is not recommended. The focus should be on **Horizontal Scaling** where adding capacity is as simple as adding a new worker node to the cluster.
