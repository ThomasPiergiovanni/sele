from django.views import View
from django.shortcuts import render

from collectivity.management.engine.manager import Manager
from information.forms.navbar_search_form import NavbarSearchForm


class EditView(View):
    """Edit collectivity view class.
    """

    def __init__(self):
        super().__init__()
        self.render = ''
        self.context = {
            'navbar_search_form': NavbarSearchForm(),
        }

    def get(self, request):
        """Home page view method on client get request.
        """
        return render(request, self.render, self.context)
