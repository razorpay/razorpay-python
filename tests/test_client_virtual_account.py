import unittest
import responses
import json
from .helpers import mock_file, ClientTestCase


class TestClientVirtualAccount(ClientTestCase):

    def setUp(self):
        super(TestClientVirtualAccount, self).setUp()
        self.base_url = '{}/virtual_accounts'.format(self.base_url)
        self.fake_virtual_account_id = 'va_4xbQrmEoA5WJ0G'

    @responses.activate
    def test_virtual_accounts_create(self):
        init = mock_file('init_virtual_accounts')
        result = mock_file('fake_virtual_accounts')
        url = self.base_url
        responses.add(responses.POST, url, status=200, body=result,
                      match_querystring=True)

        response = self.client.virtual_account.create(init)
        self.assertEqual(response['description'], 'First Virtual Account')
        self.assertEqual(response['status'], 'active')
        self.assertEqual(response['amount_paid'], 0)
        self.assertIsNotNone(response['receivers'][0]['account_number'])

    @responses.activate
    def test_virtual_accounts_all(self):
        result = mock_file('virtual_accounts_collection')
        url = self.base_url
        responses.add(responses.GET,
                      url,
                      status=200,
                      body=result,
                      match_querystring=True)

        response = self.client.virtual_account.all()
        self.assertEqual(response['entity'], 'collection')
        self.assertEqual(response['count'], 2)
        self.assertEqual(len(response['items']), 2)

    @responses.activate
    def test_virtual_accounts_all_with_options(self):
        count = 1
        result = mock_file('virtual_accounts_collection_with_one_item')
        url = '{}?count={}'.format(self.base_url, count)
        responses.add(responses.GET,
                      url,
                      status=200,
                      body=result,
                      match_querystring=True)

        response = self.client.virtual_account.all({'count': count})
        self.assertEqual(response['entity'], 'collection')
        self.assertEqual(response['count'], count)

    @responses.activate
    def test_virtual_accounts_fetch(self):
        result = mock_file('fake_virtual_accounts')
        url = '{}/{}'.format(self.base_url, self.fake_virtual_account_id)
        responses.add(responses.GET,
                      url,
                      status=200,
                      body=result,
                      match_querystring=True)

        response = self.client.virtual_account.fetch(
            self.fake_virtual_account_id)
        self.assertEqual(response['id'], self.fake_virtual_account_id)
        self.assertEqual(response['entity'], 'virtual_account')
        self.assertIsNotNone(response['receivers'][0]['account_number'])

    @responses.activate
    def test_virtual_accounts_close(self):
        result = mock_file('fake_virtual_accounts_closed')
        url = '{}/{}/close'.format(self.base_url, self.fake_virtual_account_id)
        responses.add(responses.POST,
                      url,
                      status=200,
                      body=result,
                      match_querystring=True)

        response = self.client.virtual_account.close(
            self.fake_virtual_account_id)
        self.assertEqual(response['id'], self.fake_virtual_account_id)
        self.assertEqual(response['entity'], 'virtual_account')
        self.assertEqual(response['status'], 'closed')

    @responses.activate
    def test_virtual_accounts_payments(self):
        result = mock_file('payment_collection')
        url = '{}/{}/payments'.format(
            self.base_url,
            self.fake_virtual_account_id)
        responses.add(responses.GET,
                      url,
                      status=200,
                      body=result,
                      match_querystring=True)

        response = self.client.virtual_account.payments(
            self.fake_virtual_account_id)
        self.assertEqual(response['entity'], 'collection')
        self.assertEqual(response['count'], 2)
        self.assertEqual(len(response['items']), 2)
        self.assertEqual(response['items'][0]['entity'], 'payment')
    
    @responses.activate
    def test_virtual_add_receiver(self):
        init =  {
                  "types": ["vpa"],
                  "vpa": {
                      "descriptor": "gaurikumar"
                   }
                }
        result = mock_file('fake_virtual_accounts_closed')
        url = "{}/{}/receivers".format(self.base_url, self.fake_virtual_account_id)
        responses.add(responses.POST,
                      url,
                      status=200,
                      body=result,
                      match_querystring=True)

        response = self.client.virtual_account.add_receiver(
            self.fake_virtual_account_id, init)
        self.assertEqual(response['id'], self.fake_virtual_account_id)
        self.assertEqual(response['entity'], 'virtual_account')

    @responses.activate
    def test_virtual_add_allowed_player(self):
        init =  {
                  "type": "bank_account",
                  "bank_account": {
                      "ifsc": "UTIB0000013",
                      "account_number": "914010012345679"
                    }
                }
        result = mock_file('fake_virtual_accounts_closed')
        url = "{}/{}/allowed_payers".format(self.base_url, self.fake_virtual_account_id)
        responses.add(responses.POST,
                      url,
                      status=200,
                      body=result,
                      match_querystring=True)

        response = self.client.virtual_account.add_allowed_player(
            self.fake_virtual_account_id, init)   
        self.assertEqual(response['id'], self.fake_virtual_account_id)
        self.assertEqual(response['entity'], 'virtual_account')

   
    @unittest.skip
    def test_virtual_delete_allowed_player(self):
        result = mock_file('fake_delete_allowed_payer')
        url = "{}/{}/allowed_payers/{}".format(self.base_url, self.fake_virtual_account_id, 'fake_allowed_player_id')
        responses.add(responses.DELETE,
                      url,
                      status=204,
                      body=result,
                      match_querystring=True)
        response = self.client.virtual_account.delete_allowed_player(
        self.fake_virtual_account_id, 'fake_allowed_player_id');   
        self.assertEqual(response, result)
          
