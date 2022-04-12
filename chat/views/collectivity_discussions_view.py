"""CollectivityDiscussionsView module.
"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render

from chat.forms.collectivity_discussions_form import CollectivityDiscussionsForm
from chat.management.engine.manager import Manager



class CollectivityDiscussionsView(LoginRequiredMixin, View):
    """CollectivityDiscussionsView class.
    """
    login_url = '/authentication/login/'
    redirect_field_name = None

    def __init__(self):
        super().__init__()
        self.manager = Manager()
        self.view_template = 'chat/discussions.html'
        self.context = {
            'form' : CollectivityDiscussionsForm(),
            'page_objects': None,
        }
    
    def get(self, request):
        """CollectivityDiscussionsView method on client get request.
        """
        search_input = request.session.get('c_d_v_f_search_input', None)
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
        """CollectivityDiscussionsView method on client get request.
        """
        if request.POST.get('cdf_search_button') == 'yes':
            form = CollectivityDiscussionsForm(request.POST)
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
