from .base import Resource
from ..constants.url import URL
import warnings


class Invoice(Resource):
    def __init__(self, client=None):
        super(Invoice, self).__init__(client)
        self.base_url = URL.INVOICE_URL

    def fetch_all(self, data={}, **kwargs):  # pragma: no cover
        warnings.warn("Will be Deprecated in next release", DeprecationWarning)
        return self.all(data, **kwargs)

    def all(self, data={}, **kwargs):
        """"
        Fetch all Invoice entities

        Returns:
            Dictionary of Invoice data
        """
        return super(Invoice, self).all(data, **kwargs)

    def fetch(self, invoice_id, data={}, **kwargs):
        """"
        Fetch Invoice for given Id

        Args:
            invoice_id : Id for which invoice object has to be retrieved

        Returns:
            Invoice dict for given invoice Id
        """
        return super(Invoice, self).fetch(invoice_id, data, **kwargs)

    def create(self, data={}, **kwargs):
        """"
        Create Invoice from given dict

        Args:
            data : Dictionary having keys using which invoice have to be created

        Returns:
            Invoice Dict which was created
        """
        url = self.base_url
        return self.post_url(url, data, **kwargs)

    def notify_by(self, invoice_id, medium, data={}, **kwargs):
        """"
        Send/Resend notifications to customer via email/sms

        Args:
            invoice_id : Id for trigger notify
            medium : Medium for triggering notification via email or sms

        Returns:
            True or False
        """
        url = "{}/{}/notify_by/{}".format(self.base_url, invoice_id, medium)
        return self.post_url(url, data, **kwargs)

    def cancel(self, invoice_id, data={}, **kwargs):
        """"
        Cancel an unpaid Invoice with given ID via API

        Args:
            invoice_id : Id for cancel the invoice
        Returns:
            The response for the API will be the invoice entity, similar to create/update API response, with status attribute's value as cancelled
        """
        url = "{}/{}/cancel".format(self.base_url, invoice_id)
        return self.post_url(url, data, **kwargs)

    def delete(self, invoice_id, data={}, **kwargs):
        """"
        Delete an invoice

        Args:
            invoice_id : Id for delete the invoice
        Returns:
            The response is always be an empty array
        """
        url = "{}/{}".format(self.base_url, invoice_id)
        return self.delete_url(url, data, **kwargs)

    def issue(self, invoice_id, data={}, **kwargs):
        """"
        Issues an invoice in draft state

        Args:
            invoice_id : Id for delete the invoice
        Returns:
            Its response is the invoice entity, similar to create/update API response
        """
        url = "{}/{}/issue".format(self.base_url, invoice_id)
        return self.delete_url(url, data, **kwargs)

    def edit(self, invoice_id, data={}, **kwargs):
        """"
        Update an invoice

        Args:
            invoice_id : Id for delete the invoice
            data : Dictionary having keys using which invoice have to be updated
        Returns:
            It will update the invoice
        """
        url = "{}/{}".format(self.base_url, invoice_id)
        return self.patch_url(url, data, **kwargs)
