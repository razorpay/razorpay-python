import responses
import json

from .helpers import mock_file, ClientTestCase


class TestClientPlan(ClientTestCase):

    def setUp(self):
        super(TestClientPlan, self).setUp()
        self.base_url = '{}/plans'.format(self.base_url)
        self.plan_id = 'plan_8kihN0YqhnF8a7'

    @responses.activate
    def test_plan_fetch_all(self):
        result = mock_file('plan_collection')
        url = self.base_url
        responses.add(responses.GET, url, status=200,
                      body=json.dumps(result), match_querystring=True)
        self.assertEqual(self.client.plan.all(), result)

    @responses.activate
    def test_plan_fetch(self):
        result = mock_file('fake_plan')
        url = '{}/{}'.format(self.base_url, self.plan_id)
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.plan.fetch(self.plan_id), result)

    @responses.activate
    def test_plan_create(self):
        init = mock_file('init_plan')
        result = mock_file('fake_plan')
        url = self.base_url
        responses.add(responses.POST, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.plan.create(init), result)
