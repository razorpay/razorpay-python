from .base import Resource
from .Url import URL
import warnings


class Invoice(Resource):
    def __init__(self, client=None):
        self.client = client
        self.base_url = URL.INVOICE_URL

    def fetch_all(self, data={}, **kwargs):  # pragma: no cover
        warnings.warn("Will be Deprecated in next release", DeprecationWarning)
        self.all(data, **kwargs)

    def all(self, data={}, **kwargs):
        """"
        Fetch all Invoice entities

        Returns:
            Dictionary of Invoice data
        """
        return super(Invoice, self).all(data, **kwargs)

    def fetch(self, invoice_id, data={}, **kwargs):
        """"
        Fetch Invoice for given Id

        Args:
            invoice_id : Id for which invoice object has to be retrieved

        Returns:
            Invoice dict for given invoice Id
        """
        return super(Invoice, self).fetch(invoice_id, data, **kwargs)

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
