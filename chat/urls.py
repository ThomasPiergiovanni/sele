"""Urls module
"""
from django.urls import path

from chat.views.create_discussion_view import CreateDiscussionView
from chat.views.read_discussion_view import ReadDiscussionView
from chat.views.add_view import AddView
from chat.views.detail_view import DetailView
from chat.views.overview_view import OverviewView



app_name = 'chat'

urlpatterns = [
    path(
        'create_discussion/',
        CreateDiscussionView.as_view(),
        name='create_discussion'
    ),
    path(
        'read_discussion/<int:id_discussion>/',
        ReadDiscussionView.as_view(),
        name='read_discussion'
    ),
    path('add/', AddView.as_view(), name='add'),
    path('detail/', DetailView.as_view(), name='detail'),
    path('overview/', OverviewView.as_view(), name='overview')
]
