from vote.models.vote import Vote
from vote.models.voting import Voting
from vote.models.voting_method import VotingMethod


class Manager():
    """Manager manager class.
    """
    def __init__(self):
        pass

    def create_choice_list(self):
        choice_list =[]
        for choice in VotingMethod.objects.all():
            choice_list.append((choice.id, choice.name))
        return choice_list