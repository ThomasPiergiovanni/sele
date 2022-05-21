"""CreateCustomUserview module.
"""
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from authentication.forms.create_custom_user_form import CreateCustomUserForm
from authentication.management.engine.manager import Manager


class CreateCustomUserView(View):
    """CreateCustomUserview class.
    """

    def __init__(self):
        super().__init__()
        self.manager = Manager()
        self.context = {
            'form': CreateCustomUserForm(),
        }
        self.view_template = 'authentication/create_custom_user.html'
        self.post_view_name = 'authentication:login'

    def get(self, request):
        """CreateCustomUserview view method on client get request.
        """
        return render(request, self.view_template, self.context)

    def post(self, request):
        """CreateCustomUserview method on client post request.
        """
        form = CreateCustomUserForm(request.POST)
        if form.is_valid():
            collectivity = Manager().check_collectivity(
                form.cleaned_data['postal_code'],
                form.cleaned_data['collectivity']
            )
            if collectivity:
                self.manager.create_custom_user(form, collectivity)
                self.manager.activate_collectivity(collectivity)
                messages.add_message(
                    request, messages.SUCCESS, "Création de compte réussie"
                )
                return redirect(self.post_view_name)
            messages.add_message(
                request, messages.ERROR, "Code postal != Ville",
            )
            return render(
                request, self.view_template, {'form': form}
            )
        return render(
            request, self.view_template, {'form': form}
        )
