import logging

from django.db import models
from django.utils.functional import cached_property
from django.utils.timezone import now

from .client import APIClient
from .validators import validate_registered_nfc_id

logger = logging.getLogger(__name__)


class APISubmitBase(models.Model):
    """
    Shared attributes and method for calling the API and logging the results.
    """
    received = models.DateTimeField(auto_now_add=True)
    finished = models.DateTimeField(null=True, blank=True)
    history = models.TextField(default='', blank=True)

    def submit_to_myswissalps(self):
        """
        Submit the data to the API from myswissalps.
        """
        if not self.finished:
            client = APIClient().request(endpoint=self.endpoint, data=self.data)
            if client:
                self.finished = now()
            else:
                message = 'Unsucessful attempt: {}\n'.format(now())
                self.history += message
                logger.info(message)
            self.save()

    class Meta:
        abstract = True


class NFCRegister(APISubmitBase):
    """
    Relation between nfc and rucksack code is created when a new card is
    registered at the front desk. Only the backpack id will be used for calls
    to the external API.
    """
    created = models.DateTimeField(auto_now_add=True)
    nfc_id = models.CharField(max_length=255, unique=True)
    backpack_id = models.CharField(max_length=6, unique=True)
    language_id = models.IntegerField()

    @property
    def endpoint(self):
        return 'init'

    @cached_property
    def data(self):
        return {
            'code': self.backpack_id,
            'nfcId': self.nfc_id,
            'languageId': self.language_id,
        }


class Log(APISubmitBase):
    """
    Log all requests from the internal stands. Requests are then made to
    the external API with a signal.

    This will be modified at a later point (e.g. add booth id?), this skeleton
    is the bare minimum.

    Log: status responses
    Flag: aborted
    model method: external request (10 times)
    """
    nfc_id = models.CharField(
        max_length=255, validators=[validate_registered_nfc_id]
    )
    station_id = models.CharField(max_length=20)

    def __unicode__(self):
        return self.id

    @property
    def endpoint(self):
        return 'init'

    @cached_property
    def backpack_id(self):
        return NFCRegister.objects.get(nfc_id=self.nfc_id)

    @cached_property
    def data(self):
        return {
            'code': self.backpack_id,
            'stationId': self.station_id
        }

    class Meta:
        ordering = ['-received']
