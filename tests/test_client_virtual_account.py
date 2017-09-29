import responses
import json

from .helpers import mock_file, ClientTestCase


class TestClientVirtualAccount(ClientTestCase):

    def setUp(self):
        super(TestClientVirtualAccount, self).setUp()
        self.base_url = '{}/virtual_accounts'.format(self.base_url)

    @responses.activate
    def test_virtual_accounts_all(self):
        result = mock_file('virtual_accounts_collection')
        url = self.base_url
        responses.add(responses.GET,
                      url,
                      status=200,
                      body=json.dumps(result),
                      match_querystring=True)

        self.assertEqual(self.client.virtual_account.all(), result)

    @responses.activate
    def test_virtual_accounts_all_with_options(self):
        count = 1
        result = mock_file('virtual_accounts_collection_with_one_item')
        url = '{}?count={}'.format(self.base_url, count)
        responses.add(responses.GET,
                      url,
                      status=200,
                      body=json.dumps(result),
                      match_querystring=True)

        self.assertEqual(self.client.virtual_account.all(
            {'count': count}),
            result)

    @responses.activate
    def test_virtual_accounts_fetch(self):
        result = mock_file('fake_virtual_accounts')
        url = '{}/{}'.format(self.base_url, 'fake_virtual_accounts_id')
        responses.add(responses.GET,
                      url,
                      status=200,
                      body=json.dumps(result),
                      match_querystring=True)

        self.assertEqual(self.client.virtual_account.fetch(
            'fake_virtual_accounts_id'),
            result)

    @responses.activate
    def test_virtual_accounts_close(self):
        result = mock_file('fake_virtual_accounts')
        url = '{}/{}'.format(self.base_url, 'fake_virtual_accounts_id')
        responses.add(responses.PATCH,
                      url,
                      status=200,
                      body=json.dumps(result),
                      match_querystring=True)

        self.assertEqual(self.client.virtual_account.close(
            'fake_virtual_accounts_id'),
            result)

    @responses.activate
    def test_virtual_accounts_payments(self):
        result = mock_file('fake_payment')
        url = '{}/{}/payments'.format(self.base_url, 'fake_virtual_accounts_id')
        responses.add(responses.GET,
                      url,
                      status=200,
                      body=json.dumps(result),
                      match_querystring=True)

        self.assertEqual(self.client.virtual_account.payments(
            'fake_virtual_accounts_id'),
            result)

    @responses.activate
    def test_virtual_accounts_create(self):
        init = mock_file('init_virtual_accounts')
        result = mock_file('fake_virtual_accounts')
        url = self.base_url
        responses.add(responses.POST, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.virtual_account.create(init), result)
