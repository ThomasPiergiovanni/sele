# pylint: disable=C0103
"""Urls module
"""
from django.urls import path

from vote.views.collectivity_votings_view import CollectivityVotingsView
from vote.views.create_vote_view import CreateVoteView
from vote.views.create_voting_view import CreateVotingView
from vote.views.delete_voting_view import DeleteVotingView
from vote.views.read_voting_view import ReadVotingView


app_name = 'vote'

urlpatterns = [
    path(
        'collectivity_votings/',
        CollectivityVotingsView.as_view(),
        name='collectivity_votings'
    ),
    path(
        'create_vote/<int:id_voting>/',
        CreateVoteView.as_view(),
        name='create_vote'
    ),
    path('create_voting/', CreateVotingView.as_view(), name='create_voting'),
    path(
        'delete_voting/<int:id_voting>/',
        DeleteVotingView.as_view(),
        name='delete_voting'
    ),
    path(
        'read_voting/<int:id_voting>/',
        ReadVotingView.as_view(),
        name='read_voting'
    ),
]
