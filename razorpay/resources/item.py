from .base import Resource
from ..constants.url import URL


class Item(Resource):
    def __init__(self, client=None):
        super(Item, self).__init__(client)
        self.base_url = URL.ITEM_URL

    def create(self, data={}, **kwargs):
        """"
        Create Item from given dict

        Args:
            data : Dictionary having keys (name, amount, currency, [description]) using which Item has to be created

        Returns:
            Item Dict which was created
        """
        url = self.base_url
        return self.post_url(url, data, **kwargs)

    def fetch(self, item_id, data={}, **kwargs):
        """"
        Fetch Item for given Id

        Args:
            item_id : Id for which Item object has to be retrieved

        Returns:
            Item dict for given subscription Id
        """
        return super(Item, self).fetch(item_id, data, **kwargs)

    def all(self, data={}, **kwargs):
        """"
        Fetch all item entities

        Returns:
            Dictionary of item data
        """
        return super(Item, self).all(data, **kwargs)
