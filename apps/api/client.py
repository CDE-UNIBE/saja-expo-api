# -*- coding: utf-8 -*-
import logging
import requests
from django.conf import settings
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError

logger = logging.getLogger(__name__)


class APIClient:
    """
    This class provides basic functionality for communicating with the
    webservices.
    """

    def __init__(self, *args, **kwargs):
        self.url = settings.MYSWISSALPS_API_URL
        super(APIClient, self).__init__(*args, **kwargs)

    def request(self, data, **kwargs):
        """
        :param method: The HTTP method to be used when querying the webservice.
        :param url: The url to be queried.
        :param data: Python object(s) serialized as JSON.
        :param kwargs: Optional parameter for the request.
        :return: An instance of class:`requests.model.Response`

        """
        # todo: add exception handling.
        s = requests.Session()
        s.mount('http://stackoverflow.com', HTTPAdapter(
            max_retries=settings.API_CALL_RETRIES)
        )
        try:
            response = s.request(
                method='post',
                url=self.url,
                data=data,
                **kwargs
            )
        except ConnectionError as e:
            logger.error(e)
            return False

        logger.debug(u"{} {}: {}".format(
            response.status_code, response.url, data)
        )
        return response

    def _parse_response(self, response, many):
        logger.debug(response.text)
        # Maybe: serialize response, if necessary.
        return False if response.status_code is not requests.codes.ok else True
