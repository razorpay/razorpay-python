import warnings

from .base import Resource
from ..constants import URL


class PayoutLink(Resource):
    def __init__(self, client=None):
        super(PayoutLink, self).__init__(client)
        self.base_url = URL.PAYOUT_LINKS_URL

    def create(self, data={}, **kwargs):
        """"
        Create Payout link from given dict

        Returns:
            Payout link Dict which was created
        """
        url = self.base_url
        return self.post_url(url, data, **kwargs)

    def fetch(self, payoutlink_id, data={}, **kwargs):
        """"
        Fetch Payout link for given Id

        Args:
            payoutlink_id : Id for which payout link object has to be retrieved

        Returns:
            Payout link dict
        """
        return super(PayoutLink, self).fetch(payoutlink_id, data, **kwargs)

    def fetch_all(self, data={}, **kwargs):  # pragma: no cover
        warnings.warn("Will be Deprecated in next release, use all",
                      DeprecationWarning)
        return self.all(data, **kwargs)

    def cancel(self, payoutlink_id,data={}, **kwargs):
        """
        Cancel a Payout link.

        Returns:
        Payout link dict of cancelled Payout link
        """
        url = "{}/{}/cancel".format(self.base_url, payoutlink_id)
        return self.post_url(url, data, **kwargs)
