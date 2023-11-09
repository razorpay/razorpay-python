import responses
import json

from .helpers import mock_file, ClientTestCase


class TestClientAccount(ClientTestCase):

    def setUp(self):
        super(TestClientAccount, self).setUp()
        self.base_url = '{}/accounts'.format(self.base_url_v2)
        self.account_id = 'acc_GRWKk7qQsLnDjX'

    @responses.activate
    def test_account_create(self):
        init = mock_file('init_account')
        result = mock_file('fake_account')
        url = self.base_url
        responses.add(responses.POST,
                      url,
                      status=200,
                      body=json.dumps(result),
                      match_querystring=True)

        self.assertEqual(self.client.account.create(init), result)
    
    @responses.activate
    def test_account_fetch(self):
        result = mock_file('fake_account')
        url = '{}/{}'.format(self.base_url, self.account_id)
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.account.fetch(self.account_id), result)

    @responses.activate
    def test_account_edit(self):
        init = { "customer_facing_business_name": "ABCD Ltd" }
        result = mock_file('fake_account')
        url = '{}/{}'.format(self.base_url, self.account_id)
        responses.add(responses.PATCH, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.account.edit(self.account_id, init), result)        
        
    @responses.activate
    def test_account_delete(self):
        result = mock_file('fake_account')
        url = '{}/{}'.format(self.base_url, self.account_id)
        responses.add(responses.DELETE, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.account.delete(self.account_id), result)