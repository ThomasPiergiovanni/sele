# pylint: disable=C0114,C0115,C0116,E1101,W0212,R0801
from django.test import TestCase
from django.urls import reverse

from chat.models import Discussion
from proposition.forms.proposition_form import PropositionForm
from proposition.models import (
    Category, CreatorType, Domain, Kind, Proposition
)
from proposition.tests.emulation.proposition_emulation import (
    PropositionEmulation
)


class CreatePropositionViewTest (TestCase):

    def setUp(self):
        self.proposition_emulation = PropositionEmulation()
        self.proposition_emulation.emulate_test_setup()

    def test_get_with_nominal_scenario(self):
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        response = self.client.get(
            '/proposition/create_proposition/', follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'proposition/create_proposition.html'
        )
        self.assertIsInstance(response.context['form'], PropositionForm)

    def test_get_with_alternative_scenario(self):
        response = self.client.get(
            '/proposition/create_proposition/', follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0], '/authentication/login/'
        )

    def test_post_with_nominal_scenario(self):
        Discussion.objects.all().delete()
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        form_data = {
            'name': 'Cours de Python',
            'description': 'dsdss',
            'proposition_kind': Kind.objects.get(pk=1).id,
            'proposition_category': Category.objects.get(pk=1).id,
            'proposition_domain': Domain.objects.get(pk=1).id,
            'proposition_creator_type': CreatorType.objects.get(pk=1).id,
            'start_date': "2022-01-25",
            'end_date': "2022-01-30",
            'duration': 45
        }
        response = self.client.post(
            '/proposition/create_proposition/', data=form_data, follow=True
        )
        response_msg = response.context['messages']._loaded_data[0]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            Proposition.objects.all().last().name, 'Cours de Python'
        )
        self.assertEqual(
            Discussion.objects.all().last().subject, 'Cours de Python'
        )
        self.assertEqual(
            response.redirect_chain[0][0],
            reverse('proposition:collectivity_propositions')
        )
        self.assertEqual(response_msg.level_tag, 'success')
        self.assertEqual(response_msg.message, "Création réussie")

    def test_post_with_alternative_scenario_with_wrong_form(self):
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        form_data = {
            'name': 'Cours de Python',
            'description': 'dsdss',
            'proposition_kind': Kind.objects.get(pk=2).id,
            'proposition_category': Category.objects.get(pk=1).id,
            'proposition_domain': Domain.objects.get(pk=1).id,
            'proposition_creator_type': CreatorType.objects.get(pk=1).id,
            'start_date': "2022-01-25",
            'end_date': "2022-01-30",
            'duration': 45
        }
        response = self.client.post(
            '/proposition/create_proposition/', data=form_data, follow=True
        )
        self.assertTemplateUsed(
            response,
            'proposition/create_proposition.html'
        )
        self.assertIsInstance(response.context['form'], PropositionForm)
        self.assertTrue(response.context['form'].errors)

    def test_post_with_alternative_scenario_two_unauthenticated_user(self):
        form_data = {
            'name': 'Cours de Python',
            'description': 'dsdss',
            'proposition_kind': Kind.objects.get(pk=1).id,
            'proposition_category': Category.objects.get(pk=1).id,
            'proposition_domain': Domain.objects.get(pk=1).id,
            'proposition_creator_type': CreatorType.objects.get(pk=1).id,
            'start_date': "2022-01-25",
            'end_date': "2022-01-30",
            'duration': 45
        }
        response = self.client.post(
            '/proposition/create_proposition/', data=form_data, follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0], '/authentication/login/'
        )
