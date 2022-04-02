"""CollectivityVotingsView module.
"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views import View
from django.shortcuts import redirect, render

from vote.forms.collectivity_votings_form import CollectivityVotingsForm
from vote.management.engine.manager import Manager



class CollectivityVotingsView(LoginRequiredMixin, View):
    """CollectivityVotingsView class.
    """
    login_url = '/authentication/login/'
    redirect_field_name = None

    def __init__(self):
        super().__init__()
        self.manager = Manager()
        self.view_template = 'vote/votings.html'
        self.context = {
            'form' : CollectivityVotingsForm(),
            'page_objects': None,
        }
    
    def get(self, request):
        """CollectivityVotingsView method on client get request.
        """
        attribute = request.session.get('c_v_v_f_attribute', None)
        order = request.session.get('c_v_v_f_order', None)
        if attribute and order:
            self.context['form'] = (
                self.manager.set_collectivity_votings_form_context(
                    attribute, order
                )
            )
            self.context['page_objects'] = (
                self.manager.set_collectivity_votings_page_objects_context(
                    request, attribute=attribute, order=order
                )
            )
            return render(request, self.view_template, self.context)
        else:
            self.context['page_objects'] = (
                self.manager.set_collectivity_votings_page_objects_context(
                    request, attribute='date', order='desc'
                )
            )
            return render(request, self.view_template, self.context)
    
    def post(self, request):
        """CollectivityVotingsView method on client get request.
        """
        form = CollectivityVotingsForm(request.POST)
        if form.is_valid():
            attribute = form.cleaned_data['attribute_selector']
            order = form.cleaned_data['order_selector']
            self.context['form'] = (
                self.manager.set_collectivity_votings_form_context(
                    attribute, order
                )
            )
            self.context['page_objects'] = (
                self.manager.set_collectivity_votings_page_objects_context(
                    request, attribute=attribute, order=order
                )
            )
            self.manager.set_session_vars(request, attribute, order)
            return render(request, self.view_template, self.context)
        else:
            self.context['form'] = form
            self.context['page_objects'] = (
                self.manager.set_collectivity_votings_page_objects_context(
                    request, attribute='date', order='desc'
                )
            )
            return render(
                request, self.view_template,self.context
            )
