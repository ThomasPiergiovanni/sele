from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render

from vote.management.engine.manager import Manager
from vote.models.voting import Voting


class DetailedVotingView(LoginRequiredMixin, View):
    """DetailedVotingView class.
    """
    login_url = '/authentication/login/'
    redirect_field_name = None

    def __init__(self):
        super().__init__()
        self.manager = Manager()
        self.view_template = 'vote/detailed_voting.html'
        self.context = {
            'voting': None,
            'voting_operation': None, 
            'voting_result': None,                       
            'voting_status': None
        }
        self.msg_unauthenticated = "Authentification requise"
    
    def get(self, request, id_voting):
        """Detailed voting view method on client get request.
        """
        voting = Voting.objects.get(pk=id_voting)
        self.context = self.manager.set_context(
            self.context, voting, 'read'
        )
        return render(request, self.view_template, self.context)

