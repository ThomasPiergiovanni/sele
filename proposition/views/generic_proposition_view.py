"""GenericPropositionView module.
"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from proposition.management.engine.manager import Manager


class GenericPropositionView(LoginRequiredMixin, View):
    """GenericPropositionView class.
    """

    login_url = '/authentication/login/'
    redirect_field_name = None

    def __init__(self):
        super().__init__()
        self.manager = Manager()
