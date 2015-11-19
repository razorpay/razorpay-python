from .helpers import *


class TestClientRefund(ClientTestCase):

    @responses.activate
    def test_refund_all(self):
        result = mock_file('refund_collection')
        responses.add(GET, 'https://api.razorpay.com/v1/payments/' + self.payment_id + '/refunds', status=200, body=json.dumps(result), match_querystring=True)
        self.assertEqual(self.client.refund.all(self.payment_id), result)

    @responses.activate
    def test_refund_fetch(self):
        result = mock_file('fake_refund')
        responses.add(GET, 'https://api.razorpay.com/v1/payments/' + self.payment_id + '/refunds/' + self.refund_id, status=200, body=json.dumps(result), match_querystring=True)
        self.assertEqual(self.client.refund.fetch(self.payment_id, self.refund_id), result)

    @responses.activate
    def test_refund_create(self):
        result = mock_file('fake_refund')
        responses.add(POST, 'https://api.razorpay.com/v1/payments/' + self.payment_id + '/refund', status=200, body=json.dumps(result), match_querystring=True)
        self.assertEqual(self.client.refund.create(self.payment_id), result)

    @responses.activate
    def test_refund_create_partial(self):
        result = mock_file('fake_refund')
        responses.add(POST, 'https://api.razorpay.com/v1/payments/' + self.payment_id + '/refund', status=200, body=json.dumps(result), match_querystring=True)
        self.assertEqual(self.client.refund.create(self.payment_id, {'amount': 2000}), result)
