"""Test rating use case test module. Functional test
"""
import os

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from time import sleep

from authentication.tests.emulation.authentication_emulation import (
    AuthenticationEmulation
)
from chat.tests.emulation.chat_emulation import ChatEmulation


class LoginUseCaseTest(StaticLiveServerTestCase):
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
        cls.auth_emulation = AuthenticationEmulation()
        cls.auth_emulation.emulate_custom_user()


    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def setUp(self):
        # The user logs to the home page
        self.browser.get(
            '%s%s' % (self.live_server_url, '')
        )

    def test_vote_use_case(self):
        sleep(2)
        self.assertIn('sel-e',self.browser.find_element_by_tag_name('h1').text)
        # The use select the connexion button
        self.browser.find_element_by_id('go_to_login_button').click()
        self.assertIn(
            self.browser.find_element_by_class_name('login-box-msg').text,
            "Connectez-vous à votre compte"
        )

        # The user types its email password clicks and then clicks
        # "Se connecter" button and lands on the home page.
        sleep(2)
        self.browser.find_element_by_id('input_login_email')\
        .send_keys('user1@email.com')
        sleep(1)
        self.browser.find_element_by_id('input_login_password')\
        .send_keys('xxx_Xxxx')
        sleep(1)
        self.browser.find_element_by_id('login_button').click()
        self.assertIn('sel-e',self.browser.find_element_by_tag_name('h1').text)
        sleep(2)
