"""ContactView module.
"""
from django.views import View
from django.shortcuts import render


class ContactView(View):
    """Contact view class.
    """

    def __init__(self):
        super().__init__()
        self.view_template = 'information/contact.html'
        self.context = {}

    def get(self, request):
        """ContactView method on client get request.
        """
        return render(request, self.view_template, self.context)
