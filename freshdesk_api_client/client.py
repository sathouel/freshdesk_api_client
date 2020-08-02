import base64

import requests as rq

from freshdesk_api_client import (
    utils,
    resources
)

class FreshdeskClient:
    BASE_URL = 'https://{}.freshdesk.com/api'

    def __init__(self, company, api_key, api_version='v2'):
        self._session = rq.Session()
        self._company = company
        self._api_key = api_key
        self._api_version = api_version

        self._base_url = utils.urljoin(FreshdeskClient.BASE_URL.format(self._company), self._api_version)
        self._resources = {
            'tickets': resources.TicketsPool(
                utils.urljoin(self._base_url, 'tickets'), self._session),
            'conversations': resources.ConversationsPool(
                utils.urljoin(self._base_url, 'conversations'), self._session),
            'contacts': resources.ContactsPool(
                utils.urljoin(self._base_url, 'contacts'), self._session),
            'agents': resources.AgentsPool(
                utils.urljoin(self._base_url, 'agents'), self._session),
            'skills': resources.SkillsPool(
                utils.urljoin(self._base_url, 'skills'), self._session),
            'roles': resources.RolesPool(
                utils.urljoin(self._base_url, 'roles'), self._session),
            'groups': resources.GroupsPool(
                utils.urljoin(self._base_url, 'groups'), self._session),
            'companies': resources.CompaniesPool(
                utils.urljoin(self._base_url, 'companies'), self._session),
        }

        self._authenticate()

    def _authenticate(self):
        basic_auth = '{}:X'.format(self._api_key).encode('utf-8')
        basic_auth = base64.b64encode(basic_auth).decode()
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic {}'.format(basic_auth)
        }
        self._session.headers = headers

    @property
    def endpoints(self):
        base_url = utils.urljoin(FreshdeskClient.BASE_URL.format(self._company), self._api_version)
        endpoints = {
            'base': base_url
        }
        return endpoints

    @property
    def resources(self):
        """Return all resources as a list of Resources"""
        return self._resources
