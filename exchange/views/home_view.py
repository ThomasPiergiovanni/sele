from django.views import View
from django.shortcuts import render

from exchange.forms.navbar_search_form import NavbarSearchForm


class HomeView(View):
    """Home view class.
    """
    def __init__(self):
        super().__init__()
        self.render = 'exchange/home.html'
        self.context = {
            'navbar_search_form': NavbarSearchForm()
        }

    def get(self, request):
        """Home page view method on client get request.
        """
        return render(request, self.render, self.context)
