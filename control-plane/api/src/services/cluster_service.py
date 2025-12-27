from sqlalchemy.orm import Session
from models.cluster import Cluster, ClusterType, ClusterStatus
from models.plan import Plan, ClusterStrategy
from models.organization_entitlement import OrganizationEntitlement
from models.cluster_usage import ClusterUsage
from services.entitlement_service import EntitlementService
import os
import uuid
import logging

logger = logging.getLogger(__name__)

class ClusterService:
    @staticmethod
    def get_or_create_global_cluster(db: Session) -> Cluster:
        """Get or create the global shared cluster."""
        cluster = db.query(Cluster).filter(
            Cluster.type == ClusterType.global_shared
        ).first()
        
        if not cluster:
            logger.info("Initializing global shared cluster")
            cluster = Cluster(
                id="global-shared",
                type=ClusterType.global_shared,
                status=ClusterStatus.running,
                postgres_host=os.getenv("SHARED_POSTGRES_HOST", "localhost"),
                postgres_port=int(os.getenv("SHARED_POSTGRES_PORT", "5435")),
                api_url=os.getenv("SHARED_GATEWAY_URL", "http://localhost:8081")
            )
            db.add(cluster)
            
            # Init usage stats
            usage = ClusterUsage(cluster_id=cluster.id)
            db.add(usage)
            
            db.commit()
        
        return cluster

    @staticmethod
    def get_private_cluster(db: Session, org_id: str) -> Cluster:
        """Get private cluster for an organization if it exists."""
        return db.query(Cluster).filter(
            Cluster.type == ClusterType.private_shared,
            Cluster.owner_org_id == org_id
        ).first()

    @staticmethod
    def create_pending_private_cluster(db: Session, org_id: str) -> Cluster:
        """Create a private cluster record in pending state."""
        cluster_id = f"private-{org_id}-{uuid.uuid4().hex[:6]}"
        
        cluster = Cluster(
            id=cluster_id,
            type=ClusterType.private_shared,
            owner_org_id=org_id,
            status=ClusterStatus.creating
        )
        db.add(cluster)
        
        # Init usage stats
        usage = ClusterUsage(cluster_id=cluster.id)
        db.add(usage)
        
        db.commit()
        return cluster

    @staticmethod
    def resolve_cluster_for_project(db: Session, org_id: str) -> Cluster:
        """
        Resolve which cluster an org should use based on entitlements and strategy.
        Returns a Cluster object (which might be in 'creating' state).
        """
        ent = EntitlementService.get_entitlements(db, org_id)
        plan = EntitlementService.get_plan(db, ent.plan_id)
        
        if plan.cluster_strategy == ClusterStrategy.private_per_org:
            # Check if exists
            cluster = ClusterService.get_private_cluster(db, org_id)
            
            if not cluster:
                # Create pending cluster
                logger.info(f"Creating pending private cluster for org {org_id}")
                cluster = ClusterService.create_pending_private_cluster(db, org_id)
                # Note: Scheduler will pick this up for provisioning
            
            # Shared Fallback Logic
            if cluster.status != ClusterStatus.running and plan.allow_shared_fallback:
                logger.info(f"Private cluster {cluster.id} not ready. Checking shared fallback.")
                # If specifically configured to fallback, we could return global cluster here.
                # However, usually 'allow_shared_fallback' means "User CAN use shared", 
                # but if they requested a Private one (implicit via Plan), we usually wait.
                # If we want to force fallback while creating, we'd need to change this logic.
                # For now, let's assume 'private_per_org' strategy means we prefer private.
                # If we returned global here, the Project would be permanently bound to Global.
                pass 
                
            return cluster
        else:
            # global_only
            return ClusterService.get_or_create_global_cluster(db)

    @staticmethod
    def provision_cluster(db: Session, cluster_id: str):
        """
        Actually provision the cluster resources (Docker).
        Called by Scheduler.
        """
        cluster = db.query(Cluster).filter(Cluster.id == cluster_id).first()
        if not cluster or cluster.status != ClusterStatus.creating:
            return

        logger.info(f"Provisioning cluster {cluster_id}...")
        
        try:
            # TODO: Integrate with actual Provisioner (Local/Coolify)
            # For now, we simulate success for Private clusters by pointing to localhost 
            # but on different ports if we were doing real isolation.
            # Since this is "Private Shared" logic simulation:
            
            from services.provisioning_local import LocalProvisioner
            # We assume we might spin up a new docker compose stack here.
            # For the MVP, let's simulate it becoming ready.
            
            # In a real impl, this would run `docker compose up`
            
            cluster.postgres_host = "localhost" # In real life, specific IP
            cluster.postgres_port = 5435 # Mocking: Point to Shared Cluster for dev simulation
            cluster.api_url = "http://localhost:8000"
            cluster.status = ClusterStatus.running
            
            db.commit()
            logger.info(f"Cluster {cluster_id} provisioned successfully.")
            
        except Exception as e:
            logger.error(f"Failed to provision cluster {cluster_id}: {e}")
            cluster.status = ClusterStatus.failed
            db.commit()
