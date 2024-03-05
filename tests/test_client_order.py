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
        responses.add(responses.GET,
                      url,
                      status=200,
                      body=json.dumps(result),
                      match_querystring=True)

        self.assertEqual(self.client.order.all(), result)

    @responses.activate
    def test_order_all_with_options(self):
        count = 1
        result = mock_file('order_collection_with_one_order')
        url = '{}?count={}'.format(self.base_url, count)
        responses.add(responses.GET,
                      url,
                      status=200,
                      body=json.dumps(result),
                      match_querystring=True)

        self.assertEqual(self.client.order.all({'count': count}), result)

    @responses.activate
    def test_order_fetch(self):
        result = mock_file('fake_order')
        url = '{}/{}'.format(self.base_url, 'fake_order_id')
        responses.add(responses.GET,
                      url,
                      status=200,
                      body=json.dumps(result),
                      match_querystring=True)

        self.assertEqual(self.client.order.fetch('fake_order_id'), result)

    @responses.activate
    def test_order_payments(self):
        result = mock_file('fake_order')
        url = '{}/{}/payments'.format(self.base_url, 'fake_order_id')
        responses.add(responses.GET,
                      url,
                      status=200,
                      body=json.dumps(result),
                      match_querystring=True)

        self.assertEqual(self.client.order.payments('fake_order_id'), result)

    @responses.activate
    def test_order_create(self):
        init = mock_file('init_order')
        result = mock_file('fake_order')
        url = self.base_url
        responses.add(responses.POST, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.order.create(init), result)

    @responses.activate
    def test_order_edit(self):
        param = {
                  "notes": {
                    "key1": "value3",
                    "key2": "value2"
                   }
                }
        
        result = mock_file('edit_order')
        url = '{}/{}'.format(self.base_url, 'dummy_id')
        responses.add(responses.PATCH, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.order.edit('dummy_id', param), result)

    @responses.activate
    def test_order_view_rto_review(self):
        result = mock_file('rto')
        url = '{}/{}/rto_review'.format(self.base_url, 'fake_order_id')
        responses.add(responses.POST, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.order.viewRtoReview('fake_order_id'), result)

    @responses.activate
    def test_order_edit_fulfillment(self):
        request = {
            "payment_method": "upi",
            "shipping": {
                "waybill": "123456789",
                "status": "rto",
                "provider": "Bluedart"
            }
        }
        result = mock_file('fulfillment')
        url = '{}/{}/fulfillment'.format(self.base_url, 'fake_order_id')
        responses.add(responses.POST, url, status=200, body=json.dumps(result),
                      match_querystring=True)            
        self.assertEqual(self.client.order.editFulfillment('fake_order_id', request), result)