import warnings

from .base import Resource
from ..constants import URL


class Payout(Resource):
    def __init__(self, client=None):
        super(Payout, self).__init__(client)
        self.base_url = URL.PAYOUT_URL

    def create(self, data={}, **kwargs):
        """"
        Create Payout from given dict

        Returns:
            Payout Dict which was created
        """
        url = self.base_url
        return self.post_url(url, data, **kwargs)

    def fetch(self, payout_id, data={}, **kwargs):
        """"
        Fetch Payout for given Id

        Args:
            payout_id : Id for which payout object has to be retrieved

        Returns:
            Payout dict
        """
        return super(Payout, self).fetch(payout_id, data, **kwargs)

    def fetch_all(self, data={}, **kwargs):  # pragma: no cover
        warnings.warn("Will be Deprecated in next release, use all",
                      DeprecationWarning)
        return self.all(data, **kwargs)

    def cancel_queued(self, payout_id,data={}, **kwargs):
        """
        Cancel a queued payout.

        Returns:
        Payout dict of cancelled payout
        """
        url = "{}/{}/cancel".format(self.base_url, payout_id)
        return self.post_url(url, data, **kwargs)

