"""CollectivityVotingsView module.
"""
from django.shortcuts import render

from vote.forms.collectivity_votings_form import CollectivityVotingsForm
from vote.views.generic_vote_view import GenericVoteView


class CollectivityVotingsView(GenericVoteView):
    """CollectivityVotingsView class.
    """

    def __init__(self):
        super().__init__()
        self.view_template = 'vote/votings.html'
        self.context = {
            'form': CollectivityVotingsForm(),
            'page_objects': None,
        }

    def get(self, request):
        """CollectivityVotingsView method on client get request.
        """
        search_input = request.session.get('c_v_v_f_search_input', None)
        if search_input:
            self.context['page_objects'] = (
                self.manager.set_page_objects_context(request, search_input)
            )
            return render(request, self.view_template, self.context)
        self.context['page_objects'] = (
            self.manager.set_page_objects_context(request, False)
        )
        return render(request, self.view_template, self.context)

    def post(self, request):
        """CollectivityVotingsView method on client post request.
        """
        if request.POST.get('cvf_search_button') == 'yes':
            form = CollectivityVotingsForm(request.POST)
            if form.is_valid():
                search_input = form.cleaned_data['search_input']
                self.context['page_objects'] = (
                    self.manager.set_page_objects_context(
                        request, search_input
                    )
                )
                self.manager.set_session_vars(request, search_input)
            else:
                self.context['form'] = form
                self.context['page_objects'] = (
                    self.manager.set_page_objects_context(request, False)
                )
        else:
            self.context['page_objects'] = (
                self.manager.set_page_objects_context(request, False)
            )
            self.manager.set_session_vars(request, False)
        return render(request, self.view_template, self.context)
