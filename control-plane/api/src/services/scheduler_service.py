from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.cron import CronTrigger
import atexit

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

    def start(self):
        if not self.scheduler.running:
            print("[Scheduler] Starting background scheduler...")
            self.scheduler.start()
            # Shut down the scheduler when exiting the app
            atexit.register(lambda: self.scheduler.shutdown())

    def stop(self):
        if self.scheduler.running:
            self.scheduler.shutdown()
