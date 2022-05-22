# pylint: disable=E1101
"""DeletePropositionView module
"""
from django.contrib import messages
from django.shortcuts import redirect, render

from proposition.models import Proposition, Status
from proposition.views.generic_proposition_view import (
    GenericPropositionView
)


class DeletePropositionView(GenericPropositionView):
    """DeletePropositionView class.
    """

    def __init__(self):
        super().__init__()
        self.view_template = 'proposition/delete_proposition.html'
        self.alternative_one_view_name = (
            'proposition:collectivity_propositions'
        )
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
        """DeletePropositionView method on client get request.
        """
        proposition = Proposition.objects.get(pk=id_proposition)
        if proposition.proposition_creator_id == request.user.id:
            self.context['proposition'] = proposition
            return render(request, self.view_template, self.context)
        messages.add_message(
            request, messages.ERROR, self.msg_not_owner,
        )
        return redirect(self.alternative_one_view_name)

    def post(self, request, id_proposition):
        """DeletePropositionView method on client post request.
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
