import responses
import json

from .helpers import mock_file, ClientTestCase


class TestClientTransaction(ClientTestCase):

    def setUp(self):
        super(TestClientTransaction, self).setUp()
        self.base_url = '{}/transactions'.format(self.base_url)

    @responses.activate
    def test_transactions_all_with_options(self):
        result = mock_file("transactions_collection")
        count = 3
        account_number = "12345"
        url = "{}?account_number={}&count={}".format(self.base_url,
                                                      account_number,
                                                      count)

        responses.add(responses.GET,
                      url,
                      body = json.dumps(result),
                      match_querystring = True)

        DATA = {
            "account_number": account_number,
            "count" : 3
        }

        self.assertEqual(self.client.transaction.all(data = DATA), result)

    @responses.activate
    def test_transaction_fetch(self):
        result = mock_file("fake_transaction")
        url = "{}/{}".format(self.base_url, self.transaction_id)

        responses.add(responses.GET,
                      url,
                      body = json.dumps(result),
                      match_querystring = True)

        self.assertEqual(self.client.transaction.fetch(self.transaction_id), result)
