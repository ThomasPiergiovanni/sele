"""UpdateCustomUserview module.
"""
from django.contrib import messages
from django.shortcuts import render, redirect

from authentication.forms.update_custom_user_form import UpdateCustomUserForm
from authentication.models import CustomUser
from authentication.views.generic_authentication_view import (
    GenericAuthenticationView
)


class UpdateCustomUserView(GenericAuthenticationView):
    """UpdateCustomUserview class.
    """

    def __init__(self):
        super().__init__()
        self.context = {
            'form': UpdateCustomUserForm(),
        }
        self.view_template = 'authentication/update_custom_user.html'
        self.alternative_view_name = 'information:home'

    def get(self, request):
        """UpdateCustomUserview method on client get request.
        """
        custom_user = CustomUser.objects.get(pk=request.user.id)
        form = UpdateCustomUserForm(
            initial={
                'user_name': custom_user.user_name,
                'postal_code': custom_user.collectivity.postal_code,
                'collectivity': custom_user.collectivity.name
            }
        )
        self.context['form'] = form
        return render(request, self.view_template, self.context)

    def post(self, request):
        """UpdateCustomUserview method on client post request.
        """
        form = UpdateCustomUserForm(request.POST)
        if form.is_valid():
            collectivity = self.manager.check_collectivity(
                form.cleaned_data['postal_code'],
                form.cleaned_data['collectivity']
            )
            if collectivity:
                self.manager.update_custom_user(request, form, collectivity)
                self.manager.activate_collectivity(collectivity)
                messages.add_message(
                    request, messages.SUCCESS, "Mise à jours réussie",
                )
                return redirect(self.alternative_view_name)
            messages.add_message(
                request, messages.ERROR, "Code postal != Ville",
            )
            return render(request, self.view_template, {'form': form})
        return render(
            request, self.view_template, {'form': form}
        )
