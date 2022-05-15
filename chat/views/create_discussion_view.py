"""CreateDiscussionView module.
"""
from django.contrib import messages
from django.shortcuts import redirect, render

from chat.forms.discussion_form import DiscussionForm
from chat.views.generic_chat_view import GenericChatView


class CreateDiscussionView(GenericChatView):
    """CreateDiscussionView class.
    """

    def __init__(self):
        super().__init__()
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
        """Create discussion view method on client post request.
        """
        form = DiscussionForm(request.POST)
        if form.is_valid():
            self.manager.create_discussion(form, request.user, None)
            messages.add_message(
                request, messages.SUCCESS, "Création réussie",
            )
            return redirect(self.post_view_name)
        self.context['form'] = form
        return render(request, self.view_template, self.context)
