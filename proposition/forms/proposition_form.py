"""Proposition form class
"""
from django.forms import (
    CharField, DateField, DateInput, ModelChoiceField, ModelForm,
    Select, Textarea, TextInput, 
)

from authentication.models import CustomUser
from proposition.models.category import Category
from proposition.models.creator_type import CreatorType
from proposition.models.domain import Domain
from proposition.models.kind import Kind
from proposition.models.proposition import Proposition
from proposition.models.rating import Rating
from proposition.models.status import Status


class PropositionForm(ModelForm):
    """PropositionForm class. Used for adding voting.
    """
    name = CharField(
        label='Intitulé',
        max_length=128,
        widget=TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'id': 'input_proposition_name',
                'autofocus': True,
            }
        )
    )
    description = CharField(
        label='Description',
        max_length=1000,
        widget=Textarea(
            attrs={
                'class': 'form-control form-control-sm',
                'id': 'input_proposition_description',
                'rows':4
            }
        )
    )
    # opening_date = DateField(
    #     label='Date d\'ouverture du vote',
    #     widget=DateInput(
    #         attrs={
    #             'type': 'date',
    #             'class': 'input-group date form-control form-control-sm',
    #             'data-target-input': "nearest",
    #             'id': 'input_voting_opening_date',
    #         }
    #     )
    # )
    # closure_date = DateField(
    #     label='Date de fermeture du vote',
    #     widget=DateInput(
    #         attrs={
    #             'type': 'date',
    #             'class': 'input-group date form-control form-control-sm',
    #             'data-target-input': "nearest",
    #             'id': 'input_voting_closure_date',
    #         }
    #     )
    # )
    proposition_kind = ModelChoiceField(
        queryset=Kind.objects.all(),
        label='Type de proposition (demande/offre)',
        empty_label="",
        widget=Select(
            attrs={
                'class': 'form-control form-control-sm',
                'id': 'input_proposition_proposition_kind',
            },
        )
    )

    class Meta:
        model = Proposition
        fields = (
            'name', 'description', 'proposition_kind'
        )
