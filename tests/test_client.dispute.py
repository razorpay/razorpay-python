import responses
import json

from .helpers import mock_file, ClientTestCase


class TestClientDispute(ClientTestCase):

    def setUp(self):
        super(TestClientDispute, self).setUp()
        self.base_url = '{}/disputes'.format(self.base_url)

    @responses.activate
    def test_dispute_fetch_all(self):
        result = mock_file('dispute_collection')
        url = self.base_url
        responses.add(responses.GET, url, status=200,
                      body=json.dumps(result), match_querystring=True)
        self.assertEqual(self.client.dispute.all(), result)

    @responses.activate
    def test_fetch_dispute(self):
        result = mock_file('dispute')
        url = '{}/{}'.format(self.base_url, 'fake_dispute_id')
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.dispute.fetch('fake_dispute_id'), result)

    @responses.activate
    def test_dispute_accept(self):
        result = mock_file('dispute_accept')
        url = '{}/{}/accept'.format(self.base_url, 'fake_dispute_id')
        responses.add(responses.POST, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.dispute.accept('fake_dispute_id'), result)

    @responses.activate
    def test_dispute_contest(self):
        request = {
            "amount": 5000,
            "summary": "goods delivered",
            "shipping_proof": [
                "doc_EFtmUsbwpXwBH9",
                "doc_EFtmUsbwpXwBH8"
            ],
            "others": [
                {
                "type": "receipt_signed_by_customer",
                "document_ids": [
                    "doc_EFtmUsbwpXwBH1",
                    "doc_EFtmUsbwpXwBH7"
                ]
                }
            ],
            "action": "draft"
        }

        result = mock_file('dispute_contest')
        url = '{}/{}/contest'.format(self.base_url, 'fake_dispute_id')
        responses.add(responses.PATCH, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.dispute.contest('fake_dispute_id',request), result)
