from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import redirect

from proposition.management.engine.manager import Manager
from proposition.models.proposition import Proposition


class UpdatePropositionView(LoginRequiredMixin, View):
    """UpdatePropositionView class.
    """
    login_url = '/authentication/login/'
    redirect_field_name = None

    def __init__(self):
        super().__init__()
        self.manager = Manager()
        self.post_view_name = 'proposition:read_proposition'
        self.msg_post_success = "Statut mis-à-jour"
    
    def post(self, request, id_proposition):
        """Detailed proposition view method on client get request.
        """
        update_status_button = request.POST.get('update_status_button')
        if update_status_button == 'select':
            pass
        else:
            pass
        messages.add_message(
            request, messages.SUCCESS, self.msg_post_success
        )
        return redirect(self.post_view_name, id_proposition=id_proposition)

