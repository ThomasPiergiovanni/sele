# pylint: disable=E1101
"""ReadDiscussionView module.
"""
from django.shortcuts import render

from chat.forms.comment_form import CommentForm
from chat.models import Comment, Discussion
from chat.views.generic_chat_view import GenericChatView


class ReadDiscussionView(GenericChatView):
    """ReadDiscussionView class.
    """

    def __init__(self):
        super().__init__()
        self.view_template = 'chat/read_discussion.html'
        self.context = {
            'discussion': None,
            'comments': None,
            'form': CommentForm()
        }

    def get(self, request, id_discussion):
        """Read discussion view method on client get request.
        """
        self.context['discussion'] = Discussion.objects.get(pk=id_discussion)
        self.context['comments'] = Comment.objects.filter(
            comment_discussion_id__exact=id_discussion
        )
        return render(request, self.view_template, self.context)
