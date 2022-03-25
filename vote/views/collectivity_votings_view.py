"""CollectivityVotingsView module.
"""
from django.contrib import messages
from django.views import View
from django.shortcuts import redirect, render

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
            'page_objects': None,
        }
        self.msg_unauthenticated = "Authentification requise"
    
    def get(self, request):
        """CollectivityVotingsView method on client get request.
        """
        if request.user.is_authenticated:
            self.context['page_objects'] = self.manager.create_page_objects(
                request
            )
            return render(request, self.view_template, self.context)
        else:
            messages.add_message(
                request, messages.ERROR, self.msg_unauthenticated
            )
            return redirect(self.alternative_view_name)
