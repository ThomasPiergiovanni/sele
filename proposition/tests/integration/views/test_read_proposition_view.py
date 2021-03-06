# pylint: disable=C0114,C0115,C0116,E1101,R0801
from django.test import TestCase
from django.urls import reverse

from chat.forms.comment_form import CommentForm
from chat.models import Comment, Discussion
from proposition.models import Proposition
from proposition.tests.emulation.proposition_emulation import (
    PropositionEmulation
)


class ReadPropositionViewTest(TestCase):

    def setUp(self):
        self.proposition_emulation = PropositionEmulation()
        self.proposition_emulation.emulate_test_setup()

    def test_get_with_nominal_scenario(self):
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
        response = self.client.get(
            '/proposition/read_proposition/1/', follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0], reverse('authentication:login')
        )

    def test_post_with_nominal_scenario(self):
        Comment.objects.all().delete()
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        form_data = {'comment': 'Alors???'}
        response = self.client.post(
            '/proposition/read_proposition/1/', data=form_data, follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            Comment.objects.last().comment, 'Alors???'
        )
        self.assertEqual(
            response.redirect_chain[0][0], '/proposition/read_proposition/1/'
        )

    def test_post_with_alternative_scenario_one(self):
        Comment.objects.all().delete()
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        form_data = {'comment': ''}
        response = self.client.post(
            '/proposition/read_proposition/1/', data=form_data, follow=True
        )
        self.assertEqual(
            response.templates[0].name,
            'proposition/read_proposition.html'
        )
        self.assertIsInstance(response.context['form'], CommentForm)
        self.assertTrue(response.context['form'].errors)

    def test_post_with_alternative_scenario_four(self):
        response = self.client.post(
            '/proposition/read_proposition/1/', follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0], reverse('authentication:login')
        )
