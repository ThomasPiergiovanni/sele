"""Delete voting view module
"""
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import redirect, render

from authentication.models import CustomUser
from vote.management.engine.manager import Manager
from vote.models.voting import Voting


class DeleteVotingView(LoginRequiredMixin, View):
    """DeleteVotingView class.
    """
    login_url = '/authentication/login/'
    redirect_field_name = None

    def __init__(self):
        super().__init__()
        self.manager = Manager()
        self.view_template = 'vote/delete_voting.html'
        self.alternative_one_view_name = 'vote:collectivity_votings'
        self.context = {
            'voting': None
        }
        self.msg_unauthenticated = "Authentification requise"
        self.msg_not_owner = (
            "Le créateur seulement peut supprimer la votation"
        )
        self.msg_post_success = "Suppression de votation réussie"
    
    def get(self, request, id_voting):
        """Delete voting view method on client get request.
        """
        voting = Voting.objects.get(pk=id_voting)
        if voting.voting_custom_user_id == request.user.id:
            self.context['voting'] = voting
            return render(request, self.view_template, self.context)
        else:
            messages.add_message(
                request, messages.ERROR, self.msg_not_owner,
            )
            return redirect(self.alternative_one_view_name) 

    def post(self, request, id_voting):
        """Delete voting view method on client post request.
        """
        voting = Voting.objects.get(pk=id_voting)
        if voting.voting_custom_user_id == request.user.id:
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
