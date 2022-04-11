"""Voting form class
"""
from django.forms import CharField, ModelForm, TextInput

from chat.models.discussion import Discussion


class DiscussionForm(ModelForm):
    """DiscussionForm class. Used for adding voting.
    """
    subject = CharField(
        label='Sujet',
        max_length=256,
        widget=TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'id': 'input_discussion_subject',
                'autofocus': True,
            }
        )
    )
    
    class Meta:
        model = Discussion
        fields = ('subject',)
