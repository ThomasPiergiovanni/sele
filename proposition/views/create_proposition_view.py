"""CreatePropositionsView module.
"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render

from proposition.forms.proposition_form import PropositionForm
from proposition.management.engine.manager import Manager



class CreatePropositionsView(LoginRequiredMixin,View):
    """CreatePropositionsView class.
    """
    login_url = '/authentication/login/'
    redirect_field_name = None

    def __init__(self):
        super().__init__()
        self.manager = Manager()
        self.view_template = 'proposition/create_proposition.html'
        self.context = {
            'form' : PropositionForm()
        }
    
    def get(self, request):
        """CreatePropositionView method on client get request.
        """
        return render(request, self.view_template, self.context)

    
    # def post(self, request):
    #     form = CollectivityPropositionsForm(request.POST)
    #     if form.is_valid():
    #         attribute = form.cleaned_data['attribute_selector']
    #         order = form.cleaned_data['order_selector']
    #         self.context['form'] = (
    #             self.manager.set_form_context(attribute, order)
    #         )
    #         self.context['page_objects'] = (
    #             self.manager.set_page_objects_context(request, attribute, order)
    #         )
    #         self.manager.set_session_vars(request, attribute, order)
    #         return render(request, self.view_template, self.context)
    #     else:
    #         self.context['form'] = form
    #         self.context['page_objects'] = (
    #             self.manager.set_page_objects_context(request, 'date', 'desc')
    #         )
    #         return render(request, self.view_template, self.context)
