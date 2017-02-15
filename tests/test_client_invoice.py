import responses
import json

from .helpers import mock_file, ClientTestCase


class TestClientInvoice(ClientTestCase):

    def setUp(self):
        super(TestClientInvoice, self).setUp()
        self.base_url = '{}/invoices'.format(self.base_url)

    @responses.activate
    def test_invoice_fetch_all(self):
        result = mock_file('invoice_collection')
        url = self.base_url
        responses.add(responses.GET, url, status=200,
                      body=json.dumps(result), match_querystring=True)
        self.assertEqual(self.client.invoice.all(), result)

    @responses.activate
    def test_invoice_fetch_all_with_options(self):
        count = 1
        result = mock_file('invoice_collection_with_one_invoice')
        url = '{}?count={}'.format(self.base_url, count)
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.invoice.all({'count': count}), result)

    @responses.activate
    def test_invoice_fetch(self):
        result = mock_file('fake_invoice')
        url = '{}/{}'.format(self.base_url, 'fake_invoice_id')
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.invoice.fetch('fake_invoice_id'), result)
