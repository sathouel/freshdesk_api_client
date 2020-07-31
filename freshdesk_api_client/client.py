import base64

import requests as rq

from freshdesk_api_client import (
    utils
)

class FreshdeskClient:
    BASE_URL = 'https://{}.freshdesk.com/api'

    def __init__(self, company, api_key, api_version='v2'):
        self._session = rq.Session()
        self._company = company
        self._api_key = api_key
        self._api_version = api_version

        self._authenticate()

    @property
    def endpoints(self):
        base_url = utils.urljoin(FreshdeskClient.BASE_URL.format(self._company), self._api_version)
        endpoints = {
            'base': base_url
        }
        return endpoints

    def _authenticate(self):
        basic_auth = '{}:X'.format(self._api_key).encode('utf-8')
        basic_auth = base64.b64encode(basic_auth).decode()
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic {}'.format(basic_auth)
        }
        self._session.headers = headers