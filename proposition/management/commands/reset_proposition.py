# pylint: disable=E1101,R0201
""" DB management command
"""
from django.core.management.base import BaseCommand

from proposition.models.kind import Kind


class Command(BaseCommand):
    """ Reset proposition data from DB. Use it with
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
        self.__drop_kind(),
        self.__insert_kind()


    def __drop_kind(self):
        """Method thats drop kind objects from DB
        """
        self.__drop_objects(Kind)

    def __drop_objects(self, object_class):
        """Manager method thats drop objects entities from DB
        """
        objects = object_class.objects.all()
        objects.delete()

    def __insert_kind(self):
        """Method that insert kind enumetration objects into DB.
        """
        enumerations = ["Demande", "Offre"]
        for enumeration in enumerations:
            kind = Kind(name=enumeration)
            kind.save()
