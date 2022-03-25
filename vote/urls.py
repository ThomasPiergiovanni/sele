"""Urls module
"""
from django.urls import path

from vote.views.collectivity_votings_view import CollectivityVotingsView
from vote.views.create_voting_view import CreateVotingView
from vote.views.delete_voting_view import DeleteVotingView
from vote.views.detailed_voting_view import DetailedVotingView


app_name = 'vote'

urlpatterns = [
    path(
        'collectivity_votings/',
        CollectivityVotingsView.as_view(),
        name='collectivity_votings'
    ),
    path('create_voting/', CreateVotingView.as_view(), name='create_voting'),
    path(
        'delete_voting/<int:id_voting>/',
        DeleteVotingView.as_view(),
        name='delete_voting'
    ),
    path(
        'detailed_voting/<int:id_voting>/',
        DetailedVotingView.as_view(),
        name='detailed_voting'
    ),
]
