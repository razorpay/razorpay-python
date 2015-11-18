class Payment:

    def __init__(self, client=None):
        self.client = client

    def all(self, **options):
        return self.client.get('/payments', **options)

    def fetch(self, payment_id, **options):
        return self.client.get('/payments/' + payment_id, **options)

    def capture(self, payment_id, **options):
        return self.client.post('/payments/' + payment_id + '/capture', **options)
