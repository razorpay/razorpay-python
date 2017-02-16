import hmac
import hashlib
import sys


class Utility(object):
    def __init__(self, client=None):
        self.client = client

    def verify_payment_signature(self, parameters):
        order_id = str(parameters['razorpay_order_id'])
        payment_id = str(parameters['razorpay_payment_id'])
        razorpay_signature = str(parameters['razorpay_signature'])
        msg = "{}|{}".format(order_id, payment_id)
        key = self.client.auth[1]

        if sys.version_info[0] == 3:
            key = bytes(key, 'utf-8')
            msg = bytes(msg, 'utf-8')

        dig = hmac.new(key=key,
                       msg=msg,
                       digestmod=hashlib.sha256)

        generated_signature = dig.hexdigest()

        if not hmac.compare_digest(generated_signature, razorpay_signature):
            raise ValueError('Payment Signature Verification Failed')

        return True
