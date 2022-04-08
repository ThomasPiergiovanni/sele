"""Delete proposition view module
"""
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import redirect, render

from proposition.management.engine.manager import Manager
from proposition.models.proposition import Proposition
from proposition.models.status import Status


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
        self.msg_post_success = "Suppression réussie"
        self.mgs_post_no_delete = (
            "Une proposition avec ce satut ne peut pas être supprimée"
        )
        self.msg_not_owner = (
            "Le créateur seulement peut supprimer la proposition"
        )
    
    def get(self, request, id_proposition):
        """Delete proposition view method on client get request.
        """
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
        if proposition.proposition_creator_id == request.user.id:
            if proposition.proposition_status.name in ['Terminé', 'Annulé']:
                messages.add_message(
                    request, messages.WARNING, self.mgs_post_no_delete
                )
            elif proposition.proposition_status.name == 'Nouveau':
                proposition.delete()
                messages.add_message(
                    request, messages.SUCCESS, self.msg_post_success
                )
            else:
                status = Status.objects.get(name__exact='Annulé')
                proposition.proposition_status = status
                proposition.save()
                messages.add_message(
                    request, messages.SUCCESS, self.msg_post_success
                )
        else:
            messages.add_message(request, messages.ERROR, self.msg_not_owner)
        return redirect(self.alternative_one_view_name)
