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
    def test_invoice_fetch(self):
        result = mock_file('fake_settlement')
        url = '{}/{}'.format(self.base_url, self.settlement_id)
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.settlement.fetch(self.settlement_id), result)
