# pylint: disable=C0103
"""Urls module
"""
from django.urls import path

from proposition.views.collectivity_propositions_view import (
    CollectivityPropositionsView
)
from proposition.views.create_proposition_view import CreatePropositionView
from proposition.views.delete_proposition_view import DeletePropositionView
from proposition.views.read_proposition_view import ReadPropositionView
from proposition.views.update_proposition_view import UpdatePropositionView

app_name = 'proposition'

urlpatterns = [
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
    path(
        'update_proposition/<int:id_proposition>/',
        UpdatePropositionView.as_view(),
        name='update_proposition'
    ),
]
