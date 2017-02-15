from .base import Resource
from .Url import URL


class Card(Resource):
    def __init__(self, client=None):
        self.client = client
        self.base_url = URL.CARD_URL

    def fetch(self, card_id, **kwargs):
        """"
        Fetch Card for given Id

        Args:
            card_id : Id for which card object has to be retrieved

        Returns:
            Card dict for given card Id
        """
        url = "{}/{}".format(self.base_url, card_id)
        return self.get_url(url, **kwargs)
