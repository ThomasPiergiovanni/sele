from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import redirect, render

from chat.forms.comment_form import CommentForm
from proposition.management.engine.manager import Manager


class ReadPropositionView(LoginRequiredMixin, View):
    """ReadPropositionView class.
    """
    login_url = '/authentication/login/'
    redirect_field_name = None

    def __init__(self):
        super().__init__()
        self.manager = Manager()
        self.view_template = 'proposition/read_proposition.html'
        self.post_view_name = 'proposition:read_proposition'
        self.context = None
    
    def get(self, request, id_proposition):
        """Detailed proposition view method on client get request.
        """
        self.context = self.manager.set_read_proposition_view_context(
            request,id_proposition
        )
        return render(request, self.view_template, self.context)

    def post(self, request, id_proposition):
        """Read proposition view method on client post request.
        """
        form = CommentForm(request.POST)        
        if form.is_valid():
            self.manager.create_comment(form, request.user, id_proposition)
            return redirect(self.post_view_name, id_proposition)
        else:
            self.context = {'form': form}
            return render(
                request, self.view_template, self.context
            )
