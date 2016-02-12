# -*- coding: utf-8 -*-
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Log


@receiver(post_save, sender=Log)
def send_to_external_api(instance, *args, **kwargs):
    """
    Stub.
    """
    pass
