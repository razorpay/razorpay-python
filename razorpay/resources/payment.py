from .base import Resource
from ..constants.url import URL
import warnings


class Payment(Resource):
    def __init__(self, client=None):
        super(Payment, self).__init__(client)
        self.base_url = URL.PAYMENTS_URL

    def fetch_all(self, data={}, **kwargs):  # pragma: no cover
        warnings.warn("Will be Deprecated in next release, use all",
                      DeprecationWarning)
        return self.all(data, **kwargs)

    def all(self, data={}, **kwargs):
        """"
        Fetch all Payment entities

        Returns:
            Dictionary of Payment data
        """
        return super(Payment, self).all(data, **kwargs)

    def fetch(self, payment_id, data={}, **kwargs):
        """"
        Fetch Payment for given Id

        Args:
            payment_id : Id for which payment object has to be retrieved

        Returns:
            Payment dict for given payment Id
        """
        return super(Payment, self).fetch(payment_id, data, **kwargs)

    # nosemgrep : python.lang.correctness.common-mistakes.default-mutable-dict.default-mutable-dict
    def capture(self, payment_id, amount, data={}, **kwargs):
        """"
        Capture Payment for given Id

        Args:
            payment_id : Id for which payment object has to be retrieved
            amount : Amount for which the payment has to be retrieved

        Returns:
            Payment dict after getting captured
        """
        url = f"{self.base_url}/{payment_id}/capture"

        data['amount'] = amount
        return self.post_url(url, data, **kwargs)

    def refund(self, payment_id, amount, data={}, **kwargs):  # pragma: no cover # nosemgrep : python.lang.correctness.common-mistakes.default-mutable-dict.default-mutable-dict
        """"
        Refund Payment for given Id

        Args:
            payment_id : Id for which payment object has to be refunded
            amount : Amount for which the payment has to be refunded

        Returns:
            Payment dict after getting refunded
        """
        url = f"{self.base_url}/{payment_id}/refund"

        data['amount'] = amount
        return self.post_url(url, data, **kwargs)

    def transfer(self, payment_id, data={}, **kwargs):
        """"
        Create Transfer for given Payment Id

        Args:
            payment_id : Id for which payment object has to be transferred

        Returns:
            Payment dict after getting transferred
        """
        url = f"{self.base_url}/{payment_id}/transfers"

        return self.post_url(url, data, **kwargs)

    def transfers(self, payment_id, data={}, **kwargs):
        """"
        Fetches all transfer for given Payment Id

        Args:
            payment_id : Id for which all the transfers has to be fetched

        Returns:
            A collection (dict) of transfers
            items : The key containing a list of 'transfer' entities
        """
        url = f"{self.base_url}/{payment_id}/transfers"
        return self.get_url(url, data, **kwargs)

    def bank_transfer(self, payment_id, data={}, **kwargs):
        """"
        Bank Transfer Entity for given Payment

        Args:
            payment_id : Id for which bank transfer entity has to be fetched

        Returns:
            Bank Transfer dict
        """
        url = f"{self.base_url}/{payment_id}/bank_transfer"
        return self.get_url(url, data, **kwargs)

    def upi_transfer(self, payment_id, data={}, **kwargs):
        """"
        UPI Transfer Entity for given Payment

        Args:
            payment_id : Id for which upi transfer entity has to be fetched

        Returns:
            UPI Transfer dict
        """
        url = f"{self.base_url}/{payment_id}/upi_transfer"
        return self.get_url(url, data, **kwargs)

    def refund(self, payment_id, data={}, **kwargs):
        """"
        Create a normal refund

        Returns:
            Payment dict after getting refund
        """
        url = f"{self.base_url}/{payment_id}/refund"
        return self.post_url(url, data, **kwargs)

    def fetch_multiple_refund(self, payment_id, data={}, **kwargs):
        """"
        Fetch multiple refunds for a payment

        Returns:
            refunds dict
        """
        url = f"{self.base_url}/{payment_id}/refund"
        return self.get_url(url, data, **kwargs)

    def fetch_refund_id(self, payment_id, refund_id, **kwargs):
        """"
        Fetch multiple refunds for a payment

        Returns:
            Refund dict
        """
        url = f"{self.base_url}/{payment_id}/refunds/{refund_id}"
        return self.get_url(url, {}, **kwargs)

    def edit(self, payment_id, data={}, **kwargs):
        """"
         Update the Payment
        Args:
            data : Dictionary having keys using which order have to be edited
                'notes' : key value pair as notes

            Returns:
            Payment Dict which was edited
        """
        url = f"{self.base_url}/{payment_id}"
        return self.patch_url(url, data, **kwargs)

    def fetchCardDetails(self, payment_id, **kwargs):
        """"
        Fetch Card Details of a Payment

        Args:
            payment_id : Id for which payment objects has to be retrieved

        Returns:
            Payment dict for given Order Id
        """
        url = f"{self.base_url}/{payment_id}/card"
        return self.get_url(url, {}, **kwargs)

    def fetchDownTime(self, **kwargs):
        """"
        Fetch Card Details of a Payment

        Args:
            payment_id : Id for which payment objects has to be retrieved

        Returns:
            Payment dict for given Order Id
        """
        url = f"{self.base_url}/downtimes"
        return self.get_url(url, {}, **kwargs)

    def fetchDownTimeById(self, downtime_id, **kwargs):
        """"
        Fetch Payment Downtime Details by ID

        Args:
            payment_id : Id for which payment objects has to be retrieved

        Returns:
            Payment dict for given Order Id
        """
        url = f"{self.base_url}/downtimes/{downtime_id}"
        return self.get_url(url, {}, **kwargs)

    def createPaymentJson(self, data={}, **kwargs):
        """"
        Create a Payment

        Args:
            payment_id : Id for which payment object has to be refunded
            amount : Amount for which the payment has to be refunded

        Returns:
            Payment Dict which was created
        """
        url = f"{self.base_url}/create/json"
        return self.post_url(url, data, **kwargs)

    def createRecurring(self, data={}, **kwargs):
        """"
        Create Recurring Payments
        Return:
            Recurring Payments dict
        """
        url = f"{self.base_url}/create/recurring"
        return self.post_url(url, data, **kwargs)

    def createUpi(self, data={}, **kwargs):
        """"
        Initiate a payment
        Return:
          Payments dict
        """
        url = f"{self.base_url}/create/upi"
        return self.post_url(url, data, **kwargs)

    def validateVpa(self, data={}, **kwargs):
        """"
        Validate the VPA
        Return:
          Payments dict
        """
        url = f"{self.base_url}/validate/vpa"
        return self.post_url(url, data, **kwargs)

    def fetchPaymentMethods(self, **kwargs):
        """"
        Fetch payment methods
        Return:
          Payments dict
        """
        url = f"/methods"
        return self.get_url(url, {}, **kwargs)

    def otpGenerate(self, payment_id, data={}, **kwargs):
        """"
        Otp Generate

        Args:
            payment_id : Id for which upi transfer entity has to be fetched

        Returns:
            Otp Dict which was created
        """
        url = f"{self.base_url}/{payment_id}/otp_generate"
        return self.post_url(url, data, **kwargs)

    def otpSubmit(self, payment_id, data={}, **kwargs):
        """"
        Otp Submit

        Args:
            payment_id : Id for which upi transfer entity has to be fetched

        Returns:
            Otp Dict which was created
        """
        url = f"{self.base_url}/{payment_id}/otp/submit"
        return self.post_url(url, data, **kwargs)

    def otpResend(self, payment_id, data={}, **kwargs):
        """"
        Otp Resend

        Args:
            payment_id : Id for which upi transfer entity has to be fetched

        Returns:
            Otp Dict which was created
        """
        url = f"{self.base_url}/{payment_id}/otp/resend"
        return self.post_url(url, data, **kwargs)
