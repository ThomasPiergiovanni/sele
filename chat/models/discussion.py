from django.db import models

from authentication.models import CustomUser
from chat.models.discussion_type import DiscussionType


class Discussion(models.Model):
    """Discussion class model
    """
    subject = models.CharField(max_length=256, unique=False)
    creation_date =  models.DateField(null=False)
    discussion_custom_user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="discussion_custom_user"
    )
    discussion_discussion_type = models.ForeignKey(
        DiscussionType,
        on_delete=models.CASCADE,
        related_name="discussion_discussion_type",
        null=True
    )
    comments = models.ManyToManyField(
        CustomUser, through='Comment',  related_name="comments"
    )