from django.core.paginator import Paginator

from django.contrib import messages
from django.views import View
from django.shortcuts import redirect, render

from authentication.models import CustomUser
from vote.management.engine.manager import Manager
from vote.models.voting import Voting


class CollectivityVotingsView(View):
    """CollectivityVotings class.
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
            votings = Voting.objects.filter(
                voting_custom_user_id__collectivity_id__exact=
                request.user.collectivity
            ).order_by('-creation_date')
            paginator = Paginator(votings, 6)
            page_number = request.GET.get('page')
            # self.context = self.manager.set_context(
            #     self.context, voting, 'read'
            # )
            self.context['page_objects'] = paginator.get_page(page_number)
            return render(request, self.view_template, self.context)
        else:
            messages.add_message(
                request, messages.ERROR, self.msg_unauthenticated
            )
            return redirect(self.alternative_view_name)
