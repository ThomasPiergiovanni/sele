"""UpdatePropositionView module.
"""
from django.contrib import messages
from django.shortcuts import redirect

from proposition.views.generic_proposition_view import (
    GenericPropositionView
)


class UpdatePropositionView(GenericPropositionView):
    """UpdatePropositionView class.
    """

    def __init__(self):
        super().__init__()
        self.post_view_name = 'proposition:collectivity_propositions'
        self.msg_post_success = "Le statut de la proposition a été mis-à-jour"

    def post(self, request, id_proposition):
        """UpdatePropositionView method on client get request.
        """
        self.manager.set_proposition_status(request, id_proposition)
        messages.add_message(
            request, messages.SUCCESS, self.msg_post_success
        )
        return redirect(self.post_view_name)
