import json

from freshdesk_api_client.utils import urljoin
from freshdesk_api_client.interfaces import *


class ResourcePool:
    def __init__(self, endpoint, session):
        """Initialize the ResourcePool to the given endpoint. Eg: products"""
        self._endpoint = endpoint
        self._session = session

    def get_url(self):
        return self._endpoint

class CreatableResource(CreatableResourceInterface):
    def create_item(self, item):
        res = self._session.post(self._endpoint, data=json.dumps(item))
        return res

class GettableResource(GettableResourceInterface):
    def fetch_item(self, code):
        url = urljoin(self._endpoint, code)
        res = self._session.get(url)
        return res

class ListableResource(ListableResourceInterface):
    def fetch_list(self, args=None):
        res = self._session.get(self._endpoint, )
        pass

class UpdatableResource(UpdatableResourceInterface):
    def update_create_item(self, item, code=None):
        if code is None:
            code = item.get('id')
        url = urljoin(self._endpoint, code)
        res = self._session.put(url, data=json.dumps(item))
        return res

class DeletableResource(DeletableResourceInterface):
    def delete_item(self, code):
        url = urljoin(self._endpoint, code)
        res = self._session.delete(url)
        return res

class TicketsPool(
                ResourcePool,
                CreatableResource,
                GettableResource,
                ListableResource,
                UpdatableResource,
                DeletableResource):
    # https://developers.freshdesk.com/api/#tickets
    pass

class ConversationsPool(
                    ResourcePool,
                    CreatableResource,
                    ListableResource,
                    UpdatableResource,
                    DeletableResource):
    # https://developers.freshdesk.com/api/#conversations
    pass

class ContactsPool(
                ResourcePool,
                CreatableResource,
                GettableResource,
                ListableResource,
                UpdatableResource,
                DeletableResource):
    # https://developers.freshdesk.com/api/#contacts
    pass

class AgentsPool(
                ResourcePool,
                CreatableResource,
                GettableResource,
                ListableResource,
                UpdatableResource,
                DeletableResource):
    # https://developers.freshdesk.com/api/#agents
    pass

class SkillsPool(
                ResourcePool,
                CreatableResource,
                GettableResource,
                ListableResource,
                UpdatableResource,
                DeletableResource):
    # https://developers.freshdesk.com/api/#skills
    pass

class RolesPool(
                ResourcePool,
                GettableResource,
                ListableResource,):
    # https://developers.freshdesk.com/api/#skills
    pass

class GroupsPool(
                ResourcePool,
                CreatableResource,
                GettableResource,
                ListableResource,
                UpdatableResource,
                DeletableResource):
    # https://developers.freshdesk.com/api/#groups
    pass

class CompaniesPool(
                ResourcePool,
                CreatableResource,
                GettableResource,
                ListableResource,
                UpdatableResource,
                DeletableResource):
    # https://developers.freshdesk.com/api/#companies
    pass