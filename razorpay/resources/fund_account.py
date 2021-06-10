from .base import Resource
from ..constants.url import URL
import warnings


class FundAccount(Resource):
    def __init__(self, client=None):
        super(FundAccount, self).__init__(client)
        self.base_url = URL.FUND_ACCOUNT_URL

    def fetch(self, fund_account_id, data={}, **kwargs):
        """"
        Fetch fund_account for given Id

        Args:
            fund_account_id : Id for which fund_account object has to be retrieved

        Returns:
            fund_account dict for given fund_account Id
        """
        return super(FundAccount, self).fetch(fund_account_id, data, **kwargs)

    def create(self, data={}, **kwargs):
        """"
        Create Fund Account from given dict

        Returns:
            Fund Account Dict which was created
        """
        url = self.base_url
        return self.post_url(url, data, **kwargs)

    def all(self, data={}, **kwargs):
        """"
        Fetch all Fund Account entities

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

    def update(self, fund_account_id, data={}, **kwargs):
        """
        Update Fund Account from given fund account id with given dict

        Returns:
            Dict of Fund Account which was updated.
        """
        url = "{}/{}".format(self.base_url, fund_account_id)
        return super(FundAccount, self).patch_url(url, data, **kwargs)

    def validation(self, data={}, **kwargs):
        """
        """
        url = "{}/validations".format(self.base_url)
        return self.post_url(url, data, **kwargs)

    def all_validations(self, data={}, **kwargs):
        """
        """
        url = "{}/validations".format(self.base_url)
        return self.get_url(url, data, **kwargs)

    def fetch_validation(self,fund_account_validation_id, data={}, **kwargs):
        """
        """
        url = "{}/validations/{}".format(self.base_url, fund_account_validation_id)
        return self.get_url(url, data, **kwargs)
        