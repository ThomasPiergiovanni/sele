from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View

from authentication.forms.login_form import LoginForm


class LoginView(View):
    """CreateCustomUserview class.
    """

    def __init__(self):
        super().__init__()
        self.context = {
            'form': LoginForm(),
        }
        self.nominal_template = 'authentication/login.html'
        self.post_nominal_view_name = 'information:home'

    def get(self, request):
        """Login page view method on client get request.
        """
        return render(request, self.nominal_template, self.context)

    def post(self, request):
        """Login page view method on client post request. Authenticate custom
        user into session. After login, user is redirect to
        home page.
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
                    request,
                    messages.SUCCESS,
                    "Authentification réussie",
                )
                return redirect(self.post_nominal_view_name)
        return render(request, self.nominal_template, {'form': form})

