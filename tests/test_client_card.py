import responses
import json

from .helpers import mock_file, ClientTestCase


class TestClientRefund(ClientTestCase):

    def setUp(self):
        super(TestClientRefund, self).setUp()
        self.base_url = '{}/cards'.format(self.base_url)

    @responses.activate
    def test_card_fetch(self):
        result = mock_file('fake_card')
        url = '{}/{}'.format(self.base_url, self.card_id)
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.card.fetch(self.card_id), result)

    @responses.activate
    def test_card_requestCardReference(self):
        init = {
            "number": "4854980604708430"
        }
        result = {
            "network": "Visa",
            "payment_account_reference": "V0010013819231376539033235990",
            "network_reference_id": "1001381923137653903323591234sdfds90"
        }
        url = "{}/{}".format(self.base_url, "fingerprints")
        responses.add(responses.POST, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.card.requestCardReference(init), result)
