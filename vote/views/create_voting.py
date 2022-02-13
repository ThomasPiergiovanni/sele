"""CreateVoting view module
"""
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views import View
from django.shortcuts import render
from django.urls import reverse

from vote.forms.voting_form import VotingForm
from vote.management.engine.manager import Manager


class CreateVoting(View):
    """CreateVoting view class.
    """

    def __init__(self):
        super().__init__()
        self.context = {
            'voting_form': VotingForm(),
        }
        self.get_success_template = 'vote/create_voting.html'
        self.post_success_template = 'vote:overview'
        self.post_fail_template = 'vote:create_voting'

    def get(self, request):
        """Voting page view method on user get request.
        """
        return render(request, self.get_success_template, self.context)
    
    def post(self, request):
        """Voting page view method on client post request. Create voting
        into the DB. After Voting creation, user is redirect to voting 
        overview page.
        """
        form = VotingForm(request.POST)
        if form.is_valid():
            Manager().create_voting(form)
            return HttpResponseRedirect(reverse(self.post_success_template))
        else:
            messages.add_message(
                request, messages.ERROR, (
                    "Une ou plusieurs informations a été incorrectement"
                    "saisie Veuiller ressaisir le information!"
                )
            )
            return HttpResponseRedirect(reverse(self.post_fail_template))

