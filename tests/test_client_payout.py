import responses
import json

from .helpers import mock_file, ClientTestCase
from razorpay.errors import BadRequestError


class TestClientPayout(ClientTestCase):

    def setUp(self):
        super(TestClientPayout, self).setUp()
        self.base_url = '{}/payouts'.format(self.base_url)

    @responses.activate
    def test_payout_all(self):
        result = mock_file("payout_collection")
        url = self.base_url

        responses.add(responses.GET, 
                      url, 
                      status=200,
                      body=json.dumps(result), 
                      match_querystring=True)

        self.assertEqual(self.client.payout.all(),result)

    @responses.activate
    def test_payout_all_with_options(self):
        count = 1
        result = mock_file("payout_collection_with_one_payout")
        url = '{}?count={}'.format(self.base_url, count)

        responses.add(responses.GET, 
                      url, 
                      status=200,
                      body=json.dumps(result), 
                      match_querystring=True)

        response = self.client.payout.all({'count':count})
        self.assertEqual(response,result)
        self.assertEqual(json.loads(response)['count'], 1)

    @responses.activate
    def test_payout_fetch(self):
        result = mock_file('fake_payout')
        url = '{}/{}'.format(self.base_url, self.payout_id)

        responses.add(responses.GET, 
                      url, 
                      status=200,
                      body=json.dumps(result), 
                      match_querystring=True)

        self.assertEqual(self.client.payout.fetch('fake_payout_id'), result)

    @responses.activate
    def test_payout_create(self):
        result = mock_file('fake_payout')
        DATA = {
            "fund_account_id": "fa_HIg",
        	"amount": 100,
        	"mode": "IFT",
        	"currency": "INR",
        	"account_number": "004705015597",
        	"purpose": "refund"
        }
        url = self.base_url

        responses.add(responses.POST, 
                      url, 
                      status=200,
                      body=json.dumps(result), 
                      match_querystring=True)

        response = self.client.payout.create('fake_idempotency_key', data = DATA)
        self.assertEqual(response, result)

    @responses.activate
    def test_payout_create_without_idempotency_key(self):
        url = self.base_url

        DATA = {
            "fund_account_id": "fa_HIg",
        	"amount": 100,
        	"mode": "IFT",
        	"currency": "INR",
        	"account_number": "004705015597",
        	"purpose": "refund"
        }
        
        with self.assertRaises(BadRequestError, msg = "Idempotency Key can't be None") as exception_caught:
            self.client.payout.create(None, data=DATA)
            
        self.assertEqual(str(exception_caught.exception), "Idempotency Key can't be None")

