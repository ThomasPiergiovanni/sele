from django.db import models

from authentication.models import CustomUser


class Discussion(models.Model):
    """Discussion class model
    """
    subject = models.CharField(max_length=256, unique=False)
    creation_date =  models.DateTimeField()
    discussion_custom_user = models.ForeignKey(
        CustomUser, models.CASCADE, related_name="discussion_custom_user"
    )
    comments = models.ManyToManyField(
        CustomUser, through='Comment',  related_name="comments"
    )