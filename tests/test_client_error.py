import responses
import json

from .helpers import mock_file, ClientTestCase
from razorpay.errors import BadRequestError


class TestClientError(ClientTestCase):

    def setUp(self):
        super(TestClientError, self).setUp()
        self.base_url = '{}/payments'.format(self.base_url)

    @responses.activate
    def test_payment_with_invalid_options(self):
        count = 10000
        result = {
            'error':
            {
                'field': 'count',
                'code': 'BAD_REQUEST_ERROR',
                'description': 'The count may not be greater than 100.'
            }
        }

        url = '{}?count={}'.format(self.base_url, count)
        responses.add(responses.GET, url, status=400, body=json.dumps(result),
                      match_querystring=True)
        self.assertRaises(
            BadRequestError,
            self.client.payment.all,
            {'count': count})
