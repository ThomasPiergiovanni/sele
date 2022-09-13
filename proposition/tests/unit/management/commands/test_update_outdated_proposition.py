from datetime import date, datetime
from unittest.mock import patch

from django.test import TestCase
from django.utils import timezone

from proposition.management.commands.update_outdated_proposition import Command
from proposition.models import Proposition
from proposition.tests.emulation.proposition_emulation import (
    PropositionEmulation
)


class UpdateOutdatedPropositiionTest(TestCase):

    def setUp(self):

        self.command = Command()
        self.proposition_emulation = PropositionEmulation()
        self.proposition_emulation.emulate_test_setup()

    def mock_set_newday(*args, **kwargs):
        newday = datetime(2022, 1, 12, 0, 0, 1)
        return newday
    
    @patch(
        'proposition.management.commands.update_outdated_proposition'
        '.timezone.now', side_effect=mock_set_newday
    )
    def test_update_outdated_proposition(self, mock_set_newday):
        Proposition.objects.all().delete()
        Proposition.objects.create(
            id=1,
            name="DCours1",
            description=(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
            ),
            creation_date=datetime(
                2022, 1, 2, 0, 0, 1, tzinfo=timezone.utc
            ),
            start_date=date(2022, 1, 2),
            end_date=date(2022, 1, 11),
            duration=120,
            proposition_category_id=1,
            proposition_creator_id=1,
            proposition_creator_type_id=1,
            proposition_domain_id=1,
            proposition_kind_id=1,
            proposition_rating_id=1,
            proposition_status_id=3,
            proposition_taker_id=3,
            proposition_discussion_id=1
        )
        self.command._Command__update_outdated_proposition()
        proposition = Proposition.objects.get(pk=1)
        self.assertEqual(proposition.proposition_status_id, 1)