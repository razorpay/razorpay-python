import responses

from .helpers import ClientTestCase
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
             None)

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
