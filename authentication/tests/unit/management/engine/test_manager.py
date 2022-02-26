"""Test manager module.
"""
from django.test import TestCase

from authentication.management.engine.manager import Manager
from authentication.models import CustomUser
from authentication.tests.emulation.authentication_emulation import (
    AuthenticationEmulation
)
from collectivity.models.collectivity import Collectivity
from collectivity.tests.emulation.collectivity_emulation import (
    CollectivityEmulation
)

class TestManager(TestCase):
    """Test Manager  class.
    """
    def setUp(self):
        CollectivityEmulation().emulate_postal_code()
        CollectivityEmulation().emulate_collectivity()
        CollectivityEmulation().emulate_set_collectivity_postal_code()
        self.manager = Manager()
    
    def test_check_collectivity_with_valid_form_data(self):
        method_result = self.manager.check_collectivity(
            '92220',
            'Bagneux'
        )
        self.assertIsInstance(method_result, Collectivity)

    def test_check_collectivity_with_invalid_form_data(self):
        method_result = self.manager.check_collectivity(
            '92220',
            'Bourg-la-Reine'
        )
        self.assertFalse(method_result)

    def test_create_cu_with_valid_form_and_cu_instance(self):
        form = AuthenticationEmulation().emulate_custom_user_form()
        form.is_valid()
        collectivity = Collectivity.objects.all().last()
        self.manager.create_custom_user(form, collectivity)
        self.assertEqual(
            CustomUser.objects.all().last().email,
            'user@email.com'
        )
