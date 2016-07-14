class Resource(object):

    def __init__(self, client=None):
        self.client = client

    def get_url(self, url, **kwargs):
        return self.client.get(url, **kwargs)

    def post_url(self, url, data, **kwargs):
        return self.client.post(url, data, **kwargs)
