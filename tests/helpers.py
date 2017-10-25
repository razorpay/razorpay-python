import razorpay
import os
import unittest


def mock_file(filename):
    if not filename:
        return ''
    file_dir = os.path.dirname(__file__)
    file_path = "{}/mocks/{}.json".format(file_dir, filename)
    return open(file_path).read()


class ClientTestCase(unittest.TestCase):
    def setUp(self):
        self.base_url = 'https://api.razorpay.com/v1'
        self.secondary_url = 'https://test-api.razorpay.com/v1'
        self.payment_id = 'fake_payment_id'
        self.refund_id = 'fake_refund_id'
        self.card_id = 'fake_card_id'
        self.customer_id = 'fake_customer_id'
        self.token_id = 'fake_token_id'
        self.addon_id = 'fake_addon_id'
        self.subscription_id = 'fake_subscription_id'
        self.plan_id = 'fake_plan_id'
        self.client = razorpay.Client(auth=('key_id', 'key_secret'))
        self.secondary_client = razorpay.Client(auth=('key_id', 'key_secret'),
                                                base_url=self.secondary_url)
