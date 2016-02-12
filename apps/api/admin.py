from django.contrib import admin
from .models import Log


class LogAdmin(admin.ModelAdmin):
    list_display = ('id', 'received', 'finished', 'nfc_id', 'tag_id', )
admin.site.register(Log, LogAdmin)
