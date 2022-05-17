# pylint: disable=C0114,C0115,C0116
from json import loads

from django.test import TestCase

from information.tests.emulation.information_emulation import (
    InformationEmulation
)


class HomeViewTest(TestCase):

    def setUp(self):
        self.information_emulation = InformationEmulation()
        self.information_emulation.emulate_test_setup()

    def test_get_with_nominal_scenario(self):
        response = self.client.get(
            '', follow=True
        )
        vector_layer = loads(response.context['vector_layer'])
        stats_data = loads(response.context['stats_data'])
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'information/home.html'
        )
        self.assertTrue(response.context['mapbox_url'])
        self.assertEqual(
            vector_layer['features'][0]
            ['properties']['name'], 'Bourg-la-Reine'
        )
        self.assertEqual(stats_data['cu_counts'][0], '0')
        self.assertEqual(response.context['all_p_counts'], 15)
        self.assertEqual(response.context['all_cu_counts'], 3)
        self.assertEqual(response.context['all_co_counts'], 2)
        self.assertEqual(response.context['all_v_counts'], 3)
        self.assertEqual(response.context['propositions'][0].id, 17)
