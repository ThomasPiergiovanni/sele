from django.db import models

from authentication.models import CustomUser
from chat.models.discussion import Discussion

class Comment(models.Model):
    """Comment class model
    """
    comment = models.CharField(max_length=256)
    creation_date =  models.DateTimeField()
    custom_user = models.ForeignKey(CustomUser, models.CASCADE)
    discussion = models.ForeignKey(Discussion, models.CASCADE)
