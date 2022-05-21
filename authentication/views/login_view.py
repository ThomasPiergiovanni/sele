"""LoginView module.
"""
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View

from authentication.forms.login_form import LoginForm


class LoginView(View):
    """LoginView class.
    """

    def __init__(self):
        super().__init__()
        self.context = {
            'form': LoginForm(),
        }
        self.view_template = 'authentication/login.html'
        self.post_view_name = 'information:home'

    def get(self, request):
        """LoginView method on client get request.
        """
        return render(request, self.view_template, self.context)

    def post(self, request):
        """LoginView method on client post request.
        """
        logout(request)
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                email=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                messages.add_message(
                    request, messages.SUCCESS, "Authentification réussie",
                )
                return redirect(self.post_view_name)
        return render(request, self.view_template, {'form': form})
