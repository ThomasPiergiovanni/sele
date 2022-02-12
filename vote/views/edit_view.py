from django.views import View
from django.shortcuts import render

from vote.forms.voting_form import VotingForm


class EditView(View):
    """Edit voting view class.
    """

    def __init__(self):
        super().__init__()
        self.render = 'vote/edit.html'
        self.context = {
            'voting_form': VotingForm(data={
                'description': "Bonjour",
                'opening_date': "2022-01-20",
            }),
        }

    def get(self, request):
        """Home page view method on client get request.
        """
        return render(request, self.render, self.context)
