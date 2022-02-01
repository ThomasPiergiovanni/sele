"""Test blocked taker method module.
"""
from django.db import models
from django.test import TestCase
from authentication.models import CustomUser

# from authentication.models import CustomUser
# from authentication.tests.unit.models.test_custom_user import CustomUserTest
from proposition.models.blocked_taker import BlockedTaker
from proposition.models.proposition import Proposition
from proposition.tests.unit.models.test_proposition import PropositionTest


class BlockedTakerTest(TestCase):
    """Test BlockedTaker class.
    """
    def setUp(self):
        self.emulate_blocked_taker()

    def emulate_blocked_taker(self):
        """
        """
        PropositionTest().emulate_proposition()
        BlockedTaker.objects.create(id=1,proposition_id=1,custom_user_id=1),
        BlockedTaker.objects.create(id=2,proposition_id=2,custom_user_id=2),

    def test_blocked_taker_with_blocked_taker_class(self):
        blocked_taker = BlockedTaker.objects.get(pk=1)
        self.assertIsInstance(blocked_taker, BlockedTaker)

    def test_blocked_taker_with_attr_custom_user_characteristic(self):
        attribute = BlockedTaker._meta.get_field('custom_user')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),
            type(models.ForeignKey(CustomUser, on_delete=models.CASCADE))
        )
        self.assertEqual(attribute.null, False)

    def test_blocked_taker_with_attr_proposition_characteristic(self):
        attribute = BlockedTaker._meta.get_field('proposition')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),
            type(models.ForeignKey(Proposition, on_delete=models.CASCADE))
        )
        self.assertEqual(attribute.null, False)

    def test_blocked_taker_with_emulated_blocked_taker_instance(self):
        blocked_taker = BlockedTaker.objects.get(pk=1)
        self.assertEqual(blocked_taker.custom_user_id, 1)
        self.assertEqual(blocked_taker.proposition_id, 1)
        blocked_taker = BlockedTaker.objects.get(pk=2)
        self.assertEqual(blocked_taker.custom_user_id, 2)
        self.assertEqual(blocked_taker.proposition_id, 2)
