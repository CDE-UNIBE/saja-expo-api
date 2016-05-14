from django.contrib import admin
from django.contrib.admin import register

from .models import Log


@register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('id', 'received', 'finished', 'backpack_id', )
