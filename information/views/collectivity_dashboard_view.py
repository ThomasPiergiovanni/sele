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
            'voting_pag_obj': None,
            'collectivity_p_counts': None,
            'collectivity_cu_counts': None,
            'collectivity_d_counts': None,
            'collectivity_v_counts': None
        }

    def get(self, request):
        """CollectivityDashboard page view method on client get request.
        """
        self.context = self.manager.set_collectivity_dashboard_context(
            request, self.context
        )
        return render(request, self.view_template, self.context)