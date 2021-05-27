import responses
import json

from .helpers import mock_file, ClientTestCase


class TestClientRefund(ClientTestCase):

    def setUp(self):
        super(TestClientRefund, self).setUp()
        self.payment_url = '{}/payments'.format(self.base_url)
        self.base_url = '{}/refunds'.format(self.base_url)

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
        url = '{}/{}'.format(self.base_url, self.refund_id)
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.refund.fetch(self.refund_id), result)

    @responses.activate
    def test_refund_fetch_for_payment(self):
        result = mock_file('fake_refund')
        url = '{}/{}/refunds'.format(self.payment_url,
                                     self.payment_id)
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.refund.fetch_for_payment(
            self.payment_id), result)

    @responses.activate
    def test_refund_create(self):
        init = {'payment_id': self.payment_id}
        result = mock_file('fake_refund')
        url = self.base_url
        responses.add(responses.POST, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.refund.create(init), result)
