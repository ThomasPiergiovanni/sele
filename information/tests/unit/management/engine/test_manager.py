"""Test manager module.
"""
from datetime import date
from django.contrib.auth import authenticate
from django.test import RequestFactory, TestCase
from django.utils import timezone
from json import loads

from authentication.models import CustomUser
from authentication.tests.emulation.authentication_emulation import (
    AuthenticationEmulation
)
from chat.models.discussion import Discussion
from chat.tests.emulation.chat_emulation import ChatEmulation
from collectivity.tests.emulation.collectivity_emulation import (
    CollectivityEmulation
)
from config.settings import MAPBOX_TOKEN
from proposition.models.proposition import Proposition
from proposition.tests.emulation.proposition_emulation import (
    PropositionEmulation
)
from vote.models.voting import Voting
from vote.tests.emulation.vote_emulation import VoteEmulation

from information.management.engine.manager import Manager


class TestManager(TestCase):
    """Test Manager  class.
    """
    def setUp(self):
        self.collectivty_emulation = CollectivityEmulation()
        self.auth_emulation = AuthenticationEmulation()
        self.proposition_emulation = PropositionEmulation()
        self.chat_emulation = ChatEmulation()
        self.vote_emulation = VoteEmulation()
        self.manager = Manager()

    def test_set_home_context(self):
        self.proposition_emulation.emulate_proposition()
        self.collectivty_emulation.emulate_collectivity()
        context = {
            'mapbox_url': None,
            'vector_layer': None,
            'stats_data': None
        }
        context = (
            self.manager.set_home_context(context)
        )
        mapbox_url = loads(context['mapbox_url'])
        vector_layer = loads(context['vector_layer'])
        stats_data = loads(context['stats_data'])
        today = date.today()
        today = today.replace(day=1)
        self.assertEqual(
            mapbox_url['url'],
            'https://api.mapbox.com/styles/v1/thomaspiergiovanni/ckmm3'+
            'kryyu79j17ptmgsmg9c9/tiles/{z}/{x}/{y}?access_token=' +
            MAPBOX_TOKEN
        )
        self.assertEqual(
            vector_layer['features'][0]['properties']['name'], 'Bourg-la-Reine'
        )
        self.assertEqual(stats_data['labels'][5],
        str(today.month)+"-"+str(today.year))
    
    def test_set_mapboxurl_json(self):
        data  = self.manager._Manager__set_mapboxurl_json() 
        data = loads(data)
        self.assertEqual(
            data['url'],
            'https://api.mapbox.com/styles/v1/thomaspiergiovanni/ckmm3'+
            'kryyu79j17ptmgsmg9c9/tiles/{z}/{x}/{y}?access_token=' +
            MAPBOX_TOKEN
        )

    def test_set_vectorlayer_geojson(self):
        self.collectivty_emulation.emulate_collectivity()
        data  = self.manager._Manager__set_vectorlayer_geojson() 
        data = loads(data)
        self.assertEqual(
            data['features'][0]['properties']['name'], 'Bourg-la-Reine'
        )

    def test_set_collectivity_dashboard_context_with_cus_user_prop_dis(self):
        self.proposition_emulation.emulate_proposition()
        request = RequestFactory().get('', data={'page': 1})        
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user 
        context = {
            'custom_user_pag_obj': None,
            'custom_users_p_counts': None,
            'proposition_pag_obj': None,
            'discussion_pag_obj': None,
            'voting_pag_obj': None,
            'collectivity_p_counts': None,
            'collectivity_cu_counts': None,
            'collectivity_d_counts': None
        }
        context = (
            self.manager.set_collectivity_dashboard_context(request, context)
        )
        self.assertIsInstance(context['custom_user_pag_obj'][0], CustomUser)
        self.assertEqual(context['custom_users_p_counts'][0]['count'], 15)
        self.assertIsInstance(context['proposition_pag_obj'][0], Proposition)
        self.assertIsInstance(context['discussion_pag_obj'][0], Discussion)
        self.assertEqual(context['collectivity_p_counts'], 15)
        self.assertEqual(context['collectivity_cu_counts'], 2)
        self.assertEqual(context['collectivity_d_counts'], 3)

    def test_set_collectivity_dashboard_context_with_voting(self):
        self.vote_emulation.emulate_voting()
        request = RequestFactory().get('', data={'page': 1})        
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user 
        context = {
            'custom_user_pag_obj': None,
            'custom_users_p_counts': None,
            'proposition_pag_obj': None,
            'discussion_pag_obj': None,
            'voting_pag_obj': None,
            'collectivity_v_counts': None
        }
        context = (
            self.manager.set_collectivity_dashboard_context(request, context)
        )
        self.assertIsInstance(context['voting_pag_obj'][0], Voting)
        self.assertEqual(context['collectivity_v_counts'], 2)

    def test_set_custom_user_page_obj_context(self):
        self.proposition_emulation.emulate_proposition()
        request = RequestFactory().get('', data={'page': 1})        
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user  
        page_objects = (
            self.manager._Manager__set_custom_user_page_obj(request)
        )
        self.assertIsInstance(page_objects[0], CustomUser)
        self.assertEqual(page_objects[0].id, 3)
    
    def test_custom_user_queryset_with_request_user(self):
        self.proposition_emulation.emulate_proposition()
        request = RequestFactory().get('',)        
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user     
        custom_users = self.manager._Manager__get_custom_user_queryset(
            request
        )
        self.assertEqual(custom_users[0].id, 3)
        self.assertEqual(custom_users[1].id, 1)
    
    def test_set_page_objects(self):
        self.proposition_emulation.emulate_proposition()
        custom_users = CustomUser.objects.all().order_by('-balance')
        request = RequestFactory().get('',)        
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user     
        page_objects = self.manager._Manager__set_page_objects(
            request, custom_users
        )
        self.assertIsInstance(page_objects[0], CustomUser)
        self.assertEqual(page_objects[0].id, 3)


    def test_custom_users_p_counts_with(self):
        self.proposition_emulation.emulate_proposition()
        request = RequestFactory().get('', data={'page': 1})        
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user  
        custom_user_p_counts = (
            self.manager._Manager__set_custom_user_p_counts(request)
        )
        self.assertEqual(custom_user_p_counts[0]['id'], 1)
        self.assertEqual(custom_user_p_counts[0]['count'], 15)
        self.assertEqual(custom_user_p_counts[1]['id'], 3)
        self.assertEqual(custom_user_p_counts[1]['count'], 13)

    def test_set_proposition_page_obj_context(self):
        self.proposition_emulation.emulate_proposition()
        request = RequestFactory().get('', data={'page': 1})        
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user  
        page_objects = (
            self.manager._Manager__set_proposition_page_obj(request)
        )
        self.assertIsInstance(page_objects[0], Proposition)
        self.assertEqual(page_objects[0].id, 17)

    def test_proposition_queryset_with_request_user(self):
        self.proposition_emulation.emulate_proposition()
        request = RequestFactory().get('',)        
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user     
        propositions = self.manager._Manager__get_proposition_queryset(
            request
        )
        self.assertEqual(propositions[0].id, 17)
        self.assertEqual(propositions[1].id, 16)

    def test_set_discussion_page_obj_context(self):
        self.chat_emulation.emulate_discussion()
        request = RequestFactory().get('', data={'page': 1})        
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user  
        page_objects = (
            self.manager._Manager__set_discussion_page_obj(request)
        )
        self.assertIsInstance(page_objects[0], Discussion)
        self.assertEqual(page_objects[0].id, 3)

    def test_discussiuon_queryset_with_request_user(self):
        self.chat_emulation.emulate_discussion()
        request = RequestFactory().get('',)        
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user     
        discussions = self.manager._Manager__get_discussion_queryset(
            request
        )
        self.assertEqual(discussions[0].id, 3)
        self.assertEqual(discussions[1].id, 2)

    def test_set_voting_page_obj_context(self):
        self.vote_emulation.emulate_voting()
        request = RequestFactory().get('', data={'page': 1})        
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user  
        page_objects = (
            self.manager._Manager__set_voting_page_obj(request)
        )
        self.assertIsInstance(page_objects[0], Voting)
        self.assertEqual(page_objects[0].id, 3)

    def test_voting_queryset_with_request_user(self):
        self.vote_emulation.emulate_voting()
        request = RequestFactory().get('',)        
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user     
        votings = self.manager._Manager__get_voting_queryset(
            request
        )
        self.assertEqual(votings[0].id, 3)
        self.assertEqual(votings[1].id, 1)

    def test_collectivity_p_counts(self):
        self.proposition_emulation.emulate_proposition()
        request = RequestFactory().get('',)        
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user  
        collectivity_p_counts = (
            self.manager._Manager__set_collectivity_p_counts(request)
        )
        self.assertEqual(collectivity_p_counts, 15)

    def test_collectivity_cu_counts(self):
        self.auth_emulation.emulate_custom_user()
        request = RequestFactory().get('',)        
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user  
        collectivity_cu_counts = (
            self.manager._Manager__set_collectivity_cu_counts(request)
        )
        self.assertEqual(collectivity_cu_counts, 2)

    def test_collectivity_discussion_counts(self):
        self.proposition_emulation.emulate_proposition()
        request = RequestFactory().get('',)        
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user  
        collectivity_discussion_counts = (
            self.manager._Manager__set_collectivity_discussion_counts(request)
        )
        self.assertEqual(collectivity_discussion_counts, 3)

    def test_collectivity_votings_counts(self):
        self.vote_emulation.emulate_voting()
        request = RequestFactory().get('',)        
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user  
        collectivity_voting_counts = (
            self.manager._Manager__set_collectivity_voting_counts(request)
        )
        self.assertEqual(collectivity_voting_counts, 2)

    #     self.proposition_emulation.emulate_proposition()
    #     request = RequestFactory().get('', data={'page': 1})        
    #     user = authenticate(email='user1@email.com', password='xxx_Xxxx')
    #     request.user = user     
    #     propositions = self.manager._Manager__get_proposition_queryset(
    #         request, False
    #     )
    #     self.assertEqual(propositions[0].id, 17)

    # def test_set_session_vars_with_search_input(self):
    #     self.proposition_emulation.emulate_proposition()
    #     request = RequestFactory().post('')
    #     session_middleware = SessionMiddleware(request)
    #     session_middleware.process_request(request) 
    #     self.manager.set_session_vars(request, 'Python')
    #     self.assertEqual(
    #         request.session.get('c_p_v_f_search_input'), 'Python'
    #     )

    # def test_create_proposition_with_proposition_instance(self):
    #     self.chat_emulation.emulate_discussion()
    #     self.proposition_emulation.emulate_category()
    #     self.proposition_emulation.emulate_domain()
    #     self.proposition_emulation.emulate_kind()
    #     self.proposition_emulation.emulate_creator_type()
    #     self.proposition_emulation.emulate_status()
    #     form_data = {
    #         'name': 'Cours de Python',
    #         'description': 'dsdss',
    #         'proposition_kind': Kind.objects.get(pk=1).id,
    #         'proposition_category': Category.objects.get(pk=1).id,
    #         'proposition_domain': Domain.objects.get(pk=1).id,
    #         'start_date': "2022-01-25",
    #         'end_date': "2022-01-30",
    #         'duration': 45,
    #         'proposition_creator_type': CreatorType.objects.get(pk=1).id
    #     }
    #     form = PropositionForm(data=form_data)
    #     form.is_valid()
    #     custom_user = CustomUser.objects.get(pk=1)
    #     self.manager.create_proposition(form, custom_user)
    #     self.assertEqual(
    #         Proposition.objects.all().last().name, 'Cours de Python'
    #     )
    #     self.assertEqual(
    #         Proposition.objects.all().last()
    #         .proposition_discussion.discussion_discussion_type.name,
    #         'Proposition'
    #     )
    
    # def test_create_discussion(self):
    #     self.auth_emulation.emulate_custom_user()
    #     self.chat_emulation.emulate_discussion_type()
    #     self.proposition_emulation.emulate_category()
    #     self.proposition_emulation.emulate_domain()
    #     self.proposition_emulation.emulate_kind()
    #     self.proposition_emulation.emulate_creator_type()
    #     self.proposition_emulation.emulate_status()
    #     form_data = {
    #         'name': 'Cours de Python',
    #         'description': 'dsdss',
    #         'proposition_kind': Kind.objects.get(pk=1).id,
    #         'proposition_category': Category.objects.get(pk=1).id,
    #         'proposition_domain': Domain.objects.get(pk=1).id,
    #         'start_date': "2022-01-25",
    #         'end_date': "2022-01-30",
    #         'duration': 45,
    #         'proposition_creator_type': CreatorType.objects.get(pk=1).id
    #     }
    #     form = PropositionForm(data=form_data)
    #     form.is_valid()
    #     custom_user = CustomUser.objects.get(pk=1)
    #     self.manager.create_discussion(form, custom_user)
    #     self.assertEqual(
    #         Discussion.objects.all().last()
    #         .discussion_discussion_type.name,'Proposition'
    #     )

    
    # def test_set_read_prop_view_context_with_demand_nouveau_tak_none(self):
    #     self.proposition_emulation.emulate_proposition()
    #     proposition = Proposition.objects.get(pk=3)
    #     request = RequestFactory().get('')
    #     user = authenticate(email='user3@email.com', password='xxx_Xxxx')
    #     request.user = user     
    #     context = self.manager.set_read_proposition_view_context(
    #         request, proposition.id
    #     )
    #     self.assertEqual(
    #         context['btn1_href'], "/proposition/update_proposition/3/"
    #     )
    #     self.assertEqual(context['btn1_class'],"btn btn-block btn-success")
    #     self.assertEqual(context['btn1_text'], "Sélectionner")
    #     self.assertEqual(context['btn1_value'], "select")
    #     self.assertEqual(context['proposition'], proposition)
    #     self.assertEqual(
    #         context['discussion'],
    #         proposition.proposition_discussion
    #     )
    #     self.assertEqual(
    #         context['comments'][0],
    #         Comment.objects.get(pk=1)
    #     )
    #     self.assertIsInstance(context['form'], CommentForm)

    # def test_set_read_prop_view_context_with_offer_selectionne_creator(self):
    #     self.proposition_emulation.emulate_proposition()
    #     proposition = Proposition.objects.get(pk=16)
    #     request = RequestFactory().get('')
    #     user = authenticate(email='user1@email.com', password='xxx_Xxxx')
    #     request.user = user     
    #     context = self.manager.set_read_proposition_view_context(
    #         request, proposition.id
    #     )
    #     self.assertEqual(
    #         context['btn1_href'], "/proposition/update_proposition/16/"
    #     )
    #     self.assertEqual(context['btn1_class'],"btn btn-block btn-success")
    #     self.assertEqual(context['btn1_text'], "Commencer")
    #     self.assertEqual(context['btn1_value'], "inprogress")

    # def test_set_demand_button_with_sta_nouveau_tak_none_cre_not_user(self):
    #     self.proposition_emulation.emulate_proposition()
    #     proposition = Proposition.objects.get(pk=3)
    #     request = RequestFactory().get('')
    #     user = authenticate(email='user3@email.com', password='xxx_Xxxx')
    #     request.user = user     
    #     btn = self.manager._Manager__set_demand_btn(request, proposition)
    #     self.assertEqual(btn['btn1_href'], "/proposition/update_proposition/3/")
    #     self.assertEqual(btn['btn1_class'],"btn btn-block btn-success")
    #     self.assertEqual(btn['btn1_text'], "Sélectionner")
    #     self.assertEqual(btn['btn1_value'], "select")

    # def test_set_demand_button_with_sta_selectionne_tak_user(self):
    #     self.proposition_emulation.emulate_proposition()
    #     proposition = Proposition.objects.get(pk=6)
    #     request = RequestFactory().get('')
    #     user = authenticate(email='user3@email.com', password='xxx_Xxxx')
    #     request.user = user     
    #     btn = self.manager._Manager__set_demand_btn(request, proposition)
    #     self.assertEqual(btn['btn1_href'], "/proposition/update_proposition/6/")
    #     self.assertEqual(btn['btn1_class'],"btn btn-block btn-danger")
    #     self.assertEqual(btn['btn1_text'], "Annuler")
    #     self.assertEqual(btn['btn1_value'], "new")

    # def test_set_demand_button_with_sta_selectionne_cre_user(self):
    #     self.proposition_emulation.emulate_proposition()
    #     proposition = Proposition.objects.get(pk=6)
    #     request = RequestFactory().get('')
    #     user = authenticate(email='user1@email.com', password='xxx_Xxxx')
    #     request.user = user     
    #     btn = self.manager._Manager__set_demand_btn(request, proposition)
    #     self.assertEqual(btn['btn1_href'], "/proposition/update_proposition/6/")
    #     self.assertEqual(btn['btn1_class'],"btn btn-block btn-success")
    #     self.assertEqual(btn['btn1_text'], "Confirmer")
    #     self.assertEqual(btn['btn1_value'], "inprogress")

    # def test_set_demand_button_with_sta_en_cours_tak_user(self):
    #     self.proposition_emulation.emulate_proposition()
    #     proposition = Proposition.objects.get(pk=2)
    #     request = RequestFactory().get('')
    #     user = authenticate(email='user3@email.com', password='xxx_Xxxx')
    #     request.user = user     
    #     btn = self.manager._Manager__set_demand_btn(request, proposition)
    #     self.assertEqual(btn['btn1_href'], "/proposition/update_proposition/2/")
    #     self.assertEqual(btn['btn1_class'],"btn btn-block btn-success")
    #     self.assertEqual(btn['btn1_text'], "Terminer")
    #     self.assertEqual(btn['btn1_value'], "realized")
    #     self.assertEqual(btn['btn2_href'], "/proposition/update_proposition/2/")
    #     self.assertEqual(btn['btn2_class'],"btn btn-block btn-danger")
    #     self.assertEqual(btn['btn2_text'], "Annuler")
    #     self.assertEqual(btn['btn2_value'], "new")

    # def test_set_demand_button_with_sta_realized_cre_user(self):
    #     self.proposition_emulation.emulate_proposition()
    #     proposition = Proposition.objects.get(pk=4)
    #     request = RequestFactory().get('')
    #     user = authenticate(email='user1@email.com', password='xxx_Xxxx')
    #     request.user = user     
    #     btn = self.manager._Manager__set_demand_btn(request, proposition)
    #     self.assertEqual(btn['btn1_href'], "/proposition/update_proposition/4/")
    #     self.assertEqual(btn['btn1_class'],"btn btn-block btn-success")
    #     self.assertEqual(btn['btn1_text'], "Valider")
    #     self.assertEqual(btn['btn1_value'], "done")
    #     self.assertEqual(btn['btn2_href'], "/proposition/update_proposition/4/")
    #     self.assertEqual(btn['btn2_class'],"btn btn-block btn-danger")
    #     self.assertEqual(btn['btn2_text'], "Rejeter")
    #     self.assertEqual(btn['btn2_value'], "rejected")

    # def test_set_demand_button_with_sta_rejected_tak_user(self):
    #     self.proposition_emulation.emulate_proposition()
    #     proposition = Proposition.objects.get(pk=5)
    #     request = RequestFactory().get('')
    #     user = authenticate(email='user3@email.com', password='xxx_Xxxx')
    #     request.user = user     
    #     btn = self.manager._Manager__set_demand_btn(request, proposition)
    #     self.assertEqual(btn['btn1_href'], "/proposition/update_proposition/5/")
    #     self.assertEqual(btn['btn1_class'],"btn btn-block btn-success")
    #     self.assertEqual(btn['btn1_text'], "Reprendre")
    #     self.assertEqual(btn['btn1_value'], "inprogress")
    #     self.assertEqual(btn['btn2_href'], "/proposition/update_proposition/5/")
    #     self.assertEqual(btn['btn2_class'],"btn btn-block btn-danger")
    #     self.assertEqual(btn['btn2_text'], "Forcer terminer")
    #     self.assertEqual(btn['btn2_value'], "done")

    # def test_set_demand_button_with_sta_rejected_cre_user(self):
    #     self.proposition_emulation.emulate_proposition()
    #     proposition = Proposition.objects.get(pk=5)
    #     request = RequestFactory().get('')
    #     user = authenticate(email='user1@email.com', password='xxx_Xxxx')
    #     request.user = user     
    #     btn = self.manager._Manager__set_demand_btn(request, proposition)
    #     self.assertEqual(btn['btn1_href'], "/proposition/update_proposition/5/")
    #     self.assertEqual(btn['btn1_class'],"btn btn-block btn-success")
    #     self.assertEqual(btn['btn1_text'], "Valider")
    #     self.assertEqual(btn['btn1_value'], "done")

    # def test_set_demand_button_with_sta_annule_cre_user(self):
    #     self.proposition_emulation.emulate_proposition()
    #     proposition = Proposition.objects.get(pk=1)
    #     request = RequestFactory().get('')
    #     user = authenticate(email='user1@email.com', password='xxx_Xxxx')
    #     request.user = user     
    #     btn = self.manager._Manager__set_demand_btn(request, proposition)
    #     self.assertIsNone(btn['btn1_href'])
    #     self.assertIsNone(btn['btn1_class'])
    #     self.assertIsNone(btn['btn1_text'])
    #     self.assertIsNone(btn['btn1_value'])

    # def test_set_btn_dict_with_argument(self):
    #     btn = self.manager._Manager__set_btn_dict('un', 'deux', 'trois')
    #     self.assertEqual(btn['btn1_href'],'un')
    #     self.assertIsNone(btn['btn1_value'])

    # def test_set_check_index_with_list(self):
    #     items = ['item1', 'item2', 'item3']
    #     item1 = self.manager._Manager__check_index(items,0)
    #     item4 = self.manager._Manager__check_index(items,3)
    #     self.assertIsNotNone(item1)
    #     self.assertIsNone(item4)

    # def test_set_offer_btn_with_sta_nouveau_tak_none_cre_not_user(self):
    #     self.proposition_emulation.emulate_proposition()
    #     proposition = Proposition.objects.get(pk=13)
    #     request = RequestFactory().get('')
    #     user = authenticate(email='user3@email.com', password='xxx_Xxxx')
    #     request.user = user     
    #     btn = self.manager._Manager__set_offer_btn(request, proposition)
    #     self.assertEqual(
    #         btn['btn1_href'], "/proposition/update_proposition/13/"
    #     )
    #     self.assertEqual(btn['btn1_class'],"btn btn-block btn-success")
    #     self.assertEqual(btn['btn1_text'], "Sélectionner")
    #     self.assertEqual(btn['btn1_value'], "select")

    # def test_set_offer_btn_with_sta_selectionne_tak_user(self):
    #     self.proposition_emulation.emulate_proposition()
    #     proposition = Proposition.objects.get(pk=16)
    #     request = RequestFactory().get('')
    #     user = authenticate(email='user3@email.com', password='xxx_Xxxx')
    #     request.user = user     
    #     btn = self.manager._Manager__set_offer_btn(request, proposition)
    #     self.assertEqual(
    #         btn['btn1_href'], "/proposition/update_proposition/16/"
    #     )
    #     self.assertEqual(btn['btn1_class'],"btn btn-block btn-danger")
    #     self.assertEqual(btn['btn1_text'], "Annuler")
    #     self.assertEqual(btn['btn1_value'], "new")

    # def test_set_offer_btn_with_sta_selectionne_cre_user(self):
    #     self.proposition_emulation.emulate_proposition()
    #     proposition = Proposition.objects.get(pk=16)
    #     request = RequestFactory().get('')
    #     user = authenticate(email='user1@email.com', password='xxx_Xxxx')
    #     request.user = user     
    #     btn = self.manager._Manager__set_offer_btn(request, proposition)
    #     self.assertEqual(
    #         btn['btn1_href'], "/proposition/update_proposition/16/"
    #     )
    #     self.assertEqual(btn['btn1_class'],"btn btn-block btn-success")
    #     self.assertEqual(btn['btn1_text'], "Commencer")
    #     self.assertEqual(btn['btn1_value'], "inprogress")


    # def test_set_offer_bun_with_sta_en_cours_cre_user(self):
    #     self.proposition_emulation.emulate_proposition()
    #     proposition = Proposition.objects.get(pk=12)
    #     request = RequestFactory().get('')
    #     user = authenticate(email='user1@email.com', password='xxx_Xxxx')
    #     request.user = user     
    #     btn = self.manager._Manager__set_offer_btn(request, proposition)
    #     self.assertEqual(
    #         btn['btn1_href'], "/proposition/update_proposition/12/"
    #     )
    #     self.assertEqual(btn['btn1_class'],"btn btn-block btn-success")
    #     self.assertEqual(btn['btn1_text'], "Terminer")
    #     self.assertEqual(btn['btn1_value'], "realized")

    # def test_set_offer_btn_with_sta_realized_tak_user(self):
    #     self.proposition_emulation.emulate_proposition()
    #     proposition = Proposition.objects.get(pk=14)
    #     request = RequestFactory().get('')
    #     user = authenticate(email='user3@email.com', password='xxx_Xxxx')
    #     request.user = user     
    #     btn = self.manager._Manager__set_offer_btn(request, proposition)
    #     self.assertEqual(
    #         btn['btn1_href'], "/proposition/update_proposition/14/"
    #     )
    #     self.assertEqual(btn['btn1_class'],"btn btn-block btn-success")
    #     self.assertEqual(btn['btn1_text'], "Valider")
    #     self.assertEqual(btn['btn1_value'], "done")
    #     self.assertEqual(
    #         btn['btn2_href'], "/proposition/update_proposition/14/"
    #     )
    #     self.assertEqual(btn['btn2_class'],"btn btn-block btn-danger")
    #     self.assertEqual(btn['btn2_text'], "Rejeter")
    #     self.assertEqual(btn['btn2_value'], "rejected")

    # def test_set_offer_btn_with_sta_rejected_tak_user(self):
    #     self.proposition_emulation.emulate_proposition()
    #     proposition = Proposition.objects.get(pk=15)
    #     request = RequestFactory().get('')
    #     user = authenticate(email='user3@email.com', password='xxx_Xxxx')
    #     request.user = user     
    #     btn = self.manager._Manager__set_offer_btn(request, proposition)
    #     self.assertEqual(
    #         btn['btn1_href'], "/proposition/update_proposition/15/"
    #     )
    #     self.assertEqual(btn['btn1_class'],"btn btn-block btn-success")
    #     self.assertEqual(btn['btn1_text'], "Valider")
    #     self.assertEqual(btn['btn1_value'], "done")

    # def test_set_offer_btn_with_sta_rejected_cre_user(self):
    #     self.proposition_emulation.emulate_proposition()
    #     proposition = Proposition.objects.get(pk=15)
    #     request = RequestFactory().get('')
    #     user = authenticate(email='user1@email.com', password='xxx_Xxxx')
    #     request.user = user     
    #     btn = self.manager._Manager__set_offer_btn(request, proposition)
    #     self.assertEqual(
    #         btn['btn1_href'], "/proposition/update_proposition/15/"
    #     )
    #     self.assertEqual(btn['btn1_class'],"btn btn-block btn-success")
    #     self.assertEqual(btn['btn1_text'], "Reprendre")
    #     self.assertEqual(btn['btn1_value'], "inprogress")
    #     self.assertEqual(
    #         btn['btn2_href'], "/proposition/update_proposition/15/"
    #     )
    #     self.assertEqual(btn['btn2_class'],"btn btn-block btn-danger")
    #     self.assertEqual(btn['btn2_text'], "Forcer terminer")
    #     self.assertEqual(btn['btn2_value'], "done")

    # def test_set_proposition_status_with_select_taker(self):
    #     self.proposition_emulation.emulate_proposition()
    #     request = RequestFactory().post(
    #         '', data={'update_status_button':'select'}
    #     )
    #     user = authenticate(email='user3@email.com', password='xxx_Xxxx')
    #     request.user = user
    #     self.manager.set_proposition_status(request, 3)
    #     proposition = Proposition.objects.get(pk=3)
    #     self.assertEqual(proposition.proposition_status.id,6)
    #     self.assertEqual(
    #         proposition.proposition_taker.email, 'user3@email.com'
    #     )

    # def test_set_proposition_status_with_new_taker(self):
    #     self.proposition_emulation.emulate_proposition()
    #     request = RequestFactory().post(
    #         '', data={'update_status_button':'new'}
    #     )
    #     user = authenticate(email='user3@email.com', password='xxx_Xxxx')
    #     request.user = user
    #     self.manager.set_proposition_status(request, 1)
    #     proposition = Proposition.objects.get(pk=1)
    #     self.assertEqual(proposition.proposition_status.id,3)
    #     self.assertIsNone(proposition.proposition_taker)

    # def test_set_proposition_status_with_inprogress(self):
    #     self.proposition_emulation.emulate_proposition()
    #     request = RequestFactory().post(
    #         '', data={'update_status_button':'inprogress'}
    #     )
    #     user = authenticate(email='user3@email.com', password='xxx_Xxxx')
    #     request.user = user
    #     self.manager.set_proposition_status(request, 6)
    #     proposition = Proposition.objects.get(pk=6)
    #     self.assertEqual(proposition.proposition_status.id,2)

    # def test_set_proposition_status_with_realized(self):
    #     self.proposition_emulation.emulate_proposition()
    #     request = RequestFactory().post(
    #         '', data={'update_status_button':'realized'}
    #     )
    #     user = authenticate(email='user3@email.com', password='xxx_Xxxx')
    #     request.user = user
    #     self.manager.set_proposition_status(request, 2)
    #     proposition = Proposition.objects.get(pk=2)
    #     self.assertEqual(proposition.proposition_status.id,4)

    # def test_set_proposition_status_with_rejected(self):
    #     self.proposition_emulation.emulate_proposition()
    #     request = RequestFactory().post(
    #         '', data={'update_status_button':'rejected'}
    #     )
    #     user = authenticate(email='user3@email.com', password='xxx_Xxxx')
    #     request.user = user
    #     self.manager.set_proposition_status(request, 4)
    #     proposition = Proposition.objects.get(pk=4)
    #     self.assertEqual(proposition.proposition_status.id,5)

    # def test_set_proposition_status_with_done(self):
    #     self.proposition_emulation.emulate_proposition()
    #     request = RequestFactory().post(
    #         '', data={'update_status_button':'done'}
    #     )
    #     user = authenticate(email='user3@email.com', password='xxx_Xxxx')
    #     request.user = user
    #     self.manager.set_proposition_status(request, 4)
    #     proposition = Proposition.objects.get(pk=4)
    #     self.assertEqual(proposition.proposition_status.id,7)
    #     self.assertEqual(proposition.proposition_creator.balance, 940)
    #     self.assertEqual(proposition.proposition_taker.balance, 3060)
    
    # def test_set_proposition_status_with_selectione(self):
    #     self.proposition_emulation.emulate_status()
    #     status = self.manager._Manager__set_status('Sélectionné')
    #     self.assertEqual(
    #         Status.objects.get(name__exact='Sélectionné').name,
    #         status.name
    #     )

    # def test_set_creator_taker_balance_with_demande_individuelle(self):
    #     self.proposition_emulation.emulate_proposition()
    #     proposition = Proposition.objects.get(pk=18)
    #     self.manager._Manager__set_creator_taker_balance(proposition)
    #     proposition = Proposition.objects.get(pk=18)
    #     self.assertEqual(proposition.proposition_creator.balance, 880)
    #     self.assertEqual(proposition.proposition_taker.balance, 3120)
    
    # def test_set_creator_taker_balance_with_demande_collective(self):
    #     self.proposition_emulation.emulate_proposition()
    #     proposition = Proposition.objects.get(pk=4)
    #     self.manager._Manager__set_creator_taker_balance(proposition)
    #     proposition = Proposition.objects.get(pk=4)
    #     self.assertEqual(proposition.proposition_creator.balance, 940)
    #     self.assertEqual(proposition.proposition_taker.balance, 3060)

    # def test_set_custom_users_balances_with_demande_collective(self):
    #     self.proposition_emulation.emulate_proposition()
    #     proposition = Proposition.objects.get(pk=4)
    #     self.manager._Manager__set_custom_users_balances(proposition)
    #     proposition = Proposition.objects.get(pk=4)
    #     self.assertEqual(proposition.proposition_creator.balance, 940)
    #     self.assertEqual(proposition.proposition_taker.balance, 2940)

    # def test_get_discussion_with_proposition_instance(self):
    #     self.proposition_emulation.emulate_proposition()
    #     proposition = Proposition.objects.get(pk=1)
    #     discussion = self.manager._Manager__get_discussion(proposition)
    #     self.assertEqual(discussion, Discussion.objects.get(pk=1))

    # def test_get_discussion_with_none(self):
    #     proposition = None
    #     discussion = self.manager._Manager__get_discussion(proposition)
    #     self.assertIsNone(discussion)

    # def test_get_comments_with_proposition_instance(self):
    #     self.proposition_emulation.emulate_proposition()
    #     proposition = Proposition.objects.get(pk=1)
    #     comments = self.manager._Manager__get_comments(proposition)
    #     self.assertEqual(comments[0], Comment.objects.get(pk=1))

    # def test_get_comments_with_none(self):
    #     proposition = None
    #     comments = self.manager._Manager__get_comments(proposition)
    #     self.assertIsNone(comments)

    # def test_create_comment(self):
    #     self.proposition_emulation.emulate_proposition()
    #     Comment.objects.all().delete()
    #     form = CommentForm(data={'comment': 'Alors???'})
    #     form.is_valid()
    #     custom_user = CustomUser.objects.get(pk=1)
    #     id_proposition = Proposition.objects.get(pk=1).id
    #     self.manager.create_comment(form, custom_user, id_proposition)
    #     self.assertEqual(
    #         Comment.objects.all().last().comment, 'Alors???'
    #     )
