from rest_framework import serializers
from .models import Log, NFCRegister


class LogSerializer(serializers.ModelSerializer):
    """
    Basic serializer for logs.
    """
    class Meta:
        model = Log


class NFCRegisterSerializer(serializers.ModelSerializer):
    """
    Basic serializer to register NFC ids.
    """

    class Meta:
        model = NFCRegister
