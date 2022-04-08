"""CollectivityPropositionsView module.
"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render

from proposition.forms.collectivity_propositions_form import (
    CollectivityPropositionsForm
)
from proposition.forms.collectivity_propositions_search_form import (
    CollectivityPropositionsSearchForm
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
            'sort_form' : CollectivityPropositionsForm(),
            'search_form': CollectivityPropositionsSearchForm(),
            'page_objects': None,
        }
    
    def get(self, request):
        """CollectivityPropositionsView method on client get request.
        """
        # attribute = request.session.get('c_p_v_f_attribute', None)
        # order = request.session.get('c_p_v_f_order', None)
        search_input = request.session.get('c_p_v_f_search_input', None)
        # if attribute and order:
        if search_input:
            # self.context['sort_form'] = (
            #     self.manager.set_form_context(attribute, order)
            # )
            self.context['page_objects'] = (
                self.manager.set_page_objects_context(
                    # request=request, attribute=attribute, order=order,
                    request=request, attribute=False, order=False,
                    search_input=search_input
                )
            )
            return render(request, self.view_template, self.context)
        else:
            self.context['page_objects'] = (
                self.manager.set_page_objects_context(
                    request=request,
                    attribute='date', order='desc', search_input=False
                )
            )
            return render(request, self.view_template, self.context)
    
    def post(self, request):
        if request.POST.get('collectivity_propositions_search_form_button') == 'yes':
            form = CollectivityPropositionsSearchForm(request.POST)
            if form.is_valid():
                search_input = form.cleaned_data['search_input']
                self.context['page_objects'] = (
                    self.manager.set_page_objects_context(
                        request=request, attribute=False, order=False,
                        search_input=search_input
                    )
                )
                self.manager.set_session_vars(
                        request=request, attribute=False, order=False,
                        search_input=search_input
                )
                return render(request, self.view_template, self.context)
            else:
                self.context['sort_form'] = form
                self.context['page_objects'] = (
                    self.manager.set_page_objects_context(
                        request=request,
                        attribute='date', order='desc', search_input=False
                    )
                )
                return render(request, self.view_template, self.context)
        elif request.POST.get('collectivity_propositions_clear_form_button') == 'yes':
            self.context['page_objects'] = (
                self.manager.set_page_objects_context(
                    request=request,
                    attribute='date', order='desc', search_input=False
                )
            )
            self.manager.set_session_vars(
                request=request,
                attribute='date', order='desc', search_input=False
            )
            return render(request, self.view_template, self.context)
        else:
            pass

            # form = CollectivityPropositionsForm(request.POST)
            # if form.is_valid():
            #     attribute = form.cleaned_data['attribute_selector']
            #     order = form.cleaned_data['order_selector']
            #     self.context['sort_form'] = (
            #         self.manager.set_form_context(attribute, order)
            #     )
            #     self.context['page_objects'] = (
            #         self.manager.set_page_objects_context(
            #             request=request, attribute=attribute, order=order,
            #             search_input=False
            #         )
            #     )
            #     self.manager.set_session_vars(request, attribute, order)
            #     return render(request, self.view_template, self.context)
            # else:
            #     self.context['sort_form'] = form
            #     self.context['page_objects'] = (
            #         self.manager.set_page_objects_context(
            #             request=request,
            #             attribute='date', order='desc', search_input=False
            #         )
            #     )
            #     return render(request, self.view_template, self.context)
