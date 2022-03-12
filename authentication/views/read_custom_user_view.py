"""Read custom user view module
"""
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from authentication.forms.edit_custom_user_form import EditCustomUserForm
from authentication.management.engine.manager import Manager
from authentication.models import CustomUser


class ReadCustomUserView(View):
    """ReadCustomUserview class.
    """

    def __init__(self):
        super().__init__()
        self.context = {}
        self.view_template= 'authentication/read_custom_user.html'
        self.alternative_view_name = 'information:home'

    def get(self, request):
        """Read CustomUser view method on client get request.
        """
        if request.user.is_authenticated:
            return render(request, self.view_template, self.context)
        else:
            messages.add_message(
                    request,
                    messages.ERROR,
                    "Authentification requise",
                )
            return redirect(self.alternative_view_name)
