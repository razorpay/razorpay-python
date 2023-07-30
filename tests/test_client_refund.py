import responses
import json

from .helpers import mock_file, ClientTestCase


class TestClientRefund(ClientTestCase):

    def setUp(self):
        super(TestClientRefund, self).setUp()
        self.base_url = f'{self.base_url}/refunds'

    @responses.activate
    def test_refund_all(self):
        result = mock_file('refund_collection')
        url = self.base_url
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.refund.all(), result)

    @responses.activate
    def test_refund_fetch(self):
        result = mock_file('fake_refund')
        url = f'{self.base_url}/{self.refund_id}'
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.refund.fetch(self.refund_id), result)

    @responses.activate
    def test_refund_create(self):
        init = {'payment_id': self.payment_id}
        result = mock_file('fake_refund')
        url = self.base_url
        responses.add(responses.POST, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.refund.create(init), result)

    @responses.activate
    def test_refund_edit(self):
        param = {
            "notes": {
                "notes_key_1": "Beam me up Scotty.",
                "notes_key_2": "Engage"
            }
        }
        result = mock_file('fake_refund')
        url = f"{self.base_url}/rfnd_DfjjhJC6eDvUAi"
        responses.add(responses.PATCH, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.refund.edit(
            'rfnd_DfjjhJC6eDvUAi', param), result)
