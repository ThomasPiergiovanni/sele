"""Test consult about use case test module. Functional test
"""
import os

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from time import sleep


class CreateVotingUseCaseTest(StaticLiveServerTestCase):
    """Test create voting use case test class
    """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        firefox_options = webdriver.FirefoxOptions()
        if os.name == 'nt':
            firefox_options.headless = False
            cls.browser = webdriver.Firefox(
                executable_path=str(
                    r'D:\02_oc\13_p13\config\settings\geckodriver.exe'
                ),
                options=firefox_options,
            )
        if os.name == 'posix':
            firefox_options.headless = True
            cls.browser = webdriver.Firefox(
                executable_path=str('/usr/local/bin/geckodriver'),
                options=firefox_options,
            )
        cls.browser.implicitly_wait(30)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def setUp(self):
        # The visitor or user lands on the home page.
        self.browser.get(
            '%s%s' % (self.live_server_url,'')
        )

    def tests_create_voting_use_case(self):
        self.assertIn('sel-e',self.browser.find_element_by_tag_name('h1').text)
        sleep(2)

        # The user selects "Info" on the left navigation sidebar
        # and the selects "A propos"
        self.browser.find_element_by_id('sidebar_info').click()
        sleep(2)
        self.browser.find_element_by_id('sidebar_about').click()
        self.assertIn(
            self.browser.find_element_by_tag_name('h1').text,
            'Qu\'est-ce que sel-e?',
        )
        sleep(2)
