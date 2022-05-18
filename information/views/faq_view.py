# pylint: disable=E1101
"""FaqView module.
"""
from django.shortcuts import render
from django.views import View

from information.models.question import Question


class FaqView(View):
    """FaqView class.
    """

    def __init__(self):
        super().__init__()
        self.view_template = 'information/faq.html'
        self.context = {'questions': None}

    def get(self, request):
        """FaqView method on client get request.
        """
        self.context['questions'] = Question.objects.all().order_by('id')
        return render(request, self.view_template, self.context)
