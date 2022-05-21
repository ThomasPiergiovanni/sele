"""CollectivityPropositionsView module.
"""
from django.shortcuts import render

from proposition.forms.collectivity_propositions_form import (
    CollectivityPropositionsForm
)
from proposition.views.generic_proposition_view import (
    GenericPropositionView
)


class CollectivityPropositionsView(GenericPropositionView):
    """CollectivityPropositionsView class.
    """

    def __init__(self):
        super().__init__()
        self.view_template = 'proposition/propositions.html'
        self.context = {
            'form': CollectivityPropositionsForm(),
            'page_objects': None,
        }

    def get(self, request):
        """CollectivityPropositionsView method on client get request.
        """
        search_input = request.session.get('c_p_v_f_search_input', None)
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
        """CollectivityPropositionsView method on client post request.
        """
        if request.POST.get('cpf_search_button') == 'yes':
            form = CollectivityPropositionsForm(request.POST)
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
