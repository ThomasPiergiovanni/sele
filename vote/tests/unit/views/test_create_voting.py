"""Test add voting view module.
"""
from django.test import TestCase
from django.urls import reverse

from vote.views.create_voting import CreateVoting


class TestCreateVoting(TestCase):
    """Test CreateVoting view class.
    """
    def setUp(self):
        self.view = CreateVoting()

    def test_init_with_create_voting_instance(self):
        self.assertTrue(self.view)

    def test_init_with_attr(self):
        self.assertEqual(self.view.view_template,'vote/create_voting.html')
        self.assertEqual(self.view.alternative_view_name, 'vote:overview')
