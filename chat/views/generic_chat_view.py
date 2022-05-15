"""GenericChatView module.
"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from chat.management.engine.manager import Manager


class GenericChatView(LoginRequiredMixin, View):
    """GenericChatView class.
    """

    login_url = '/authentication/login/'
    redirect_field_name = None

    def __init__(self):
        super().__init__()
        self.manager = Manager()
