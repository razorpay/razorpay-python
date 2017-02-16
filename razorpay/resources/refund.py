from .base import Resource
from .Url import URL
import warnings


class Refund(Resource):
    def __init__(self, client=None):
        self.client = client
        self.base_url = URL.REFUNDS_URL

    def fetch_all(self, data={}, **kwargs):  # pragma: no cover
        warnings.warn("Will be Deprecated in next release, use all",
                      DeprecationWarning)
        self.all(data, **kwargs)

    def create(self, data={}, **kwargs):
        """
        Create refund for given payment id
        """
        url = self.base_url
        return self.post_url(url, data, **kwargs)

    def all(self, data={}, **kwargs):
        """"
        All Refund for given payment Id

        Args:
            payment_id : Payment Id for which refund has to be retrieved

        Returns:
            Refund dict for given payment Id
        """
        return super(Refund, self).all(data, **kwargs)

    def fetch(self, refund_id, data={}, **kwargs):
        """"
        Refund object for given payment Id and given paymnet Id

        Args:
            payment_id : Payment Id for which refund has to be retrieved
            payment_id : Refund Id for which refund has to be retrieved

        Returns:
            Refund dict for given payment and refund Id
        """
        return super(Refund, self).fetch(refund_id, data, **kwargs)
