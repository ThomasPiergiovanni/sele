"""Test rating use case test module. Functional test
"""
import os

from datetime import date, timedelta
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from time import sleep

from authentication.tests.emulation.authentication_emulation import (
    AuthenticationEmulation
)
from chat.tests.emulation.chat_emulation import ChatEmulation
from proposition.tests.emulation.proposition_emulation import (
    PropositionEmulation
)


class CreatePropositionUseCaseTest(StaticLiveServerTestCase):
    """Test create proposition use case test class
    """
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
        self.chat_emulation = ChatEmulation()
        self.chat_emulation.emulate_discussion_type()
        self.proposition_emulation = PropositionEmulation()
        self.proposition_emulation.emulate_category()
        self.proposition_emulation.emulate_creator_type()
        self.proposition_emulation.emulate_domain()
        self.proposition_emulation.emulate_kind()
        self.proposition_emulation.emulate_rating()
        self.proposition_emulation.emulate_status()

    def tearDown(self):
        self.browser.quit()

    def test_create_proposition_use_case(self):
        # The user is to the login page
        self.browser.get(
            '%s%s' % (self.live_server_url, '/authentication/login/')
        )
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
        sleep(2)

        # The user selects "Mon groupe Local" on the left navigation sidebar
        # and selects "Propositions"
        self.browser.find_element_by_id('sidebar_my_local_group').click()
        sleep(2)
        self.browser.find_element_by_id('sidebar_mlg_propositions').click()
        sleep(2)

        #The user selects the "Créer une votation" button
        self.browser.find_element_by_id('go_to_create_proposition_button')\
        .click()
        self.assertIn(
            self.browser.find_element_by_tag_name('h1').text,
            'Proposition - Créer',
        )
        sleep(2)
        
        # The user fills the form and select the créer button. The user
        # should land on the votings page and see is created voting
        # on th top of the list.

        self.browser.find_element_by_id('input_proposition_name')\
        .send_keys('Cours de python')
        sleep(1)
        self.browser.find_element_by_id('input_proposition_description')\
        .send_keys('bla bla bla')
        sleep(1)
        self.browser.find_element_by_id('input_proposition_proposition_kind')\
        .send_keys('Offre')
        sleep(1)
        self.browser.find_element_by_id(
            'input_proposition_proposition_category'
        ).send_keys('Activité')
        sleep(1)
        self.browser.find_element_by_id('input_proposition_proposition_domain')\
        .send_keys('Spectacle')
        sleep(1)
        today = date.today()
        self.browser.find_element_by_id('input_proposition_start_date')\
        .send_keys(str(today))
        sleep(1)
        self.browser.find_element_by_id('input_proposition_end_date')\
        .send_keys(str(today + timedelta(days=5)))
        sleep(1)
        self.browser.find_element_by_id('input_proposition_duration')\
        .send_keys(60)
        sleep(1)
        self.browser.find_element_by_id(
            'input_proposition_proposition_creator_type'
        ).send_keys('Individuelle')
        sleep(1)
        self.browser.find_element_by_id('create_proposition_button').click()
        sleep(1)
        self.assertIn(self.browser.find_element_by_tag_name('td').text,'1')
        sleep(2)
