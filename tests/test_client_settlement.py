import responses
import json

from .helpers import mock_file, ClientTestCase


class TestClientSettlement(ClientTestCase):

    def setUp(self):
        super(TestClientSettlement, self).setUp()
        self.base_url = '{}/settlements'.format(self.base_url)

    @responses.activate
    def test_settlement_fetch_all(self):
        result = mock_file('settlement_collection')
        url = self.base_url
        responses.add(responses.GET, url, status=200,
                      body=json.dumps(result), match_querystring=True)
        self.assertEqual(self.client.settlement.all(), result)

    @responses.activate
    def test_settlement_fetch_all_with_options(self):
        count = 1
        result = mock_file('settlement_collection_with_one_settlement')
        url = '{}?count={}'.format(self.base_url, count)
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.settlement.all({'count': count}), result)

    @responses.activate
    def test_settlement_fetch(self):
        result = mock_file('fake_settlement')
        url = '{}/{}'.format(self.base_url, self.settlement_id)
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.settlement.fetch(self.settlement_id), result)

    @responses.activate
    def test_settlement_report(self):
        init = {"year":2020,"month":9}
        result = mock_file('settlement_collection')
        url = "{}/recon/{}".format(self.base_url, 'combined')
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.settlement.report(self.settlement_id), result)    

    @responses.activate
    def test_settlement_create_ondemand_settlement(self):
        init = {
                 "amount": 1221,
                 "description": "Need this to make vendor",
                 "notes": {
                     "notes_key_1": "Tea, Earl Grey, Hot",
                     "notes_key_2": "Tea, Earl Grey… decaf."
                 }
               }
        result = mock_file('init_settlement')
        url = "{}/{}".format(self.base_url,"ondemand")
        responses.add(responses.POST, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.settlement.create_ondemand_settlement(init), result)     

    @responses.activate
    def test_settlement_fetch_all_ondemand_settlement(self):
        result = mock_file('settlement_collection')
        url = "{}/{}".format(self.base_url,"ondemand")
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.settlement.fetch_all_ondemand_settlement(), result)        

    @responses.activate
    def test_settlement_fetch_ondemand_settlement_id(self):
        result = mock_file('init_settlement')
        url = "{}/ondemand/{}".format(self.base_url, 'fake_settlement_id')
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.settlement.fetch_ondemand_settlement_id('fake_settlement_id'), result)