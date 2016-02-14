import logging

from django.db import models
from django.utils.functional import cached_property
from django.utils.timezone import now

from .client import APIClient

logger = logging.getLogger(__name__)


class Log(models.Model):
    """
    Log all requests from the internal stands. Requests are then made to
    the external API with a signal.

    This will be modified at a later point (e.g. add booth id?), this skeleton
    is the bare minimum.

    Log: status responses
    Flag: aborted
    model method: external request (10 times)
    """
    received = models.DateTimeField(auto_now_add=True)
    finished = models.DateTimeField(null=True, blank=True)
    nfc_id = models.CharField(max_length=255)
    tag_id = models.CharField(max_length=50)
    history = models.TextField(default='', blank=True)

    def __unicode__(self):
        return self.id

    @cached_property
    def data(self):
        return {
            'nfc': self.nfc_id,
            'tag_id': self.tag_id
        }

    def submit_to_myswissalps(self):
        """
        Submit the data to the API from myswissalps.
        """
        if not self.finished:
            client = APIClient().request(self.data)
            if client:
                self.finished = now()
            else:
                message = 'Unsucessful attempt: {}\n'.format(now())
                self.history += message
                logger.error(message)
            self.save()

    class Meta:
        ordering = ['-received']
