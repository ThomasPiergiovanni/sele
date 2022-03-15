"""Delete voting view module
"""
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
            'voting_operation': None, 
            'voting_result': None,                       
            'voting_status': None
        }
        self.msg_unauthenticated = "Authentification requise"
        self.msg_not_owner = (
            "Le créateur seulement peut supprimer la votation"
        )
        self.msg_post_success = "Suppression de votation réussie"
    
    def get(self, request, id_voting):
        """Delete voting view method on client get request.
        """
        if request.user.is_authenticated:
            voting = Voting.objects.get(pk=id_voting)
            custom_user = CustomUser.objects.get(pk=request.user.id)
            if voting.custom_user_id == custom_user.id:
                self.context = self.manager.set_context(
                    self.context, voting
                )
                return render(request, self.view_template, self.context)
            else:
                messages.add_message(
                    request, messages.ERROR, self.msg_not_owner
                )
                return redirect(self.alternative_one_view_name) 
        else:
            messages.add_message(
                request, messages.ERROR, self.msg_unauthenticated
            )
            return redirect(self.alternative_two_view_name)

    def post(self, request, id_voting):
        """Delete voting view method on client post request.
        """
        if request.user.is_authenticated:
            voting = Voting.objects.get(pk=id_voting)
            custom_user = CustomUser.objects.get(pk=request.user.id)
            if voting.custom_user_id == custom_user.id:
                voting.delete()
                messages.add_message(
                    request, messages.SUCCESS, self.msg_post_success
                )
                return redirect(self.alternative_one_view_name)
            else:
                messages.add_message(
                    request, messages.ERROR, self.msg_not_owner
                )
                return redirect(self.alternative_one_view_name)

        else:
            messages.add_message(
                request, messages.ERROR, self.msg_unauthenticated
            )
            return redirect(self.alternative_two_view_name)
