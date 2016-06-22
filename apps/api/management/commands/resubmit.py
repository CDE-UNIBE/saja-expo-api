from datetime import timedelta
from django.core.management.base import BaseCommand
from django.utils.timezone import now

from ...models import Log


class Command(BaseCommand):
    """
    Simple command to resubmit logs. Execute this as a crontab.
    """
    help = 'Submit logs that were not yet submitted to myswissalps.'

    def handle(self, *args, **options):
        filters = {
            'finished__isnull': True,
            'received__lte': now() - timedelta(minutes=5)
        }

        logs = Log.objects.filter(**filters)
        for log in logs:
            log.submit_to_myswissalps()
