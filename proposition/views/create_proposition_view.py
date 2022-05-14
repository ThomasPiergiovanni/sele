"""CreatePropositionView module.
"""
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import redirect, render

from proposition.forms.proposition_form import PropositionForm
from proposition.management.engine.manager import Manager



class CreatePropositionView(LoginRequiredMixin,View):
    """CreatePropositionView class.
    """
    login_url = '/authentication/login/'
    redirect_field_name = None

    def __init__(self):
        super().__init__()
        self.manager = Manager()
        self.view_template = 'proposition/create_proposition.html'
        self.post_view_name = 'proposition:collectivity_propositions'
        self.context = {'form' : PropositionForm()}
    
    def get(self, request):
        """CreatePropositionView method on client get request.
        """
        return render(request, self.view_template, self.context)

    def post(self, request):
        """CreatePropositionView method on client post request.
        """
        form = PropositionForm(request.POST)
        if form.is_valid():
            self.manager.create_discussion(form, request.user)
            self.manager.create_proposition(form, request.user)
            messages.add_message(
                request, messages.SUCCESS, "Création réussie",
            )
            return redirect(self.post_view_name)
        else:
            self.context = {'form': form}
            return render(request, self.view_template, self.context)