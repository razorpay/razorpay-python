from .base import Resource
from ..constants.url import URL


class FundAccount(Resource):
    def __init__(self, client=None):
        super(FundAccount, self).__init__(client)
        self.base_url = URL.FUND_ACCOUNT_URL

    def all(self, data={}, **kwargs):
        """"
        Fetch all Fund Account entities

        Returns:
            Dictionary of Fund Account
        """
        return super(FundAccount, self).all(data, **kwargs)

    def create(self, data={}, **kwargs):
        """"
        Create a fund account

        Args:
            data : Dictionary having keys using which order have to be created
                'customerId' :  Customer Id for the customer
                'account_type' : The bank_account to be linked to the customer ID
                'bank_account' : key value pair

        Returns:
            fund account Dict which was created
        """
        url = self.base_url
        return self.post_url(url, data, **kwargs)

    def fetch(self, fundaccount_id, data={}, **kwargs):
        """"
        Fetch fund account for given Id

        Args:
            fundaccount_id : Id for which fund account object has to be retrieved

        Returns:
            fund account dict
        """
        return super(FundAccount, self).fetch(fundaccount_id, data, **kwargs)

    def status(self, fundaccount_id, data={}, **kwargs):
        """"
        Update the status of  fund account from given dict (ACTIVE/INACTIVE)

        Returns:
            fund account dict which was edited
        """
        url = '{}/{}'.format(self.base_url, fundaccount_id)

        return self.patch_url(url, data, **kwargs)

    def create_public(self, data={}, **kwargs):
        """"
        Create Fund account for cards (only for Non- PCI DSS Compliant) from given dict

        Returns:
            Fund account Dict which was created
        """
        url = '{}/public'.format(self.base_url)
        return self.post_url(url, data, **kwargs)
