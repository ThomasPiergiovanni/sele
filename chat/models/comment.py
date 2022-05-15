"""Comment model module.
"""
from django.db import models

from authentication.models import CustomUser


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
        "Discussion",
        on_delete=models.CASCADE,
        null=False,
        related_name="comment_discussion"
    )
