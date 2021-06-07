from .base import Resource
from ..constants.url import URL
import warnings


class FundAccount(Resource):
    def __init__(self, client=None):
        super(FundAccount, self).__init__(client)
        self.base_url = URL.FUND_ACCOUNT_URL

    def fetch(self, fund_account_id, data={}, **kwargs):
        """
        """
        return super(FundAccount, self).fetch(fund_account_id, data, **kwargs)

    def create(self, data={}, **kwargs):
        """
        """
        url = self.base_url
        return self.post_url(url, data, **kwargs)

    def all(self, data={}, **kwargs):
        """"
        Fetch all Fund Accounts entities

        Returns:
            Dictionary of Fund Accounts data
        """
        return super(FundAccount, self).all(data, **kwargs)

    # def delete(self, fund_account_id, data={}, **kwargs):
    #     """
    #     """
    #     url = "{}/{}".format(self.base_url, fund_account_id)
    #     print(url)
    #     return self.delete_url(url, data, **kwargs)

    