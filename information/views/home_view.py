from django.views import View
from django.shortcuts import render

from information.management.engine.manager import Manager


class HomeView(View):
    """Home view class.
    """
    def __init__(self):
        super().__init__()
        self.manager = Manager()
        self.view_template = 'information/home.html'
        self.context = {
            'mapbox_url': None,
            'vector_layer': None,
            'stats_data': None,
            'all_p_counts': None,
            'all_cu_counts': None,
            'all_co_counts': None,
            'all_v_counts': None
        }

    def get(self, request):
        """Home page view method on client get request.
        """
        self.context = self.manager.set_home_context(self.context)
        return render(request, self.view_template, self.context)
    
