from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render

from information.management.engine.manager import Manager


class CollectivityDashboardView(LoginRequiredMixin, View):
    """Collectivity Dashboard view  class.
    """
    login_url = '/authentication/login/'
    redirect_field_name = None

    def __init__(self):
        super().__init__()
        self.manager = Manager()
        self.view_template = 'information/collectivity_dashboard.html'
        self.context = {
            'custom_user_pag_obj': None,
            'custom_users_p_counts': None,
            'proposition_pag_obj': None,
            'discussion_pag_obj': None,
            'votation_pag_obj': None
        }

    def get(self, request):
        """Home page view method on client get request.
        """
        self.context['custom_user_pag_obj'] = (
            self.manager.set_cus_use_pag_obj_context(request)
        )
        self.context['custom_users_p_counts'] = (
            self.manager.set_custom_users_propositions_counts_context(request)
        )
        return render(request, self.view_template, self.context)