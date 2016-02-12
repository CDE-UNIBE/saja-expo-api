from rest_framework.response import Response
from rest_framework.views import APIView


class APIRoot(APIView):
    """
    Welcome to the API provided by saja expo. This is a list with all endpoints
    that are available.

    This API is intended to be consumed by internal expo machines.
    """
    http_method_names = ('get', )

    def get(self, request, format=None):
        urls = {

        }
        return Response(urls)
