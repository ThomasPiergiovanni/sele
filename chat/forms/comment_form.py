# pylint: disable=R0903
"""Comment form module.
"""
from django.forms import CharField, ModelForm, TextInput

from chat.models import Comment


class CommentForm(ModelForm):
    """CommentForm class. Used for adding Comment.
    """

    comment = CharField(
        label='Commenter',
        max_length=256,
        widget=TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'id': 'input_comment_comment',
                'placeholder': 'Tapez un message...',
                'autofocus': True,
            }
        )
    )

    class Meta:
        """ModelForm used metadata class.
        """
        model = Comment
        fields = ('comment',)
