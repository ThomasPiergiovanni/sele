
"""Delete custom user view module.
"""
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from authentication.forms.edit_custom_user_form import EditCustomUserForm
from authentication.management.engine.manager import Manager
from authentication.models import CustomUser


class DeleteCustomUserView(View):
    """DeleteCustomUserview class.
    """

    def __init__(self):
        super().__init__()
        self.context = {}
        self.view_template= 'authentication/delete_custom_user.html'
        self.alternative_view_name = 'information:home'

    def get(self, request):
        """DeleteCustomUser get method on client request.
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

    def post(self, request):
        """Delete custom user view method on client post request. Delete
        CustomUser into the DB. After deletion, user is redirect to
        home page.
        """
        if request.user.is_authenticated:
            custom_user = CustomUser.objects.get(pk=request.user.id)
            custom_user.delete()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Suppression de compte réussie",
            )
            logout(request)
            return redirect(self.alternative_view_name)
        else:
            messages.add_message(
                    request,
                    messages.ERROR,
                    "Authentification requise",
                )
            return redirect(self.alternative_view_name)

