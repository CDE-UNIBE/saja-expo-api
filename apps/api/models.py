from django.db import models


class Log(models.Model):
    """
    Log all requests from the internal stands. Requests are then made to
    the external API with a signal.

    This will be modified at a later point (e.g. add booth id?), this skeleton
    is the bare minimum.
    """
    received = models.DateTimeField(auto_now_add=True)
    finished = models.DateTimeField(null=True, blank=True)
    nfc_id = models.CharField(max_length=255)
    tag_id = models.CharField(max_length=50)

    def __unicode__(self):
        return self.id

    class Meta:
        ordering = ['-received']
