from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from authentication.forms.login_form import LoginForm
from authentication.management.engine.manager import Manager


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
        """Home page view method on client get request.
        """
        return render(request, self.nominal_template, self.context)

    def post(self, request):
        """Create custom user page view method on client post request. Create
        CustomUser into the DB. After Voting creation, user is redirect to
         voting overview page.
        """
        logout(request)

        form = LoginForm(data=request.POST)
        if form.is_valid():
            print("here")
            user = authenticate(
                email=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect(self.post_nominal_view_name)
        return render(request, self.nominal_template, {'form': form})

