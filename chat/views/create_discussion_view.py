"""Creat Discussion view module
"""
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import redirect, render

from chat.forms.discussion_form import DiscussionForm
from chat.management.engine.manager import Manager


class CreateDiscussionView(LoginRequiredMixin,View):
    """CreateDiscussionView class.
    """
    login_url = '/authentication/login/'
    redirect_field_name = None

    def __init__(self):
        super().__init__()
        self.manager =  Manager()
        self.context = {
            'form': DiscussionForm(),
        }
        self.view_template = 'chat/create_discussion.html'
        self.alternative_view_name = 'authentication:login'
        self.post_view_name = 'chat:collectivity_discussions'

    def get(self, request):
        """Create discussions view method on user get request.
        """
        return render(request, self.view_template, self.context)           
    
    def post(self, request):
        """Create discussion view method on client post request. Create 
        discussion into the DB. After Discussion creation, user is redirected to 
        discussions overview page.
        """
        form = DiscussionForm(request.POST)
        if form.is_valid():
            self.manager.create_discussion(form, request.user, None)
            messages.add_message(
                request, messages.SUCCESS, "Création réussie",
            )
            return redirect(self.post_view_name)
        else:
            self.context['form'] = form
            return render(request, self.view_template, self.context)
