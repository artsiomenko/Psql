from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class MainFlowTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
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
        next_button = self.selenium.find_element(By.NAME, 'submit_add')
        next_button.click()
        next_button = self.selenium.find_element(By.NAME, 'mainpage')
        next_button.click()
        self.selenium.refresh()
        assert 'Велосипед' in self.selenium.page_source
        self.selenium.close()


