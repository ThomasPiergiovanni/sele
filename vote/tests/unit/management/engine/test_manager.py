"""Test manager module.
"""
from datetime import date, timedelta

from django.test import TestCase
from authentication.models import CustomUser

from authentication.tests.emulation.authentication_emulation import (
    AuthenticationEmulation
)
from vote.forms.voting_form import VotingForm
from vote.management.engine.manager import Manager
from vote.models.voting import Voting
from vote.models.voting_method import VotingMethod
from vote.tests.emulation.vote_emulation import VoteEmulation


class TestManager(TestCase):
    """Test Manager  class.
    """
    def setUp(self):
        self.auth_emulation = AuthenticationEmulation()
        self.vote_emulation = VoteEmulation()
        self.manager = Manager()

    def test_create_voting_with_voting_instance(self):
        self.auth_emulation.emulate_custom_user()
        self.vote_emulation.emulate_voting_method()
        form_data = {
            'question': 'Ma question est',
            'description': 'dsdss',
            'opening_date': "2022-01-02",
            'closure_date': "2022-01-25",
            'voting_method': VotingMethod.objects.get(pk=1).id
        }
        form = VotingForm(data=form_data)
        form.is_valid()
        custom_user = CustomUser.objects.get(pk=1)
        self.manager.create_voting(form, custom_user)
        self.assertEqual(
            Voting.objects.all().order_by('-id')[0].description,
            'dsdss'
        )

    def test_get_voting_status_with_return_open(self):
        self.auth_emulation.emulate_custom_user()
        self.vote_emulation.emulate_voting_method()

        Voting.objects.create(
            question='Emulated question',
            description='Emulated description',
            creation_date=date.today() - timedelta(2),
            opening_date=date.today() - timedelta(1),
            closure_date=date.today() + timedelta(1),
            voting_method=VotingMethod.objects.get(pk=1),
            custom_user = CustomUser.objects.get(pk=1)    
        )
        voting = Voting.objects.all().order_by('-id')[0]
        self.assertEqual(
            self.manager.get_voting_status(voting), 'Ouvert'
        )

    def test_get_voting_status_with_return_closed(self):
        self.vote_emulation.emulate_voting()
        voting = Voting.objects.get(pk=1)
        self.assertEqual(
            self.manager.get_voting_status(voting), 'Fermé'
        )
