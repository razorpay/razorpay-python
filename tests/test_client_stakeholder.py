import responses
import json

from razorpay.constants.url import URL

from .helpers import mock_file, ClientTestCase


class TestClientStakeholder(ClientTestCase):

    def setUp(self):
        super(TestClientStakeholder, self).setUp()
        self.base_url = '{}/accounts'.format(self.base_url_v2)
        self.account_id = 'acc_GRWKk7qQsLnDjX'
        self.stakeholder_id = 'sth_MDdinTcycAkdK3'

    @responses.activate
    def test_stakeholder_create(self):
        init = mock_file('init_stakeholder')
        result = mock_file('fake_stakeholder')
        url = '{}/{}{}'.format(self.base_url, self.account_id, URL.STAKEHOLDER)
        responses.add(responses.POST,
                      url,
                      status=200,
                      body=json.dumps(result),
                      match_querystring=True)

        self.assertEqual(self.client.stakeholder.create(
            self.account_id, init), result)

    @responses.activate
    def test_stakeholder_fetch(self):
        result = mock_file('fake_stakeholder')
        url = '{}/{}{}/{}'.format(self.base_url, self.account_id,
                                   URL.STAKEHOLDER, self.stakeholder_id)
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.stakeholder.fetch(
            self.account_id, self.stakeholder_id), result)

    @responses.activate
    def test_stakeholder_edit(self):
        init = {
            "percentage_ownership": 20,
            "name": "Gauri Kumar",
            "relationship": {
                    "director": False,
                    "executive": True
            },
            "phone": {
                "primary": "9000090000",
                "secondary": "9000090000"
            },
            "addresses": {
                "residential": {
                    "street": "507, Koramangala 1st block",
                    "city": "Bangalore",
                    "state": "Karnataka",
                    "postal_code": "560035",
                    "country": "IN"
                }
            },
            "kyc": {
                "pan": "AVOPB1111J"
            },
            "notes": {
                "random_key_by_partner": "random_value2"
            }
        }
        result = mock_file('fake_stakeholder')
        url = '{}/{}{}/{}'.format(self.base_url, self.account_id,
                                   URL.STAKEHOLDER, self.stakeholder_id)
        responses.add(responses.PATCH, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.stakeholder.edit(
            self.account_id, self.stakeholder_id, init), result)

    @responses.activate
    def test_stakeholder_all(self):
        result = mock_file('stakeholder_collection')
        url = '{}/{}{}'.format(self.base_url,
                                self.account_id, URL.STAKEHOLDER)
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.stakeholder.all(self.account_id), result)
