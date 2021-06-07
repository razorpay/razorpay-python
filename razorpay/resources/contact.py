from .base import Resource
from ..constants.url import URL
import warnings


class Contact(Resource):
    def __init__(self, client=None):
        super(Contact, self).__init__(client)
        self.base_url = URL.CONTACT_URL

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