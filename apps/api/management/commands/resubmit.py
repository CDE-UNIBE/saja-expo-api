from datetime import timedelta
from django.core.management.base import BaseCommand
from django.utils.timezone import now

from ...models import Log


class Command(BaseCommand):
    """
    Simple command to resubmit logs. Execute this as a crontab.
    """
    help = 'Re-submit logs that were not yet submitted to myswissalps.'

    def handle(self, *args, **options):
        logs = Log.objects.filter(
            finished__isnull=True,
            received__lte=now() - timedelta(minutes=5)
        )
        for log in logs:
            log.submit_to_myswissalps()
