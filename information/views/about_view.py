"""AboutView module.
"""
from django.shortcuts import render
from django.views import View


class AboutView(View):
    """About view class.
    """

    def __init__(self):
        super().__init__()
        self.view_template = 'information/about.html'
        self.context = {}

    def get(self, request):
        """AboutView method on client get request.
        """
        return render(request, self.view_template, self.context)
