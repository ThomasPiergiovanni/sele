# pylint: disable=E1101,R0201,W0106
""" DB management command
"""
from django.core.management.base import BaseCommand
from django.utils import timezone

from proposition.models import Proposition


class Command(BaseCommand):
    """ Update outdated proposition status.
    """

    help = "Update outdated proposition status."

    def __init__(self):
        super().__init__()

    def handle(self, *args, **options):
        self.__update_outdated_proposition()

    def __update_outdated_proposition(self):
        propositions = Proposition.objects.filter(
            end_date__lte=timezone.now(),
            proposition_status_id__exact='3'
        )
        for proposition in propositions:
            proposition.proposition_status_id = 1
            proposition.save()
