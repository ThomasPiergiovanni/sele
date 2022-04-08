"""Urls module
"""
from django.urls import path

from proposition.views.add_view import AddView
from proposition.views.collectivity_propositions_view import (
    CollectivityPropositionsView
)
from proposition.views.create_proposition_view import CreatePropositionView
from proposition.views.delete_proposition_view import DeletePropositionView
from proposition.views.read_proposition_view import (
    ReadPropositionView
)
from proposition.views.detail_view import DetailView
from proposition.views.delete_view import DeleteView
from proposition.views.edit_view import EditView
from proposition.views.member_view import MemberView


app_name = 'proposition'

urlpatterns = [
    path('add/', AddView.as_view(), name='add'),
    path(
        'collectivity_propositions/',
        CollectivityPropositionsView.as_view(),
        name='collectivity_propositions'
    ),
    path(
        'create_proposition/',
        CreatePropositionView.as_view(),
        name='create_proposition'
    ),
    path(
        'delete_proposition/<int:id_proposition>/',
        DeletePropositionView.as_view(),
        name='delete_proposition'
    ),
    path(
        'read_proposition/<int:id_proposition>/',
        ReadPropositionView.as_view(),
        name='read_proposition'
    ),
    path('detail/', DetailView.as_view(), name='detail'),
    path('delete/', DeleteView.as_view(), name='delete'),
    path('edit/', EditView.as_view(), name='edit'),
    path('member/', MemberView.as_view(),name='member'),
]
