import responses
import json

from .helpers import mock_file, ClientTestCase


class TestClientItem(ClientTestCase):

    def setUp(self):
        super(TestClientItem, self).setUp()
        self.base_url = f'{self.base_url}/items'

    @responses.activate
    def test_item_all(self):
        result = mock_file('item_collection')
        url = self.base_url
        responses.add(responses.GET, url, status=200,
                      body=json.dumps(result), match_querystring=True)
        self.assertEqual(self.client.item.all(), result)

    @responses.activate
    def test_item_fetch(self):
        result = mock_file('item_collection')
        url = self.base_url
        responses.add(responses.GET, url, status=200,
                      body=json.dumps(result), match_querystring=True)
        self.assertEqual(self.client.item.all(), result)

    @responses.activate
    def test_item_create(self):
        result = mock_file('item_collection')
        url = f'{self.base_url}/fake_item_id'
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.item.fetch('fake_item_id'), result)

    @responses.activate
    def test_item_delete(self):
        result = []
        url = f'{self.base_url}/fake_item_id'
        responses.add(responses.DELETE, url, status=200,
                      body=json.dumps(result), match_querystring=True)
        self.assertEqual(self.client.item.delete('fake_item_id'), result)
