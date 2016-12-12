from .base import Resource
from .Url import URL


class Refund(Resource):
    def __init__(self, client=None):
        self.client = client
        self.base_url = URL.PAYMENTS_URL

    def fetch_all(self, payment_id, **kwargs):
        """"
        All Refund for given payment Id

        Args:
            payment_id : Payment Id for which refund has to be retrieved

        Returns:
            Refund dict for given payment Id
        """
        url = "{}/{}/refunds".format(self.base_url, payment_id)
        return self.get_url(url, **kwargs)

    def fetch(self, payment_id, refund_id, **kwargs):
        """"
        Refund object for given payment Id and given paymnet Id

        Args:
            payment_id : Payment Id for which refund has to be retrieved
            payment_id : Refund Id for which refund has to be retrieved

        Returns:
            Refund dict for given payment and refund Id
        """
        url = "{}/{}/refunds/{}".format(self.base_url, payment_id, refund_id)
        return self.get_url(url, **kwargs)
