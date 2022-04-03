"""Creat Voting view module
"""
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import redirect, render

from vote.forms.voting_form import VotingForm
from vote.management.engine.manager import Manager


class CreateVotingView(LoginRequiredMixin,View):
    """CreateVotingView class.
    """
    login_url = '/authentication/login/'
    redirect_field_name = None

    def __init__(self):
        super().__init__()
        self.manager =  Manager()
        self.context = {
            'form': VotingForm(),
        }
        self.view_template = 'vote/create_voting.html'
        self.alternative_view_name = 'information:home'
        self.post_view_name = 'vote:collectivity_votings'

    def get(self, request):
        """Create voting view method on user get request.
        """
        return render(request, self.view_template, self.context)           
    
    def post(self, request):
        """Create voting view method on client post request. Create voting
        into the DB. After Voting creation, user is redirect to voting 
        overview page.
        """
        form = VotingForm(request.POST)
        if form.is_valid():
            self.manager.create_voting(form, request.user)
            messages.add_message(
                request, messages.SUCCESS, "Création réussie",
            )
            return redirect(self.post_view_name)
        else:
            self.context['form'] = form
            return render(request, self.view_template, self.context)
