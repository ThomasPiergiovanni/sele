from django.db import models

from authentication.models import CustomUser


class Discussion(models.Model):
    """Discussion class model
    """
    subject = models.CharField(max_length=256, unique=False)
    creation_date =  models.DateTimeField()
    custom_user = models.ForeignKey(
        CustomUser, models.CASCADE, related_name="custom_user"
    )
    relation_custom_user = models.ManyToManyField(
        CustomUser, through='Comment',  related_name="relation_custom_user"
    )