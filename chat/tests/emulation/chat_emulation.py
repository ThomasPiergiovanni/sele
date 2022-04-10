"""Test vote emulation module.
"""
from datetime import date

from django.utils import timezone

from authentication.tests.emulation.authentication_emulation import (
    AuthenticationEmulation
)
from chat.models.discussion import Discussion
from chat.models.comment import Comment

class ChatEmulation():
    """Test ChatEmulation class.
    """
    def __init__(self):
        self.auth_emulation = AuthenticationEmulation()

    def emulate_discussion(self):
        """
        """
        self.auth_emulation.emulate_custom_user()
        Discussion.objects.create(
            id=1,
            subject="Sujet est HTML",
            creation_date=date(2022, 1, 20),
            discussion_custom_user=1
        ),
        Discussion.objects.create(
            id=2,
            subject="Sujet est CSS",
            creation_date=date(2022, 1, 21),
            discussion_custom_user=1
        ),
        Discussion.objects.create(
            id=3,
            subject="Sujet est CSS",
            creation_date=date(2022, 1, 22),
            discussion_custom_user=3
        ),
