""" DB management command
"""
from django.core.management.base import BaseCommand

from config.settings.data.enumeration import VOTING_METHODS
from vote.models.vote import Vote
from vote.models.voting import Voting
from vote.models.voting_method import VotingMethod


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
        self.__drop_voting_method(),
        self.__insert_voting_method(),
        self.__drop_voting(),
        self.__drop_vote(),

    def __drop_voting_method(self):
        """Method thats drop voting method objects from DB
        """
        self.__drop_objects(VotingMethod)

    def __drop_objects(self, object_class):
        """Manager method thats drop objects entities from DB
        """
        objects = object_class.objects.all()
        objects.delete()

    def __insert_voting_method(self):
        """Method that insert voting method enumetration objects into DB.
        """
        enumerations = VOTING_METHODS
        for enumeration in enumerations:
            voting_method = VotingMethod(
                name=enumeration['name'], percentage=enumeration['percentage']
            )
            voting_method.save()

    def __drop_voting(self):
        """Method thats drop voting method objects from DB
        """
        self.__drop_objects(Voting)
    
    def __drop_vote(self):
        """Method thats drop vote method objects from DB
        """
        self.__drop_objects(Vote)
