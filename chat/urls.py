"""Urls module
"""
from django.urls import path

from chat.views.collectivity_discussions_view import CollectivityDiscussionsView
from chat.views.create_comment_view import CreateCommentView
from chat.views.create_discussion_view import CreateDiscussionView
from chat.views.read_discussion_view import ReadDiscussionView



app_name = 'chat'

urlpatterns = [
    path(
        'collectivity_discussions/',
        CollectivityDiscussionsView.as_view(),
        name='collectivity_discussions'
    ),
    path(
        'create_comment/<int:id_discussion>/',
        CreateCommentView.as_view(),
        name='create_comment'
    ),
    path(
        'create_discussion/',
        CreateDiscussionView.as_view(),
        name='create_discussion'
    ),
    path(
        'read_discussion/<int:id_discussion>/',
        ReadDiscussionView.as_view(),
        name='read_discussion'
    )
]
