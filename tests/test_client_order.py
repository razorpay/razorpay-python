import responses
import json

from .helpers import mock_file, ClientTestCase


class TestClientOrder(ClientTestCase):

    def setUp(self):
        super(TestClientOrder, self).setUp()
        self.base_url = '{}/orders'.format(self.base_url)

    @responses.activate
    def test_order_all(self):
        result = mock_file('order_collection')
        url = self.base_url
        responses.add(responses.GET, url, status=200,
                      body=json.dumps(result), match_querystring=True)
        self.assertEqual(self.client.order.all(), result)

    @responses.activate
    def test_order_all_with_options(self):
        count = 1
        result = mock_file('order_collection_with_one_order')
        url = '{}?count={}'.format(self.base_url, count)
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.order.all({'count': count}), result)

    @responses.activate
    def test_order_fetch(self):
        result = mock_file('fake_order')
        url = '{}/{}'.format(self.base_url, 'fake_order_id')
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.order.fetch('fake_order_id'), result)

    @responses.activate
    def test_order_payments(self):
        result = mock_file('fake_order')
        url = '{}/{}/payments'.format(self.base_url, 'fake_order_id')
        responses.add(responses.GET, url, status=200,
                      body=json.dumps(result), match_querystring=True)
        self.assertEqual(self.client.order.payments('fake_order_id'),
                         result)
