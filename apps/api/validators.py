from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def validate_registered_nfc_id(value):
    """
    Allow only registered NFC ids.

    :param value: nfc_id
    """
    from .models import NFCRegister

    if not NFCRegister.objects.filter(nfc_id=value).exists():
        raise ValidationError(
            _('%(value)s is not a registered nfc id.'),
            params={'value': value},
        )
