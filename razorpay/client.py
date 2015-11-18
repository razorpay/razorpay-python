from types import ModuleType
import json

import requests

from . import resources
from . import errors

# Create a dict of resource classes
RESOURCE_CLASSES = {}
for name, module in resources.__dict__.items():
    if isinstance(module, ModuleType) and name.capitalize() in module.__dict__:
        RESOURCE_CLASSES[name] = module.__dict__[name.capitalize()]

# Create a mapping of status codes to classes
STATUS_MAP = {}
for name, Klass in errors.__dict__.items():
    if isinstance(Klass, type) and issubclass(Klass, errors.RazorpayError):
        STATUS_MAP[Klass().status] = Klass


class Client:
    """Razorpay client class"""

    DEFAULTS = {
        'base_url': 'https://api.razorpay.com/v1'
    }

    CLIENT_OPTIONS = set(DEFAULTS.keys())
    QUERY_OPTIONS = set(['from', 'to', 'count', 'skip'])
    REQUEST_OPTIONS = set(['headers', 'params', 'data'])

    ALL_OPTIONS = CLIENT_OPTIONS | QUERY_OPTIONS | REQUEST_OPTIONS

    def __init__(self, session=None, auth=None, **options):
        """Initialize a Client object with session, optional auth handler, and options"""
        self.session = session or requests.Session()
        self.auth = auth
        # merge the provided options (if any) with the global DEFAULTS
        self.options = _merge(self.DEFAULTS, options)
        # intializes each resource, injecting this client object into the constructor
        for name, Klass in RESOURCE_CLASSES.items():
            setattr(self, name, Klass(self))

    def request(self, method, path, **options):
        """Dispatches a request to the Razorpay HTTP API"""
        options = self._merge_options(options)
        url = options['base_url'] + path
        request_options = self._parse_request_options(options)
        response = getattr(self.session, method)(url, auth=self.auth, **request_options)
        if response.status_code in STATUS_MAP:
            raise STATUS_MAP[response.status_code](response)
        elif response.status_code >= 500 and response.status_code < 600:
            raise errors.ServerError(response)
        else:
            return response.json()

    def get(self, path, **options):
        """Parses GET request options and dispatches a request."""
        query_options = self._parse_query_options(options)
        parameter_options = self._parse_parameter_options(options)
        query = _merge(query_options, parameter_options)  # options in the query takes precendence
        return self.request('get', path, params=query, **options)

    def post(self, path, data, **options):
        """Parses POST request options and dispatches a request."""
        parameter_options = self._parse_parameter_options(options)
        data = _merge(parameter_options, data)  # values in the data body takes precendence
        return self.request('post', path, data=data, headers={'content-type': 'application/json'}, **options)

    def _merge_options(self, *objects):
        """Merges one or more options objects with client's options and returns a new options object"""
        return _merge(self.options, *objects)

    def _parse_query_options(self, options):
        """Selects query string options out of the provided options object"""
        return self._select_options(options, self.QUERY_OPTIONS)

    def _parse_parameter_options(self, options):
        """Selects all unknown options (not query string, API, or request options)"""
        return self._select_options(options, self.ALL_OPTIONS, invert=True)

    def _parse_request_options(self, options):
        """Select and formats options to be passed to the 'requests' library's request methods"""
        request_options = self._select_options(options, self.REQUEST_OPTIONS)
        if 'params' in request_options:
            params = request_options['params']
            for key in params:
                if isinstance(params[key], bool):
                    params[key] = json.dumps(params[key])
        if 'data' in request_options:
            # remove empty 'options':
            if 'options' in request_options['data'] and len(request_options['data']['options']) == 0:
                del request_options['data']['options']
            # serialize 'data' to JSON, requests doesn't do this automatically:
            request_options['data'] = json.dumps(request_options['data'])
        return request_options

    def _select_options(self, options, keys, invert=False):
        """Selects the provided keys (or everything except the provided keys) out of an options object"""
        options = self._merge_options(options)
        result = {}
        for key in options:
            if (invert and key not in keys) or (not invert and key in keys):
                result[key] = options[key]
        return result


def _merge(*objects):
    """Merge one or more objects into a new object"""
    result = {}
    [result.update(obj) for obj in objects]
    return result
