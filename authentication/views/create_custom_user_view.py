from queue import Empty
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views import View
from django.shortcuts import render
from django.urls import reverse

from authentication.forms.create_custom_user_form import CreateCustomUserForm
from authentication.management.engine.manager import Manager


class CreateCustomUser(View):
    """CreateCustomUser view class.
    """

    def __init__(self):
        super().__init__()
        self.context = {
            'form': CreateCustomUserForm(),
        }
        self.get_success_template = 'authentication/create_custom_user.html'
        self.post_success_template = 'information:home'
        self.post_fail_template = 'authentication:create_custom_user'

    def get(self, request):
        """Home page view method on client get request.
        """
        return render(request, self.get_success_template, self.context)

    def post(self, request):
        """Create custom user page view method on client post request. Create
        CustomUser into the DB. After Voting creation, user is redirect to
         voting overview page.
        """
        form = CreateCustomUserForm(request.POST)

        if form.is_valid():
            collectivity = Manager().check_collectivity(
                form.cleaned_data['postal_code'],
                form.cleaned_data['collectivity']
            )
            if collectivity:
                Manager().create_custom_user(request, form, collectivity)
                return HttpResponseRedirect(reverse(self.post_success_template))
            else:
                messages.add_message(
                    request,
                    messages.ERROR,
                    "Le couple Code postal et Ville n'est pas valide.",
                )

                return render(request, self.get_success_template, {'form': form})


        else:
            return render(request, self.get_success_template, {'form': form})

