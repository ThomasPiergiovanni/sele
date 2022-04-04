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
from proposition.forms.collectivity_propositions_form import (
    CollectivityPropositionsForm
)
from proposition.forms.proposition_form import PropositionForm
from proposition.management.engine.manager import Manager
from proposition.models.category import Category
from proposition.models.creator_type import CreatorType
from proposition.models.domain import Domain
from proposition.models.kind import Kind
from proposition.models.proposition import Proposition
from proposition.tests.emulation.proposition_emulation import (
    PropositionEmulation
)


class TestManager(TestCase):
    """Test Manager  class.
    """
    def setUp(self):
        self.auth_emulation = AuthenticationEmulation()
        self.proposition_emulation = PropositionEmulation()
        self.manager = Manager()

    def test_create_proposition_with_proposition_instance(self):
        self.auth_emulation.emulate_custom_user()
        self.proposition_emulation.emulate_category()
        self.proposition_emulation.emulate_domain()
        self.proposition_emulation.emulate_kind()
        self.proposition_emulation.emulate_creator_type()
        self.proposition_emulation.emulate_status()
        form_data = {
            'name': 'Cours de Python',
            'description': 'dsdss',
            'proposition_kind': Kind.objects.get(pk=1).id,
            'proposition_category': Category.objects.get(pk=1).id,
            'proposition_domain': Domain.objects.get(pk=1).id,
            'start_date': "2022-01-25",
            'end_date': "2022-01-30",
            'duration': 45,
            'proposition_creator_type': CreatorType.objects.get(pk=1).id,
        }
        form = PropositionForm(data=form_data)
        form.is_valid()
        custom_user = CustomUser.objects.get(pk=1)
        self.manager.create_proposition(form, custom_user)
        self.assertEqual(
            Proposition.objects.all().last().name, 'Cours de Python'
        )

    def test_set_form_context(self):
        form = self.manager.set_form_context(
            'creation_date', 'asc'
        )
        self.assertIsInstance(form, CollectivityPropositionsForm)
        self.assertEqual(
            form.fields['attribute_selector']._choices[6][0], 'creation_date'
        )
        self.assertEqual(form.fields['order_selector']._choices[0][0], 'asc')
    
    def test_set_page_objects_context(self):
        self.proposition_emulation.emulate_proposition()
        request = RequestFactory().get('', data={'page': 1})        
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user  
        page_objects = (
            self.manager.set_page_objects_context(
                request, 'creation_date','asc'
            )
        )
        self.assertEqual(page_objects[0].id, 1)
    
    def test_get_sorted_proposition_with_creation_date_asc(self):
        self.proposition_emulation.emulate_proposition()
        request = RequestFactory().get('', data={'page': 1})        
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user
        propositions = self.manager._Manager__get_sorted_propositions(
            request, 'creation_date','asc'
        )
        self.assertIsInstance(propositions[0], Proposition)
        self.assertEqual(propositions[0].id, 1)

    def test_get_sorted_proposition_with_creation_date_desc(self):
        self.proposition_emulation.emulate_proposition()
        request = RequestFactory().get('', data={'page': 1})        
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user
        propositions = self.manager._Manager__get_sorted_propositions(
            request, 'creation_date', 'desc'
        )
        self.assertIsInstance(propositions[0], Proposition)
        self.assertEqual(propositions[0].id, 3)

    def test_get_sorted_proposition_with_proposition_kind_asc(self):
        self.proposition_emulation.emulate_proposition()
        request = RequestFactory().get('', data={'page': 1})        
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user
        propositions = self.manager._Manager__get_sorted_propositions(
            request, 'proposition_kind', 'asc'
        )
        self.assertIsInstance(propositions[0], Proposition)
        self.assertEqual(propositions[0].id, 1)

    def test_get_sorted_proposition_with_proposition_kind_desc(self):
        self.proposition_emulation.emulate_proposition()
        request = RequestFactory().get('', data={'page': 1})        
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user
        propositions = self.manager._Manager__get_sorted_propositions(
            request, 'proposition_kind', 'desc'
        )
        self.assertIsInstance(propositions[0], Proposition)
        self.assertEqual(propositions[0].id, 3)

    def test_get_proposition_queryset(self):
        self.proposition_emulation.emulate_proposition()
        request = RequestFactory().get('', data={'page': 1})        
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user     
        propositions = self.manager._Manager__get_proposition_queryset(
            request, 'creation_date'
        )
        self.assertEqual(propositions[0].id, 1)

    def test_set_session_vars_with_proposition_status_desc(self):
        self.proposition_emulation.emulate_proposition()
        request = RequestFactory().post('')
        session_middleware = SessionMiddleware(request)
        session_middleware.process_request(request) 
        self.manager.set_session_vars(request, 'proposition_status', 'desc')
        self.assertEqual(
            request.session.get('c_p_v_f_attribute'), 'proposition_status'
        )

    def test_set_session_vars_with_question_asc(self):
        self.proposition_emulation.emulate_proposition()
        request = RequestFactory().post('')
        session_middleware = SessionMiddleware(request)
        session_middleware.process_request(request) 
        self.manager.set_session_vars(request, 'duration', 'asc')
        self.assertEqual(request.session.get('c_p_v_f_order'), 'asc')

    # def test_create_vote_with_vote_yes(self):
    #     self.vote_emulation.emulate_voting()
    #     voting = Voting.objects.get(pk=1)
    #     request = RequestFactory().post('', data={'form_vote': 'yes'})        
    #     user = authenticate(email='user1@email.com', password='xxx_Xxxx')
    #     request.user = user 
    #     self.manager.create_vote(request, voting.id)
    #     vote = Vote.objects.last() 
    #     self.assertTrue(vote.choice)

    # def test_create_vote_with_vote_no(self):
    #     self.vote_emulation.emulate_voting()
    #     voting = Voting.objects.get(pk=1)
    #     request = RequestFactory().post('', data={'form_vote': 'no'})        
    #     user = authenticate(email='user1@email.com', password='xxx_Xxxx')
    #     request.user = user 
    #     self.manager.create_vote(request, voting.id)
    #     vote = Vote.objects.last()
    #     self.assertFalse(vote.choice)
