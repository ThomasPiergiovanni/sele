# pylint: disable=E0307
"""Chat models module.
"""
from django.db import models

from authentication.models import CustomUser


class DiscussionType(models.Model):
    """Discussion type model class.
    """

    name = models.CharField(max_length=32, unique=True, default=None)

    def __str__(self):
        return self.name


class Discussion(models.Model):
    """Discussion model class.
    """

    subject = models.CharField(max_length=256, unique=False)
    creation_date = models.DateField(null=False)
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
        CustomUser, through="Comment",  related_name="comments"
    )


class Comment(models.Model):
    """Comment model class.
    """

    comment = models.CharField(max_length=256)
    creation_date = models.DateTimeField()
    comment_custom_user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        null=False,
        related_name="comment_custom_user"
    )
    comment_discussion = models.ForeignKey(
        Discussion,
        on_delete=models.CASCADE,
        null=False,
        related_name="comment_discussion"
    )
