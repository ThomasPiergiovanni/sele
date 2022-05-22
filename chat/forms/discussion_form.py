# pylint: disable=R0903
"""Discussion form module
"""
from django.forms import CharField, ModelForm, TextInput

from chat.models import Discussion


class DiscussionForm(ModelForm):
    """DiscussionForm class. Used for adding Discussion.
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
        """ModelForm "inner" metadata class.
        """
        model = Discussion
        fields = ('subject',)
