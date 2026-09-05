import importlib.metadata
import unittest
import warnings
from unittest import mock

import razorpay


class TestClientVersion(unittest.TestCase):

    def setUp(self):
        self.client = razorpay.Client(auth=('key_id', 'key_secret'))

    def test_version_comes_from_package_metadata(self):
        self.assertEqual(self.client._get_version(),
                         importlib.metadata.version('razorpay'))

    def test_missing_metadata_falls_back_with_a_warning(self):
        def missing(name):
            raise importlib.metadata.PackageNotFoundError(name)

        with mock.patch('importlib.metadata.version', missing):
            with warnings.catch_warnings(record=True) as caught:
                warnings.simplefilter('always')
                version = self.client._get_version()

        self.assertTrue(version)
        self.assertTrue(any(issubclass(w.category, UserWarning) for w in caught),
                        'a UserWarning should explain the fallback')

    def test_requests_still_work_without_package_metadata(self):
        def missing(name):
            raise importlib.metadata.PackageNotFoundError(name)

        with mock.patch('importlib.metadata.version', missing):
            with warnings.catch_warnings():
                warnings.simplefilter('ignore')
                options = self.client._update_user_agent_header({})

        self.assertIn('Razorpay-Python/', options['headers']['User-Agent'])
