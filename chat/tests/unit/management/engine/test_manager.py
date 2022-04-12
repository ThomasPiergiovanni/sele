"""Test manager module.
"""
from datetime import date, timedelta

from django.contrib.auth import authenticate
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import RequestFactory, TestCase

from authentication.models import CustomUser
from authentication.tests.emulation.authentication_emulation import (
    AuthenticationEmulation
)

from chat.forms.discussion_form import DiscussionForm
from chat.management.engine.manager import Manager
from chat.models.discussion import Discussion


class TestManager(TestCase):
    """Test Manager  class.
    """
    def setUp(self):
        self.auth_emulation = AuthenticationEmulation()
        self.manager = Manager()

    def test_create_voting_with_voting_instance(self):
        self.auth_emulation.emulate_custom_user()
        form_data = {
            'subject': 'Le sujet est',
        }
        form = DiscussionForm(data=form_data)
        form.is_valid()
        custom_user = CustomUser.objects.get(pk=1)
        self.manager.create_discussion(form, custom_user)
        self.assertEqual(Discussion.objects.all().last().subject,'Le sujet est')
        self.assertEqual(
            Discussion.objects.all().last().creation_date,
            date.today()
        )
