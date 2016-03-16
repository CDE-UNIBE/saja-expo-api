# -*- coding: utf-8 -*-
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import NFCRegister, Log


@receiver(post_save, sender=NFCRegister)
def register_nfc_at_api(instance, created, *args, **kwargs):
    if created:
        instance.submit_to_myswissalps()

@receiver(post_save, sender=Log)
def send_to_external_api(instance, created, *args, **kwargs):
    """
    Submit the data to myswissalps.
    :param created: bool
    :param instance: api.models.Log
    """
    if created:
        instance.submit_to_myswissalps()
