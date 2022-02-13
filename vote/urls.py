"""Urls module
"""
from django.urls import path

from vote.views.add_voting import AddVoting
from vote.views.detail_view import DetailView
from vote.views.delete_view import DeleteView
from vote.views.edit_view import EditView
from vote.views.overview_view import OverviewView
from vote.views.voting_view import VotingView


app_name = 'vote'

urlpatterns = [
    path('add_voting/', AddVoting.as_view(), name='add_voting'),
    path('delete/', DeleteView.as_view(), name='delete'),
    path('detail/', DetailView.as_view(), name='detail'),
    path('edit/', EditView.as_view(), name='edit'),
    path('overview/', OverviewView.as_view(), name='overview'),
    path('voting/', VotingView.as_view(), name='voting')
]
