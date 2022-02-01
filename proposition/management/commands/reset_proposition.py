# pylint: disable=E1101,R0201
""" DB management command
"""
from django.core.management.base import BaseCommand

from config.settings.data.enumeration import (
    CATEGORIES, CREATOR_TYPES, DOMAINS, KINDS, STATUSES, RATINGS
)
from proposition.models.category import Category
from proposition.models.creator_type import CreatorType
from proposition.models.domain import Domain
from proposition.models.kind import Kind
from proposition.models.proposition import Proposition
from proposition.models.rating import Rating
from proposition.models.status import Status


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
        self.__insert_kind(),
        self.__drop_category(),
        self.__insert_category(),
        self.__drop_creator_type(),
        self.__insert_creator_type(),
        self.__drop_domain(),
        self.__insert_domain(),
        self.__drop_status(),
        self.__insert_status(),
        self.__drop_rating(),
        self.__insert_rating(),
        self.__drop_proposition()

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
        enumerations = KINDS
        for enumeration in enumerations:
            kind = Kind(name=enumeration)
            kind.save()

    def __drop_category(self):
        """Method that drop category objects from DB
        """
        self.__drop_objects(Category)

    def __insert_category(self):
        """Method that insert category enumetration objects into DB.
        """
        enumerations = CATEGORIES
        for enumeration in enumerations:
            category = Category(name=enumeration)
            category.save()

    def __drop_creator_type(self):
        """Method that drops status objects from DB
        """
        self.__drop_objects(CreatorType)

    def __insert_creator_type(self):
        """Method that insert domain enumetration objects into DB.
        """
        enumerations = CREATOR_TYPES
        for enumeration in enumerations:
            creator_type = CreatorType(name=enumeration)
            creator_type.save()

    def __drop_domain(self):
        """Method that drops domain objects from DB
        """
        self.__drop_objects(Domain)

    def __insert_domain(self):
        """Method that insert domain enumetration objects into DB.
        """
        enumerations = DOMAINS
        for enumeration in enumerations:
            domain = Domain(name=enumeration)
            domain.save()

    def __drop_status(self):
        """Method that drops status objects from DB
        """
        self.__drop_objects(Status)

    def __insert_status(self):
        """Method that insert domain enumetration objects into DB.
        """
        enumerations = STATUSES
        for enumeration in enumerations:
            status = Status(name=enumeration)
            status.save()

    def __drop_rating(self):
        """Method that drops status objects from DB
        """
        self.__drop_objects(Rating)

    def __insert_rating(self):
        """Method that insert domain enumetration objects into DB.
        """
        enumerations = RATINGS
        for enumeration in enumerations:
            rating = Rating(rate=enumeration)
            rating.save()

    def __drop_proposition(self):
        """Method that drop proposition objects from DB
        """
        self.__drop_objects(Proposition)
