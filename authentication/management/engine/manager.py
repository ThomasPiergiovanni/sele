from authentication.models import CustomUser
from collectivity.models.collectivity import Collectivity
from collectivity.models.postal_code import PostalCode


class Manager():
    """Manager class.
    """
    def __init__(self):
        pass
    
    def create_custom_user(self, form):
        """Method for creating CustomUser instances into DB
        """
        CustomUser(
            email=str(form.cleaned_data['email']),
            password=(form.cleaned_data['password1']),
            user_name=(form.cleaned_data['user_name']),
            balance=1,
            collectivity_id=self.__get_collectivity_id(
                form.cleaned_data['postal_code'],
                form.cleaned_data['collectivity']
            )
        ).save()
    
    def __get_collectivity_id(self, form_postal_code, form_collectivity):
        postal_code = PostalCode.objects.get(
            postal_code__exact=form_postal_code
        )
        collectivity = (
            Collectivity.objects.get(
                name__exact=form_collectivity,
                postal_code__exact=postal_code.id
            )
        )
        return collectivity.id


