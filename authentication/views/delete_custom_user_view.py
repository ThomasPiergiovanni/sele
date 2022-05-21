"""DeleteCustomUserview module.
"""
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import render, redirect

from authentication.models import CustomUser
from authentication.views.generic_authentication_view import (
    GenericAuthenticationView
)


class DeleteCustomUserView(GenericAuthenticationView):
    """DeleteCustomUserview class.
    """

    def __init__(self):
        super().__init__()
        self.context = {}
        self.view_template = 'authentication/delete_custom_user.html'
        self.alternative_view_name = 'information:home'

    def get(self, request):
        """DeleteCustomUserview method on client get request.
        """
        return render(request, self.view_template, self.context)

    def post(self, request):
        """DeleteCustomUserview method on client post request.
        """
        custom_user = CustomUser.objects.get(pk=request.user.id)
        custom_user.delete()
        messages.add_message(
            request, messages.SUCCESS, "Suppression de compte réussie"
        )
        logout(request)
        return redirect(self.alternative_view_name)
