from django.db import models


class Question(models.Model):
    """Question class model
    """
    question = models.CharField(max_length=256, unique=False)
    answer = models.TextField(max_length=1000)
