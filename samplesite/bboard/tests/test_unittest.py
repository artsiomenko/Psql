from django.test import Client
from django.test import TestCase


class SimpleTest(TestCase):
    def test_bboard(self):
        client = Client()
        response = client.get('/bboard/')
        self.assertEqual(response.status_code, 200)

    def test_bboard_add(self):
        client = Client()
        response = client.get('/bboard/add/')
        self.assertEqual(response.status_code, 200)
