"""Urls module
"""
from django.urls import path

from information.management.engine.manager import Manager
from information.views.about_view import AboutView
from information.views.collectivity_dashboard_view import (
    CollectivityDashboardView
)
from information.views.faq_view import FaqView
from information.views.legal_view import LegalView
from information.views.member_dashboard_view import (
    MemberDashboardView
)
from information.views.home_view import HomeView

app_name = 'information'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path(
        'collectivity_dashboard/',
        CollectivityDashboardView.as_view(),
        name='collectivity_dashboard'
    ),
    path('faq/', FaqView.as_view(), name='faq'),
    path('legal/', LegalView.as_view(), name='legal'),
    path(
        'member_dashboard/',
        MemberDashboardView.as_view(),
        name='member_dashboard'
    )
]
