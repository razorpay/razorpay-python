import os
import json
import requests
import pkg_resources

from types import ModuleType

from . import resources

from .errors import (BadRequestError, NoAuthorizationError,
                     NotFoundError, ServerError)


# Create a dict of resource classes
RESOURCE_CLASSES = {}
for name, module in resources.__dict__.items():
    if isinstance(module, ModuleType) and name.capitalize() in module.__dict__:
        RESOURCE_CLASSES[name] = module.__dict__[name.capitalize()]


class Client:
    """Razorpay client class"""

    DEFAULTS = {
        'base_url': 'https://api.razorpay.com/v1'
    }

    def __init__(self, session=None, auth=None, **options):
        """
        Initialize a Client object with session,
        optional auth handler, and options
        """
        self.session = session or requests.Session()
        self.auth = auth
        file_dir = os.path.dirname(__file__)
        self.cert_path = file_dir + '/ca-bundle.crt'

        # intializes each resource
        # injecting this client object into the constructor
        for name, Klass in RESOURCE_CLASSES.items():
            setattr(self, name, Klass(self))

    def _update_user_agent_header(self, options):
        user_agent = "{}{}".format('Razorpay-Python/',  self._get_version())

        if 'headers' in options:
            options['headers']['User-Agent'] = user_agent
        else:
            options['headers'] = {'User-Agent': user_agent}

        return options

    def _get_version(self):
        return pkg_resources.require("razorpay")[0].version

    def request(self, method, path, **options):
        """
        Dispatches a request to the Razorpay HTTP API
        """
        base_url = self.DEFAULTS['base_url']

        if 'base_url' in options:
            base_url = options['base_url']
            del(options['base_url'])

        options = self._update_user_agent_header(options)

        url = "{}{}".format(base_url,  path)
        response = getattr(self.session, method)(url, auth=self.auth,
                                                 verify=self.cert_path,
                                                 **options)
        if response.status_code == 200:
            return response.json()
        else:
            msg = ""
            json_response = response.json()
            if 'error' in json_response:
                if 'description' in json_response['error']:
                    msg = json_response['error']['description']
            if response.status_code == 400:
                raise BadRequestError(msg)
            if response.status_code == 401:
                raise NoAuthorizationError(msg)
            if response.status_code == 404:
                raise NotFoundError(msg)
            elif response.status_code >= 500 and response.status_code < 600:
                raise ServerError(msg)

    def get(self, path, params, **options):
        """
        Parses GET request options and dispatches a request
        """
        return self.request('get', path, params=params, **options)

    def post(self, path, data, **options):
        """
        Parses POST request options and dispatches a request
        """
        data, options = self._update_request(data, options)
        return self.request('post', path, data=data, **options)

    def _update_request(self, data, options):
        """
        Updates The resource data and header options
        """
        data = json.dumps(data)
        if 'headers' in options:
            options['headers']['Content-type'] = 'application/json'
        else:
            options['headers'] = {'Content-type': 'application/json'}

        return data, options
