import responses
import json

from razorpay.constants.url import URL

from .helpers import mock_file, ClientTestCase


class TestClientProduct(ClientTestCase):

    def setUp(self):
        super(TestClientProduct, self).setUp()
        self.base_url = '{}/accounts'.format(self.base_url_v2)
        self.account_id = 'acc_GRWKk7qQsLnDjX'
        self.product_id = 'acc_prd_HEgNpywUFctQ9e'

    @responses.activate
    def test_product_requestProductConfiguration(self):
        init = {
            "product_name": "payment_gateway",
            "tnc_accepted": True,
            "ip": "233.233.233.234"
        }
        result = mock_file('fake_product')
        url = '{}/{}{}'.format(self.base_url, self.account_id, URL.PRODUCT)

        responses.add(responses.POST,
                      url,
                      status=200,
                      body=json.dumps(result),
                      match_querystring=True)

        self.assertEqual(self.client.product.requestProductConfiguration(
            self.account_id, init), result)

    @responses.activate
    def test_product_fetch(self):
        result = mock_file('fake_product')
        url = '{}/{}{}/{}'.format(self.base_url,
                                  self.account_id, URL.PRODUCT, self.product_id)
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.product.fetch(
            self.account_id, self.product_id), result)

    @responses.activate
    def test_account_edit(self):
        init = {
            "notifications": {
                "email": [
                    "gaurav.kumar@example.com",
                    "acd@gmail.com"
                ]
            },
            "checkout": {
                "theme_color": "#528FFF"
            },
            "refund": {
                "default_refund_speed": "optimum"
            },
            "settlements": {
                "account_number": "1234567890",
                "ifsc_code": "HDFC0000317",
                "beneficiary_name": "Gaurav Kumar"
            },
            "tnc_accepted": True,
            "ip": "233.233.233.234"
        }

        result = mock_file('fake_account')
        url = '{}/{}{}/{}'.format(self.base_url,
                                  self.account_id, URL.PRODUCT, self.product_id)

        responses.add(responses.PATCH, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.product.edit(
            self.account_id, self.product_id, init), result)

    @responses.activate
    def test_product_fetchTnc(self):
        result = {
            "entity": "tnc_map",
            "product_name": "payments",
            "id": "tnc_map_HjOVhIdpVDZ0FB",
            "tnc": {
                "terms": "https://razorpay.com/terms",
                "privacy": "https://razorpay.com/privacy",
                "agreement": "https://razorpay.com/agreement"
            },
            "last_published_at": 1640589653
        }
        product_name = "payments"

        url = '{}{}/{}{}'.format(self.base_url_v2, URL.PRODUCT, product_name, URL.TNC )

        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                        match_querystring=True)
        self.assertEqual(self.client.product.fetchTnc(product_name), result)
