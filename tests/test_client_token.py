import responses
import json

from .helpers import mock_file, ClientTestCase


class TestClientCustomer(ClientTestCase):

    def setUp(self):
        super(TestClientCustomer, self).setUp()
        self.base_url = '{}/customers'.format(self.base_url)

    @responses.activate
    def test_tokens_all(self):
        result = mock_file('token_collection')
        url = '{}/{}/tokens'.format(self.base_url, self.customer_id)
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.token.all(self.customer_id),
                         result)

    @responses.activate
    def test_token_fetch(self):
        result = mock_file('token_collection')
        url = '{}/{}/tokens/{}'.format(self.base_url,
                                       self.customer_id,
                                       self.token_id)
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(
            self.client.token.fetch(self.customer_id, self.token_id),
            result)

    @responses.activate
    def test_token_delete(self):
        url = '{}/{}/tokens/{}'.format(self.base_url,
                                       self.customer_id,
                                       self.token_id)
        responses.add(responses.DELETE,
                      url,
                      status=200,
                      body=json.dumps({'deleted': True}),
                      match_querystring=True)
        self.assertEqual(
            self.client.token.delete(self.customer_id, self.token_id),
            {'deleted': True})
