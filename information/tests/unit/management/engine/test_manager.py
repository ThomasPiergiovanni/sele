# pylint: disable=C0114,C0115,C0116,E1136,R0904,R0201,R0801,W0212
from datetime import timedelta
from json import loads

from django.contrib.auth import authenticate
from django.test import RequestFactory, TestCase
from django.utils import timezone

from authentication.models import CustomUser
from chat.models import Discussion
from config.settings import MAPBOX_TOKEN
from information.management.engine.manager import Manager
from information.tests.emulation.information_emulation import (
    InformationEmulation
)
from proposition.models import Proposition
from vote.models import Voting


class TestManager(TestCase):

    def setUp(self):
        self.information_emulation = InformationEmulation()
        self.information_emulation.emulate_test_setup()
        self.manager = Manager()

    def emulate_ref_date(self):
        today = timezone.now()
        return today.replace(day=1)

    def emulate_ref_dates(self):
        ref_date = self.emulate_ref_date()

        def previous_date(day_one):
            last_day = day_one - timedelta(days=1)
            previous_date = last_day.replace(day=1)
            return previous_date
        ref_date_1 = previous_date(ref_date)
        ref_date_2 = previous_date(ref_date_1)
        ref_date_3 = previous_date(ref_date_2)
        ref_date_4 = previous_date(ref_date_3)
        ref_date_5 = previous_date(ref_date_4)
        ref_dates = {
            'r0': ref_date, 'r1': ref_date_1, 'r2': ref_date_2,
            'r3': ref_date_3, 'r4': ref_date_4, 'r5': ref_date_5
        }
        return ref_dates

    def test_set_home_context(self):
        context = {
            'mapbox_url': None,
            'vector_layer': None,
            'stats_data': None,
            'all_p_counts': None,
            'all_cu_counts': None,
            'all_co_counts': None,
            'all_v_counts': None,
            'propositions': None
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
            'https://api.mapbox.com/styles/v1/thomaspiergiovanni/ckmm3' +
            'kryyu79j17ptmgsmg9c9/tiles/{z}/{x}/{y}?access_token=' +
            MAPBOX_TOKEN
        )
        self.assertEqual(
            vector_layer['features'][0]['properties']['name'], 'Bourg-la-Reine'
        )
        self.assertEqual(
            stats_data['labels'][5], str(ref_date.month)+"-"+str(ref_date.year)
        )
        self.assertEqual(context['all_p_counts'], 15)
        self.assertEqual(context['all_cu_counts'], 3)
        self.assertEqual(context['all_co_counts'], 2)
        self.assertEqual(context['all_v_counts'], 3)
        self.assertEqual(context['propositions'][0].id, 17)

    def test_set_mapboxurl_json(self):
        data = self.manager._Manager__set_mapboxurl_json()
        data = loads(data)
        self.assertEqual(
            data['url'],
            'https://api.mapbox.com/styles/v1/thomaspiergiovanni/ckmm3' +
            'kryyu79j17ptmgsmg9c9/tiles/{z}/{x}/{y}?access_token=' +
            MAPBOX_TOKEN
        )

    def test_set_vectorlayer_geojson(self):
        data = self.manager._Manager__set_vectorlayer_geojson()
        data = loads(data)
        self.assertEqual(
            data['features'][0]['properties']['name'], 'Bourg-la-Reine'
        )

    def test_set_stats_data_json_with_label(self):
        ref_date = self.emulate_ref_date()
        data_json = self.manager._Manager__set_stats_data_json()
        data_json = loads(data_json)
        self.assertEqual(
            data_json['labels'][5], str(ref_date.month)+"-"+str(ref_date.year)
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
        day_one = today.replace(day=1)
        mm_yyyy = self.manager._Manager__set_mm_yyyy(day_one)
        self.assertEqual(mm_yyyy, str(day_one.month) + "-" + str(day_one.year))

    def test_set_stats_cu_counts(self):
        ref_dates = self.emulate_ref_dates()
        cu_counts = self.manager._Manager__set_stats_cu_counts(ref_dates)
        self.assertEqual(cu_counts['cu_0'], 0)

    def test_set_cu_counts(self):
        ref_date = self.emulate_ref_date()
        cu_counts = self.manager._Manager__set_cu_counts(ref_date)
        self.assertEqual(cu_counts, 0)

    def test_set_stats_p_counts(self):
        ref_dates = self.emulate_ref_dates()
        p_counts = self.manager._Manager__set_stats_p_counts(ref_dates)
        self.assertEqual(p_counts['p_0'], 15)

    def test_set_p_counts(self):
        ref_date = self.emulate_ref_date()
        p_counts = self.manager._Manager__set_p_counts(ref_date)
        self.assertEqual(p_counts, 15)

    def test_set_stats_data(self):
        label = {
            'm_0': '04-2022', 'm_min_1': None, 'm_min_2': None,
            'm_min_3': None, 'm_min_4': None, 'm_min_5': '11-2021'
        }
        cu_counts = {
            'cu_0': 4, 'cu_min_1': None, 'cu_min_2': None, 'cu_min_3': None,
            'cu_min_4': None, 'cu_min_5': 2
        }
        p_counts = {
            'p_0': 6, 'p_min_1': None, 'p_min_2': None, 'p_min_3': None,
            'p_min_4': None, 'p_min_5': 3
        }
        data = self.manager._Manager__set_stats_chart_data(
            label, cu_counts, p_counts
        )
        self.assertEqual(data['p_counts'][0], str(3))

    def test_set_all_co_counts(self):
        request = RequestFactory().get('',)
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user
        all_co_counts = (
            self.manager._Manager__set_all_co_counts()
        )
        self.assertEqual(all_co_counts, 2)

    def test_set_all_v_counts(self):
        request = RequestFactory().get('',)
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user
        all_v_counts = (
            self.manager._Manager__set_all_v_counts()
        )
        self.assertEqual(all_v_counts, 3)

    def test_set_home_propositions(self):
        request = RequestFactory().get('',)
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user
        propositions = (
            self.manager._Manager__set_home_propositions()
        )
        self.assertEqual(propositions[0].id, 17)

    def test_set_collectivity_dashboard_context_with_cus_user_prop_dis(self):
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
        self.assertTrue(context['custom_users_p_counts'][0]['count'])
        self.assertIsInstance(context['proposition_pag_obj'][0], Proposition)
        self.assertIsInstance(context['discussion_pag_obj'][0], Discussion)
        self.assertEqual(context['collectivity_p_counts'], 15)
        self.assertEqual(context['collectivity_cu_counts'], 2)
        self.assertEqual(context['collectivity_d_counts'], 3)

    def test_set_collectivity_dashboard_context_with_voting(self):
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
        request = RequestFactory().get('', data={'page': 1})
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user
        page_objects = (
            self.manager._Manager__set_custom_user_page_obj(request)
        )
        self.assertIsInstance(page_objects[0], CustomUser)
        self.assertEqual(page_objects[0].id, 3)

    def test_custom_user_queryset_with_request_user(self):
        request = RequestFactory().get('',)
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user
        custom_users = self.manager._Manager__get_custom_user_queryset(
            request
        )
        self.assertEqual(custom_users[0].id, 3)
        self.assertEqual(custom_users[1].id, 1)

    def test_set_page_objects(self):
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
        request = RequestFactory().get('', data={'page': 1})
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user
        custom_user_p_counts = (
            self.manager._Manager__set_custom_user_p_counts(request)
        )
        self.assertTrue(custom_user_p_counts[0]['id'])
        self.assertTrue(custom_user_p_counts[0]['count'])
        self.assertTrue(custom_user_p_counts[1]['id'])
        self.assertTrue(custom_user_p_counts[1]['count'])

    def test_set_proposition_page_obj_context(self):
        request = RequestFactory().get('', data={'page': 1})
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user
        page_objects = (
            self.manager._Manager__set_proposition_page_obj(request)
        )
        self.assertIsInstance(page_objects[0], Proposition)
        self.assertEqual(page_objects[0].id, 17)

    def test_proposition_queryset_with_request_user(self):
        request = RequestFactory().get('',)
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user
        propositions = self.manager._Manager__get_proposition_queryset(
            request
        )
        self.assertEqual(propositions[0].id, 17)
        self.assertEqual(propositions[1].id, 16)

    def test_set_discussion_page_obj_context(self):
        request = RequestFactory().get('', data={'page': 1})
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user
        page_objects = (
            self.manager._Manager__set_discussion_page_obj(request)
        )
        self.assertIsInstance(page_objects[0], Discussion)
        self.assertEqual(page_objects[0].id, 3)

    def test_discussiuon_queryset_with_request_user(self):
        request = RequestFactory().get('',)
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user
        discussions = self.manager._Manager__get_discussion_queryset(
            request
        )
        self.assertEqual(discussions[0].id, 3)
        self.assertEqual(discussions[1].id, 2)

    def test_set_voting_page_obj_context(self):
        request = RequestFactory().get('', data={'page': 1})
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user
        page_objects = (
            self.manager._Manager__set_voting_page_obj(request)
        )
        self.assertIsInstance(page_objects[0], Voting)
        self.assertEqual(page_objects[0].id, 1)

    def test_voting_queryset_with_request_user(self):
        request = RequestFactory().get('',)
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user
        votings = self.manager._Manager__get_voting_queryset(
            request
        )
        self.assertEqual(votings[0].id, 1)
        self.assertEqual(votings[1].id, 3)

    def test_collectivity_p_counts(self):
        request = RequestFactory().get('',)
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user
        collectivity_p_counts = (
            self.manager._Manager__set_collectivity_p_counts(request)
        )
        self.assertEqual(collectivity_p_counts, 15)

    def test_collectivity_cu_counts(self):
        request = RequestFactory().get('',)
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user
        collectivity_cu_counts = (
            self.manager._Manager__set_collectivity_cu_counts(request)
        )
        self.assertEqual(collectivity_cu_counts, 2)

    def test_collectivity_discussion_counts(self):
        request = RequestFactory().get('',)
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user
        collectivity_discussion_counts = (
            self.manager._Manager__set_collectivity_discussion_counts(request)
        )
        self.assertEqual(collectivity_discussion_counts, 3)

    def test_collectivity_votings_counts(self):
        request = RequestFactory().get('',)
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user
        collectivity_voting_counts = (
            self.manager._Manager__set_collectivity_voting_counts(request)
        )
        self.assertEqual(collectivity_voting_counts, 2)
