from .helpers import *


class TestClientPayment(ClientTestCase):

    @responses.activate
    def test_payment_all(self):
        result = mock_file('payment_collection')
        responses.add(GET, 'https://api.razorpay.com/v1/payments', status=200, body=json.dumps(result), match_querystring=True)
        self.assertEqual(self.client.payment.all(), result)

    @responses.activate
    def test_payment_all_with_options(self):
        result = mock_file('payment_collection_with_one_payment')
        responses.add(GET, 'https://api.razorpay.com/v1/payments?count=1', status=200, body=json.dumps(result), match_querystring=True)
        self.assertEqual(self.client.payment.all(count=1), result)

    @responses.activate
    def test_payment_fetch(self):
        result = mock_file('fake_payment')
        responses.add(GET, 'https://api.razorpay.com/v1/payments/' + self.payment_id, status=200, body=json.dumps(result), match_querystring=True)
        self.assertEqual(self.client.payment.fetch('fake_payment_id'), result)

    @responses.activate
    def test_payment_capture(self):
        result = mock_file('fake_captured_payment')
        responses.add(POST, 'https://api.razorpay.com/v1/payments/' + self.payment_id + '/capture', status=200, body=json.dumps(result), match_querystring=True)
        self.assertEqual(self.client.payment.capture(self.payment_id, amount=5100), result)
