"""LegalView module.
"""
from django.shortcuts import render
from django.views import View


class LegalView(View):
    """LegalView class.
    """

    def __init__(self):
        super().__init__()
        self.view_template = 'information/legal.html'
        self.context = {}

    def get(self, request):
        """LegalView method on client get request.
        """
        return render(request, self.view_template, self.context)
