"""Urls module
"""
from django.urls import path

from vote.views.create_voting_view import CreateVotingView
from vote.views.detail_view import DetailView
from vote.views.delete_view import DeleteView
from vote.views.edit_view import EditView
from vote.views.overview_view import OverviewView
from vote.views.voting_view import VotingView


app_name = 'vote'

urlpatterns = [
    path('create_voting/', CreateVotingView.as_view(), name='create_voting'),
    path('delete/', DeleteView.as_view(), name='delete'),
    path('detail/', DetailView.as_view(), name='detail'),
    path('edit/', EditView.as_view(), name='edit'),
    path('overview/', OverviewView.as_view(), name='overview'),
    path('voting/', VotingView.as_view(), name='voting')
]
