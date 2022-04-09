
from django.core.paginator import Paginator
from django.utils import timezone

from proposition.models.proposition import Proposition
from proposition.models.status import Status


class Manager():
    """Manager app class.
    """
    def __init__(self):
        pass

    def set_page_objects_context(self, request, search_input):
        propositions = self.__get_proposition_queryset(request, search_input)
        paginator = Paginator(propositions, 1)
        page_number = request.GET.get('page')
        page_objects = paginator.get_page(page_number)
        return page_objects

    def __get_proposition_queryset(self, request, search_input):
        queryset = None
        if search_input:
            queryset = (
                Proposition.objects.filter(
                    proposition_creator_id__collectivity_id__exact=
                    request.user.collectivity,
                    name__icontains=search_input
                ).order_by('-creation_date')|
                Proposition.objects.filter(
                    proposition_creator_id__collectivity_id__exact=
                    request.user.collectivity,
                    id__icontains=search_input
                ).order_by('-creation_date')|
                Proposition.objects.filter(
                    proposition_creator_id__collectivity_id__exact=
                    request.user.collectivity,
                    proposition_creator_id__email__icontains=search_input
                ).order_by('-creation_date')|
                Proposition.objects.filter(
                    proposition_creator_id__collectivity_id__exact=
                    request.user.collectivity,
                    proposition_taker_id__email__icontains=search_input
                ).order_by('-creation_date')
            )
        else:
            queryset = (
                Proposition.objects.filter(
                    proposition_creator_id__collectivity_id__exact=
                    request.user.collectivity
                ).order_by('-creation_date')
            )
        return queryset

    def set_session_vars(self, request, search_input):
        request.session['c_p_v_f_search_input'] = search_input
    
    def create_proposition(self, form, custom_user):
        """Method for creating Proposition instances into DB
        """
        Proposition.objects.create(
            name=form.cleaned_data['name'],
            description=form.cleaned_data['description'],
            creation_date=timezone.now(),
            start_date=form.cleaned_data['start_date'],
            end_date=form.cleaned_data['end_date'],
            duration=form.cleaned_data['duration'],
            proposition_category = form.cleaned_data['proposition_category'],
            proposition_creator=custom_user,
            proposition_creator_type=(
                form.cleaned_data['proposition_creator_type']
            ),
            proposition_domain=form.cleaned_data['proposition_domain'],
            proposition_kind=form.cleaned_data['proposition_kind'],
            proposition_status=Status.objects.get(name__exact="Nouveau"),
        )

    def set_read_proposition_view_context(self, request, id_proposition):
        context = {}
        proposition = Proposition.objects.get(pk=id_proposition)
        context['proposition'] = proposition
        if proposition.proposition_kind.name == 'Demande':
            html_vars = self.__set_demand_button(request, proposition)
            context['href'] = html_vars['href']
            context['class'] = html_vars['class']
            context['text'] = html_vars['text']
            context['value'] = html_vars['value']
        else:
            context['href'] = None
            context['class'] = None
            context['text'] = None
            context['value'] = None
        return context
    
    def __set_demand_button(self, request, proposition):
        html_vars = {}
        html_href = (
            "/proposition/update_proposition/{0}/".format(proposition.id)
        )
        success_class = (
            "text-success btn btn-block btn-light border border-success"
        )
        danger_class = (
            "text-danger btn btn-block btn-light border border-danger"
        )
        if (
                proposition.proposition_status.name == 'Nouveau' and
                proposition.proposition_taker is None and
                proposition.proposition_creator != request.user
        ):
            html_vars['href'] = html_href
            html_vars['class'] = success_class
            html_vars['text'] = "S'assigner"
            html_vars['value'] = "select"
        elif (
                proposition.proposition_status.name == 'Sélectionné' and
                proposition.proposition_taker == request.user and
                proposition.proposition_creator != request.user
        ):
            html_vars['href'] = html_href
            html_vars['class'] = danger_class
            html_vars['text'] = "Annuler l'assignation"
            html_vars['value'] = "new"
        else:
            html_vars['href'] = None
            html_vars['class'] = None
            html_vars['text'] = None
            html_vars['value'] = "select"

        return html_vars
