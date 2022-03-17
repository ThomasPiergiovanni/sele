from django.contrib import messages
from django.views import View
from django.shortcuts import redirect, render

from authentication.models import CustomUser
from vote.management.engine.manager import Manager
from vote.models.voting import Voting


class DetailedVotingView(View):
    """DetailedVotingView class.
    """
    def __init__(self):
        super().__init__()
        self.manager = Manager()
        self.view_template = 'vote/detailed_voting.html'
        self.alternative_view_name = 'information:home'
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
        if request.user.is_authenticated:
            voting = Voting.objects.get(pk=id_voting)
            self.context = self.manager.set_context(
                self.context, voting, 'read'
            )
            return render(request, self.view_template, self.context)
        else:
            messages.add_message(
                request, messages.ERROR, self.msg_unauthenticated
            )
            return redirect(self.alternative_view_name)
