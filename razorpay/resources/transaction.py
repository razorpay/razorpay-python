from .base import Resource
from ..constants.url import URL
import warnings


class Transaction(Resource):
    def __init__(self, client=None):
        super(Transaction, self).__init__(client)
        self.base_url = URL.TRANSACTION_URL

    def fetch(self, transaction_id, data={}, **kwargs):
        """"
        Fetch transaction for given Id

        Args:
            transaction_id : Id for which transaction object has to be retrieved

        Returns:
            transaction dict for given transaction Id
        """
        return super(Transaction, self).fetch(transaction_id, data, **kwargs)

    def all(self, data={}, **kwargs):
        """
        Fetch all transaction entities

        Returns:
            Dictionary of transaction data
        """
        return super(Transaction, self).all(data,**kwargs)