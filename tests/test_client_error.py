import responses
import json

from .helpers import ClientTestCase
from razorpay.errors import BadRequestError, GatewayError, ServerError


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

    @responses.activate
    def test_gateway_error(self):
        count = 10
        result = {
            'error':
            {
                'code': 'GATEWAY_ERROR',
                'description': 'Payment processing failed due to error at bank/wallet gateway'
            }
        }

        url = '{}?count={}'.format(self.base_url, count)
        responses.add(responses.GET, url, status=504, body=json.dumps(result),
                      match_querystring=True)
        self.assertRaises(
            GatewayError,
            self.client.payment.all,
            {'count': count})

    @responses.activate
    def test_server_error(self):
        count = 10
        result = {
            'error':
            {
                'code': 'SERVER_ERROR',
                'description': 'The server encountered an error. The incident has been reported to admins.'
            }
        }

        url = '{}?count={}'.format(self.base_url, count)
        responses.add(responses.GET, url, status=500, body=json.dumps(result),
                      match_querystring=True)
        self.assertRaises(
            ServerError,
            self.client.payment.all,
            {'count': count})
