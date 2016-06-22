from datetime import datetime
from django.core.management.base import BaseCommand

from ...models import Log


class Command(BaseCommand):
    """
    Simple command to resubmit logs. Execute this as a crontab.
    """
    help = 'Re-submit logs that were already processed. Use this, if the myswissalps server crashed and the database' \
           'is not fully restored. Example: python manage.py restore_sent 2016-01-31:23.00'

    def add_arguments(self, parser):
        parser.add_argument('from', nargs='+', type=str)

    def handle(self, *args, **options):
        try:

            from_date = datetime.strptime(options['from'][0], '%Y-%m-%d:%I.%M')
        except (TypeError, KeyError):
            print('Invalid format of argument. Please use the format: yyyy-mm-dd:HH.mm (e.g. 2016-01-31:23.59)')
            return

        # confirmation required.
        confirmation = input('Confirm re-submitting all logged calls to the proxy since {}: y/n\n'.format(from_date))
        if confirmation == 'y':
            logs = Log.objects.filter(received__gte=from_date)
            for log in logs:
                log.submit_to_myswissalps()
        else:
            print('Re-submitting aborted.')
