from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from bboard.models import Rubric, Bb


class NewOneAdd(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        Rubric.objects.create(name='Транспорт')
        cls.selenium = WebDriver()

    def test_add(self):
        self.selenium.get(self.live_server_url + '')
        self.selenium.get('%s%s' % (self.live_server_url, '/bboard'))
        add_button = self.selenium.find_element(By.NAME, 'add')
        add_button.click()
        title = self.selenium.find_element(By.NAME, 'title')
        title.send_keys('Велосипед')
        content = self.selenium.find_element(By.NAME, 'content')
        content.send_keys('Велосипед как велосипед')
        rubr = Select(self.selenium.find_element(By.NAME, 'rubric'))
        rubr.select_by_value('1')
        next_button = self.selenium.find_element(By.NAME, 'submit_add')
        next_button.click()
        next_button = self.selenium.find_element(By.NAME, 'mainpage')
        next_button.click()
        assert 'Велосипед' in self.selenium.page_source
        self.selenium.quit()


