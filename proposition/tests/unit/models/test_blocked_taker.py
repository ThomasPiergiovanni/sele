"""Test blocked taker method module.
"""
from django.db import models
from django.test import TestCase

from authentication.models import CustomUser
from proposition.models.blocked_taker import BlockedTaker
from proposition.models.proposition import Proposition
from proposition.tests.emulation.proposition_emulation import (
    PropositionEmulation
)

class BlockedTakerTest(TestCase):
    """Test BlockedTaker class.
    """
    def setUp(self):
        self.proposition_emulation = PropositionEmulation()

    def test_blocked_taker_with_blocked_taker_class(self):
        self.proposition_emulation.emulate_blocked_taker()
        blocked_taker = BlockedTaker.objects.get(pk=1)
        self.assertIsInstance(blocked_taker, BlockedTaker)

    def test_blocked_taker_with_attr_custom_user_characteristic(self):
        self.proposition_emulation.emulate_blocked_taker()
        attribute = BlockedTaker._meta.get_field('blocked_taker_custom_user')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),
            type(models.ForeignKey(CustomUser, on_delete=models.CASCADE))
        )
        self.assertEqual(attribute.null, False)

    def test_blocked_taker_with_attr_proposition_characteristic(self):
        self.proposition_emulation.emulate_blocked_taker()
        attribute = BlockedTaker._meta.get_field('blocked_taker_proposition')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),
            type(models.ForeignKey(Proposition, on_delete=models.CASCADE))
        )
        self.assertEqual(attribute.null, False)

    def test_blocked_taker_with_emulated_blocked_taker_instance(self):
        self.proposition_emulation.emulate_blocked_taker()
        blocked_taker = BlockedTaker.objects.get(pk=1)
        self.assertEqual(blocked_taker.blocked_taker_custom_user_id, 1)
        self.assertEqual(blocked_taker.blocked_taker_proposition_id, 1)
        blocked_taker = BlockedTaker.objects.get(pk=2)
        self.assertEqual(blocked_taker.blocked_taker_custom_user_id, 2)
        self.assertEqual(blocked_taker.blocked_taker_proposition_id, 2)
