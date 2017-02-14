class Resource(object):

    def __init__(self, client=None):
        self.client = client

    def all(self, **kwargs):
        return self.get_url(self.base_url, **kwargs)

    def fetch(self, id, **kwargs):
        url = "{}/{}".format(self.base_url, id)
        return self.get_url(url, **kwargs)

    def get_url(self, url, **kwargs):
        return self.client.get(url, **kwargs)

    def post_url(self, url, data, **kwargs):
        return self.client.post(url, data, **kwargs)
