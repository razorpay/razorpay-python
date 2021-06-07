from .base import Resource
from ..constants.url import URL
import warnings


class Payout(Resource):
    def __init__(self, client=None):
        super(Payout, self).__init__(client)
        self.base_url = URL.PAYOUTS_URL

    def fetch(self, payout_id, data={}, **kwargs):
        """"
        Fetch Payout for given Id

        Args:
            payout_id : Id for which payout object has to be retrieved

        Returns:
            Payout dict for given payout Id
        """
        return super(Payout, self).fetch(payout_id, data, **kwargs)

    def create(self, data={}, **kwargs):
        """"
        Create Payout from given dict

        Returns:
            Payout Dict which was created
        """
        url = self.base_url
        return self.post_url(url, data, **kwargs)

    def purposes(self, data={}, **kwargs):
        """

        """
        url = "{}/purposes".format(self.base_url)
        return self.get_url(url, data, **kwargs)

    def cancel(self, payout_id, data={}, **kwargs):
        """

        """
        url = "{}/{}/cancel".format(self.base_url,payout_id)
        return self.post_url(url, data, **kwargs)