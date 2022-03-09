from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from authentication.forms.login_form import LoginForm
from authentication.management.engine.manager import Manager


class LogoutView(View):
    """Logoutview class.
    """

    def __init__(self):
        super().__init__()
        self.context = {}
        self.get_nominal_view_name = 'information:home'

    def get(self, request):
        """Home page view method on client get request.
        """
        logout(request)
        return redirect(self.get_nominal_view_name)
