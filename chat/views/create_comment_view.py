"""Create comment view module
"""
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import redirect, render

from chat.forms.comment_form import CommentForm
from chat.management.engine.manager import Manager
from chat.models.comment import Comment


class CreateCommentView(LoginRequiredMixin, View):
    """CreateCommentView class.
    """
    login_url = '/authentication/login/'
    redirect_field_name = None

    def __init__(self):
        super().__init__()
        self.manager = Manager()
        self.view_name = 'chat:read_discussion'
        self.alternative_one_view_template = 'chat/read_discussion.html'
        self.context = {'form': None}


    def post(self, request, id_discussion):
        """Create vote view method on client post request.
        """
        form = CommentForm(request.POST)        
        if form.is_valid():
            self.manager.create_comment(form, request.user, id_discussion)
            return redirect(self.view_name, id_discussion)
        else:
            self.context['form'] = form
            return render(
                request, self.alternative_one_view_template, self.context
            )
