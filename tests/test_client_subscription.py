import responses
import json

from .helpers import mock_file, ClientTestCase


class TestClientSubscription(ClientTestCase):

    def setUp(self):
        super(TestClientSubscription, self).setUp()
        self.base_url = '{}/subscriptions'.format(self.base_url)
        self.subscription_id = 'sub_8RlLljfA4AnDVx'

    @responses.activate
    def test_subscription_fetch_all(self):
        result = mock_file('subscription_collection')
        url = self.base_url
        responses.add(responses.GET, url, status=200,
                      body=json.dumps(result), match_querystring=True)
        self.assertEqual(self.client.subscription.all(), result)

    @responses.activate
    def test_subscription_fetch(self):
        result = mock_file('fake_subscription')
        url = '{}/{}'.format(self.base_url, 'fake_subscription_id')
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(
            self.client.subscription.fetch('fake_subscription_id'),
            result)

    @responses.activate
    def test_subscription_create(self):
        init = mock_file('init_subscription')
        result = mock_file('fake_subscription')
        url = self.base_url
        responses.add(responses.POST, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.subscription.create(init), result)

    @responses.activate
    def test_subscription_cancel(self):
        result = mock_file('fake_subscription_cancelled')
        url = '{}/{}/cancel'.format(self.base_url, self.subscription_id)
        responses.add(responses.POST, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        response = json.loads(
            self.client.subscription.cancel(self.subscription_id))
        self.assertEqual(response['id'], self.subscription_id)
        self.assertEqual(response['entity'], 'subscription')
        self.assertEqual(response['status'], 'cancelled')

    @responses.activate
    def test_subscription_cancel_scheduled_changes(self):
        result = mock_file('fake_subscription_resumed')
        url = '{}/{}/cancel_scheduled_changes'.format(self.base_url, self.subscription_id)
        responses.add(responses.POST, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        response = json.loads(
            self.client.subscription.cancel_scheduled_changes(self.subscription_id))
        self.assertEqual(response['id'], self.subscription_id)
        self.assertEqual(response['entity'], 'subscription')   

    @responses.activate
    def test_subscription_create_addon(self):
        result = mock_file('fake_subscription_addon')
        url = '{}/{}/addons'.format(self.base_url, self.subscription_id)
        responses.add(responses.POST,
                      url,
                      status=200,
                      body=json.dumps(result),
                      match_querystring=True)
        response = json.loads(
            self.client.subscription.createAddon(
                self.subscription_id,
                {'item': {'name': 'Extra Chair', 'amount': 30000,
                          'currency': 'INR'}, 'quantity': 2}))
        self.assertEqual(response['subscription_id'], self.subscription_id)
        self.assertEqual(response['entity'], 'addon')
        self.assertEqual(response['item']['name'], 'Extra Chair')
        self.assertEqual(response['item']['amount'], 30000)

    @responses.activate
    def test_subscription_edit(self):
        param = {
                 "quantity":2,
                 "schedule_change_at":"cycle_end",
               }

        result = mock_file('fake_subscription')
        url = '{}/{}'.format(self.base_url, 'subscription_id')
        responses.add(responses.PATCH, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.subscription.edit('subscription_id', param), result)     

    @responses.activate
    def test_subscription_pending_update(self):
        result = mock_file('fake_subscription')
        url = '{}/{}/retrieve_scheduled_changes'.format(self.base_url, 'fake_subscription_id')
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(
            self.client.subscription.pending_update('fake_subscription_id'),
            result)

    @responses.activate
    def test_subscription_pause(self):
        result = mock_file('fake_subscription_paused')
        url = '{}/{}/pause'.format(self.base_url, self.subscription_id)
        responses.add(responses.POST, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        response = json.loads(
            self.client.subscription.pause(self.subscription_id))
        self.assertEqual(response['id'], self.subscription_id)
        self.assertEqual(response['entity'], 'subscription')
        self.assertEqual(response['status'], 'paused')  

    @responses.activate
    def test_subscription_resume(self):
        result = mock_file('fake_subscription_resumed')
        url = '{}/{}/resume'.format(self.base_url, self.subscription_id)
        responses.add(responses.POST, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        response = json.loads(
            self.client.subscription.resume(self.subscription_id))
        self.assertEqual(response['id'], self.subscription_id)
        self.assertEqual(response['entity'], 'subscription')
        self.assertEqual(response['status'], 'active')

    @responses.activate
    def test_subscription_delete_offer(self):
        result = mock_file('fake_subscription')
        url = '{}/{}/{}'.format(self.base_url, 'sub_8kip7ybbcOyc9J','offer_IjA06IHSz33cw2')
        responses.add(responses.DELETE, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        response = json.loads(
            self.client.subscription.delete_offer('sub_8kip7ybbcOyc9J','offer_IjA06IHSz33cw2'))
        self.assertEqual(response['id'], 'sub_8kip7ybbcOyc9J')
        self.assertEqual(response['entity'], 'subscription')               