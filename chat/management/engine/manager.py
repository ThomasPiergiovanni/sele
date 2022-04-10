# from chat.models.discussion import Comment
from datetime import date

from django.core.paginator import Paginator
from django.utils import timezone

from chat.models.comment import Comment
from chat.models.discussion import Discussion


class Manager():
    """Manager manager class.
    """
    def __init__(self):
        pass
