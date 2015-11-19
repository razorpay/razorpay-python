import json
import razorpay
import responses
import os
import unittest

from responses import GET, POST


def mock_file(filename):
    if filename == '':
        return ''
    file_path = os.path.join(os.path.dirname(__file__), 'mocks/' + filename + '.json')
    return open(file_path).read()


class ClientTestCase(unittest.TestCase):
    def setUp(self):
        self.payment_id = 'fake_payment_id'
        self.refund_id = 'fake_refund_id'
        self.client = razorpay.Client(auth=('fake_key_id', 'fake_key_secret'))
