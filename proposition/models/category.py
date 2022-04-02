from django.db import models


class Category(models.Model):
    """Category class model
    """
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name
