from django.views import View
from django.shortcuts import render

from information.forms.navbar_search_form import NavbarSearchForm
from vote.forms.add_voting import AddVoting
from vote.management.engine.manager import Manager


class AddView(View):
    """Add chat view class.
    """

    def __init__(self):
        super().__init__()
        self.render = 'vote/add.html'
        self.context = {
            'add_voting': AddVoting(),
        }

    def get(self, request):
        """Home page view method on client get request.
        """
        return render(request, self.render, self.context)
