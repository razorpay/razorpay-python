from .base import Resource
from ..constants.url import URL
import warnings


class Contact(Resource):
    def __init__(self, client=None):
        super(Contact, self).__init__(client)
        self.base_url = URL.CONTACT_URL

    def fetch(self, contact_id, data={}, **kwargs):
        """"
        Fetch Contact for given Id

        Args:
            contact_id : Id for which Contact object has to be retrieved

        Returns:
            Contact dict for given Contact Id
        """
        return super(Contact, self).fetch(contact_id, data, **kwargs)

    def all(self, data={}, **kwargs):
        """"
        Fetch all Contact entities

        Returns:
            Dictionary of Contact data
        """
        return super(Contact, self).all(data, **kwargs)

    def create(self, data={}, **kwargs):
        """"
        Create Contact from given dict

        Returns:
            Contact Dict which was created
        """
        url = self.base_url
        return self.post_url(url, data, **kwargs)

    def update(self, contact_id, data={}, **kwargs):
        """

        """
        url = "{}/{}".format(self.base_url, contact_id)
        return super(Contact, self).patch_url(url, data, **kwargs)

    def get_types(self, data={}, **kwargs):
        """
        """
        url = "{}/types".format(self.base_url)
        return self.get_url(url, data, **kwargs)

    def post_type(self, data={}, **kwargs):
        """
        """
        url = "{}/types".format(self.base_url)
        return self.post_url(url, data, **kwargs)