from .base import Resource


class Order(Resource):
    def __init__(self, client=None):
        self.client = client
        self.base_url = "/order"

    def all(self, payment_id, **kwargs):
        url = self.base_url
        return self.get_url(url, **kwargs)

    def fetch(self, order_id, **kwargs):
        url = "{}/{}".format(self.base_url, order_id)
        return self.get_url(url, **kwargs)

    def payments(self, order_id, **kwargs):
        url = "{}/{}/payments".format(self.base_url, order_id)
        return self.get_url(url, **kwargs)

    def create(self, data={}, **kwargs):
        url = self.base_url
        return self.post_url(url, data, **kwargs)
