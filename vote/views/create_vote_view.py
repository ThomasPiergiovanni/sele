# pylint: disable=E1101
"""CreateVoteView module.
"""
from django.contrib import messages
from django.shortcuts import redirect, render

from vote.models import Vote, Voting
from vote.views.generic_vote_view import GenericVoteView


class CreateVoteView(GenericVoteView):
    """CreateVoteView class.
    """

    def __init__(self):
        super().__init__()
        self.view_template = 'vote/create_vote.html'
        self.alternative_one_view_name = 'vote:read_voting'
        self.context = {
            'voting': None,
        }
        self.msg_already_voted = "Vous avez déja voté"
        self.msg_post_success = "A voté!"

    def get(self, request, id_voting):
        """CreateVoteView method on client get request.
        """
        voting = Voting.objects.get(pk=id_voting)
        vote = Vote.objects.filter(
            vote_voting__exact=id_voting,
            vote_custom_user__exact=request.user.id
        )
        if len(vote) == 0:
            self.context['voting'] = voting
            return render(request, self.view_template, self.context)
        messages.add_message(
            request, messages.ERROR, self.msg_already_voted
        )
        return redirect(self.alternative_one_view_name, id_voting)

    def post(self, request, id_voting):
        """CreateVoteView method on client post request.
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
        messages.add_message(
            request, messages.ERROR, self.msg_already_voted
        )
        return redirect(self.alternative_one_view_name, id_voting)
