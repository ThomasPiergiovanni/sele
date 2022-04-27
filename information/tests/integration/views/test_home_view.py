# pylint: disable=C0116
"""Test home view module.
"""
from django.test import TestCase
from json import loads

from collectivity.tests.emulation.collectivity_emulation import (
    CollectivityEmulation
)
from proposition.tests.emulation.proposition_emulation import PropositionEmulation


class HomeViewTest(TestCase):
    """Test home view class.
    """

    def setUp(self):
        self.collectivity_emulation = CollectivityEmulation()
        self.emulate_proposition = PropositionEmulation()

    def test_get_with_nominal_scenario(self):
        self.collectivity_emulation.emulate_collectivity()
        self.emulate_proposition.emulate_proposition()
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
        self.assertEqual(stats_data['cu_counts'][0], 0)

