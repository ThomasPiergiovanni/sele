""" DB management command
"""
from django.core.management.base import BaseCommand

from authentication.models import CustomUser


class Command(BaseCommand):
    """ Reset vote data from DB. Use it with
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
        self.__drop_custom_user()


    def __drop_custom_user(self):
        """Method thats drop voting method objects from DB
        """
        self.__drop_objects(CustomUser)

    def __drop_objects(self, object_class):
        """Manager method thats drop objects entities from DB
        """
        objects = object_class.objects.all()
        objects.delete()
