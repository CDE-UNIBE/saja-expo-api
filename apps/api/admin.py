from django.contrib import admin
from django.contrib.admin import register

from .models import Log, NFCRegister


@register(NFCRegister)
class NFCRegisterAdmin(admin.ModelAdmin):
    list_display = ('nfc_id', 'created', )


@register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('id', 'received', 'finished', 'nfc_id', 'tag_id', )
