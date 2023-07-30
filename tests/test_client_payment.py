import responses
import json

from .helpers import mock_file, ClientTestCase


class TestClientPayment(ClientTestCase):

    def setUp(self):
        super(TestClientPayment, self).setUp()
        self.base_url = f"{self.base_url}/payments"

    @responses.activate
    def test_payment_all(self):
        result = mock_file('payment_collection')
        url = self.base_url
        responses.add(responses.GET, url, status=200,
                      body=json.dumps(result), match_querystring=True)
        self.assertEqual(self.client.payment.all(), result)

    @responses.activate
    def test_payment_all_with_options(self):
        count = 1
        result = mock_file('payment_collection_with_one_payment')
        url = f"{self.base_url}?count={count}"
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.payment.all({'count': count}), result)

    @responses.activate
    def test_payment_fetch(self):
        result = mock_file('fake_payment')
        url = f"{self.base_url}/{self.payment_id}"
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.payment.fetch('fake_payment_id'), result)

    @responses.activate
    def test_payment_capture(self):
        result = mock_file('fake_captured_payment')
        url = f"{self.base_url}/{self.payment_id}/capture"
        responses.add(responses.POST, url, status=200,
                      body=json.dumps(result), match_querystring=True)
        self.assertEqual(self.client.payment.capture(self.payment_id,
                                                     amount=5100), result)

    @responses.activate
    def test_refund_create(self):
        result = mock_file('fake_refund')
        url = f"{self.base_url}/{self.payment_id}/refund"
        responses.add(responses.POST, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.payment.refund(self.payment_id, 2000),
                         result)

    @responses.activate
    def test_transfer(self):
        param = {
            'transfers': {
                'currency': {
                    'amount': 100,
                    'currency': 'INR',
                    'account': 'dummy_acc'
                }
            }
        }
        result = mock_file('transfers_collection_with_payment_id')
        url = f"{self.base_url}/{self.payment_id}/transfers"
        responses.add(responses.POST, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.payment.transfer(self.payment_id, param),
                         result)

    @responses.activate
    def test_transfer_fetch(self):
        result = mock_file('transfers_collection_with_payment_id')
        url = f"{self.base_url}/{self.payment_id}/transfers"
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.payment.transfers(
            self.payment_id), result)

    @responses.activate
    def test_bank_transfer_fetch(self):
        result = mock_file('fake_bank_transfer')
        url = f"{self.base_url}/{self.payment_id}/bank_transfer"
        responses.add(responses.GET,
                      url,
                      status=200,
                      body=result,
                      match_querystring=True)

        response = self.client.payment.bank_transfer(self.payment_id)
        self.assertEqual(response['virtual_account_id'], 'va_8J2ny4Naokqbpe')
        self.assertEqual(response['payment_id'], self.payment_id)

    @responses.activate
    def test_upi_transfer_fetch(self):
        result = mock_file('fake_upi_transfer')
        url = f"{self.base_url}/{self.payment_id}/upi_transfer"
        responses.add(responses.GET,
                      url,
                      status=200,
                      body=result,
                      match_querystring=True)

        response = self.client.payment.upi_transfer(self.payment_id)
        self.assertEqual(response['virtual_account_id'], 'va_8J2ny4Naokqbpf')
        self.assertEqual(response['payment_id'], self.payment_id)

    @responses.activate
    def test_payment_refund(self):
        init = {
            "amount": "100"
        }
        result = mock_file('fake_refund')
        url = f"{self.base_url}/{self.payment_id}/refund"
        responses.add(responses.POST, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.payment.refund(
            'fake_refund_id', init), result)

    @responses.activate
    def test_payment_fetch_multiple_refund(self):
        result = mock_file('refund_collection')
        url = f"{self.base_url}/fake_payment_id/refunds"
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.payment.fetch_multiple_refund(
            self.payment_id), result)

    @responses.activate
    def test_payment_fetch_refund_id(self):
        result = mock_file('refund_collection')
        url = f"{self.base_url}/fake_payment_id/refunds/fake_refund_id"
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.payment.fetch_refund_id(
            'fake_payment_id', 'fake_refund_id'), result)

    @responses.activate
    def test_payment_edit(self):
        param = {
            "notes": {
                "key1": "value3",
                "key2": "value2"
            }
        }

        result = mock_file('edit_payment')
        url = f"{self.base_url}/dummy_id"
        responses.add(responses.PATCH, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.payment.edit('dummy_id', param), result)

    @responses.activate
    def test_fetch_card_detail(self):
        result = mock_file('fake_card_detail_payment')
        url = f"{self.base_url}/dummy_id/card"
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(
            self.client.payment.fetchCardDetails('dummy_id'), result)

    @responses.activate
    def test_fetch_downtimes(self):
        result = mock_file('fake_card_detail_payment')
        url = f"{self.base_url}/downtimes"
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.payment.fetchDownTime(), result)

    @responses.activate
    def test_fetch_downtime_by_id(self):
        result = mock_file('fake_card_detail_payment')
        url = f"{self.base_url}/downtimes/dummy_id"
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(
            self.client.payment.fetchDownTimeById('dummy_id'), result)

    @responses.activate
    def test_payment_json(self):
        param = {
            "amount": "500",
            "currency": "INR",
            "email": "gaurav.kumar@example.com",
            "contact": "9123456789",
            "order_id": "order_IfCjbAb066hM9i",
            "method": "upi",
            "card": {
                "number": "4854980604708430",
                "cvv": "123",
                "expiry_month": "12",
                "expiry_year": "21",
                "name": "Gaurav Kumar"
            }
        }
        result = mock_file('fake_payment_json')
        url = f"{self.base_url}/create/json"
        responses.add(responses.POST, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.payment.createPaymentJson(param), result)

    @responses.activate
    def test_createRecurring(self):
        init = mock_file('init_create_recurring')
        result = mock_file('fake_create_recurring')
        url = f"{self.base_url}/create/recurring"
        responses.add(responses.POST,
                      url,
                      status=200,
                      body=json.dumps(result),
                      match_querystring=True)

        self.assertEqual(self.client.payment.createRecurring(init), result)

    @responses.activate
    def test_otpGenerate(self):
        result = mock_file('fake_otp_generate')
        url = f"{self.base_url}/dummy_id/otp_generate"
        responses.add(responses.POST,
                      url,
                      status=200,
                      body=json.dumps(result),
                      match_querystring=True)

        self.assertEqual(self.client.payment.otpGenerate('dummy_id'), result)

    @responses.activate
    def test_otpSubmit(self):
        param = {
            "otp": "123456"
        }

        result = mock_file('fake_otp_submit')
        url = f"{self.base_url}/dummy_id/otp/submit"
        responses.add(responses.POST,
                      url,
                      status=200,
                      body=json.dumps(result),
                      match_querystring=True)

        self.assertEqual(self.client.payment.otpSubmit(
            'dummy_id', param), result)

    @responses.activate
    def test_otpResend(self):
        result = mock_file('fake_otp_resend')
        url = f"{self.base_url}/dummy_id/otp/resend"
        responses.add(responses.POST,
                      url,
                      status=200,
                      body=json.dumps(result),
                      match_querystring=True)

        self.assertEqual(self.client.payment.otpResend('dummy_id'), result)
