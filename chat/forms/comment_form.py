"""Comment form class
"""
from django.forms import CharField, ModelForm, TextInput

from chat.models.comment import Comment


class CommentForm(ModelForm):
    """CommentForm class. Used for adding comment.
    """
    comment = CharField(
        label='Commenter',
        max_length=256,
        widget=TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'id': 'input_comment_comment',
                'autofocus': True,
            }
        )
    )
    
    class Meta:
        model = Comment
        fields = ('comment',)
