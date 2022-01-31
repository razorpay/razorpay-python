import responses
import json

from .helpers import mock_file, ClientTestCase


class TestClientRegistrationLink(ClientTestCase):

    def setUp(self):
        super(TestClientRegistrationLink, self).setUp()
        self.base_url = '{}/subscription_registration/{}'.format(self.base_url, 'auth_links')

    @responses.activate
    def test_create(self):
        param = mock_file('init_registration_link')
        result = mock_file('fake_registration_link')
        url = self.base_url
        responses.add(responses.POST,
                      url,
                      status=200,
                      body=json.dumps(result),
                      match_querystring=True)

        self.assertEqual(self.client.registration_link.create(param), result)
