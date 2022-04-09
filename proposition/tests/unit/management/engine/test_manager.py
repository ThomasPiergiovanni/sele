"""Test manager module.
"""
from django.contrib.auth import authenticate
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import RequestFactory, TestCase

from authentication.models import CustomUser
from authentication.tests.emulation.authentication_emulation import (
    AuthenticationEmulation
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

    def test_set_page_objects_context(self):
        self.proposition_emulation.emulate_proposition()
        request = RequestFactory().get('', data={'page': 1})        
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user  
        page_objects = (
            self.manager.set_page_objects_context(request, 'DCours1')
        )
        self.assertEqual(page_objects[0].id, 1)
    
    def test_get_proposition_queryset_with_search_input(self):
        self.proposition_emulation.emulate_proposition()
        request = RequestFactory().get('', data={'page': 1})        
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user     
        propositions = self.manager._Manager__get_proposition_queryset(
            request, 'DCours1'
        )
        self.assertEqual(propositions[0].id, 1)

    def test_get_proposition_queryset_with_search_input_is_false(self):
        self.proposition_emulation.emulate_proposition()
        request = RequestFactory().get('', data={'page': 1})        
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user     
        propositions = self.manager._Manager__get_proposition_queryset(
            request, False
        )
        self.assertEqual(propositions[0].id, 17)

    def test_set_session_vars_with_search_input(self):
        self.proposition_emulation.emulate_proposition()
        request = RequestFactory().post('')
        session_middleware = SessionMiddleware(request)
        session_middleware.process_request(request) 
        self.manager.set_session_vars(request, 'Python')
        self.assertEqual(
            request.session.get('c_p_v_f_search_input'), 'Python'
        )

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
    
    def test_srpv_context_with_kin_dem_sta_nou_tak_none_cre_not_user(self):
        self.proposition_emulation.emulate_proposition()
        proposition = Proposition.objects.get(pk=3)
        request = RequestFactory().get('')
        user = authenticate(email='user3@email.com', password='xxx_Xxxx')
        request.user = user     
        context = self.manager.set_read_proposition_view_context(
            request, proposition.id
        )
        self.assertEqual(context['href'], "/proposition/update_proposition/3/")
        self.assertEqual(
            context['class'],
            "text-success btn btn-block btn-light border border-success"
        )
        self.assertEqual(context['text'], "S'assigner")
        self.assertEqual(context['value'], "select")

    def test_set_demand_button_with_sta_nouveau_tak_none_cre_not_user(self):
        self.proposition_emulation.emulate_proposition()
        proposition = Proposition.objects.get(pk=3)
        request = RequestFactory().get('')
        user = authenticate(email='user3@email.com', password='xxx_Xxxx')
        request.user = user     
        html_vars = self.manager._Manager__set_demand_button(
            request, proposition
        )
        self.assertEqual(
            html_vars['href'], "/proposition/update_proposition/3/"
        )
        self.assertEqual(
            html_vars['class'],
            "text-success btn btn-block btn-light border border-success"
        )
        self.assertEqual(html_vars['text'], "S'assigner")
        self.assertEqual(html_vars['value'], "select")

    def test_set_demand_button_with_sta_selectionne_tak_user_cre_not_user(self):
        self.proposition_emulation.emulate_proposition()
        proposition = Proposition.objects.get(pk=6)
        request = RequestFactory().get('')
        user = authenticate(email='user3@email.com', password='xxx_Xxxx')
        request.user = user     
        html_vars = self.manager._Manager__set_demand_button(
            request, proposition
        )
        self.assertEqual(
            html_vars['href'], "/proposition/update_proposition/6/"
        )
        self.assertEqual(
            html_vars['class'],
            "text-danger btn btn-block btn-light border border-danger"
        )
        self.assertEqual(html_vars['text'], "Annuler l'assignation")
        self.assertEqual(html_vars['value'], "new")
