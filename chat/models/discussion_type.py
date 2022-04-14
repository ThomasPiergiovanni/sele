from django.db import models


class DiscussionType(models.Model):
    """Discussion type class model
    """
    name = models.CharField(max_length=32, unique=True, default=None)

    def __str__(self):
        return self.name
