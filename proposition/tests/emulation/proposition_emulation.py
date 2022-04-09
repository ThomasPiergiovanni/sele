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
            name="Cours de Python",
            description=(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
                " Sed non risus. Suspendisse lectus tortor, dignissim sit"
                " amet, adipiscing nec, ultricies sed, dolor. Cras elementum"
                " ultrices diam. Maecenas ligula massa, varius a, semper"
            ),
            creation_date=datetime(
                2022, 1, 20, 15, 56, 22, tzinfo=timezone.utc
            ),
            start_date=date(2021, 12, 25),
            end_date=date(2022, 1, 25),
            duration=120,
            proposition_category_id=2,
            proposition_creator_id=1,
            proposition_creator_type_id=1,
            proposition_domain_id=1,
            proposition_kind_id=1,
            proposition_rating_id=1,
            proposition_status_id=1,
            proposition_taker_id=2
        ),
        Proposition.objects.create(
            id=2,
            name="Nettoyage du Mur",
            description=(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
                " Sed non risus. Suspendisse lectus tortor, dignissim sit"
                " amet, adipiscing nec, ultricies sed, dolor. Cras elementum"
                " ultrices diam. Maecenas ligula massa, varius a, semper"
            ),
            creation_date=datetime(
                2022, 1, 23, 8, 21, 3, tzinfo=timezone.utc
            ),
            start_date=date(2021, 12, 28),
            end_date=date(2022, 1, 3),
            duration=3680,
            proposition_category_id=2,
            proposition_creator_id=2,
            proposition_creator_type_id=2,
            proposition_domain_id=2,
            proposition_kind_id=2,
            proposition_rating_id=2,
            proposition_status_id=2,
            proposition_taker_id=1
        )
        Proposition.objects.create(
            id=3,
            name="Cours de Java",
            description=(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
                " Sed non risus. Suspendisse lectus tortor, dignissim sit"
                " amet, adipiscing nec, ultricies sed, dolor. Cras elementum"
                " ultrices diam. Maecenas ligula massa, varius a, semper"
            ),
            creation_date=datetime(
                2022, 3, 15, 1, 1, 22, tzinfo=timezone.utc
            ),
            start_date=date(2022, 3, 15),
            end_date=date(2022, 3, 25),
            duration=240,
            proposition_category_id=2,
            proposition_creator_id=1,
            proposition_creator_type_id=2,
            proposition_domain_id=2,
            proposition_kind_id=2,
            proposition_rating_id=2,
            proposition_status_id=2,
            proposition_taker_id=1
        ),
        Proposition.objects.create(
            id=4,
            name="Cours de CSS",
            description=(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
            ),
            creation_date=datetime(
                2022, 2, 15, 1, 1, 22, tzinfo=timezone.utc
            ),
            start_date=date(2022, 3, 15),
            end_date=date(2022, 3, 25),
            duration=240,
            proposition_category_id=2,
            proposition_creator_id=1,
            proposition_creator_type_id=1,
            proposition_domain_id=2,
            proposition_kind_id=1,
            proposition_rating_id=2,
            proposition_status_id=3,
            proposition_taker_id=None
        ),
        Proposition.objects.create(
            id=5,
            name="Cours de JS",
            description=(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
            ),
            creation_date=datetime(
                2022, 2, 16, 1, 1, 22, tzinfo=timezone.utc
            ),
            start_date=date(2022, 3, 15),
            end_date=date(2022, 3, 25),
            duration=240,
            proposition_category_id=2,
            proposition_creator_id=1,
            proposition_creator_type_id=2,
            proposition_domain_id=2,
            proposition_kind_id=2,
            proposition_rating_id=2,
            proposition_status_id=4,
            proposition_taker_id=1
        ),
        Proposition.objects.create(
            id=6,
            name="Cours de HTML",
            description=(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
            ),
            creation_date=datetime(
                2022, 2, 17, 1, 1, 22, tzinfo=timezone.utc
            ),
            start_date=date(2022, 3, 15),
            end_date=date(2022, 3, 25),
            duration=240,
            proposition_category_id=2,
            proposition_creator_id=1,
            proposition_creator_type_id=2,
            proposition_domain_id=2,
            proposition_kind_id=2,
            proposition_rating_id=2,
            proposition_status_id=5,
            proposition_taker_id=1
        ),
        Proposition.objects.create(
            id=7,
            name="Cours de Node",
            description=(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
            ),
            creation_date=datetime(
                2022, 2, 18, 1, 1, 22, tzinfo=timezone.utc
            ),
            start_date=date(2022, 3, 15),
            end_date=date(2022, 3, 25),
            duration=240,
            proposition_category_id=2,
            proposition_creator_id=1,
            proposition_creator_type_id=2,
            proposition_domain_id=2,
            proposition_kind_id=2,
            proposition_rating_id=2,
            proposition_status_id=5,
            proposition_taker_id=1
        ),
        Proposition.objects.create(
            id=8,
            name="Cours de React",
            description=(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
            ),
            creation_date=datetime(
                2022, 2, 19, 1, 1, 22, tzinfo=timezone.utc
            ),
            start_date=date(2022, 3, 15),
            end_date=date(2022, 3, 25),
            duration=240,
            proposition_category_id=2,
            proposition_creator_id=1,
            proposition_creator_type_id=2,
            proposition_domain_id=2,
            proposition_kind_id=2,
            proposition_rating_id=2,
            proposition_status_id=6,
            proposition_taker_id=3
        ),
        Proposition.objects.create(
            id=9,
            name="Cours de JQuery",
            description=(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
            ),
            creation_date=datetime(
                2022, 2, 20, 1, 1, 22, tzinfo=timezone.utc
            ),
            start_date=date(2022, 3, 15),
            end_date=date(2022, 3, 25),
            duration=240,
            proposition_category_id=2,
            proposition_creator_id=1,
            proposition_creator_type_id=2,
            proposition_domain_id=2,
            proposition_kind_id=2,
            proposition_rating_id=2,
            proposition_status_id=7,
            proposition_taker_id=1
        ),
    

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