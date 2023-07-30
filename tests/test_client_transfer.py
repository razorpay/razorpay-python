import responses
import json

from .helpers import mock_file, ClientTestCase


class TestClientTransfer(ClientTestCase):

    def setUp(self):
        super(TestClientTransfer, self).setUp()
        self.payment_url = f"{self.base_url}/payments"
        self.base_url = f"{self.base_url}/transfers"

    @responses.activate
    def test_transfer_all(self):
        result = mock_file('transfers_collection')
        url = self.base_url
        responses.add(responses.GET,
                      url,
                      status=200,
                      body=json.dumps(result),
                      match_querystring=True)

        self.assertEqual(self.client.transfer.all(), result)

    @responses.activate
    def test_transfer_all_with_payment_id(self):
        result = mock_file('transfers_collection_with_payment_id')
        url = f"{self.payment_url}/dummy_payment/transfers"
        responses.add(responses.GET,
                      url,
                      status=200,
                      body=json.dumps(result),
                      match_querystring=True)

        self.assertEqual(self.client.transfer.all(
            {'payment_id': 'dummy_payment'}),
            result)

    @responses.activate
    def test_transfer_fetch(self):
        result = mock_file('fake_transfer')
        url = f"{self.base_url}/fake_transfer_id"
        responses.add(responses.GET,
                      url,
                      status=200,
                      body=json.dumps(result),
                      match_querystring=True)

        self.assertEqual(self.client.transfer.fetch(
            'fake_transfer_id'), result)

    @responses.activate
    def test_transfer_create(self):
        init = mock_file('init_transfer')
        result = mock_file('fake_transfer')
        url = self.base_url
        responses.add(responses.POST, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.transfer.create(init), result)

    @responses.activate
    def test_transfer_edit(self):
        param = {'on_hold': False}
        result = mock_file('fake_transfer')
        url = f"{self.base_url}/dummy_id"
        responses.add(responses.PATCH, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.transfer.edit('dummy_id', param), result)

    @responses.activate
    def test_transfer_reversal(self):
        result = mock_file('fake_reversal')
        url = f"{self.base_url}/dummy_id/reversals"
        responses.add(responses.POST, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.transfer.reverse('dummy_id'), result)

    @responses.activate
    def test_transfer_reversal_fetch(self):
        result = mock_file('reversal_collection')
        url = f"{self.base_url}/dummy_id/reversals"
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.transfer.reversals('dummy_id'), result)
