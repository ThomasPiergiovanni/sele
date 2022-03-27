"""Test manager module.
"""
from datetime import date, timedelta

from django.contrib.auth import authenticate
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import RequestFactory, TestCase

from authentication.models import CustomUser
from authentication.tests.emulation.authentication_emulation import (
    AuthenticationEmulation
)
from vote.forms.voting_form import VotingForm
from vote.forms.collectivity_votings_form import CollectivityVotingsForm
from vote.management.engine.manager import Manager
from vote.models.vote import Vote
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
    
    def test_set_context_with_return_context(self):
        self.vote_emulation.emulate_vote()
        context = {
            'voting': None,
            'voting_operation': None, 
            'voting_result': None,  
            'voting_status': None
        }
        voting = Voting.objects.get(pk=1)
        context = self.manager.set_context(context, voting ,'delete')
        self.assertEqual(context['voting'], voting )
        self.assertEqual(context['voting_operation'], 'delete')
        self.assertEqual(context['voting_result'], 50 )
        self.assertEqual(context['voting_status'], 'Fermé' )

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
            voting_custom_user = CustomUser.objects.get(pk=1)    
        )
        voting = Voting.objects.all().order_by('-id')[0]
        self.assertEqual(
            self.manager._Manager__get_voting_status(voting), 'Ouvert'
        )

    def test_get_voting_status_with_return_closed(self):
        self.vote_emulation.emulate_voting()
        voting = Voting.objects.get(pk=1)
        self.assertEqual(
            self.manager._Manager__get_voting_status(voting), 'Fermé'
        )
    
    def test_get_votation_result(self):
        self.vote_emulation.emulate_vote()
        voting = Voting.objects.get(pk=1)
        votes = Vote.objects.filter(vote_voting_id__exact=voting)
        self.assertEqual(
            self.manager._Manager__get_voting_result(votes), 50
        )

    def test_set_collectivity_votings_form_context(self):
        form = self.manager.set_collectivity_votings_form_context(
            'date', 'asc'
        )
        self.assertIsInstance(form, CollectivityVotingsForm)
        self.assertEqual(
            form.fields['attribute_selector']._choices[1][0], 'date'
        )
        self.assertEqual(form.fields['order_selector']._choices[0][0], 'asc')
    
    def test_set_collectivity_votings_page_objects_context(self):
        self.vote_emulation.emulate_vote()
        request = RequestFactory().get('', data={'page': 1})        
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user  
        page_objects = (
            self.manager.set_collectivity_votings_page_objects_context(
                request, attribute='date', order='asc'
            )
        )
        self.assertEqual(page_objects[0].id, 1)
    
    def test_get_sorted_votings_with_date_asc(self):
        self.vote_emulation.emulate_vote()
        request = RequestFactory().get('', data={'page': 1})        
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user
        votings = self.manager._Manager__get_sorted_votings(
            request, attribute='date', order='asc'
        )
        self.assertIsInstance(votings[0],Voting)
        self.assertEqual(votings[0].id, 1)

    def test_get_sorted_votings_with_date_desc(self):
        self.vote_emulation.emulate_vote()
        request = RequestFactory().get('', data={'page': 1})        
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user
        votings = self.manager._Manager__get_sorted_votings(
            request, attribute='date', order='desc'
        )
        self.assertIsInstance(votings[0],Voting)
        self.assertEqual(votings[0].id, 3)

    def test_get_sorted_votings_with_question_asc(self):
        self.vote_emulation.emulate_vote()
        request = RequestFactory().get('', data={'page': 1})        
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user
        votings = self.manager._Manager__get_sorted_votings(
            request, attribute='question', order='asc'
        )
        self.assertIsInstance(votings[0],Voting)
        self.assertEqual(votings[0].id, 1)

    def test_get_sorted_votings_with_question_desc(self):
        self.vote_emulation.emulate_vote()
        request = RequestFactory().get('', data={'page': 1})        
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user
        votings = self.manager._Manager__get_sorted_votings(
            request, attribute='question', order='desc'
        )
        self.assertIsInstance(votings[0],Voting)
        self.assertEqual(votings[0].id, 3)
    
    def test_set_session_vars_with_date_desc(self):
        self.vote_emulation.emulate_vote()
        request = RequestFactory().post(
            '',
            data={
                'attribute': 'date',
                'order': 'desc'
            }
        )
        session_middleware = SessionMiddleware(request)
        session_middleware.process_request(request) 
        self.manager.set_session_vars(request, attribute='date', order='desc')
        self.assertEqual(request.session.get('c_v_v_f_attribute'), 'date')

    def test_set_session_vars_with_question_asc(self):
        self.vote_emulation.emulate_vote()
        request = RequestFactory().post(
            '',
            data={
                'attribute': 'question',
                'order': 'asc'
            }
        )
        session_middleware = SessionMiddleware(request)
        session_middleware.process_request(request) 
        self.manager.set_session_vars(
            request, attribute='question', order='asc'
        )
        self.assertEqual(request.session.get('c_v_v_f_order'), 'asc')

    def test_create_vote_with_vote_yes(self):
        self.vote_emulation.emulate_voting()
        voting = Voting.objects.get(pk=1)
        request = RequestFactory().post('', data={'form_vote': 'yes'})        
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user 
        self.manager.create_vote(request, voting.id)
        vote = Vote.objects.get(pk=1) 
        self.assertTrue(vote.choice)

    def test_create_vote_with_vote_yes(self):
        self.vote_emulation.emulate_voting()
        voting = Voting.objects.get(pk=1)
        request = RequestFactory().post('', data={'form_vote': 'no'})        
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user 
        self.manager.create_vote(request, voting.id)
        vote = Vote.objects.get(pk=1) 
        self.assertFalse(vote.choice)
