"""CollectivityPropositionsView module.
"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render

from proposition.forms.collectivity_propositions_form import (
    CollectivityPropositionsForm
)
from proposition.management.engine.manager import Manager


class CollectivityPropositionsView(LoginRequiredMixin,View):
    """CollectivityPropositionsView class.
    """
    login_url = '/authentication/login/'
    redirect_field_name = None

    def __init__(self):
        super().__init__()
        self.manager = Manager()
        self.view_template = 'proposition/propositions.html'
        self.context = {
            'form' : CollectivityPropositionsForm(),
            'page_objects': None,
        }
    
    def get(self, request):
        """CollectivityPropositionsView method on client get request.
        """
        search_input = request.session.get('c_p_v_f_search_input', None)
        if search_input:
            self.context['page_objects'] = (
                self.manager.set_page_objects_context(request, search_input)
            )
            return render(request, self.view_template, self.context)
        else:
            self.context['page_objects'] = (
                self.manager.set_page_objects_context(request, False)
            )
            return render(request, self.view_template, self.context)
    
    def post(self, request):
        if request.POST.get('cpf_search_button') == 'yes':
            form = CollectivityPropositionsForm(request.POST)
            if form.is_valid():
                search_input = form.cleaned_data['search_input']
                self.context['page_objects'] = (
                    self.manager.set_page_objects_context(request, search_input)
                )
                self.manager.set_session_vars(request, search_input)
            else:
                self.context['form'] = form
                self.context['page_objects'] = (
                    self.manager.set_page_objects_context(request, False)
                )
        else:
            self.context['page_objects'] = (
                self.manager.set_page_objects_context(request, False)
            )
            self.manager.set_session_vars(request, False)
        return render(request, self.view_template, self.context)
