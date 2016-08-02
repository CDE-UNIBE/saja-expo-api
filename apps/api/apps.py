from django.apps import AppConfig


class APIConfig(AppConfig):
    """
    Load the signal receivers on startup.
    """
    name = 'api'
    verbose_name = "API"

    # def ready(self):
    #    from .signals import send_to_external_api  # noqa
