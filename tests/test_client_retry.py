import unittest
from unittest.mock import patch, MagicMock
import requests

from .helpers import ClientTestCase
from razorpay.errors import BadRequestError, ServerError


class TestClientRetry(ClientTestCase):

    def test_retry_disabled_by_default(self):
        self.assertFalse(self.client.retry_enabled)

    def test_enable_retry_sets_flag(self):
        self.client.enable_retry(True)
        self.assertTrue(self.client.retry_enabled)

    def test_disable_retry_clears_flag(self):
        self.client.enable_retry(True)
        self.client.enable_retry(False)
        self.assertFalse(self.client.retry_enabled)

    def test_enable_retry_default_arg_is_false(self):
        self.client.enable_retry(True)
        self.client.enable_retry()
        self.assertFalse(self.client.retry_enabled)

    @patch('time.sleep', return_value=None)
    def test_retry_on_connection_error(self, mock_sleep):
        """Retries when a ConnectionError is raised, succeeds on second attempt."""
        self.client.enable_retry(True)
        self.client.max_retries = 3

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'id': 'pay_123'}

        with patch.object(self.client.session, 'get',
                          side_effect=[requests.exceptions.ConnectionError, mock_response]):
            result = self.client.get('/payments', {})

        self.assertEqual(result, {'id': 'pay_123'})
        self.assertEqual(mock_sleep.call_count, 1)

    @patch('time.sleep', return_value=None)
    def test_retry_on_timeout(self, mock_sleep):
        """Retries when a Timeout is raised, succeeds on second attempt."""
        self.client.enable_retry(True)
        self.client.max_retries = 3

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'id': 'pay_456'}

        with patch.object(self.client.session, 'get',
                          side_effect=[requests.exceptions.Timeout, mock_response]):
            result = self.client.get('/payments', {})

        self.assertEqual(result, {'id': 'pay_456'})
        self.assertEqual(mock_sleep.call_count, 1)

    @patch('time.sleep', return_value=None)
    def test_raises_after_max_retries_exceeded(self, mock_sleep):
        """Raises ConnectionError after exhausting all retry attempts."""
        self.client.enable_retry(True)
        self.client.max_retries = 3

        with patch.object(self.client.session, 'get',
                          side_effect=requests.exceptions.ConnectionError("down")):
            with self.assertRaises(requests.exceptions.ConnectionError):
                self.client.get('/payments', {})

        self.assertEqual(mock_sleep.call_count, 2)  # sleeps between attempts, not after last

    def test_no_retry_when_disabled(self):
        """With retry disabled, a ConnectionError propagates immediately without sleep."""
        self.client.enable_retry(False)

        with patch.object(self.client.session, 'get',
                          side_effect=requests.exceptions.ConnectionError("down")):
            with patch('time.sleep') as mock_sleep:
                with self.assertRaises(requests.exceptions.ConnectionError):
                    self.client.get('/payments', {})

        mock_sleep.assert_not_called()

    @patch('time.sleep', return_value=None)
    def test_no_retry_on_bad_request_error(self, mock_sleep):
        """BadRequestError (4xx) is never retried."""
        self.client.enable_retry(True)
        self.client.max_retries = 3

        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.json.return_value = {
            'error': {'code': 'BAD_REQUEST_ERROR', 'description': 'invalid param'}
        }

        with patch.object(self.client.session, 'get', return_value=mock_response):
            with self.assertRaises(BadRequestError):
                self.client.get('/payments', {})

        mock_sleep.assert_not_called()

    @patch('time.sleep', return_value=None)
    def test_no_retry_on_server_error(self, mock_sleep):
        """ServerError (5xx API errors) are not retried."""
        self.client.enable_retry(True)
        self.client.max_retries = 3

        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_response.json.return_value = {
            'error': {'code': 'SERVER_ERROR', 'description': 'internal error'}
        }

        with patch.object(self.client.session, 'get', return_value=mock_response):
            with self.assertRaises(ServerError):
                self.client.get('/payments', {})

        mock_sleep.assert_not_called()

    def test_custom_retry_params_via_constructor(self):
        """Retry parameters passed to constructor are stored on the client."""
        import razorpay
        client = razorpay.Client(
            auth=('key_id', 'key_secret'),
            max_retries=10,
            initial_delay=2,
            max_delay=30,
            jitter=0.1,
        )
        self.assertEqual(client.max_retries, 10)
        self.assertEqual(client.initial_delay, 2)
        self.assertEqual(client.max_delay, 30)
        self.assertEqual(client.jitter, 0.1)


if __name__ == '__main__':
    unittest.main()
