"""CollectivityPropositionsView module.
"""
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import redirect, render

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
        attribute = request.session.get('c_p_v_f_attribute', None)
        order = request.session.get('c_p_v_f_order', None)
        if attribute and order:
            self.context['form'] = (
                self.manager.set_colvity_propositions_form_context(
                    attribute, order
                )
            )
            self.context['page_objects'] = (
                self.manager.set_colvity_propositions_page_obj_context(
                    request, attribute=attribute, order=order
                )
            )
            return render(request, self.view_template, self.context)
        else:
            self.context['page_objects'] = (
                self.manager.set_colvity_propositions_page_obj_context(
                    request, attribute='date', order='desc'
                )
            )
            return render(request, self.view_template, self.context)
    
    # def post(self, request):
    #     if request.user.is_authenticated:
    #         form = CollectivityVotingsForm(request.POST)
    #         if form.is_valid():
    #             attribute = form.cleaned_data['attribute_selector']
    #             order = form.cleaned_data['order_selector']
    #             self.context['form'] = (
    #                 self.manager.set_collectivity_votings_form_context(
    #                     attribute, order
    #                 )
    #             )
    #             self.context['page_objects'] = (
    #                 self.manager.set_collectivity_votings_page_objects_context(
    #                     request, attribute=attribute, order=order
    #                 )
    #             )
    #             self.manager.set_session_vars(request, attribute, order)
    #             return render(request, self.view_template, self.context)
    #         else:
    #             self.context['form'] = form
    #             self.context['page_objects'] = (
    #                 self.manager.set_collectivity_votings_page_objects_context(
    #                     request, attribute='date', order='desc'
    #                 )
    #             )
    #             return render(
    #                 request, self.view_template,self.context
    #             )
    #     else:
    #         messages.add_message(
    #                 request, messages.ERROR, "Authentification requise",
    #             )
    #         return redirect(self.alternative_view_name)
