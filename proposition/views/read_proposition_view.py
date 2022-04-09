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
        self.context = {
            'proposition': None,
            'href': None,  
            'class': None, 
            'text': None,          
        }
    
    def get(self, request, id_proposition):
        """Detailed proposition view method on client get request.
        """
        context = self.manager.set_read_proposition_view_context(
            request,id_proposition
        )
        self.context['proposition'] = context['proposition']
        self.context['href'] = context['href']
        self.context['class'] = context['class']
        self.context['text'] = context['text']

        return render(request, self.view_template, self.context)

