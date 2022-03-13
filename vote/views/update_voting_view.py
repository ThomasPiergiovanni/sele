"""Update voting view module
"""
from datetime import date

from django.views import View
from django.shortcuts import render
from authentication.models import CustomUser

from vote.forms.voting_form import VotingForm
from vote.management.engine.manager import Manager
from vote.models.voting import Voting


class UpdateVotingView(View):
    """UpdateVoting view class.
    """
    def __init__(self):
        super().__init__()
        self.manager = Manager()
        self.view_template = 'vote/update_voting.html'
        self.alternative_view_name = 'information:home'
        self.post_view_name = 'vote:overview'
        self.context = {
            'form': VotingForm,
            'voting': None
        }
    

    def get(self, request, id_voting):
        """Home page view method on client get request.
        """
        if request.user.is_authenticated:
            voting = Voting.objects.get(pk=id_voting)
            custom_user = CustomUser.objects.get(pk=request.user.id)
            if voting.custom_user_id == custom_user.id:
                print(voting.closure_date)
                form = VotingForm(
                    initial={
                        'question': voting.question,
                        'description': voting.description,
                        'opening_date': voting.opening_date,
                        'closure_date': voting.closure_date,
                        'voting_method' : voting.voting_method
                    }
                )
                self.context['form'] = form
                self.context['voting'] = voting
                return render(request, self.view_template, self.context)
