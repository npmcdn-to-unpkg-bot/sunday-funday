import httplib

from django import test

class TestIndex(test.TestCase):

    def test_index(self):
        c = test.Client()
        response = c.get('/')
        self.assertEqual(response.status_code, httplib.OK)
