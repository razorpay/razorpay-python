import unittest
from unittest import mock

import razorpay


class TestClientSession(unittest.TestCase):

    def test_close_closes_session(self):
        session = mock.Mock()
        client = razorpay.Client(session=session, auth=('key_id', 'key_secret'))
        client.close()
        session.close.assert_called_once_with()

    def test_context_manager_returns_client_and_closes_on_exit(self):
        session = mock.Mock()
        with razorpay.Client(session=session, auth=('key_id', 'key_secret')) as client:
            self.assertIsInstance(client, razorpay.Client)
            session.close.assert_not_called()
        session.close.assert_called_once_with()

    def test_context_manager_closes_on_exception(self):
        session = mock.Mock()
        with self.assertRaises(RuntimeError):
            with razorpay.Client(session=session, auth=('key_id', 'key_secret')):
                raise RuntimeError('boom')
        session.close.assert_called_once_with()

    def test_default_session_is_closed(self):
        client = razorpay.Client(auth=('key_id', 'key_secret'))
        with mock.patch.object(client.session, 'close') as close:
            with client:
                pass
        close.assert_called_once_with()
