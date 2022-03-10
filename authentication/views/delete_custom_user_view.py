
"""Delete custom user view module.
"""
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

    # def post(self, request):
    #     """Edit custom user page view method on client post request. Create
    #     CustomUser into the DB. After Voting creation, user is redirect to
    #      voting overview page.
    #     """
    #     if request.user.is_authenticated:
    #         form = EditCustomUserForm(request.POST)
    #         if form.is_valid():
    #             collectivity = Manager().check_collectivity(
    #                 form.cleaned_data['postal_code'],
    #                 form.cleaned_data['collectivity']
    #             )
    #             if collectivity:
    #                 Manager().edit_custom_user(request, form, collectivity)
    #                 Manager().activate_collectivity(collectivity)
    #                 messages.add_message(
    #                     request,
    #                     messages.SUCCESS,
    #                     "Mise à jours réussie",
    #                 )
    #                 return redirect(self.alternative_view_name)
    #             else:
    #                 messages.add_message(
    #                     request,
    #                     messages.ERROR,
    #                     "Le couple \"code postal\" et \"ville\" n'est pas valide.",
    #                 )
    #                 return render(request, self.view_template, {'form': form})
    #         else:
    #             return render(
    #                 request, self.view_template, {'form': form}
    #             )
    #     else:
    #         messages.add_message(
    #                 request,
    #                 messages.ERROR,
    #                 "Authentification requise",
    #             )
    #         return redirect(self.alternative_view_name)

