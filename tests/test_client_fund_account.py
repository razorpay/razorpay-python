import responses
import json

from .helpers import mock_file, ClientTestCase


class TestClientFundAccount(ClientTestCase):

    def setUp(self):
        super(TestClientFundAccount, self).setUp()
        self.base_url = '{}/fund_accounts'.format(self.base_url)

    @responses.activate
    def test_fund_account_all(self):
        result = mock_file('fund_account_collection')
        url = self.base_url

        responses.add(responses.GET,
                      url,
                      status=200,
                      body=json.dumps(result),
                      match_querystring=True)

        self.assertEqual(self.client.fund_account.all(), result)

    @responses.activate
    def test_fund_account_all_with_options(self):
        count = 1
        result = mock_file('fund_account_collection_with_one_fund_account')
        url = '{}?count={}'.format(self.base_url, count)

        responses.add(responses.GET,
                      url, status=200,
                      body=json.dumps(result),
                      match_querystring=True)

        self.assertEqual(self.client.fund_account.all({'count': count}), result)

    @responses.activate
    def test_fund_account_fetch(self):
        result = mock_file('fake_fund_account')
        url = '{}/{}'.format(self.base_url, self.fund_account_id)

        responses.add(responses.GET,
                      url,
                      status=200,
                      body=json.dumps(result),
                      match_querystring=True)

        self.assertEqual(self.client.fund_account.fetch(self.fund_account_id), result)

    @responses.activate
    def test_fund_account_create(self):
        result = mock_file("fake_fund_account")
        url = self.base_url

        responses.add(responses.POST,
                      url,
                      status = 200,
                      body = json.dumps(result),
                      match_querystring = True)
        DATA = {
            "contact_id":"cont_HK9dzUuBsHhCtW",
            "account_type":"bank_account",
            "bank_account":{
                "name" : "abc" ,
                "account_number" : "123456",
                "ifsc" : "ABC"
            }
        }

        response = self.client.fund_account.create(data = DATA)

        self.assertEqual(response, result)

    @responses.activate
    def test_fund_account_update(self):
        result = mock_file("fake_fund_account")
        url = "{}/{}".format(self.base_url, self.fund_account_id)

        responses.add(responses.PATCH,
                      url,
                      status = 200,
                      body = json.dumps(result),
                      match_querystring = True)
        
        DATA = {
            "active" : True
        }

        response = self.client.fund_account.update(self.fund_account_id, data = DATA)

        self.assertEqual(response, result)

    @responses.activate
    def test_fund_account_validation(self):
        result = mock_file("fake_fund_account_validation")
        url = "{}/validations".format(self.base_url)

        responses.add(responses.POST,
                      url,
                      status = 200,
                      body = json.dumps(result),
                      match_querystring = True)
        
        DATA = {
            "fund_account": {
                "id": "fa_GygwgcU2kokIm1"
            },
            "notes":{
                "random_key_1": "Making the test in local.",
                "random_key_2": "locall 2."
            },
            "amount":100
        }

        response = self.client.fund_account.validation(data = DATA)

    @responses.activate
    def test_fund_account_all_validations(self):
        result = mock_file("fund_account_validation_collection")
        url = "{}/validations".format(self.base_url)

        responses.add(responses.GET,
                      url,
                      status=200,
                      body=json.dumps(result),
                      match_querystring=True)

        self.assertEqual(self.client.fund_account.all_validations(), result)

    @responses.activate
    def test_fund_account_all_validations_with_options(self):
        count = 1
        result = mock_file('fund_account_validation_collection_with_one_fund_account')
        url = '{}/validations?count={}'.format(self.base_url, count)

        responses.add(responses.GET,
                      url, status=200,
                      body=json.dumps(result),
                      match_querystring=True)

        self.assertEqual(self.client.fund_account.all_validations({"count": count}), result)


