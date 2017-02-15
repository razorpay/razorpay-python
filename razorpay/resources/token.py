from .base import Resource
from .Url import URL


class Token(Resource):
    def __init__(self, client=None):
        self.client = client
        self.base_url = URL.CUSTOMER_URL

    def fetch(self, customer_id, token_id, data={}, **kwargs):
        """"
        Fetch Customer for given Id

        Args:
            customer_id : Id for which customer object has to be retrieved

        Returns:
            Order dict for given customer Id
        """
        url = "{}/{}/tokens/{}".format(self.base_url, customer_id, token_id)
        return self.get_url(url, data, **kwargs)

    def all(self, customer_id, data={}, **kwargs):
        """"
        Create Customer from given dict

        Returns:
            Customer Dict which was created
        """
        url = "{}/{}/tokens".format(self.base_url, customer_id)
        return self.post_url(url, data, **kwargs)

    def delete(self, customer_id, token_id, data={}, **kwargs):
        """"
        Delete Given Token For a Customer

        Returns:
            Dict for deleted token
        """
        url = "{}/{}/tokens/{}".format(self.base_url, customer_id, token_id)
        return self.delete_url(url, data, **kwargs)
