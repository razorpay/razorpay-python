from .base import Resource


class Refund(Resource):
    def __init__(self, client=None):
        self.client = client
        self.base_url = "/payments"

    def all(self, payment_id, **kwargs):
        url = "{}/{}/refunds".format(self.base_url, payment_id)
        return self.get_url(url, **kwargs)

    def fetch(self, payment_id, refund_id, **kwargs):
        url = "{}/{}/refunds/{}".format(self.base_url, payment_id, refund_id)
        return self.get_url(url, **kwargs)

