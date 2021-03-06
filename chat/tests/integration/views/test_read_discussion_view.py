# pylint: disable=C0114,C0115,C0116,E1101,R0201
from django.test import TestCase
from django.urls import reverse

from chat.forms.comment_form import CommentForm
from chat.models import Comment, Discussion
from chat.tests.emulation.chat_emulation import ChatEmulation


class ReadDiscussionViewTest(TestCase):

    def setUp(self):
        self.chat_emulation = ChatEmulation()
        self.chat_emulation.emulate_test_setup()

    def test_get_with_nominal_scenario(self):
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.get('/chat/read_discussion/1/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat/read_discussion.html')
        self.assertIsInstance(response.context['discussion'], Discussion)
        self.assertIsInstance(response.context['form'], CommentForm)
        self.assertIsInstance(response.context['comments'][0], Comment)

    def test_get_with_alternative_scenario(self):
        response = self.client.get('/chat/read_discussion/1/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0], reverse('authentication:login')
        )
