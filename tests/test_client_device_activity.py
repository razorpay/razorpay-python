import unittest
import responses
import json

from .helpers import mock_file, ClientTestCase
from razorpay.errors import BadRequestError
import razorpay


class TestClientDeviceActivity(ClientTestCase):

    def setUp(self):
        super(TestClientDeviceActivity, self).setUp()
        self.device_activity_base_url = f"{self.base_url}/devices/activity"
        # Device APIs automatically use public authentication (key_id only) 
        # by passing use_public_auth=True internally in device_activity.py
        self.public_client = razorpay.Client(auth=('key_id', 'key_secret'))

    @responses.activate
    def test_create_device_activity(self):
        result = mock_file('fake_device_activity')
        url = self.device_activity_base_url
        responses.add(responses.POST, url, status=200,
                      body=json.dumps(result), match_querystring=True)
        self.assertEqual(self.public_client.device_activity.create({'foo': 'bar'}, device_mode='wired'), result)

    @responses.activate
    def test_get_status_device_activity(self):
        activity_id = 'act_123'
        result = mock_file('fake_device_activity_status')
        url = f"{self.device_activity_base_url}/{activity_id}"
        responses.add(responses.GET, url, status=200,
                      body=json.dumps(result), match_querystring=True)
        self.assertEqual(self.public_client.device_activity.get_status(activity_id, device_mode='wireless'), result)

    def test_invalid_device_mode_raises(self):
        with self.assertRaises(BadRequestError):
            self.public_client.device_activity.create({'foo': 'bar'}, device_mode='invalid') 