import responses
import json

from razorpay.constants.url import URL

from .helpers import mock_file, ClientTestCase


class TestClientCustomer(ClientTestCase):

    def setUp(self):
        super(TestClientCustomer, self).setUp()
        self.url = self.base_url
        self.base_url = '{}/customers'.format(self.base_url)

    @responses.activate
    def test_tokens_all(self):
        result = mock_file('token_collection')
        url = '{}/{}/tokens'.format(self.base_url, self.customer_id)
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.token.all(self.customer_id),
                         result)

    @responses.activate
    def test_token_fetch(self):
        result = mock_file('token_collection')
        url = '{}/{}/tokens/{}'.format(self.base_url,
                                       self.customer_id,
                                       self.token_id)
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(
            self.client.token.fetch(self.customer_id, self.token_id),
            result)

    @responses.activate
    def test_token_delete(self):
        url = '{}/{}/tokens/{}'.format(self.base_url,
                                       self.customer_id,
                                       self.token_id)
        responses.add(responses.DELETE,
                      url,
                      status=200,
                      body=json.dumps({'deleted': True}),
                      match_querystring=True)
        self.assertEqual(
            self.client.token.delete(self.customer_id, self.token_id),
            {'deleted': True})

    @responses.activate
    def test_token_create(self):
        init = {
            "customer_id": "cust_1Aa00000000001",
            "method": "card",
            "card": {
                "number": "4111111111111111",
                "cvv": "123",
                "expiry_month": "12",
                "expiry_year": "21",
                "name": "Gaurav Kumar"
            },
            "authentication": {
                "provider": "razorpay",
                "provider_reference_id": "pay_123wkejnsakd",
                "authentication_reference_number": "100222021120200000000742753928"
            },
            "notes": []
        }
        result = mock_file('fake_merchant_token')
        url = '{}{}'.format(self.url, URL.TOKEN)
        responses.add(responses.POST, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.token.create(init), result)

    @responses.activate
    def test_token_fetchToken(self):
        init = {
            "id": "token_4lsdksD31GaZ09"
        }
        result = mock_file('fake_merchant_token')
        url = '{}{}/{}'.format(self.url, URL.TOKEN, "fetch")
        responses.add(responses.POST, url, status=200, body=json.dumps(result))
        self.assertEqual(
            self.client.token.fetchToken(init),
            result)

    @responses.activate
    def test_token_processPaymentOnAlternatePAorPG(self):
        init = {
            "id": "spt_4lsdksD31GaZ09"
        }
        result = {
            "card": {
                "number": "4111111111111111",
                "expiry_month": "12",
                "expiry_year": 2030
            }
        }

        url = '{}{}/{}'.format(self.url, URL.TOKEN, "service_provider_tokens/token_transactional_data")
        responses.add(responses.POST, url, status=200, body=json.dumps(result), match_querystring=True)
        self.assertEqual(
            self.client.token.processPaymentOnAlternatePAorPG(init),
            result)
