"""Delete voting view module
"""
from datetime import date

from django.contrib import messages
from django.views import View
from django.shortcuts import redirect, render

from authentication.models import CustomUser
from vote.management.engine.manager import Manager
from vote.models.voting import Voting


class DeleteVotingView(View):
    """DeleteVotingView class.
    """
    def __init__(self):
        super().__init__()
        self.manager = Manager()
        self.view_template = 'vote/detailed_voting.html'
        self.alternative_one_view_name = 'vote:overview'
        self.alternative_two_view_name = 'information:home'
        self.context = {
            'voting': None,
            'voting_status': None,
            'voting_ops': None,
            'voting_result': None
        }
    
    def get(self, request, id_voting):
        """Delete voting view method on client get request.
        """
        if request.user.is_authenticated:
            voting = Voting.objects.get(pk=id_voting)
            custom_user = CustomUser.objects.get(pk=request.user.id)
            if voting.custom_user_id == custom_user.id:
                self.context['voting'] = voting
                # self.context['voting_status'] = 'Ouvert'
                self.context['voting_status'] = (
                    self.manager.get_voting_status(voting)
                )
                self.context['voting_ops'] = 'delete'
                self.context['voting_result'] = '45.3'
                return render(request, self.view_template, self.context)
            else:
                messages.add_message(
                    request, messages.ERROR, "Le crétaeur seulement peut "
                    "supprimer la votation",
                )
                return redirect(self.alternative_one_view_name) 
        else:
            messages.add_message(
                request, messages.ERROR, "Authentification requise",
            )
            return redirect(self.alternative_two_view_name)  
