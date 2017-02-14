from .base import Resource
from .Url import URL


class Order(Resource):
    def __init__(self, client=None):
        self.client = client
        self.base_url = URL.ORDER_URL

    def all(self, **kwargs):
        """"
        Fetch all Order entities

        Returns:
            Dictionary of Order data
        """
        return super(Order, self).all(**kwargs)

    def fetch(self, order_id, **kwargs):
        """"
        Fetch Order for given Id

        Args:
            order_id : Id for which order object has to be retrieved

        Returns:
            Order dict for given order Id
        """
        return super(Order, self).fetch(order_id, **kwargs)

    def payments(self, order_id, **kwargs):
        """"
        Fetch Payment for Order Id

        Args:
            order_id : Id for which payment objects has to be retrieved

        Returns:
            Payment dict for given Order Id
        """
        url = "{}/{}/payments".format(self.base_url, order_id)
        return self.get_url(url, **kwargs)

    def create(self, data={}, **kwargs):
        """"
        Create Order from given dict

        Args:
            data : Dictionary having keys using which order have to be created
                'amount' :  Amount of Order
                'currency' : Currency used in Order
                'receipt' : Receipt Id for the order
                'notes' : key value pair as notes
                'payment_capture': 0/1 if payment should be auto captured or not

        Returns:
            Order Dict which was created
        """
        url = self.base_url
        return self.post_url(url, data, **kwargs)
