"""Test read proposition view module.
"""
from django.test import TestCase
from django.urls import reverse

from chat.forms.comment_form import CommentForm
from chat.models.comment import Comment
from chat.tests.emulation.chat_emulation import ChatEmulation
from chat.models.discussion import Discussion
from proposition.models.proposition import Proposition
from proposition.tests.emulation.proposition_emulation import (
    PropositionEmulation
)

class ReadPropositionViewTest(TestCase):
    """Test ReadPropositionView class.
    """
    def setUp(self):
        self.proposition_emulation = PropositionEmulation()
        self.chat_emulation = ChatEmulation()

    def test_get_with_nominal_scenario(self):
        self.proposition_emulation.emulate_proposition()
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.get(
            '/proposition/read_proposition/1/', follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'proposition/read_proposition.html')
        self.assertIsInstance(response.context['proposition'], Proposition)
        self.assertIsInstance(response.context['form'], CommentForm)
        self.assertIsInstance(response.context['discussion'], Discussion)
        self.assertIsInstance(response.context['comments'][0], Comment)   
        self.assertEqual(response.context['btn1_href'], None)
        self.assertEqual(response.context['btn1_class'], None)
        self.assertEqual(response.context['btn1_text'], None)
        self.assertEqual(response.context['btn1_value'], None)



    def test_get_with_alternative_scenario(self):
        self.proposition_emulation.emulate_proposition()
        response = self.client.get(
            '/proposition/read_proposition/1/', follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0],reverse('authentication:login')
        )

    def test_post_with_nominal_scenario(self):
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        form_data = {'comment':'Alors???'}
        response = self.client.post(
            '/proposition/read_proposition/1/', data=form_data, follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            Comment.objects.all().last().comment, 'Alors'
        )
        self.assertEqual(
            response.redirect_chain[0][0], '/proposition/read_proposition/1/'
        )
