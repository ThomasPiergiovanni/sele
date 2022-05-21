"""ReadPropositionView module.
"""
from django.shortcuts import redirect, render

from chat.forms.comment_form import CommentForm
from proposition.views.generic_proposition_view import (
    GenericPropositionView
)


class ReadPropositionView(GenericPropositionView):
    """ReadPropositionView class.
    """

    def __init__(self):
        super().__init__()

        self.view_template = 'proposition/read_proposition.html'
        self.post_view_name = 'proposition:read_proposition'
        self.context = None

    def get(self, request, id_proposition):
        """ReadPropositionView method on client get request.
        """
        self.context = self.manager.set_read_proposition_view_context(
            request, id_proposition
        )
        return render(request, self.view_template, self.context)

    def post(self, request, id_proposition):
        """ReadPropositionView method on client post request.
        """
        form = CommentForm(request.POST)
        if form.is_valid():
            self.manager.create_comment(form, request.user, id_proposition)
            return redirect(self.post_view_name, id_proposition)
        self.context = {'form': form}
        return render(
            request, self.view_template, self.context
        )
