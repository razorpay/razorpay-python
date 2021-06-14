from .base import Resource
from ..constants.url import URL
import warnings
from ..errors import BadRequestError


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

    def all(self, data={}, **kwargs):
        """"
        Fetch all Payout entities

        Returns:
            Dictionary of Payout data
        """
        return super(Payout, self).all(data, **kwargs)

    def create(self, idempotency_key, data={}, **kwargs):
        """"
        Create Payout from given dict

        Args:
            idempotency_key: idempotency key which will be unique for each payout. idempotency_key should be a none empty string.

        Returns:
            Payout Dict which was created
        """

        if idempotency_key == None:
            msg = "Idempotency Key can't be None"
            raise BadRequestError(msg)

        if not idempotency_key.strip():
            msg = "Idempotency Key can't be empty"
            raise BadRequestError(msg)
        
        kwargs['headers'] = {'X-Payout-Idempotency': idempotency_key}
        url = self.base_url
        return self.post_url(url, data, **kwargs)

    def purposes(self, data={}, **kwargs):
        """
        Fetch all puposes

        Returns:
            Dictionary of all purposes
        """
        url = "{}/purposes".format(self.base_url)
        return self.get_url(url, data, **kwargs)

    def cancel(self, payout_id, data={}, **kwargs):
        """
        Cancels Payout for given payout_id

        Args:
            payout_id: ID for which payout has to be cancelled.

        Returns:
            Payout Dict for the payout id.
        """
        url = "{}/{}/cancel".format(self.base_url,payout_id)
        return self.post_url(url, data, **kwargs)
