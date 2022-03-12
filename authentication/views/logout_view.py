from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View


class LogoutView(View):
    """LogoutView class.
    """

    def __init__(self):
        super().__init__()
        self.view_name = 'information:home'

    def get(self, request):
        """Logout method on client get request.
        """
        if request.user.is_authenticated:
            logout(request)
            messages.add_message(
                request, messages.SUCCESS, "Déconnexion réussie",
            )
            return redirect(self.view_name)
        else:
            messages.add_message(
                request, messages.WARNING, "L'utilisateur est déja déconnecté"
            )
            return redirect(self.view_name)

