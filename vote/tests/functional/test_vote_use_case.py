"""Test rating use case test module. Functional test
"""
import os

from time import sleep

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver

from authentication.tests.emulation.authentication_emulation import (
    AuthenticationEmulation
)
from vote.tests.emulation.vote_emulation import VoteEmulation


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
        # The user logs to the login page
        self.auth_emulation = AuthenticationEmulation()
        self.auth_emulation.emulate_custom_user()
        self.vote_emulation = VoteEmulation()
        self.vote_emulation.emulate_voting_method()
        self.vote_emulation.emulate_voting()
        self.browser.get(
            '%s%s' % (self.live_server_url, '/authentication/login/')
        )

    def test_vote_use_case(self):
        # The user types its email and password.
        sleep(2)
        self.browser.find_element_by_id('input_login_email')\
        .send_keys('user1@email.com')
        sleep(1)
        self.browser.find_element_by_id('input_login_password')\
        .send_keys('xxx_Xxxx')
        sleep(1)

        # The user clicks then "Se connecter" button and lands on the
        # home page.
        self.browser.find_element_by_id('login_button').click()
        self.assertIn('sel-e',self.browser.find_element_by_tag_name('h1').text)
        sleep(1)

        # The user selects "Mon groupe Local" on the left navigation sidebar
        # and the selects "Votes"
        self.browser.find_element_by_id('sidebar_my_local_group').click()
        sleep(1)
        self.browser.find_element_by_id('sidebar_mlg_votings').click()
        sleep(2)

        # The user select the "Regarder" button on the first voting
        self.browser.find_element_by_id('watch_voting_button').click()
        sleep(2)
        self.assertIn(
            self.browser.find_element_by_tag_name('h1').text,
            'Votation - Voulez-vous créer une demande de nettoyage?',
        )

        # The user select "Participer au vote" button
        self.browser.find_element_by_id('participate_to_voting_button')\
        .click()
        sleep(2)
        self.assertIn(
            self.browser.find_element_by_class_name('login-box-msg').text,
            'Participer au vote',
        )
        self.browser.find_element_by_id('yes_button').click()
        sleep(2)
        self.assertIn(
            self.browser.find_element_by_id('voting_result').text,
            'Votation en cours...',
        )
