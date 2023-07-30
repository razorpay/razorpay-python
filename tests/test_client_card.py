import responses
import json

from .helpers import mock_file, ClientTestCase


class TestClientRefund(ClientTestCase):

    def setUp(self):
        super(TestClientRefund, self).setUp()
        self.base_url = f'{self.base_url}/cards'

    @responses.activate
    def test_card_fetch(self):
        result = mock_file('fake_card')
        url = f'{self.base_url}/{self.card_id}'
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.card.fetch(self.card_id), result)
