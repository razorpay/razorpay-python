from .base import Resource
from .Url import URL
import warnings


class Payment(Resource):
    def __init__(self, client=None):
        super(Payment, self).__init__(client)
        self.base_url = URL.PAYMENTS_URL

    def fetch_all(self, data={}, **kwargs):  # pragma: no cover
        warnings.warn("Will be Deprecated in next release, use all",
                      DeprecationWarning)
        self.all(data, **kwargs)

    def all(self, data={}, **kwargs):
        """"
        Fetch all Payment entities

        Returns:
            Dictionary of Payment data
        """
        return super(Payment, self).all(data, **kwargs)

    def fetch(self, payment_id, data={}, **kwargs):
        """"
        Fetch Payment for given Id

        Args:
            payment_id : Id for which payment object has to be retrieved

        Returns:
            Payment dict for given payment Id
        """
        return super(Payment, self).fetch(payment_id, data, **kwargs)

    def capture(self, payment_id, amount, data={}, **kwargs):
        """"
        Capture Payment for given Id

        Args:
            payment_id : Id for which payment object has to be retrieved
            Amount : Amount for which the payment has to be retrieved

        Returns:
            Payment dict after getting captured
        """
        url = "{}/{}/capture".format(self.base_url, payment_id)
        data['amount'] = amount
        return self.post_url(url, data, **kwargs)

    def refund(self, payment_id, amount, data={}, **kwargs):
        """"
        Refund Payment for given Id

        Args:
            payment_id : Id for which payment object has to be refunded
            Amount : Amount for which the payment has to be refunded

        Returns:
            Payment dict after getting refunded
        """
        url = "{}/{}/refund".format(self.base_url, payment_id)
        data['amount'] = amount
        return self.post_url(url, data, **kwargs)
