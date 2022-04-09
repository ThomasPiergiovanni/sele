"""Test proposition emulation module.
"""
from datetime import datetime, date

from django.utils import timezone

from authentication.tests.emulation.authentication_emulation import (
    AuthenticationEmulation
)
from proposition.models.category import Category
from proposition.models.creator_type import CreatorType
from proposition.models.domain import Domain
from proposition.models.kind import Kind
from proposition.models.proposition import Proposition
from proposition.models.rating import Rating
from proposition.models.status import Status

class PropositionEmulation():
    """Test PropositionEmulation class.
    """
    def __init__(self):
        self.auth_emulation = AuthenticationEmulation()

    def emulate_category(self):
        Category.objects.create(id=1, name="Activité")
        Category.objects.create(id=2, name="Produit")
    
    def emulate_creator_type(self):
        CreatorType.objects.create(id=1, name="Collective")
        CreatorType.objects.create(id=2, name="Individuelle")

    def emulate_domain(self):
        Domain.objects.create(id=1, name="Santé")
        Domain.objects.create(id=2, name="Support à l'entreprise")

    def emulate_kind(self):
        Kind.objects.create(id=1, name="Demande")
        Kind.objects.create(id=2, name="Offre")

    def emulate_proposition(self):
        """
        """
        self.auth_emulation.emulate_custom_user()
        self.emulate_category()
        self.emulate_creator_type()
        self.emulate_domain()
        self.emulate_kind()
        self.emulate_rating()
        self.emulate_status()
        Proposition.objects.create(
            id=1,
            name="DCours1",
            description=(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
            ),
            creation_date=datetime(
                2022, 1, 1, 21, 56, 22, tzinfo=timezone.utc
            ),
            start_date=date(2022, 1, 1),
            end_date=date(2022, 1, 11),
            duration=120,
            proposition_category_id=1,
            proposition_creator_id=1,
            proposition_creator_type_id=1,
            proposition_domain_id=1,
            proposition_kind_id=1,
            proposition_rating_id=1,
            proposition_status_id=1,
            proposition_taker_id=3
        ),
        Proposition.objects.create(
            id=2,
            name="DCours2",
            description=(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
            ),
            creation_date=datetime(
                2022, 1, 2, 21, 56, 22, tzinfo=timezone.utc
            ),
            start_date=date(2022, 1, 1),
            end_date=date(2022, 1, 11),
            duration=120,
            proposition_category_id=1,
            proposition_creator_id=1,
            proposition_creator_type_id=1,
            proposition_domain_id=1,
            proposition_kind_id=1,
            proposition_rating_id=1,
            proposition_status_id=2,
            proposition_taker_id=3
        )
        Proposition.objects.create(
            id=3,
            name="DCours3",
            description=(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
            ),
            creation_date=datetime(
                2022, 1, 3, 21, 56, 22, tzinfo=timezone.utc
            ),
            start_date=date(2022, 1, 1),
            end_date=date(2022, 1, 11),
            duration=120,
            proposition_category_id=1,
            proposition_creator_id=1,
            proposition_creator_type_id=1,
            proposition_domain_id=1,
            proposition_kind_id=1,
            proposition_rating_id=1,
            proposition_status_id=3,
            proposition_taker_id=None
        ),
        Proposition.objects.create(
            id=4,
            name="DCours4",
            description=(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
            ),
            creation_date=datetime(
                2022, 1, 4, 21, 56, 22, tzinfo=timezone.utc
            ),
            start_date=date(2022, 1, 1),
            end_date=date(2022, 1, 11),
            duration=120,
            proposition_category_id=1,
            proposition_creator_id=1,
            proposition_creator_type_id=1,
            proposition_domain_id=1,
            proposition_kind_id=1,
            proposition_rating_id=1,
            proposition_status_id=4,
            proposition_taker_id=3
        ),
        Proposition.objects.create(
            id=5,
            name="DCours5",
            description=(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
            ),
            creation_date=datetime(
                2022, 1, 5, 21, 56, 22, tzinfo=timezone.utc
            ),
            start_date=date(2022, 1, 1),
            end_date=date(2022, 1, 11),
            duration=120,
            proposition_category_id=1,
            proposition_creator_id=1,
            proposition_creator_type_id=1,
            proposition_domain_id=1,
            proposition_kind_id=1,
            proposition_rating_id=1,
            proposition_status_id=5,
            proposition_taker_id=3
        ),
        Proposition.objects.create(
            id=6,
            name="DCours6",
            description=(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
            ),
            creation_date=datetime(
                2022, 1, 6, 21, 56, 22, tzinfo=timezone.utc
            ),
            start_date=date(2022, 1, 1),
            end_date=date(2022, 1, 11),
            duration=120,
            proposition_category_id=1,
            proposition_creator_id=1,
            proposition_creator_type_id=1,
            proposition_domain_id=1,
            proposition_kind_id=1,
            proposition_rating_id=1,
            proposition_status_id=6,
            proposition_taker_id=3
        ),
        Proposition.objects.create(
            id=7,
            name="DCours7",
            description=(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
            ),
            creation_date=datetime(
                2022, 1, 7, 21, 56, 22, tzinfo=timezone.utc
            ),
            start_date=date(2022, 1, 1),
            end_date=date(2022, 1, 11),
            duration=120,
            proposition_category_id=1,
            proposition_creator_id=1,
            proposition_creator_type_id=1,
            proposition_domain_id=1,
            proposition_kind_id=1,
            proposition_rating_id=1,
            proposition_status_id=7,
            proposition_taker_id=3
        ),
        Proposition.objects.create(
            id=11,
            name="OCours11",
            description=(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
            ),
            creation_date=datetime(
                2022, 1, 11, 21, 56, 22, tzinfo=timezone.utc
            ),
            start_date=date(2022, 1, 1),
            end_date=date(2022, 1, 11),
            duration=120,
            proposition_category_id=1,
            proposition_creator_id=1,
            proposition_creator_type_id=1,
            proposition_domain_id=1,
            proposition_kind_id=2,
            proposition_rating_id=1,
            proposition_status_id=1,
            proposition_taker_id=3
        ),
        Proposition.objects.create(
            id=12,
            name="OCours12",
            description=(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
            ),
            creation_date=datetime(
                2022, 1, 12, 21, 56, 22, tzinfo=timezone.utc
            ),
            start_date=date(2022, 1, 1),
            end_date=date(2022, 1, 11),
            duration=120,
            proposition_category_id=1,
            proposition_creator_id=1,
            proposition_creator_type_id=1,
            proposition_domain_id=1,
            proposition_kind_id=2,
            proposition_rating_id=1,
            proposition_status_id=2,
            proposition_taker_id=3
        )
        Proposition.objects.create(
            id=13,
            name="OCours13",
            description=(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
            ),
            creation_date=datetime(
                2022, 1, 13, 21, 56, 22, tzinfo=timezone.utc
            ),
            start_date=date(2022, 1, 1),
            end_date=date(2022, 1, 11),
            duration=120,
            proposition_category_id=1,
            proposition_creator_id=1,
            proposition_creator_type_id=1,
            proposition_domain_id=1,
            proposition_kind_id=2,
            proposition_rating_id=1,
            proposition_status_id=3,
            proposition_taker_id=None
        ),
        Proposition.objects.create(
            id=14,
            name="OCours14",
            description=(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
            ),
            creation_date=datetime(
                2022, 1, 14, 21, 56, 22, tzinfo=timezone.utc
            ),
            start_date=date(2022, 1, 1),
            end_date=date(2022, 1, 11),
            duration=120,
            proposition_category_id=1,
            proposition_creator_id=1,
            proposition_creator_type_id=1,
            proposition_domain_id=1,
            proposition_kind_id=2,
            proposition_rating_id=1,
            proposition_status_id=4,
            proposition_taker_id=3
        ),
        Proposition.objects.create(
            id=15,
            name="OCours15",
            description=(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
            ),
            creation_date=datetime(
                2022, 1, 15, 21, 56, 22, tzinfo=timezone.utc
            ),
            start_date=date(2022, 1, 1),
            end_date=date(2022, 1, 11),
            duration=120,
            proposition_category_id=1,
            proposition_creator_id=1,
            proposition_creator_type_id=1,
            proposition_domain_id=1,
            proposition_kind_id=2,
            proposition_rating_id=1,
            proposition_status_id=5,
            proposition_taker_id=3
        ),
        Proposition.objects.create(
            id=16,
            name="OCours16",
            description=(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
            ),
            creation_date=datetime(
                2022, 1, 16, 21, 56, 22, tzinfo=timezone.utc
            ),
            start_date=date(2022, 1, 1),
            end_date=date(2022, 1, 11),
            duration=120,
            proposition_category_id=1,
            proposition_creator_id=1,
            proposition_creator_type_id=1,
            proposition_domain_id=1,
            proposition_kind_id=2,
            proposition_rating_id=1,
            proposition_status_id=6,
            proposition_taker_id=3
        ),
        Proposition.objects.create(
            id=17,
            name="OCours17",
            description=(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
            ),
            creation_date=datetime(
                2022, 1, 17, 21, 56, 22, tzinfo=timezone.utc
            ),
            start_date=date(2022, 1, 1),
            end_date=date(2022, 1, 11),
            duration=120,
            proposition_category_id=1,
            proposition_creator_id=1,
            proposition_creator_type_id=1,
            proposition_domain_id=1,
            proposition_kind_id=2,
            proposition_rating_id=1,
            proposition_status_id=7,
            proposition_taker_id=3
        )

    

    def emulate_rating(self):
        """
        """
        Rating.objects.create(id=1, rate=1)
        Rating.objects.create(id=2, rate=2)

    def emulate_status(self):
        """
        """
        Status.objects.create(id=1, name="Annulé")
        Status.objects.create(id=2, name="En cours")
        Status.objects.create(id=3, name="Nouveau")
        Status.objects.create(id=4, name="Réalisé")
        Status.objects.create(id=5, name="Rejeté")
        Status.objects.create(id=6, name="Sélectionné")
        Status.objects.create(id=7, name="Terminé")