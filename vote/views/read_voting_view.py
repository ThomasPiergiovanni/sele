# pylint: disable=E1101
"""ReadVotingView module.
"""
from django.shortcuts import render

from vote.models import Voting
from vote.views.generic_vote_view import GenericVoteView


class ReadVotingView(GenericVoteView):
    """ReadVotingView class.
    """

    def __init__(self):
        super().__init__()
        self.view_template = 'vote/read_voting.html'
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
