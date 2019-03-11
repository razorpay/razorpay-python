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

    @responses.activate
    def test_invoice_create(self):
        init = mock_file('init_invoice')
        result = mock_file('fake_invoice')
        url = self.base_url
        responses.add(responses.POST, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.invoice.create(init), result)

    @responses.activate
    def test_invoice_notify_by(self):
        medium = "sms"
        result = mock_file('fake_invoice_notify_by')
        url = '{}/{}/notify_by/{}'.format(self.base_url, 'fake_invoice_id', medium)
        responses.add(responses.POST, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.invoice.notify_by('fake_invoice_id', medium=medium), result)

    @responses.activate
    def test_invoice_cancel(self):
        result = mock_file('fake_invoice_cancel')
        url = '{}/{}/cancel'.format(self.base_url, 'fake_invoice_id')
        responses.add(responses.POST, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.invoice.cancel('fake_invoice_id'), result)

    @responses.activate
    def test_invoice_delete(self):
        result = mock_file('fake_invoice_delete')
        url = '{}/{}'.format(self.base_url, 'fake_invoice_id')
        responses.add(responses.DELETE, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.invoice.delete('fake_invoice_id'), result)

    @responses.activate
    def test_invoice_issue(self):
        result = mock_file('fake_invoice')
        url = '{}/{}/issue'.format(self.base_url, 'fake_invoice_id')
        responses.add(responses.POST, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.invoice.issue('fake_invoice_id'), result)

    @responses.activate
    def test_invoice_edit(self):
        init = mock_file('init_invoice_edit')
        result = mock_file('fake_invoice_edit')
        url = '{}/{}'.format(self.base_url, 'fake_invoice_id')
        responses.add(responses.PATCH, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.invoice.edit('fake_invoice_id', init), result)
