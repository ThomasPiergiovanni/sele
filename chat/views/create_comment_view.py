"""CreateCommentView module.
"""
from django.shortcuts import redirect, render

from chat.forms.comment_form import CommentForm
from chat.views.generic_chat_view import GenericChatView


class CreateCommentView(GenericChatView):
    """CreateCommentView class.
    """

    def __init__(self):
        super().__init__()
        self.view_name = 'chat:read_discussion'
        self.alternative_one_view_template = 'chat/read_discussion.html'
        self.context = {'form': None}

    def post(self, request, id_discussion):
        """Create Coment view method on client post request.
        """
        form = CommentForm(request.POST)
        if form.is_valid():
            self.manager.create_comment(form, request.user, id_discussion)
            return redirect(self.view_name, id_discussion)
        self.context['form'] = form
        return render(
            request, self.alternative_one_view_template, self.context
        )
