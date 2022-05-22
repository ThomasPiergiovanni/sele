# pylint: disable=E1101,R0201
"""Authentication Manager module.
"""
from authentication.models import CustomUser
from collectivity.models import Collectivity, PostalCode


class Manager():
    """Authentication Manager class.
    """

    def check_collectivity(self, form_postal_code, form_collectivity):
        """Method checking Collectivity.
        """
        try:
            postal_code = PostalCode.objects.get(
                postal_code__exact=form_postal_code
            )
            collectivity = (
                Collectivity.objects.get(
                    name__exact=form_collectivity,
                    postal_code__exact=postal_code.id
                )
            )
            return collectivity
        except Collectivity.DoesNotExist:
            return False

    def create_custom_user(self, form, collectivity):
        """Method for creating CustomUser into DB.
        """
        CustomUser.objects.create_user(
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password1'],
            user_name=form.cleaned_data['user_name'],
            balance=1,
            collectivity_id=collectivity.id

        )

    def activate_collectivity(self, collectivity):
        """Method for "activating" Collectivity.
        """
        if collectivity.activity == 'no':
            collectivity.activity = 'yes'
            collectivity.save()

    def update_custom_user(self, request, form, collectivity):
        """Method updating CustomUser into DB.
        """
        custom_user = CustomUser.objects.get(pk=request.user.id)
        custom_user.user_name = form.cleaned_data['user_name']
        custom_user.collectivity_id = collectivity.id
        custom_user.save()
