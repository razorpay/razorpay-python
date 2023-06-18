import warnings

from .base import Resource
from ..constants.url import URL


class Validations(Resource):
    def __init__(self, client=None):
        super(Validations, self).__init__(client)
        self.base_url = URL.FUND_ACCOUNT_VALIDATION_URL

    def create(self, data={}, **kwargs):
        """"
        Create FAV from given dict

        Returns:
            FAV Dict which was created
        """
        url = self.base_url
        return self.post_url(url, data, **kwargs)

    def fetch(self, fundaccountvalidation_id, data={}, **kwargs):
        """"
        Fetch FAV for given Id

        Args:
            fundaccountvalidation_id : Id for which FAV object has to be retrieved

        Returns:
            FAV dict
        """
        return super(Validations, self).fetch(fundaccountvalidation_id, data, **kwargs)

    def fetch_all(self, data={}, **kwargs):  # pragma: no cover
        warnings.warn("Will be Deprecated in next release, use all",
                      DeprecationWarning)
        return self.all(data, **kwargs)
