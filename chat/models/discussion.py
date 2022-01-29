from django.db import models


# class Discussion(models.Model):
#     """Discussion class model
#     """
#     subject = models.CharField(max_length=256, unique=False)
#     creation_date =  models.DateTimeField()
#     user = models.ForeignKey(CustomUser, models.CASCADE)
#     relation_custom_user = models.ManyToManyField(
#         CustomUser, through='Comment'
#     )