# pylint: disable=R0201
"""Management command module to reset Authentication data from DB.
"""
from django.core.management.base import BaseCommand

from authentication.models import CustomUser


class Command(BaseCommand):
    """ Reset authentication data from DB.
    """
    help = "Reset authentication info from DB."

    def __init__(self):
        super().__init__()

    def handle(self, *args, **options):
        """Method that reset CustomUser data from DB.
        """
        self.__drop_custom_user()

    def __drop_custom_user(self):
        """Method thats drop CustomUser from DB.
        """
        self.__drop_objects(CustomUser)

    def __drop_objects(self, object_class):
        """Method thats drop objects entities from DB.
        """
        objects = object_class.objects.all()
        objects.delete()
