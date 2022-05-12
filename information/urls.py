"""Urls module
"""
from django.urls import path

from information.views.about_view import AboutView
from information.views.contact_view import ContactView
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
    path('contact/', ContactView.as_view(), name='contact'),
    path('faq/', FaqView.as_view(), name='faq'),
    path(
        'information/collectivity_dashboard/',
        CollectivityDashboardView.as_view(),
        name='collectivity_dashboard'
    ),
    path('legal/', LegalView.as_view(), name='legal'),
    path(
        'member_dashboard/',
        MemberDashboardView.as_view(),
        name='member_dashboard'
    ),
]
