from django.views import View
from django.shortcuts import render

from information.forms.navbar_search_form import NavbarSearchForm


class AboutView(View):
    """About view  class.
    """

    def __init__(self):
        super().__init__()
        self.view_template = 'information/about.html'
        self.context = {}

    def get(self, request):
        """Home page view method on client get request.
        """
        return render(request, self.view_template, self.context)
