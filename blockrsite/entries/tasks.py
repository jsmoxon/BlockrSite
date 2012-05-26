from celery.task import PeriodicTask
from models import UserProfile
from datetime import timedelta
from blockrsite.entries.views import check_flag

class CheckFlag(PeriodicTask):
    run_every = timedelta(seconds=30)

    def run(self, **kwargs):
        check_flag()
        logger = self.get_logger(**kwargs)
        logger.info("running the flag check")
        return True
