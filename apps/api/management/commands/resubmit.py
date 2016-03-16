from datetime import timedelta
from django.core.management.base import BaseCommand
from django.utils.timezone import now

from ...models import Log, NFCRegister


class Command(BaseCommand):
    """
    Simple command to resubmit logs. Execute this as a crontab.
    """
    help = 'Re-submit logs that were not yet submitted to myswissalps.'

    def handle(self, *args, **options):
        filters = {
            'finished__isnull': True,
            'received__lte': now() - timedelta(minutes=5)
        }

        registers = NFCRegister.objects.filter(**filters)
        for register in registers:
            register.submit_to_myswissalps()

        logs = Log.objects.filter(**filters)
        for log in logs:
            log.submit_to_myswissalps()
