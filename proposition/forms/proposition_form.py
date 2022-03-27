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
    question = CharField(
        label='Question',
        max_length=256,
        widget=TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'id': 'input_voting_question',
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
                'id': 'input_voting_description',
                'rows':4
            }
        )
    )
    opening_date = DateField(
        label='Date d\'ouverture du vote',
        widget=DateInput(
            attrs={
                'type': 'date',
                'class': 'input-group date form-control form-control-sm',
                'data-target-input': "nearest",
                'id': 'input_voting_opening_date',
            }
        )
    )
    closure_date = DateField(
        label='Date de fermeture du vote',
        widget=DateInput(
            attrs={
                'type': 'date',
                'class': 'input-group date form-control form-control-sm',
                'data-target-input': "nearest",
                'id': 'input_voting_closure_date',
            }
        )
    )
    voting_method = ModelChoiceField(
        queryset=VotingMethod.objects.all(),
        label='Mode de scrutin',
        empty_label="",
        widget=Select(
            attrs={
                'class': 'form-control form-control-sm',
                'id': 'input_voting_voting_method',
            },
        )
    )

    class Meta:
        model = Voting
        fields = (
            'question', 'description', 'voting_method', 'opening_date',
            'closure_date'
        )
