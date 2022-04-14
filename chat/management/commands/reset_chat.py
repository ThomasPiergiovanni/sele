# pylint: disable=E1101,R0201
""" DB management command
"""
from django.core.management.base import BaseCommand

from config.settings.data.enumeration import DISCUSSIONS_TYPE
from chat.models.discussion_type import DiscussionType



class Command(BaseCommand):
    """ Reset chat data from DB. Use it with
    option --all to reset all users as well. This including superuser
    """
    help = "Reset proposition info from DB. Use it with"\
        " option --all to reset all users as well. This including superuser"

    def __init__(self):
        super().__init__()

    def add_arguments(self, parser):
        parser.add_argument(
            '--all',
            action='store_true',
            help='Reset all DB tables values including users and superusers'
        )

    def handle(self, *args, **options):
        self.__drop_discussion_type(),
        self.__insert_discussion_type(),

    def __drop_discussion_type(self):
        """Method thats drop kind objects from DB
        """
        self.__drop_objects(DiscussionType)

    def __drop_objects(self, object_class):
        """Manager method thats drop objects entities from DB
        """
        objects = object_class.objects.all()
        objects.delete()

    def __insert_discussion_type(self):
        """Method that insert kind enumetration objects into DB.
        """
        enumerations = DISCUSSIONS_TYPE
        for enumeration in enumerations:
            discussion_type = DiscussionType(name=enumeration)
            discussion_type.save()
