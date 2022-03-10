from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View


class LogoutView(View):
    """LogoutView class.
    """

    def __init__(self):
        super().__init__()
        self.get_nominal_view_name = 'information:home'

    def get(self, request):
        """Home page view method on client get request.
        """
        logout(request)
        messages.add_message(
            request,
            messages.SUCCESS,
            "Déconnexion réussie",
        )
        return redirect(self.get_nominal_view_name)
