from celery.task import PeriodicTask
from models import UserProfile
from datetime import timedelta

class CheckFlag(PeriodicTask):
    run_every = timedelta(seconds=30)

    def run(self, **kwargs):
        print "it ran!"
        print UserProfile
        logger = self.get_logger(**kwargs)
        logger.info("running the flag check")
        return True
