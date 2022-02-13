from django.views import View
from django.shortcuts import render

from authentication.forms.create_custom_user_form import CreateCustomUserForm


class CreateCustomUser(View):
    """CreateCustomUser view class.
    """

    def __init__(self):
        super().__init__()
        self.context = {
            'form': CreateCustomUserForm(),
        }
        self.get_success_template = 'authentication/create_custom_user.html'


    def get(self, request):
        """Home page view method on client get request.
        """
        return render(request, self.get_success_template, self.context)
