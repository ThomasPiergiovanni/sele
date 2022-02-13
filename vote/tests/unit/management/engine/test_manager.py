"""Test manager module.
"""
from django.test import TestCase

from vote.forms.voting_form import VotingForm
from vote.management.engine.manager import Manager
from vote.models.voting import Voting
from vote.models.voting_method import VotingMethod
from vote.tests.unit.models.test_voting_method import VotingMethodTest


class TestManager(TestCase):
    """Test Manager  class.
    """
    def setUp(self):
        VotingMethodTest().emulate_voting_method()
        self.manager = Manager()

    def test_create_voting_with_voting_instance(self):
        form_data = {
            'question': 'Ma question est',
            'description': 'dsdss',
            'opening_date': "2022-01-02",
            'closure_date': "2022-01-25",
            'voting_method': VotingMethod.objects.get(pk=1).id
        }
        voting_form = VotingForm(data=form_data)
        voting_form.is_valid()
        self.manager.create_voting(voting_form)
        self.assertEqual(
            Voting.objects.all().order_by('-id')[0].description,
            'dsdss'
        )
