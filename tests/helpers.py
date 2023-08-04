import razorpay
import os
import unittest


def mock_file(filename):
    if not filename:
        return ''
    file_dir = os.path.dirname(__file__)
    file_path = f"{file_dir}/mocks/{filename}.json"
    with open(file_path) as f:
        mock_file_data = f.read()
    return mock_file_data


class ClientTestCase(unittest.TestCase):
    def setUp(self):
        self.base_url = 'https://api.razorpay.com/v1'
        self.base_url_v2 = 'https://api.razorpay.com/v2'
        self.secondary_url = 'https://test-api.razorpay.com'
        self.v1 = 'v1'
        self.v2 = 'v2'
        self.payment_id = 'fake_payment_id'
        self.refund_id = 'fake_refund_id'
        self.card_id = 'fake_card_id'
        self.customer_id = 'fake_customer_id'
        self.token_id = 'fake_token_id'
        self.addon_id = 'fake_addon_id'
        self.subscription_id = 'fake_subscription_id'
        self.plan_id = 'fake_plan_id'
        self.settlement_id = 'fake_settlement_id'
        self.client = razorpay.Client(auth=('key_id', 'key_secret'))
        self.secondary_client = razorpay.Client(auth=('key_id', 'key_secret'),
                                                base_url=self.secondary_url)
