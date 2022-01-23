from django.views import View
from django.shortcuts import render

from information.forms.navbar_search_form import NavbarSearchForm
from proposition.management.engine.manager import Manager


class AddView(View):
    """Add proposition view class.
    """

    def __init__(self):
        super().__init__()
        self.render = 'proposition/add.html'
        self.context = {
            'navbar_search_form': NavbarSearchForm(),
        }

    def get(self, request):
        """Home page view method on client get request.
        """
        return render(request, self.render, self.context)
