# pylint: disable=E1101,R0201,W0106
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
from proposition.models.rating import Rating
from proposition.models.status import Status


class Command(BaseCommand):
    """ Reset proposition data from DB.
    """

    help = "Reset proposition info from DB."

    def __init__(self):
        super().__init__()

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
        self.__insert_rating()

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
        counter = 1
        for enumeration in enumerations:
            kind = Kind(id=counter, name=enumeration)
            kind.save()
            counter += 1

    def __drop_category(self):
        """Method that drop category objects from DB
        """
        self.__drop_objects(Category)

    def __insert_category(self):
        """Method that insert category enumetration objects into DB.
        """
        enumerations = CATEGORIES
        counter = 1
        for enumeration in enumerations:
            category = Category(id=counter, name=enumeration)
            category.save()
            counter += 1

    def __drop_creator_type(self):
        """Method that drops status objects from DB
        """
        self.__drop_objects(CreatorType)

    def __insert_creator_type(self):
        """Method that insert domain enumetration objects into DB.
        """
        enumerations = CREATOR_TYPES
        counter = 1
        for enumeration in enumerations:
            creator_type = CreatorType(id=counter, name=enumeration)
            creator_type.save()
            counter += 1

    def __drop_domain(self):
        """Method that drops domain objects from DB
        """
        self.__drop_objects(Domain)

    def __insert_domain(self):
        """Method that insert domain enumetration objects into DB.
        """
        enumerations = DOMAINS
        counter = 1
        for enumeration in enumerations:
            domain = Domain(id=counter, name=enumeration)
            domain.save()
            counter += 1

    def __drop_status(self):
        """Method that drops status objects from DB
        """
        self.__drop_objects(Status)

    def __insert_status(self):
        """Method that insert domain enumetration objects into DB.
        """
        enumerations = STATUSES
        counter = 1
        for enumeration in enumerations:
            status = Status(id=counter, name=enumeration)
            status.save()
            counter += 1

    def __drop_rating(self):
        """Method that drops status objects from DB
        """
        self.__drop_objects(Rating)

    def __insert_rating(self):
        """Method that insert domain enumetration objects into DB.
        """
        enumerations = RATINGS
        counter = 1
        for enumeration in enumerations:
            rating = Rating(id=counter, rate=enumeration)
            rating.save()
            counter += 1
