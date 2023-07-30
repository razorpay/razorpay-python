import responses
import json

from .helpers import mock_file, ClientTestCase


class TestClientPayment(ClientTestCase):

    def setUp(self):
        super(TestClientPayment, self).setUp()
        self.base_url = f'{self.base_url}/payments'
        self.secondary_base_url = f'{self.secondary_url}/payments'

    @responses.activate
    def test_payment_primary_url(self):
        result = mock_file('payment_collection')
        url = self.base_url
        responses.add(responses.GET, url, status=200,
                      body=json.dumps(result), match_querystring=True)
        self.assertEqual(self.client.payment.all(), result)

    @responses.activate
    def test_payment_secondary_url(self):
        result = mock_file('payment_collection')
        url = self.secondary_base_url
        responses.add(responses.GET, url, status=200,
                      body=json.dumps(result), match_querystring=True)
        self.assertEqual(self.secondary_client.payment.all(), result)

    @responses.activate
    def test_payment_with_headers(self):
        result = mock_file('payment_collection')
        url = self.base_url
        responses.add(responses.GET, url, status=200,
                      body=json.dumps(result), match_querystring=True)
        self.assertEqual(self.client.payment.all(
            headers={'Content-type': 'text'}),
            result)
