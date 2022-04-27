"""Test chat emulation module.
"""
from datetime import date, datetime
from django.utils import timezone

from authentication.tests.emulation.authentication_emulation import (
    AuthenticationEmulation
)
from chat.models.discussion import Discussion
from chat.models.discussion_type import DiscussionType
from chat.models.comment import Comment


class ChatEmulation():
    """Test ChatEmulation class.
    """
    def __init__(self):
        self.auth_emulation = AuthenticationEmulation()

    def emulate_discussion(self):
        """
        """
        # self.auth_emulation.emulate_custom_user()
        self.emulate_discussion_type()
        Discussion.objects.create(
            id=1,
            subject="Sujet est HTML",
            creation_date=date(2022, 1, 20),
            discussion_custom_user_id=1,
            discussion_discussion_type_id = None
        ),
        Discussion.objects.create(
            id=2,
            subject="Sujet est CSS",
            creation_date=date(2022, 1, 21),
            discussion_custom_user_id=1,
            discussion_discussion_type_id = None
        ),
        Discussion.objects.create(
            id=3,
            subject="Sujet est JS",
            creation_date=date(2022, 1, 22),
            discussion_custom_user_id=3,
            discussion_discussion_type_id = None
        )
        Discussion.objects.create(
            id=4,
            subject="DCours1",
            creation_date=date(2022, 1, 1),
            discussion_custom_user_id=1,
            discussion_discussion_type_id = 1
        )

    def emulate_comment(self):
        """
        """
        # self.emulate_discussion()
        timezone.now()
        Comment.objects.create(
            id=1,
            comment="Comment vas-tu?",
            creation_date=datetime(
                2022, 1, 20, 15, 56, 22, tzinfo=timezone.utc
            ),
            comment_custom_user_id=1,
            comment_discussion_id=1
        ),
        Comment.objects.create(
            id=2,
            comment="Ca vas et toi?",
            creation_date=datetime(
                2022, 1, 20, 17, 10, 38, tzinfo=timezone.utc
            ),
            comment_custom_user_id=3,
            comment_discussion_id=1
        )

    def emulate_discussion_type(self):
        """
        """
        DiscussionType.objects.create(
            id=1,
            name="Proposition"
        ),
        DiscussionType.objects.create(
            id=2,
            name="Votation"
        )
