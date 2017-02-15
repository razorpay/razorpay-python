import responses
import json

from .helpers import mock_file, ClientTestCase


class TestClientCard(ClientTestCase):

    def setUp(self):
        super(TestClientCard, self).setUp()
        self.base_url = '{}/cards'.format(self.base_url)

    @responses.activate
    def test_order_fetch(self):
        result = mock_file('fake_card')
        url = '{}/{}'.format(self.base_url, 'fake_card_id')
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.order.fetch('fake_card_id'), result)
