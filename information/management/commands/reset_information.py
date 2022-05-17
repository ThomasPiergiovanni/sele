# pylint: disable=R0201
"""Management command module to reset Information data from DB.
"""
from django.core.management.base import BaseCommand

from information.models.question import Question


class Command(BaseCommand):
    """ Reset Information data from DB.
    """

    help = "Reset Information data from DB.. Use it with"

    def __init__(self):
        super().__init__()

    def handle(self, *args, **options):
        """Method that reset Question data from DB.
        """
        self.__drop_question()

    def __drop_question(self):
        """Method thats drop Question from DB
        """
        self.__drop_objects(Question)

    def __drop_objects(self, object_class):
        """Method thats drop objects entities from DB.
        """
        objects = object_class.objects.all()
        objects.delete()
