"""Delete proposition view module
"""
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import redirect, render

from proposition.management.engine.manager import Manager
from proposition.models.proposition import Proposition


class DeletePropositionView(LoginRequiredMixin, View):
    """DeletePropositionView class.
    """
    login_url = '/authentication/login/'
    redirect_field_name = None

    def __init__(self):
        super().__init__()
        self.manager = Manager()
        self.view_template = 'proposition/delete_proposition.html'
        self.alternative_one_view_name = 'proposition:collectivity_propositions'
        self.context = {
            'proposition': None
        }
        self.msg_not_owner = (
            "Le créateur seulement peut supprimer la proposition"
        )
        self.msg_post_success = "Suppression de proposition réussie"
    
    def get(self, request, id_proposition):
        """Delete proposition view method on client get request.
        """
        print('horo')
        proposition = Proposition.objects.get(pk=id_proposition)
        if proposition.proposition_creator_id == request.user.id:
            self.context['proposition'] = proposition
            return render(request, self.view_template, self.context)
        else:
            messages.add_message(
                request, messages.ERROR, self.msg_not_owner,
            )
            return redirect(self.alternative_one_view_name) 

    def post(self, request, id_proposition):
        """Delete proposition view method on client post request.
        """
        proposition = Proposition.objects.get(pk=id_proposition)
        print(proposition.id)
        if proposition.proposition_creator_id == request.user.id:
            proposition.delete()
            messages.add_message(
                request, messages.SUCCESS, self.msg_post_success
            )
            return redirect(self.alternative_one_view_name)
        else:
            messages.add_message(
                request, messages.ERROR, self.msg_not_owner
            )
            return redirect(self.alternative_one_view_name)
