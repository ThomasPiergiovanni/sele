# pylint: disable=C0114,C0115,C0116,E1101,R0801
import os
from time import sleep

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver

from authentication.tests.emulation.authentication_emulation import (
    AuthenticationEmulation
)
from vote.tests.emulation.vote_emulation import VoteEmulation


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
        self.auth_emulation = AuthenticationEmulation()
        self.auth_emulation.emulate_custom_user()
        self.vote_emulation = VoteEmulation()
        self.vote_emulation.emulate_voting_method()
        self.vote_emulation.emulate_voting()

    def tearDown(self):
        self.browser.quit()

    def test_vote_use_case(self):
        # The user is on the login page
        self.browser.get(f"{self.live_server_url}{'/authentication/login/'}")

        # The user types its email password clicks and then clicks
        # "Se connecter" button and lands on the home page.
        sleep(2)
        self.browser.find_element_by_id('input_login_email')\
            .send_keys('user1@email.com')
        sleep(2)
        self.browser.find_element_by_id('input_login_password')\
            .send_keys('xxx_Xxxx')
        sleep(2)
        self.browser.find_element_by_id('login_button').click()
        self.assertIn(
            'sel-e',
            self.browser.find_element_by_tag_name('h1').text
        )
        sleep(2)

        # The user selects "Mon groupe Local" on the left navigation sidebar
        # and the selects "Votes"
        self.browser.find_element_by_id('sidebar_my_local_group').click()
        sleep(2)
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
