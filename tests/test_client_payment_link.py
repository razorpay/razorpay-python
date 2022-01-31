import responses
import json

from .helpers import mock_file, ClientTestCase


class TestClientPaymentLink(ClientTestCase):

    def setUp(self):
        super(TestClientPaymentLink, self).setUp()
        self.base_url = '{}/payment_links'.format(self.base_url)
    
    @responses.activate
    def test_payment_link_create(self):
        init = mock_file('init_payment_link')

        result = mock_file('fake_payment_link')
        url = '{}/{}'.format(self.base_url, 'fake_payment_link_id')
        responses.add(responses.PATCH, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.payment_link.edit('fake_payment_link_id', init), result)


    @responses.activate
    def test_payment_link_edit(self):
        init = {
            "reference_id": "TS35",
            "expire_by": 1653347540,
            "reminder_enable":0,
            "notes":{
            "policy_name": "Jeevan Saral"
            }
        }

        result = mock_file('edit_payment_link')
        url = '{}/{}'.format(self.base_url, 'fake_payment_link_id')
        responses.add(responses.PATCH, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.payment_link.edit('fake_payment_link_id', init), result)
    
    @responses.activate
    def test_payment_link_notifyBy(self):
        result = {"success": 1}

        url = "{}/{}/notify_by/{}".format(self.base_url, 'fake_payment_link_id', 'email')

        responses.add(responses.POST, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.payment_link.notifyBy('fake_payment_link_id',medium='email'), result)

    @responses.activate
    def test_payment_link_all(self):
        result = mock_file('payment_link_collection')
        url = self.base_url
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.payment_link.all(), result)

    @responses.activate
    def test_payment_all_fetch(self):
        result = mock_file('fake_payment_link')
        url = '{}/{}'.format(self.base_url, 'fake_payment_link_id')
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.payment_link.fetch('fake_payment_link_id'),result)    

    @responses.activate
    def test_payment_link_cancel(self):
        result = mock_file('cancel_payment_link')

        url = "{}/{}/cancel".format(self.base_url, 'fake_payment_link_id')

        responses.add(responses.POST, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.payment_link.cancel('fake_payment_link_id'), result)    
