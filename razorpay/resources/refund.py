from .base import Resource
from .Url import URL


class Refund(Resource):
    def __init__(self, client=None):
        self.client = client
        self.base_url = URL.REFUND_URL

    def all(self, **kwargs):
        """"
        All Refund for given payment Id

        Args:
            payment_id : Payment Id for which refund has to be retrieved

        Returns:
            Refund dict for given payment Id
        """
        return super(Refund, self).all(**kwargs)

    def fetch(self, refund_id, **kwargs):
        """"
        Refund object for given payment Id and given paymnet Id

        Args:
            payment_id : Payment Id for which refund has to be retrieved
            payment_id : Refund Id for which refund has to be retrieved

        Returns:
            Refund dict for given payment and refund Id
        """
        return super(Refund, self).fetch(refund_id, **kwargs)
