# pylint: disable=C0114,C0115,C0116,E1101,R0201
import os
from time import sleep

from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from authentication.tests.emulation.authentication_emulation import (
    AuthenticationEmulation
)
from chat.tests.emulation.chat_emulation import ChatEmulation


class CreateCommentUseCaseTest(StaticLiveServerTestCase):

    def setUp(self):
        firefox_options = webdriver.FirefoxOptions()
        if os.name == 'nt':
            firefox_options.headless = False
            self.browser = webdriver.Firefox(
                executable_path=str(
                    r'D:\projects\sele\config\settings\geckodriver.exe'
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
        self.chat_emulation.emulate_discussion()

    def tearDown(self):
        self.browser.quit()

    def test_create_comment_use_case(self):
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
        sleep(2)
        self.assertIn(
            'sel-e', self.browser.find_element_by_tag_name('h1').text
        )
        sleep(2)

        # The user selects "Mon groupe local" on the left navigation sidebar
        # and then selects "Discussion".
        self.browser.find_element_by_id('sidebar_my_local_group').click()
        sleep(2)
        self.browser.find_element_by_id('sidebar_mlg_chat').click()
        sleep(2)

        # On the "Discussions" page, the user select the "Regarder" button
        # on the first Discussion
        self.browser.find_element_by_id('watch_disscussion_button').click()
        sleep(2)
        self.assertIn(
            self.browser.find_element_by_tag_name('h1').text,
            'Discussion - Sujet est JS',
        )

        # The user type its comment on the comment form and then sends it.
        self.browser.find_element_by_id('input_comment_comment')\
            .send_keys('Mon commentaire est celui ci')
        sleep(2)
        self.browser.find_element_by_id('comment_button').click()
        sleep(2)
        self.assertIn(
            self.browser.find_element_by_class_name('direct-chat-text').text,
            'Mon commentaire est celui ci',
        )
