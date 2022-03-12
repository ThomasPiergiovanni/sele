from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from authentication.forms.edit_custom_user_form import EditCustomUserForm
from authentication.management.engine.manager import Manager
from authentication.models import CustomUser


class EditCustomUserView(View):
    """EditCustomUserview class.
    """

    def __init__(self):
        super().__init__()
        self.manager = Manager()
        self.context = {
            'form': EditCustomUserForm(),
        }
        self.view_template= 'authentication/edit_custom_user.html'
        self.alternative_view_name = 'information:home'

    def get(self, request):
        """Edit CustomUser page view method on client get request.
        """
        if request.user.is_authenticated:
            custom_user = CustomUser.objects.get(pk=request.user.id)
            form = EditCustomUserForm(
                initial={
                    'user_name': custom_user.user_name,
                    'postal_code': custom_user.collectivity.postal_code,
                    'collectivity': custom_user.collectivity.name
                }
            )
            self.context['form'] = form
            return render(request, self.view_template, self.context)
        else:
            messages.add_message(
                    request, messages.ERROR, "Authentification requise",
                )
            return redirect(self.alternative_view_name)

    def post(self, request):
        """Edit custom user page view method on client post request. Create
        CustomUser into the DB. After Voting creation, user is redirect to
         voting overview page.
        """
        if request.user.is_authenticated:
            form = EditCustomUserForm(request.POST)
            if form.is_valid():
                collectivity = Manager().check_collectivity(
                    form.cleaned_data['postal_code'],
                    form.cleaned_data['collectivity']
                )
                if collectivity:
                    self.manager.edit_custom_user(request, form, collectivity)
                    self.manager.activate_collectivity(collectivity)
                    messages.add_message(
                        request, messages.SUCCESS, "Mise à jours réussie",
                    )
                    return redirect(self.alternative_view_name)
                else:
                    messages.add_message(
                        request, messages.ERROR, "Code postal != Ville",
                    )
                    return render(request, self.view_template, {'form': form})
            else:
                return render(
                    request, self.view_template, {'form': form}
                )
        else:
            messages.add_message(
                request, messages.ERROR, "Authentification requise",
            )
            return redirect(self.alternative_view_name)

