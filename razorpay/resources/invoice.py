from .base import Resource
from .Url import URL


class Invoice(Resource):
    def __init__(self, client=None):
        self.client = client
        self.base_url = URL.INVOICE_URL

    def all(self, **kwargs):
        """"
        Fetch all Invoice entities

        Returns:
            Dictionary of Invoice data
        """
        url = self.base_url
        return self.get_url(url, **kwargs)

    def fetch(self, invoice_id, **kwargs):
        """"
        Fetch Invoice for given Id

        Args:
            invoice_id : Id for which invoice object has to be retrieved

        Returns:
            Invoice dict for given invoice Id
        """
        url = "{}/{}".format(self.base_url, invoice_id)
        return self.get_url(url, **kwargs)

    def create(self, data={}, **kwargs):
        """"
        Create Invoice from given dict

        Args:
            data : Dictionary having keys using which invoice have to be created

        Returns:
            Invoice Dict which was created
        """
        url = self.base_url
        return self.post_url(url, data, **kwargs)
