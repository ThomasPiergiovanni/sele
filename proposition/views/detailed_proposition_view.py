from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render

from proposition.management.engine.manager import Manager
from proposition.models.proposition import Proposition


class DetailedPropositionView(LoginRequiredMixin, View):
    """DetailedPropositionView class.
    """
    login_url = '/authentication/login/'
    redirect_field_name = None

    def __init__(self):
        super().__init__()
        self.manager = Manager()
        self.view_template = 'proposition/detailed_proposition.html'
        self.context = {
            'proposition': None,
            'proposition_operation': None,                      
        }
    
    def get(self, request, id_proposition):
        """Detailed proposition view method on client get request.
        """
        self.context['proposition'] = (
            Proposition.objects.get(pk=id_proposition)
        )
        self.context['proposition_operation'] = 'read'
        return render(request, self.view_template, self.context)

