import hmac
import hashlib
import unittest

from .helpers import ClientTestCase
from razorpay.errors import SignatureVerificationError


class TestClientValidatorNegative(ClientTestCase):

    def setUp(self):
        super(TestClientValidatorNegative, self).setUp()
        self.webhook_payload = '{"event":"payment.authorized"}'
        self.webhook_secret = 'test_webhook_secret'

    def compute_signature(self, payload, secret):
        return hmac.new(
            secret.encode('utf-8'),
            payload.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()

    def test_empty_signature_rejected(self):
        self.assertRaises(
            SignatureVerificationError,
            self.client.utility.verify_webhook_signature,
            self.webhook_payload,
            '',
            self.webhook_secret
        )

    def test_wrong_length_signature_rejected(self):
        self.assertRaises(
            SignatureVerificationError,
            self.client.utility.verify_webhook_signature,
            self.webhook_payload,
            'abc123',
            self.webhook_secret
        )

    def test_non_hex_signature_rejected(self):
        non_hex_sig = 'z' * 64
        self.assertRaises(
            SignatureVerificationError,
            self.client.utility.verify_webhook_signature,
            self.webhook_payload,
            non_hex_sig,
            self.webhook_secret
        )

    def test_tampered_valid_hex_signature_rejected(self):
        tampered_sig = 'a' * 64
        self.assertRaises(
            SignatureVerificationError,
            self.client.utility.verify_webhook_signature,
            self.webhook_payload,
            tampered_sig,
            self.webhook_secret
        )

    def test_valid_dynamic_signature_accepted(self):
        valid_sig = self.compute_signature(self.webhook_payload, self.webhook_secret)
        result = self.client.utility.verify_webhook_signature(
            self.webhook_payload,
            valid_sig,
            self.webhook_secret
        )
        self.assertTrue(result)

    def test_special_chars_in_payload(self):
        special_payload = '{"event":"payment","data":{"notes":"Test & <script>alert(1)</script>"}}'
        valid_sig = self.compute_signature(special_payload, self.webhook_secret)
        result = self.client.utility.verify_webhook_signature(
            special_payload,
            valid_sig,
            self.webhook_secret
        )
        self.assertTrue(result)

    def test_unicode_in_payload(self):
        unicode_payload = '{"event":"payment","data":{"name":"日本語テスト"}}'
        valid_sig = self.compute_signature(unicode_payload, self.webhook_secret)
        result = self.client.utility.verify_webhook_signature(
            unicode_payload,
            valid_sig,
            self.webhook_secret
        )
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
