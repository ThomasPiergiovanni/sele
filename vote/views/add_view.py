from django.views import View
from django.shortcuts import render

from vote.forms.voting_form import VotingForm
from vote.management.engine.manager import Manager


class AddView(View):
    """Add chat view class.
    """

    def __init__(self):
        super().__init__()
        self.render = 'vote/add.html'
        self.context = {
            'voting_form': VotingForm(),
        }

    def get(self, request):
        """Home page view method on client get request.
        """
        return render(request, self.render, self.context)
