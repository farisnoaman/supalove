from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.cron import CronTrigger
import atexit
from datetime import datetime

from services.project_service import get_projects
from services.backup_service import BackupService

class SchedulerService:
    def __init__(self):
        self.scheduler = BackgroundScheduler()
        self.backup_service = BackupService()
        self._setup_jobs()

    def _setup_jobs(self):
        # Schedule daily backup at 3 AM
        self.scheduler.add_job(
            func=self.run_daily_backups,
            trigger=CronTrigger(hour=3),
            id="daily_backup",
            name="Daily Database & Storage Backup",
            replace_existing=True
        )
        
        # Schedule resource provisioning check every 10s
        self.scheduler.add_job(
            func=self.provision_pending_resources,
            trigger=IntervalTrigger(seconds=10),
            id="provision_resources",
            name="Provision Pending Resources",
            replace_existing=True
        )
        
        # Schedule usage stats collection every 1 minute
        self.scheduler.add_job(
            func=self.update_cluster_usage,
            trigger=IntervalTrigger(seconds=60),
            id="cluster_usage",
            name="Update Cluster Usage Stats",
            replace_existing=True
        )

    def run_daily_backups(self):
        print("[Scheduler] Starting daily backups...")
        projects = get_projects()
        for project in projects:
            if project.status == "running":
                try:
                    print(f"[Scheduler] Backing up project {project.id}")
                    self.backup_service.backup_database(project.id)
                    self.backup_service.backup_storage(project.id)
                except Exception as e:
                    print(f"[Scheduler] Backup failed for {project.id}: {e}")
        print("[Scheduler] Daily backups completed.")

    def provision_pending_resources(self):
        """Check for pending resources and provision them."""
        from core.database import SessionLocal
        from services.cluster_service import ClusterService
        from models.cluster import Cluster, ClusterStatus
        
        db = SessionLocal()
        try:
            # 1. Check for pending clusters
            clusters = db.query(Cluster).filter(Cluster.status == ClusterStatus.creating).all()
            for cluster in clusters:
                ClusterService.provision_cluster(db, cluster.id)
        except Exception as e:
            print(f"[Scheduler] Provisioning error: {e}")
        finally:
            db.close()

    def update_cluster_usage(self):
        """Update usage stats for all clusters."""
        from core.database import SessionLocal
        from models.cluster import Cluster, ClusterStatus
        from models.cluster_usage import ClusterUsage
        from models.project import Project, ProjectStatus
        import random
        
        db = SessionLocal()
        try:
            clusters = db.query(Cluster).filter(Cluster.status == ClusterStatus.running).all()
            
            for cluster in clusters:
                usage = db.query(ClusterUsage).filter(ClusterUsage.cluster_id == cluster.id).first()
                if not usage:
                    usage = ClusterUsage(cluster_id=cluster.id)
                    db.add(usage)
                
                # count projects on this cluster
                # Note: This is an approximation. Ideally detailed query.
                project_count = db.query(Project).filter(
                    Project.cluster_id == cluster.id,
                    Project.status == ProjectStatus.RUNNING
                ).count()
                
                usage.db_count = project_count
                
                # Mock CPU/Memory for now as we don't have direct Docker access easily from here
                # In real prod, this comes from a monitoring agent or Docker socket
                usage.cpu_percent = round(random.uniform(5.0, 30.0), 1) + (project_count * 0.5)
                usage.memory_mb = 128 + (project_count * 50)
                
                # Active connections query could go here if we had admin access to each cluster
                usage.active_connections = project_count * 2  # Mock estimation
                
                usage.updated_at = datetime.utcnow()
                db.commit()
                
        except Exception as e:
            print(f"[Scheduler] Usage update error: {e}")
        finally:
            db.close()

    def start(self):
        if not self.scheduler.running:
            print("[Scheduler] Starting background scheduler...")
            self.scheduler.start()
            # Shut down the scheduler when exiting the app
            atexit.register(lambda: self.scheduler.shutdown())

    def stop(self):
        if self.scheduler.running:
            self.scheduler.shutdown()
