from datetime import timedelta
from django.core.management.base import BaseCommand
from django.utils.timezone import now

from ...models import Log


class Command(BaseCommand):
    """
    Simple command to resubmit logs. Execute this as a crontab.
    """
    help = 'Remove submitted logs older than 14 days. This should help to keep the db file at a reasonable size.'

    def handle(self, *args, **options):
        two_weeks_ago = now() - timedelta(days=14)
        Log.objects.filter(received__lte=two_weeks_ago, finished__isnull=False).delete()
