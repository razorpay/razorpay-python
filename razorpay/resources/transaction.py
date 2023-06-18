import warnings

from .base import Resource
from ..constants import URL


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
            transaction dict
        """
        return super(Transaction, self).fetch(transaction_id, data, **kwargs)

    def fetch_all(self, data={}, **kwargs):  # pragma: no cover
        warnings.warn("Will be Deprecated in next release, use all",
                      DeprecationWarning)
        return self.all(data, **kwargs)
