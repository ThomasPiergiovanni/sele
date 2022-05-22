# pylint: disable=R0201, W0106
"""Management command module to reset Vote data from DB.
"""
from django.core.management.base import BaseCommand

from config.settings.data.enumeration import VOTING_METHODS
from vote.models import Vote, Voting, VotingMethod



class Command(BaseCommand):
    """ Reset vote data from DB.
    """

    help = "Reset proposition info from DB."

    def __init__(self):
        super().__init__()

    def handle(self, *args, **options):
        """Method that reset Vote, Voting and VotingMethod
        data from DB.
        """
        self.__drop_voting_method(),
        self.__insert_voting_method(),
        self.__drop_voting(),
        self.__drop_vote(),

    def __drop_voting_method(self):
        """Method that drop VotingMethod from DB.
        """
        self.__drop_objects(VotingMethod)

    def __drop_objects(self, object_class):
        """Method that drop objects entities from DB.
        """
        objects = object_class.objects.all()
        objects.delete()

    def __insert_voting_method(self):
        """Method that insert VotingMethod from DB.
        """
        enumerations = VOTING_METHODS
        counter = 1
        for enumeration in enumerations:
            voting_method = VotingMethod(
                id=counter,
                name=enumeration['name'], percentage=enumeration['percentage']
            )
            voting_method.save()
            counter += 1

    def __drop_voting(self):
        """Method that drop Voting from DB.
        """
        self.__drop_objects(Voting)

    def __drop_vote(self):
        """Method that drop Vote from DB.
        """
        self.__drop_objects(Vote)
