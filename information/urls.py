"""Urls module
"""
from django.urls import path

from information.views.home_view import HomeView

app_name = 'information'

urlpatterns = [
    path('', HomeView.as_view(), name='home')
]
