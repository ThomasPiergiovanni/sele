from authentication.models import CustomUser



class Manager():
    """Manager class.
    """
    def __init__(self):
        pass
    
    # def create_custom_user(self, form):
    #     """Method for creating CustomUser instances into DB
    #     """
    #     CustomUser(
    #         email=form.cleaned_data['email'],
    #         password=form.cleaned_data['password1'],
    #         user_name=form.cleaned_data['user_name'],
    #         balance=0,
    #         collectivity_id=self.__get_collectivity_id(
    #             form.cleaned_data['postal_code']
    #         )
    #     ).save()
    
    # def __get_collectivity_id(self, form_data):
    #     postal_code = PostalCode.objects.get(postal_code__exact=form_data)


