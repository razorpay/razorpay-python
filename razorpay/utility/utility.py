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

        secret = str(self.client.auth[1])

        self.verify_signature(msg, razorpay_signature, secret)

    def verify_webhook_signature(self, body, signature, secret):
        self.verify_signature(body, signature, secret)

    def verify_signature(self, body, signature, key):
        if sys.version_info[0] == 3:  # pragma: no cover
            key = bytes(key, 'utf-8')
            body = bytes(body, 'utf-8')

        dig = hmac.new(key=key,
                       msg=body,
                       digestmod=hashlib.sha256)

        generated_signature = dig.hexdigest()

        if sys.hexversion >= 0x020707F0:
            if not hmac.compare_digest(generated_signature, signature):
                raise SignatureVerificationError('Payment Signature Verification Failed')
        else:
            if str(generated_signature) != str(signature):
                raise SignatureVerificationError('Payment Signature Verification Failed')
