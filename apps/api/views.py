import logging

from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from .serializers import LogSerializer


class APIRoot(APIView):
    """
    Welcome to the API provided by saja expo. This is a list with all endpoints
    that are available.

    This API is intended to be consumed by internal expo machines.
    """
    http_method_names = ('get', )

    def get(self, request, format=None):
        urls = {
            'logs': reverse('log-create', request=request, format=format),
        }
        return Response(urls)


class CreateLogView(CreateAPIView):
    """
    Create new logs.

    Pass nfc_id and tag_id in the request body.
    """
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = (IsAuthenticated, )
    serializer_class = LogSerializer

    def handle_exception(self, exc):
        """
        Log all exceptions. A bad request (invalid data) indicates that a station submitted an invalid message.
        """
        logger = logging.getLogger(__name__)
        logger.warn('Invalid request from a nfc tag station with following data: {data} (Exception: {exc})'.format(
            data=self.request.data, exc=exc))
        return super().handle_exception(exc)
