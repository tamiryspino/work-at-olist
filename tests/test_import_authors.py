
# Standard library imports
import unittest
# from unittest.mock import Mock, patch
import json

# Third-party imports
# from nose.tools import assert_is_none, assert_list_equal

# Local imports
# from services import get_authors
from app import app
from database.db import db
from import_authors import read_data, import_authors


class ParseCSVTest(unittest.TestCase):

    def setUp(self):
        self.file = 'authors.csv'
        self.data = read_data(self.file)
        self.app = app.test_client()
        self.db = db.get_db()

    def tearDown(self):
        # Delete ALL database collections after the test is complete
        for collection in self.db.list_collection_names():
            self.db.drop_collection(collection)

    def test_csv_read_data_headers(self):
        '''Assert that the archive header contains the column `name`'''
        self.assertTrue(
            set(['name']).
            issuperset(list(self.data.columns)))

    def test_csv_read_data_name(self):
        self.assertEqual(self.data.values[0][0], 'Luciano Ramalho')

    def test_post_authors(self):
        # When
        author = {"name": self.data.values[1][0]}
        response = self.app.post('/api/authors',
                                 headers={"Content-Type": "application/json"},
                                 data=json.dumps(author))

        # Then
        self.assertEqual(str, type(response.json['id']))
        self.assertEqual(200, response.status_code)

    def test_import_authors(self):
        import_authors(self.file)
        self.assertEqual(self.db.author.count_documents({}), 6)

# TODO Mock
# @patch('services.requests.get')
# def test_getting_authors_when_response_is_ok(mock_get):
#    authors = [{
#        'id': 1,
#        'name': 'Osvaldo Santana Neto'
#    }]

    # Configure the mock to return a response with an OK status code.
    # Also, the mock should have
    # a `json()` method that returns a list of authors.
#    mock_get.return_value = Mock(ok=True)
#    mock_get.return_value.json.return_value = authors

    # Call the service, which will send a request to the server.
#    response = get_authors()

    # If the request is sent successfully, then a response will be returned.
#    assert_list_equal(response.json(), authors)


# @patch('services.requests.get')
# def test_getting_authors_when_response_is_not_ok(mock_get):
    # Configure the mock to not return a response with an OK status code.
#    mock_get.return_value.ok = False

    # Call the service, which will send a request to the server.
#    response = get_authors()

    # If the response contains an error, I should get no authors.
#    assert_is_none(response)
