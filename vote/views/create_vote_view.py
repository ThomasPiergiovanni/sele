"""Create vote view module
"""
from django.contrib import messages
from django.views import View
from django.shortcuts import redirect, render

from authentication.models import CustomUser
from vote.management.engine.manager import Manager
from vote.models.voting import Voting
from vote.models.vote import Vote


class CreateVoteView(View):
    """CreateVoteView class.
    """
    def __init__(self):
        super().__init__()
        self.manager = Manager()
        self.view_template = 'vote/create_vote.html'
        self.alternative_one_view_name = 'vote:overview'
        self.alternative_two_view_name = 'information:home'
        self.context = {
            'voting': None,
        }
        self.msg_unauthenticated = "Authentification requise"
        self.msg_already_voted = "Vous avez déja voté"
        self.msg_post_success = "A voté!"
    
    def get(self, request, id_voting):
        """Create vote view method on client get request.
        """
        if request.user.is_authenticated:
            voting = Voting.objects.get(pk=id_voting)
            custom_user = CustomUser.objects.get(pk=request.user.id)
            vote = Vote.objects.filter(
                vote_voting__exact=id_voting,
                vote_custom_user__exact=request.user
            )
            if vote is None:
                self.context = self.manager.set_context(
                    self.context, voting, 'delete'
                )
                return render(request, self.view_template, self.context)
            else:
                messages.add_message(
                    request, messages.ERROR, self.msg_not_owner,
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
            if voting.voting_custom_user_id == custom_user.id:
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
