# from chat.models.discussion import Comment
from datetime import date


from chat.models.discussion import Discussion


class Manager():
    """Manager manager class.
    """
    def __init__(self):
        pass

    def create_discussion(self, form, custom_user):
        """Method creating Discussion instances into DB
        """
        Discussion.objects.create(
            subject=form.cleaned_data['subject'],
            creation_date=date.today(),
            discussion_custom_user = custom_user
        )