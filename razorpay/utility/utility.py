import hmac
import hashlib
import sys


from ..errors import SignatureVerificationError


class Utility(object):
    def __init__(self, client=None):
        self.client = client
        self.payment_methods = client.payment_method.all()

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

        if sys.version_info[0] == 3:  # pragma: no cover
            key = bytes(key, 'utf-8')
            body = bytes(body, 'utf-8')

        dig = hmac.new(key=key,
                       msg=body,
                       digestmod=hashlib.sha256)

        generated_signature = dig.hexdigest()

        if not hmac.compare_digest(generated_signature, signature):
            raise SignatureVerificationError('Payment Signature Verification Failed')

    def strf_payment_method(self, payment_info):
        try:
            method_id = payment_info["method"]

            if method_id == "wallet":
                return "Wallet - {}".format(payment_info["wallet"]).title()

            elif method_id == "card":
                card_info = self.client.card.fetch(payment_info["card_id"])
                return "{} Card - {} **** **** **** {}".format(
                    card_info["type"], card_info["network"], card_info["last4"]
                ).title()

            elif method_id == "netbanking":
                bank_code = payment_info["bank"]
                try:
                    bank_verbose = self.payment_methods["netbanking"][bank_code]
                except KeyError as ke:
                    # Try an reload the payment method dict because
                    # we seem to have encountered a new bank
                    self.payment_methods = self.client.payment_method.all()
                    bank_verbose = self.payment_methods["netbanking"].get(
                        bank_code, bank_code)
                return "Netbanking - {}".format(bank_verbose)

            elif method_id == "upi":
                return "Upi - {}".format(payment_info["vpa"])
                
            elif method_id == "emi":
                return "EMI"
                # TO DO show details for EMI - no public documentation found

            raise NotImplementedError("Payment method unknown")

        except KeyError as ke:
            return None
