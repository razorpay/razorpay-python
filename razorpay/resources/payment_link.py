import warnings
from typing import Dict, Any, Union, Optional

from .base import Resource
from ..constants.url import URL


class PaymentLink(Resource):
    def __init__(self, client=None):
        super(PaymentLink, self).__init__(client)
        self.base_url = URL.V1 + URL.PAYMENT_LINK_URL

    def fetch_all(self, data: Optional[Dict[str, Any]] = None, **kwargs) -> Dict[str, Any]: # pragma: no cover
        """
        Fetch all Payment Link entities (Deprecated)
        """
        warnings.warn("Will be Deprecated in next release", DeprecationWarning)
        return self.all(data, **kwargs)

    def all(self, data: Optional[Dict[str, Any]] = None, **kwargs) -> Dict[str, Any]:
        """
        Fetch all Payment Link entities

        Args:
            data: Dictionary of filters

        Returns:
            Dictionary of Payment Link data
        """
        return super(PaymentLink, self).all(data, **kwargs)

    def fetch(self, payment_link_id: str, data: Optional[Dict[str, Any]] = None, **kwargs) -> Dict[str, Any]:
        """
        Fetch Payment Link for given ID

        Args:
            payment_link_id : Unique identifier for the Payment Link

        Returns:
            Payment Link dictionary
        """
        return super(PaymentLink, self).fetch(payment_link_id, data, **kwargs)

    def create(self, data: Dict[str, Any], **kwargs) -> Dict[str, Any]:
        """
        Create Payment Link from given dict

        Args:
            data : Dictionary containing Payment Link details

        Returns:
            Payment Link Dict which was created

        """
        # Fix for Issue #321: Intercept and fix "string boolean" mistakes
        # If user passes "true"/"false" strings, convert them to 1/0 integers
        if 'options' in data:
            checkout = data['options'].get('checkout', {})
            if 'method' in checkout:
                for key, value in checkout['method'].items():
                    if isinstance(value, str):
                        if value.lower() == 'true':
                            checkout['method'][key] = 1
                        elif value.lower() == 'false':
                            checkout['method'][key] = 0

        url = self.base_url
        return self.post_url(url, data, **kwargs)

    def cancel(self, payment_link_id: str, **kwargs) -> Dict[str, Any]:
        """
        Cancel an unpaid Payment Link with given ID via API.
        It can only be called on a Payment Link that is not in the paid state.

        Args:
            payment_link_id : Unique identifier for the Payment Link

        Returns:
            Payment Link entity with status attribute as 'cancelled'
        """
        url = f"{self.base_url}/{payment_link_id}/cancel"
        return self.post_url(url, {}, **kwargs)

    def edit(self, payment_link_id: str, data: Optional[Dict[str, Any]] = None, **kwargs) -> Dict[str, Any]:
        """
        Edit the Payment Link

        Args:
            payment_link_id: Unique identifier for the Payment Link
            data : Dictionary having keys to update:
                - reference_id : Adds a unique reference number
                - expire_by : Timestamp (Unix) when the link should expire
                - notes : Key-value pair as notes

        Returns:
            Payment Link Dict which was edited
        """
        url = f"{self.base_url}/{payment_link_id}"
        return self.patch_url(url, data, **kwargs)

    def notifyBy(self, payment_link_id: str, medium: str, **kwargs) -> Dict[str, Any]:
        """
        Send notification for the Payment Link

        Args:
            payment_link_id : Unique identifier of the Payment Link
            medium : The medium to send notification (sms/email)

        Returns:
            API response dictionary
        """
        url = f"{self.base_url}/{payment_link_id}/notify_by/{medium}"
        return self.post_url(url, {}, **kwargs)

    # Alias to fix camelCase naming violation (PEP 8)
    notify_by = notifyBy