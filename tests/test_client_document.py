import responses
import json

from .helpers import mock_file, ClientTestCase


class TestClientDocument(ClientTestCase):

    def setUp(self):
        super(TestClientDocument, self).setUp()
        self.base_url = f"{self.base_url}/documents"

    @responses.activate
    def test_document_fetch(self):
        result = mock_file('document')
        id = 'fake_document_id'
        url = f"{self.base_url}/{id}"
        responses.add(responses.GET, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.document.fetch(id), result)

    @responses.activate
    def test_document_create(self):
        request = {
         'file': '',
         'purpose': 'dispute_evidence'
        }
        result = mock_file('document')
        url = self.base_url
        responses.add(responses.POST, url, status=200, body=json.dumps(result),
                      match_querystring=True)
        self.assertEqual(self.client.document.create(request), result)
