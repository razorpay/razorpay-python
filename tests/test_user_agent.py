import responses
import json

from .helpers import mock_file, ClientTestCase


class TestClientUserAgent(ClientTestCase):

    def setUp(self):
        super(TestClientUserAgent, self).setUp()
        app_details = json.loads(mock_file('fake_app_details'))
        self.client.set_app_details(app_details)
        self.base_url = f"{self.base_url}/payments"

    @responses.activate
    def test_payment_all(self):
        result = mock_file('payment_collection')
        url = self.base_url
        responses.add(responses.GET, url, status=200,
                      body=json.dumps(result), match_querystring=True)
        self.assertEqual(self.client.payment.all(), result)
