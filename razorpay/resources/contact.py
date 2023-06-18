import warnings

from .base import Resource
from ..constants.url import URL


class Contact(Resource):
    def __init__(self, client=None):
        super(Contact, self).__init__(client)
        self.base_url = URL.CONTACTS_URL

    def create(self, data={}, **kwargs):
        """"
        Create Contact from given dict

        Returns:
            Contact Dict which was created
        """
        url = self.base_url
        return self.post_url(url, data, **kwargs)

    def fetch(self, contact_id, data={}, **kwargs):
        """"
        Fetch Contact for given Id

        Args:
            contact_id : Id for which contact object has to be retrieved

        Returns:
            contact dict
        """
        return super(Contact, self).fetch(contact_id, data, **kwargs)

    def fetch_all(self, data={}, **kwargs):  # pragma: no cover
        warnings.warn("Will be Deprecated in next release, use all",
                      DeprecationWarning)
        return self.all(data, **kwargs)

    def update(self, contact_id, data={}, **kwargs):
        """"
        Update Contact information from given dict

        Returns:
            Contact Dict which was edited
        """
        url = '{}/{}'.format(self.base_url, contact_id)

        return self.patch_url(url, data, **kwargs)

    def status(self, contact_id, data={}, **kwargs):
        """"
        Update the status of  Contact from given dict (ACTIVE/INACTIVE)

        Returns:
            Contact dict which was edited
        """
        url = '{}/{}'.format(self.base_url, contact_id)

        return self.patch_url(url, data, **kwargs)
