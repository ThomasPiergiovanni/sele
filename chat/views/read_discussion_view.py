from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render

from chat.management.engine.manager import Manager
from chat.models.comment import Comment
from chat.models.discussion import Discussion


class ReadDiscussionView(LoginRequiredMixin, View):
    """ReadDiscussionView class.
    """
    login_url = '/authentication/login/'
    redirect_field_name = None

    def __init__(self):
        super().__init__()
        self.manager = Manager()
        self.view_template = 'chat/read_discussion.html'
        self.context = {
            'discussion': None,
            'comments': None
        }
    
    def get(self, request, id_discussion):
        """Read discussion view method on client get request.
        """
        self.context['discussion'] = Discussion.objects.get(pk=id_discussion)
        self.context['comments'] = Comment.objects.filter(
            comment_discussion_id__exact=id_discussion
        )
        return render(request, self.view_template, self.context)

