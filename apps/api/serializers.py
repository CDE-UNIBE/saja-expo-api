from rest_framework import serializers
from .models import Log


class LogSerializer(serializers.ModelSerializer):
    """
    Basic serializer for logs.
    """
    class Meta:
        model = Log
