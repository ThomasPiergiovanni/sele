# pylint: disable=C0114,C0115,C0116
import os
from time import sleep

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver


class CreateVotingUseCaseTest(StaticLiveServerTestCase):

    def setUp(self):
        firefox_options = webdriver.FirefoxOptions()
        if os.name == 'nt':
            firefox_options.headless = False
            self.browser = webdriver.Firefox(
                executable_path=str(
                    r'D:\02_oc\13_p13\config\settings\geckodriver.exe'
                ),
                options=firefox_options,
            )
        if os.name == 'posix':
            firefox_options.headless = True
            self.browser = webdriver.Firefox(
                executable_path=str('/usr/local/bin/geckodriver'),
                options=firefox_options,
            )
        self.browser.implicitly_wait(30)

    def tearDown(self):
        self.browser.quit()

    def tests_create_voting_use_case(self):
        # The user is on the home page
        self.browser.get(f"{self.live_server_url}{''}")
        self.assertIn(
            'sel-e',
            self.browser.find_element_by_tag_name('h1').text
        )
        sleep(2)

        # The user selects "Info" on the left navigation sidebar
        # and the selects "A propos"
        self.browser.find_element_by_id('sidebar_info').click()
        sleep(2)
        self.browser.find_element_by_id('sidebar_about').click()
        self.assertIn(
            self.browser.find_element_by_tag_name('h1').text,
            'A propos',
        )
        sleep(2)
