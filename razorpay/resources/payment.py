from .base import Resource


class Payment(Resource):
    def __init__(self, client=None):
        self.client = client
        self.base_url = "/payments"

    def all(self, **kwargs):
        url = self.base_url
        return self.get_url(url, **kwargs)

    def fetch(self, payment_id, **kwargs):
        url = "{}/{}".format(self.base_url, payment_id)
        return self.get_url(url, **kwargs)

    def capture(self, payment_id, amount, **kwargs):
        url = "{}/{}/capture".format(self.base_url, payment_id)
        data = {'amount': amount}
        return self.post_url(url, data, **kwargs)

    def refund(self, payment_id, amount, **kwargs):
        url = "{}/{}/refund".format(self.base_url, payment_id)
        data = {'amount': amount}
        return self.post_url(url, data, **kwargs)

    def refunds(self, payment_id, **kwargs):
        url = "{}/{}/refunds".format(self.base_url, payment_id)
        return self.get_url(url, **kwargs)
