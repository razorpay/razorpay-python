from .base import Resource
from ..constants.url import URL
import warnings

class PaymentMethod(Resource):
    def __init__(self, client=None):
        super(PaymentMethod, self).__init__(client)
        self.base_url = URL.PAYMENT_METHODS_URL
        self.is_public = True

    def all(self, data={}, **kwargs):
        """"
        Fetch all Payment Methods possible

        Returns:
            Dictionary of Payment Methods
        """
        return super(PaymentMethod, self).all(data, **kwargs)