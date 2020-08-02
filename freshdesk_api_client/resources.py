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
        pass

class GettableResource(GettableResourceInterface):
    def fetch_item(self, item):
        pass

class ListableResource(ListableResourceInterface):
    def fetch_list(self, args=None):
        pass

class UpdatableResource(UpdatableResourceInterface):
    def update_create_item(self, item):
        pass

class DeletableResource(DeletableResourceInterface):
    def delete_item(self, item):
        pass

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