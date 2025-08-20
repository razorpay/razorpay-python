import responses
import sys

from .helpers import mock_file, ClientTestCase
from razorpay.errors import SignatureVerificationError


class TestClientValidator(ClientTestCase):

    def setUp(self):
        super(TestClientValidator, self).setUp()

    @responses.activate
    def test_verify_payment_signature(self):
        sig = 'b2335e3b0801106b84a7faff035df56ecffde06918c9ddd1f0fafbb37a51cc89'
        parameters = {}
        parameters['razorpay_order_id'] = 'fake_order_id'
        parameters['razorpay_payment_id'] = 'fake_payment_id'
        parameters['razorpay_signature'] = sig

        self.assertEqual(
             self.client.utility.verify_payment_signature(parameters),
             True)

    @responses.activate
    def test_subscription_payment_signature(self):
        sig = '601f383334975c714c91a7d97dd723eb56520318355863dcf3821c0d07a17693'
        parameters = {}
        parameters['razorpay_subscription_id'] = 'sub_ID6MOhgkcoHj9I'
        parameters['razorpay_payment_id'] = 'pay_IDZNwZZFtnjyym'
        parameters['razorpay_signature'] = sig
        parameters['secret'] = 'EnLs21M47BllR3X8PSFtjtbd'

        self.assertEqual(
             self.client.utility.verify_subscription_payment_signature(parameters),
             True)

    @responses.activate
    def test_verify_payment_link_signature(self):
        sig = '07ae18789e35093e51d0a491eb9922646f3f82773547e5b0f67ee3f2d3bf7d5b'
        parameters = {}
        parameters['razorpay_payment_id'] = 'pay_IH3d0ara9bSsjQ'
        parameters['payment_link_id'] = 'plink_IH3cNucfVEgV68'
        parameters['payment_link_reference_id'] = 'TSsd1989'
        parameters['payment_link_status'] = 'paid'
        parameters['razorpay_signature'] = sig
        parameters['secret'] = 'EnLs21M47BllR3X8PSFtjtbd'
       # x = self.client.utility.verify_payment_link_signature(parameters)

        self.assertEqual(
             self.client.utility.verify_payment_link_signature(parameters),
             True)

    @responses.activate
    def test_verify_payment_signature_with_exception(self):
        parameters = {}
        parameters['razorpay_order_id'] = 'fake_order_id'
        parameters['razorpay_payment_id'] = 'fake_payment_id'
        parameters['razorpay_signature'] = 'test_signature'

        self.assertRaises(
            SignatureVerificationError,
            self.client.utility.verify_payment_signature,
            parameters)

    @responses.activate
    def test_verify_webhook_signature(self):
        secret = self.client.auth[1]
        sig = 'd60e67fd884556c045e9be7dad57903e33efc7172c17c6e3ef77db42d2b366e9'
        body = mock_file('fake_payment_authorized_webhook')

        self.assertEqual(
             self.client.utility.verify_webhook_signature(body, sig, secret),
             True)

    if sys.version_info[0] == 3:
        @responses.activate
        def test_verify_webhook_signature_with_bytes_data(self):
            secret = self.client.auth[1]
            sig = 'd60e67fd884556c045e9be7dad57903e33efc7172c17c6e3ef77db42d2b366e9'
            body = bytes(mock_file('fake_payment_authorized_webhook'), 'utf-8')

            self.assertEqual(
                self.client.utility.verify_webhook_signature(body, sig, secret),
                True)

    @responses.activate
    def test_verify_webhook_signature_with_exception(self):
        secret = self.client.auth[1]
        sig = 'test_signature'
        body = ''

        self.assertRaises(
            SignatureVerificationError,
            self.client.utility.verify_webhook_signature,
            body,
            sig,
            secret)
