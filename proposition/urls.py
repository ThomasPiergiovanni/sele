"""Urls module
"""
from django.urls import path


from proposition.views.collectivity_proposition_view import (
    CollectivityPropositionView
)
from proposition.views.member_proposition_view import (
    MemberPropositionView
)
from proposition.views.detail_view import DetailView


app_name = 'proposition'

urlpatterns = [
    path(
        'collectivity_proposition/',
        CollectivityPropositionView.as_view(),
        name='collectivity_proposition'
    ),
    path(
        'member_proposition/',
        MemberPropositionView.as_view(),
        name='member_proposition'
    ),
    path('detail/', DetailView.as_view(), name='detail')
]
