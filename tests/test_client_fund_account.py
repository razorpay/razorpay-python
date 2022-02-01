import responses
import json

from .helpers import mock_file, ClientTestCase


class TestClientFundAccount(ClientTestCase):

    def setUp(self):
        super(TestClientFundAccount, self).setUp()
        self.base_url = '{}/fund_accounts'.format(self.base_url)

    @responses.activate
    def test_all(self):
        result = mock_file('fund_account_collection')
        url = self.base_url
        responses.add(responses.GET, url, status=200,
                      body=json.dumps(result), match_querystring=True)
        self.assertEqual(self.client.fund_account.all(), result)

    @responses.activate
    def test_create(self):
        param = {
            "customer_id": "cust_IEfAt3ruD4OEzo",
            "account_type":"bank_account",
            "bank_account":{
                "name":"Gaurav Kumar",
                "account_number":"11214311215411",
                "ifsc":"HDFC0000053"
            }
        }
        result = mock_file('fund_account_collection')
        url = self.base_url
        responses.add(responses.POST,
                      url,
                      status=200,
                      body=json.dumps(result),
                      match_querystring=True)

        self.assertEqual(self.client.fund_account.create(param), result)
 