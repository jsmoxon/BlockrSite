from celery.task import PeriodicTask
from models import UserProfile
from datetime import timedelta
from blockrsite.entries.views import check_flag, print_something

class CheckFlag(PeriodicTask):
    run_every = timedelta(seconds=60)

    def run(self, **kwargs):
        check_flag()
        logger = self.get_logger(**kwargs)
        logger.info("running the flag check")
        return True
