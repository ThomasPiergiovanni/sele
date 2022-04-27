"""Test vote emulation module.
"""
from datetime import datetime

from django.utils import timezone

from vote.models.vote import Vote
from vote.models.voting import Voting
from vote.models.voting_method import VotingMethod

class VoteEmulation():
    """Test collectivity class.
    """
    def __init__(self):
        pass

    def emulate_voting_method(self):
        """
        """
        VotingMethod.objects.create(id=1, name="Majoritaire", percentage=0.5)
        VotingMethod.objects.create(id=2, name="Consensus75",  percentage=0.75)
    
    def emulate_voting(self):
        """
        """
        Voting.objects.create(
            id=1,
            question="Voulez-vous créer une demande de nettoyage?",
            description=(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
                " Sed non risus. Suspendisse lectus tortor, dignissim sit"
                " amet, adipiscing nec, ultricies sed, dolor. Cras elementum"
                " ultrices diam. Maecenas ligula massa, varius a, semper"
                " congue, euismod non, mi. Proin porttitor, orci nec nonummy"
                " molestie, enim est eleifend mi, non fermentum diam nisl sit"
                " amet erat. Duis semper. Duis arcu massa, scelerisque vitae,"
                " consequat in, pretium a, enim. Pellentesque congue"
            ),
            creation_date = "2022-01-10",
            opening_date = "2022-01-11",
            closure_date = "2022-01-19",
            voting_method_id=1,
            voting_custom_user_id=1
        )
        Voting.objects.create(
            id=2,
            question="Voulez-vous créer une offre commune d'aide au devoir?",
            description=(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
                " Sed non risus. Suspendisse lectus tortor, dignissim sit"
                " amet, adipiscing nec, ultricies sed, dolor. Cras elementum"
                " ultrices diam. Maecenas ligula massa, varius a, semper"
                " congue, euismod non, mi. Proin porttitor, orci nec nonummy"
                " molestie, enim est eleifend mi, non fermentum diam nisl sit"
                " amet erat. Duis semper. Duis arcu massa, scelerisque vitae,"
                " consequat in, pretium a, enim. Pellentesque congue"
            ),
            creation_date = "2022-01-20",
            opening_date = "2022-01-21",
            closure_date = "2022-01-29",
            voting_method_id=2,
            voting_custom_user_id=2
        )
        Voting.objects.create(
            id=3,
            question="Voulez-vous créer une demande de python?",
            description=(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
                " Sed non risus. Suspendisse lectus tortor, dignissim sit"
                " amet, adipiscing nec, ultricies sed, dolor. Cras elementum"
                " ultrices diam. Maecenas ligula massa, varius a, semper"
                " congue, euismod non, mi. Proin porttitor, orci nec nonummy"
                " molestie, enim est eleifend mi, non fermentum diam nisl sit"
                " amet erat. Duis semper. Duis arcu massa, scelerisque vitae,"
                " consequat in, pretium a, enim. Pellentesque congue"
            ),
            creation_date = "2022-01-30",
            opening_date = "2022-01-30",
            closure_date = "2022-02-28",
            voting_method_id=2,
            voting_custom_user_id=1
        )

    def emulate_vote(self):
        """
        """
        Vote.objects.create(
            id=1,
            choice=True,
            creation_date=datetime(
                2022, 1, 20, 15, 56, 22, tzinfo=timezone.utc
            ), 
            vote_voting_id=1,
            vote_custom_user_id=1,
        ),
        Vote.objects.create(
            id=2,
            choice=False,
            creation_date=datetime(
                2022, 1, 20, 17, 10, 38, tzinfo=timezone.utc
            ), 
            vote_voting_id=1,
            vote_custom_user_id=2,
        )
