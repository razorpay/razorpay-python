import responses
import json

from .helpers import mock_file, ClientTestCase


class TestClientQrcode(ClientTestCase):

    def setUp(self):
        super(TestClientQrcode, self).setUp()
        self.base_url = f"{self.base_url}/payments/qr_codes"
        self.plan_id = 'qr_IAgePI1GuSMTFN'

    @responses.activate
    def test_qrcode_all(self):
        result = mock_file('qrcode_collection')
        url = self.base_url
        responses.add(responses.GET, url, status=200,
                      body=json.dumps(result), match_querystring=True)
        self.assertEqual(self.client.qrcode.all(), result)

    @responses.activate
    def test_qrcode_fetch(self):
        result = mock_file('fake_qrcode')
        url = f"{self.base_url}/fake_qrcode_id"
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.qrcode.fetch('fake_qrcode_id'), result)

    @responses.activate
    def test_qrcode_create(self):
        init = {
            "type": "upi_qr",
            "name": "Store_1",
            "usage": "single_use",
            "fixed_amount": 1,
            "payment_amount": 300,
            "description": "For Store 1",
            "customer_id": "cust_HKsR5se84c5LTO",
            "close_by": 1681615838,
            "notes": {
                "purpose": "Test UPI QR code notes"
            }
        }
        result = mock_file('fake_qrcode')
        url = self.base_url
        responses.add(responses.POST, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.qrcode.create(init), result)

    @responses.activate
    def test_qrcode_fetch_all_payment(self):
        result = mock_file('qrcode_payments_collection')
        url = f"{self.base_url}/fake_qrcode_id/payments"
        responses.add(responses.GET, url, status=200,
                      body=json.dumps(result), match_querystring=True)
        self.assertEqual(self.client.qrcode.fetch_all_payments(
            'fake_qrcode_id'), result)

    @responses.activate
    def test_qrcode_close(self):
        result = mock_file('fake_qrcode')
        url = f"{self.base_url}/fake_qrcode_id/close"
        responses.add(responses.POST, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.qrcode.close('fake_qrcode_id'), result)
