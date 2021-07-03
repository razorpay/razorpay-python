import responses
import json

from .helpers import mock_file, ClientTestCase


class TestClientContact(ClientTestCase):

    def setUp(self):
        super(TestClientContact, self).setUp()
        self.base_url = '{}/contacts'.format(self.base_url)

    @responses.activate
    def test_contact_all(self):

        result = mock_file('contact_collection')
        url = self.base_url

        responses.add(responses.GET,
                      url,
                      status=200,
                      body=json.dumps(result),
                      match_querystring=True)

        self.assertEqual(self.client.contact.all(), result)

    @responses.activate
    def test_contact_all_with_options(self):

        count = 1
        result = mock_file('contact_collection_with_one_contact')
        url = '{}?count={}'.format(self.base_url, count)

        responses.add(responses.GET,
                      url,
                      status=200,
                      body=json.dumps(result),
                      match_querystring=True)

        self.assertEqual(self.client.contact.all({'count': count}), result)

    @responses.activate
    def test_contact_fetch(self):

        result = mock_file('fake_contact')
        url = '{}/{}'.format(self.base_url, self.contact_id)

        responses.add(responses.GET,
                      url,
                      status=200,
                      body=json.dumps(result),
                      match_querystring=True)

        self.assertEqual(self.client.contact.fetch('fake_contact_id'), result)

    @responses.activate
    def test_contact_create(self):
        result = mock_file('fake_contact')
        DATA = {
            "name":"math",
            "email":"gggggh@gmail.com",
            "contact":"8000000000",
            "type":"employee",
            "notes":{}
        }
        url = self.base_url

        responses.add(responses.POST, 
                      url, 
                      status=200,
                      body=json.dumps(result), 
                      match_querystring=True)

        response = self.client.contact.create(data = DATA)
        self.assertEqual(response, result)

    @responses.activate
    def test_contact_update(self):
        result = mock_file('fake_contact')

        DATA = {
            "contact": "8000000000"
        }

        url = "{}/{}".format(self.base_url, self.contact_id)

        responses.add(responses.PATCH,
                      url,
                      status = 200,
                      body=json.dumps(result),
                      match_querystring=True)

        response = self.client.contact.update(self.contact_id, data = DATA)
        self.assertEqual(response, result)

    @responses.activate
    def test_contact_get_types(self):
        result = mock_file("contact_types_collection")
        url = "{}/types".format(self.base_url)

        responses.add(responses.GET,
                      url,
                      status = 200,
                      body = json.dumps(result),
                      match_querystring = True)

        response = self.client.contact.get_types()
        self.assertEqual(response, result)

    @responses.activate
    def test_contact_post_types(self):
        result = mock_file("contact_types_collection")
        url = "{}/types".format(self.base_url)

        responses.add(responses.POST,
                      url,
                      status = 200,
                      body = json.dumps(result),
                      match_querystring = True)

        DATA = {"type": "SDK"}

        response = self.client.contact.post_type(data = DATA)
        self.assertEqual(response, result)
