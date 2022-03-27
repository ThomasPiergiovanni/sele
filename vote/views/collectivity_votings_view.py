"""CollectivityVotingsView module.
"""
from django.contrib import messages
from django.views import View
from django.shortcuts import redirect, render

from vote.forms.collectivity_votings_form import CollectivityVotingsForm
from vote.management.engine.manager import Manager



class CollectivityVotingsView(View):
    """CollectivityVotingsView class.
    """
    def __init__(self):
        super().__init__()
        self.manager = Manager()
        self.view_template = 'vote/votings.html'
        self.alternative_view_name = 'information:home'
        self.context = {
            'form' : CollectivityVotingsForm(),
            'page_objects': None,
        }
        self.msg_unauthenticated = "Authentification requise"
    
    def get(self, request):
        """CollectivityVotingsView method on client get request.
        """
        if request.user.is_authenticated:
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

        else:
            messages.add_message(
                request, messages.ERROR, self.msg_unauthenticated
            )
            return redirect(self.alternative_view_name)
    
    def post(self, request):
        if request.user.is_authenticated:
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
        else:
            messages.add_message(
                    request, messages.ERROR, "Authentification requise",
                )
            return redirect(self.alternative_view_name)