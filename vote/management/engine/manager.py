from datetime import date
from vote.models.voting import Voting
from vote.models.voting_method import VotingMethod


class Manager():
    """Manager manager class.
    """
    def __init__(self):
        pass
    
    def create_voting(self, form):
        """Method for creating Voting instances into DB
        """
        Voting(
            question=form.cleaned_data['question'],
            description=form.cleaned_data['description'],
            creation_date=date.today(),
            opening_date=form.cleaned_data['opening_date'],
            closure_date=form.cleaned_data['closure_date'],
            voting_method=form.cleaned_data['voting_method']
        ).save()