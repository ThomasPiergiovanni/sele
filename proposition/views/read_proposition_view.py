from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render

from proposition.management.engine.manager import Manager
from proposition.models.proposition import Proposition


class ReadPropositionView(LoginRequiredMixin, View):
    """ReadPropositionView class.
    """
    login_url = '/authentication/login/'
    redirect_field_name = None

    def __init__(self):
        super().__init__()
        self.manager = Manager()
        self.view_template = 'proposition/read_proposition.html'
        self.context = None
    
    def get(self, request, id_proposition):
        """Detailed proposition view method on client get request.
        """
        self.context = self.manager.set_read_proposition_view_context(
            request,id_proposition
        )
        return render(request, self.view_template, self.context)

