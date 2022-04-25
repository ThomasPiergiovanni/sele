"""Test manager module.
"""
from datetime import date, timedelta
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
    
    def emulate_ref_date(self):
        today = timezone.now()
        return today.replace(day=1)
    
    def emulate_ref_dates(self):
        ref_date = self.emulate_ref_date()
        def previous_date(d):
            ld = d - timedelta(days=1)
            previous_date = ld.replace(day=1)
            return previous_date
        ref_date_1 = previous_date(ref_date)
        ref_date_2 = previous_date(ref_date_1)
        ref_date_3 = previous_date(ref_date_2)
        ref_date_4 = previous_date(ref_date_3)
        ref_date_5 = previous_date(ref_date_4)
        ref_dates = {
            'r0': ref_date,'r1': ref_date_1,'r2': ref_date_2, 'r3': ref_date_3,
            'r4': ref_date_4,'r5': ref_date_5
        }
        return ref_dates

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
        ref_date = self.emulate_ref_date()
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
        str(ref_date.month)+"-"+str(ref_date.year))
    
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

    def test_set_stats_data_json_with_label(self):
        self.proposition_emulation.emulate_proposition()
        self.collectivty_emulation.emulate_collectivity()
        ref_date = self.emulate_ref_date()
        data_json = self.manager._Manager__set_stats_data_json()
        data_json = loads(data_json)
        self.assertEqual(
            data_json['labels'][5],str(ref_date.month)+"-"+str(ref_date.year)
        )

    def test_set_stats_ref_dates_with_today(self):
        ref_date = self.emulate_ref_date()
        ref_dates = self.manager._Manager__set_ref_dates()
        self.assertEqual(ref_dates['r0'].date(), ref_date.date())

    def test__set_previous_date(self):
        ref_date = self.emulate_ref_date()
        last = ref_date - timedelta(days=1)
        last_first = last.replace(day=1)
        previous_date = self.manager._Manager__set_previous_date(ref_date)
        self.assertEqual(previous_date.date(), last_first.date())

    def test_set_stats_label(self):
        ref_dates = self.emulate_ref_dates()
        label = self.manager._Manager__set_stats_label(ref_dates)
        self.assertEqual(
            label['m_0'],
            str(ref_dates['r0'].month) + "-" + str(ref_dates['r0'].year)
        )
        self.assertEqual(
            label['m_min_5'],
            str(ref_dates['r5'].month) + "-" + str(ref_dates['r5'].year)
        )

    def test_set_mm_yyyy(self):
        today = timezone.now()
        r0 = today.replace(day=1)
        mm_yyyy = self.manager._Manager__set_mm_yyyy(r0)
        self.assertEqual(mm_yyyy, str(r0.month) + "-" + str(r0.year))   

    def test_set_stats_cu_counts(self):
        ref_dates = self.emulate_ref_dates()
        cu_counts = self.manager._Manager__set_stats_cu_counts(ref_dates)
        self.assertEqual(cu_counts['cu_0'], 0)

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
