"""Create vote view module
"""
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import redirect, render

from vote.management.engine.manager import Manager
from vote.models.voting import Voting
from vote.models.vote import Vote


class CreateVoteView(LoginRequiredMixin, View):
    """CreateVoteView class.
    """
    login_url = '/authentication/login/'
    redirect_field_name = None

    def __init__(self):
        super().__init__()
        self.manager = Manager()
        self.view_template = 'vote/create_vote.html'
        self.alternative_one_view_name = 'vote:read_voting'
        self.context = {
            'voting': None,
        }
        self.msg_already_voted = "Vous avez déja voté"
        self.msg_post_success = "A voté!"
    
    def get(self, request, id_voting):
        """Create vote view method on client get request.
        """
        voting = Voting.objects.get(pk=id_voting)
        vote = Vote.objects.filter(
            vote_voting__exact=id_voting,
            vote_custom_user__exact=request.user.id
        )
        if len(vote) == 0:
            self.context['voting'] = voting
            return render(request, self.view_template, self.context)
        else:
            messages.add_message(
                request, messages.ERROR, self.msg_already_voted
            )
            return redirect(self.alternative_one_view_name, id_voting)

    def post(self, request, id_voting):
        """Create vote view method on client post request.
        """
        vote = Vote.objects.filter(
            vote_voting__exact=id_voting,
            vote_custom_user__exact=request.user.id
        )
        if len(vote) == 0:
            self.manager.create_vote(request, id_voting) 
            messages.add_message(
                request, messages.SUCCESS, self.msg_post_success
            )
            return redirect(self.alternative_one_view_name, id_voting)

        else:
            messages.add_message(
                request, messages.ERROR, self.msg_already_voted
            )
            return redirect(self.alternative_one_view_name, id_voting)
