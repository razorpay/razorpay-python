import responses
import json

from .helpers import mock_file, ClientTestCase


class TestClientIin(ClientTestCase):

    def setUp(self):
        super(TestClientIin, self).setUp()
        self.base_url = '{}/iins'.format(self.base_url)
        self.token_iin = '412345'

    @responses.activate
    def test_addon_fetch(self):
        result = mock_file('fake_iin')
        url = '{}/{}'.format(self.base_url, self.token_iin)
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.iin.fetch(self.token_iin), result)
