from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import Client
from bboard.tests.model_factory import BbFactory
import requests


class ViewPage(StaticLiveServerTestCase):
    def test_response_code(self):
        client = Client()
        bb = BbFactory()
        response = self.client.get('/bboard/')
        self.assertEqual(response.status_code, 200)
        page_text = str((requests.get(self.live_server_url +'/bboard/')).text)
        self.assertTrue('Автомобиль' in page_text)
