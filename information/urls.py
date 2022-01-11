"""Urls module
"""
from django.urls import path

from information.views.collectivity_dashboard_view import (
    CollectivityDashboardView
)
from information.views.member_dashboard_view import (
    MemberDashboardView
)
from information.views.home_view import HomeView

app_name = 'information'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path(
        'collectivity_dashboard/',
        CollectivityDashboardView.as_view(),
        name='collectivity_dashboard'
    ),
    path(
        'member_dashboard/',
        MemberDashboardView.as_view(),
        name='member_dashboard'
    )
]
