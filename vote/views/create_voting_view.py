"""CreateVotingView module.
"""
from django.contrib import messages
from django.shortcuts import redirect, render

from vote.forms.voting_form import VotingForm
from vote.views.generic_vote_view import GenericVoteView


class CreateVotingView(GenericVoteView):
    """CreateVotingView class.
    """

    def __init__(self):
        super().__init__()
        self.context = {
            'form': VotingForm(),
        }
        self.view_template = 'vote/create_voting.html'
        self.alternative_view_name = 'information:home'
        self.post_view_name = 'vote:collectivity_votings'

    def get(self, request):
        """CreateVotingView method on user get request.
        """
        return render(request, self.view_template, self.context)

    def post(self, request):
        """CreateVotingView method on client post request.
        """
        form = VotingForm(request.POST)
        if form.is_valid():
            self.manager.create_voting(form, request.user)
            messages.add_message(
                request, messages.SUCCESS, "Création réussie",
            )
            return redirect(self.post_view_name)
        self.context['form'] = form
        return render(request, self.view_template, self.context)
