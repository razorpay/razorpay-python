import responses
import json

from .helpers import mock_file, ClientTestCase


class TestClientCustomer(ClientTestCase):

    def setUp(self):
        super(TestClientCustomer, self).setUp()
        self.base_url = '{}/customers'.format(self.base_url)

    @responses.activate
    def test_customer_fetch(self):
        result = mock_file('fake_customer')
        url = '{}/{}'.format(self.base_url, self.customer_id)

        responses.add(responses.GET,
                      url,
                      status=200,
                      body=json.dumps(result),
                      match_querystring=True)

        self.assertEqual(self.client.customer.fetch(self.customer_id), result)

    @responses.activate
    def test_customer_create(self):
        init = mock_file('init_customer')
        result = mock_file('fake_customer')
        url = self.base_url
        responses.add(responses.POST,
                      url,
                      status=200,
                      body=json.dumps(result),
                      match_querystring=True)

        self.assertEqual(self.client.customer.create(init), result)

    @responses.activate
    def test_customer_edit(self):
        email = 'test@test.com'
        result = mock_file('fake_customer')
        url = '{}/{}'.format(self.base_url, self.customer_id)
        responses.add(responses.PUT,
                      url,
                      status=200,
                      body=json.dumps(result),
                      match_querystring=True)

        self.assertEqual(self.client.customer.edit(self.customer_id, email), result)
    
    @responses.activate
    def test_item_all(self):
        result = mock_file('customer_collection')
        url = self.base_url
        responses.add(responses.GET, url, status=200,
                      body=json.dumps(result), match_querystring=True)
        self.assertEqual(self.client.customer.all(), result)