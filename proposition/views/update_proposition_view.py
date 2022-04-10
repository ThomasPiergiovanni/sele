from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import redirect

from proposition.management.engine.manager import Manager


class UpdatePropositionView(LoginRequiredMixin, View):
    """UpdatePropositionView class.
    """
    login_url = '/authentication/login/'
    redirect_field_name = None

    def __init__(self):
        super().__init__()
        self.manager = Manager()
        self.post_view_name = 'proposition:collectivity_propositions'
        self.msg_post_success = "Le statut de la proposition a été mis-à-jour"
    
    def post(self, request, id_proposition):
        """Detailed proposition view method on client get request.
        """
        self.manager.set_proposition_status(request, id_proposition)
        messages.add_message(
            request, messages.SUCCESS, self.msg_post_success
        )
        return redirect(self.post_view_name)

