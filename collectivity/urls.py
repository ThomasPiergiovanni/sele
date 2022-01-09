"""Urls module
"""
from django.urls import path

from collectivity.views.dashboard_view import (
    DashboardView
)

app_name = 'collectivity'

urlpatterns = [
    path(
        'dashboard/',
        DashboardView.as_view(),
        name='dashboard'
    )
]
