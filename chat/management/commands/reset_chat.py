# pylint: disable=R0201, W0106
""" DB management command
"""
from django.core.management.base import BaseCommand

from config.settings.data.enumeration import DISCUSSIONS_TYPE
from chat.models.comment import Comment
from chat.models.discussion import Discussion
from chat.models.discussion_type import DiscussionType


class Command(BaseCommand):
    """Reset chat data from DB.
    """

    help = "Reset chat data from DB"

    def __init__(self):
        super().__init__()

    def handle(self, *args, **options):
        """Method that reset Comment, Discussion and DiscussionType
        data from DB.
        """
        self.__drop_discussion_type(),
        self.__insert_discussion_type(),
        self.__drop_comment(),
        self.__drop_discussion(),

    def __drop_discussion_type(self):
        """Method thats drop DiscussionType from DB.
        """
        self.__drop_objects(DiscussionType)

    def __drop_objects(self, object_class):
        """Method thats drop objects entities from DB.
        """
        objects = object_class.objects.all()
        objects.delete()

    def __insert_discussion_type(self):
        """Method that insert DiscussionType enumeration into DB.
        """
        enumerations = DISCUSSIONS_TYPE
        counter = 1
        for enumeration in enumerations:
            discussion_type = DiscussionType(id=counter, name=enumeration)
            discussion_type.save()
            counter += 1

    def __drop_comment(self):
        """Method thats drop Comment from DB.
        """
        self.__drop_objects(Comment)

    def __drop_discussion(self):
        """Method thats drop Discussion from DB.
        """
        self.__drop_objects(Discussion)
