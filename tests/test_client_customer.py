import responses
import json

from .helpers import mock_file, ClientTestCase


class TestClientCustomer(ClientTestCase):

    def setUp(self):
        super(TestClientCustomer, self).setUp()
        self.base_url = f"{self.base_url}/customers"

    @responses.activate
    def test_customer_fetch(self):
        result = mock_file('fake_customer')
        url = f"{self.base_url}/{self.customer_id}"

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
        url = f"{self.base_url}/{self.customer_id}"
        responses.add(responses.PUT,
                      url,
                      status=200,
                      body=json.dumps(result),
                      match_querystring=True)

        self.assertEqual(self.client.customer.edit(
            self.customer_id, email), result)

    @responses.activate
    def test_item_all(self):
        result = mock_file('customer_collection')
        url = self.base_url
        responses.add(responses.GET, url, status=200,
                      body=json.dumps(result), match_querystring=True)
        self.assertEqual(self.client.customer.all(), result)

    @responses.activate
    def test_addbank_account(self):
        result = mock_file('bank_account')
        payload = {
            "ifsc_code": "UTIB0000194",
            "account_number": "916010082985661",
            "beneficiary_name": "Pratheek",
            "beneficiary_address1": "address 1",
            "beneficiary_address2": "address 2",
            "beneficiary_address3": "address 3",
            "beneficiary_address4": "address 4",
            "beneficiary_email": "random@email.com",
            "beneficiary_mobile": "8762489310",
            "beneficiary_city": "Bangalore",
            "beneficiary_state": "KA",
            "beneficiary_country": "IN"
        }
        url = f"{self.base_url}/{self.customer_id}/bank_account"
        responses.add(responses.POST, url, status=200,
                      body=json.dumps(result), match_querystring=True)
        self.assertEqual(self.client.customer.addBankAccount(
            self.customer_id, payload), result)

    @responses.activate
    def test_deletebank_account(self):
        result = mock_file('bank_account')
        bankaccountId = "ba_LSZht1Cm7xFTwF"
        url = f"{self.base_url}/{self.customer_id}/bank_account/{bankaccountId}"
        responses.add(responses.DELETE, url, status=200,
                      body=json.dumps(result), match_querystring=True)
        self.assertEqual(self.client.customer.deleteBankAccount(
            self.customer_id, bankaccountId), result)

    @responses.activate
    def test_request_eligibility_check(self):
        request = {
            "inquiry": "affordability",
            "amount": 500,
            "currency": "INR",
            "customer": {
                "id": "elig_KkCNLzlNeMYQyZ",
                "contact": "+918220276214",
                "ip": "105.106.107.108",
                "referrer": "https://merchansite.com/example/paybill",
                "user_agent": "Mozilla/5.0"
            }
        }
        result = mock_file('eligibility_check')
        url = f"{self.base_url}/eligibility"
        responses.add(responses.POST, url, status=200,
                      body=json.dumps(result), match_querystring=True)
        self.assertEqual(self.client.customer.requestEligibilityCheck(request), result)

    @responses.activate
    def test_fetch_eligibility(self):
        result = mock_file('eligibility')
        id = 'fake_eligibility_id'
        url = f"{self.base_url}/eligibility/{id}"
        responses.add(responses.GET, url, status=200,
                      body=json.dumps(result), match_querystring=True)
        self.assertEqual(self.client.customer.fetchEligibility(id), result)
