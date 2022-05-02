from django.views import View
from django.shortcuts import render

from information.models.question import Question


class FaqView(View):
    """FAQ view  class.
    """

    def __init__(self):
        super().__init__()
        self.view_template = 'information/faq.html'
        self.context = {'questions': None}

    def get(self, request):
        """Faq page view method on client get request.
        """
        self.context['questions'] = Question.objects.all().order_by('id')
        return render(request, self.view_template, self.context)