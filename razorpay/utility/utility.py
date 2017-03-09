import hmac
import hashlib
import sys


from ..errors import SignatureVerificationError


class Utility(object):
    def __init__(self, client=None):
        self.client = client

    def verify_payment_signature(self, parameters):
        order_id = str(parameters['razorpay_order_id'])
        payment_id = str(parameters['razorpay_payment_id'])
        razorpay_signature = str(parameters['razorpay_signature'])

        msg = "{}|{}".format(order_id, payment_id)

        self.verify_signature(razorpay_signature, msg)

    def verify_webhook_signature(self, signature, body):
        self.verify_signature(signature, body)

    def verify_signature(self, signature, body):
        key = self.client.auth[1]

        if sys.version_info[0] == 3:
            key = bytes(key, 'utf-8')
            body = bytes(body, 'utf-8')

        dig = hmac.new(key=key,
                       msg=body,
                       digestmod=hashlib.sha256)

        generated_signature = dig.hexdigest()

        if not hmac.compare_digest(generated_signature, signature):
            raise SignatureVerificationError('Payment Signature Verification Failed')
