import responses
import json

from razorpay.constants.url import URL

from .helpers import mock_file, ClientTestCase


class TestClientWebhook(ClientTestCase):

    def setUp(self):
        super(TestClientWebhook, self).setUp()
        self.base_url = '{}{}'.format(self.base_url_v2, URL.ACCOUNT)
        self.account_id = "acc_H3kYHQ635sBwXG"
        self.webhookId = "HK890egfiItP3H"

    @responses.activate
    def test_webhook_all(self):
        result = mock_file('webhook_collection')
        url = '{}/{}{}'.format(self.base_url, self.account_id, URL.WEBHOOK)
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.webhook.all({},self.account_id),
                         result)

    @responses.activate
    def test_webhook_fetch(self):
        result = mock_file('fake_webhook')
        url = '{}/{}{}/{}'.format(self.base_url,
                                  self.account_id, URL.WEBHOOK, self.webhookId)
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(
            self.client.webhook.fetch(self.webhookId, self.account_id),
            result)

    @responses.activate
    def test_webhook_create(self):
        init = mock_file('init_webhook')
        result = mock_file('fake_webhook')
        url = '{}/{}{}'.format(self.base_url, self.account_id, URL.WEBHOOK)
        responses.add(responses.POST,
                      url,
                      status=200,
                      body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(
            self.client.webhook.create(init, self.account_id),
            result)

    @responses.activate
    def test_webhook_edit(self):
        init = {
            "url": "https://www.linkedin.com",
            "events": [
                "refund.created"
            ]
        }
        result = mock_file('fake_webhook')
        url = '{}/{}{}/{}'.format(self.base_url,
                                  self.account_id, URL.WEBHOOK, self.webhookId)
        responses.add(responses.PATCH, url, status=200, body=json.dumps(result))
        self.assertEqual(
            self.client.webhook.edit(self.webhookId, self.account_id, init),
            result)

    @responses.activate
    def test_webhook_delete(self):

        result = mock_file('fake_webhook')
        url = '{}/{}{}/{}'.format(self.base_url,
                                  self.account_id, URL.WEBHOOK, self.webhookId)
        responses.add(responses.DELETE, url, status=200, body=json.dumps(result), match_querystring=True)
        self.assertEqual(
            self.client.webhook.delete(self.webhookId, self.account_id),
            result)
