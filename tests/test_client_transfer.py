import responses
import json

from .helpers import mock_file, ClientTestCase


class TestClientTransfer(ClientTestCase):

    def setUp(self):
        super(TestClientTransfer, self).setUp()
        self.base_url = '{}/transfers'.format(self.base_url)

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
    def test_transfer_fetch(self):
        result = mock_file('fake_transfer')
        url = '{}/{}'.format(self.base_url, 'fake_transfer_id')
        responses.add(responses.GET,
                      url,
                      status=200,
                      body=json.dumps(result),
                      match_querystring=True)

        self.assertEqual(self.client.transfer.fetch('fake_transfer_id'), result)

    @responses.activate
    def test_transfer_create(self):
        init = mock_file('init_transfer')
        result = mock_file('fake_transfer')
        url = self.base_url
        responses.add(responses.POST, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.transfer.create(init), result)
