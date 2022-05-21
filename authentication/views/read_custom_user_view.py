"""ReadCustomUserview module.
"""
# from django.contrib import messages
from django.shortcuts import render
# from django.views import View
from authentication.views.generic_authentication_view import (
    GenericAuthenticationView
)


class ReadCustomUserView(GenericAuthenticationView):
    """ReadCustomUserview class.
    """

    def __init__(self):
        super().__init__()
        self.context = {}
        self.view_template = 'authentication/read_custom_user.html'

    def get(self, request):
        """ReadCustomUserview method on client get request.
        """
        return render(request, self.view_template, self.context)
