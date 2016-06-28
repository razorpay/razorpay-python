import responses
import json

from .helpers import mock_file, ClientTestCase


class TestClientRefund(ClientTestCase):

    def setUp(self):
        super(TestClientRefund, self).setUp()
        self.base_url = '{}/payments'.format(self.base_url)

    @responses.activate
    def test_refund_all(self):
        result = mock_file('refund_collection')
        url = '{}/{}/refunds'.format(self.base_url, self.payment_id)
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.refund.all(self.payment_id), result)

    @responses.activate
    def test_refund_fetch(self):
        result = mock_file('fake_refund')
        url = '{}/{}/refunds/{}'.format(self.base_url,
                                        self.payment_id, self.refund_id)
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.refund.fetch(self.payment_id,
                                                  self.refund_id), result)
