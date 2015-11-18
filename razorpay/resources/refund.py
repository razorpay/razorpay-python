class Refund:

    def __init__(self, client=None):
        self.client = client

    def all(self, payment_id, **options):
        return self.client.get('/payments/' + payment_id + '/refunds', **options)

    def fetch(self, payment_id, refund_id, **options):
        return self.client.get('/payments/' + payment_id + '/refunds/' + refund_id, **options)

    def create(self, payment_id, data, **options):
        return self.client.post('/payments/' + payment_id + '/refund', data, **options)
