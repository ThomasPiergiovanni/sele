"""CreatePropositionView module.
"""
from django.contrib import messages
from django.shortcuts import redirect, render

from proposition.forms.proposition_form import PropositionForm
from proposition.views.generic_proposition_view import (
    GenericPropositionView
)


class CreatePropositionView(GenericPropositionView):
    """CreatePropositionView class.
    """

    def __init__(self):
        super().__init__()
        self.view_template = 'proposition/create_proposition.html'
        self.post_view_name = 'proposition:collectivity_propositions'
        self.context = {'form': PropositionForm()}

    def get(self, request):
        """CreatePropositionView method on client get request.
        """
        return render(request, self.view_template, self.context)

    def post(self, request):
        """CreatePropositionView method on client post request.
        """
        form = PropositionForm(request.POST)
        if form.is_valid():
            self.manager.proposition_creates_discussion(form, request.user)
            self.manager.create_proposition(form, request.user)
            messages.add_message(
                request, messages.SUCCESS, "Création réussie",
            )
            return redirect(self.post_view_name)
        self.context = {'form': form}
        return render(request, self.view_template, self.context)
