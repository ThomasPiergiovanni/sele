"""Add voting form
"""
from datetime import date
from django.forms import (
    CharField, DateField, DateInput, IntegerField, ModelForm, Select, Textarea,
    TextInput, 
)

from vote.management.engine.manager import Manager
from vote.models.voting import Voting
from vote.models.voting_method import VotingMethod


class VotingForm(ModelForm):
    """Add voting form class. Used for adding voting.
    """
    question = CharField(
        label='Question',
        max_length=256,
        widget=TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'id': 'input_voting_question'
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
    voting_method = IntegerField(
        label='Mode de scrutin',
        widget=Select(
            attrs={
                'class': 'form-control form-control-sm',
                'id': 'input_voting_voting_method',
            },
            choices=VotingMethod.objects.values_list('id', 'name')
        )
    )

    class Meta:
        model = Voting
        fields = ('question', 'description', 'opening_date', 'closure_date')
