from django.views import View
from django.shortcuts import render

from information.forms.navbar_search_form import NavbarSearchForm


class EditView(View):
    """Edit voting view class.
    """

    def __init__(self):
        super().__init__()
        self.render = 'vote/edit.html'
        self.context = {
            'navbar_search_form': NavbarSearchForm(),
        }

    def get(self, request):
        """Home page view method on client get request.
        """
        return render(request, self.render, self.context)
