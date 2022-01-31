from django.db import models

from authentication.models import CustomUser


class Question(models.Model):
    """Question class model
    """
    question = models.CharField(max_length=256, unique=False)
    answer = models.TextField(max_length=1000)
    custom_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
