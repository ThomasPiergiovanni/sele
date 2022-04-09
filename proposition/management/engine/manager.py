
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
        paginator = Paginator(propositions, 4)
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
        if proposition.proposition_kind.name == 'Demande':
            context = self.__set_demand_btn(request, proposition)
        else:
            context = self.__set_offer_btn(request, proposition)
        context['proposition'] = proposition
        return context
    
    def __set_demand_btn(self, request, proposition):
        """
        """
        href = (
            "/proposition/update_proposition/{0}/".format(proposition.id)
        )
        success = "text-success btn btn-block btn-light border border-success"
        danger = "text-danger btn btn-block btn-light border border-danger"
        warning = "text-warning btn btn-block btn-light border border-warning"
        if (
                proposition.proposition_status.name == 'Nouveau' and
                proposition.proposition_taker is None and
                proposition.proposition_creator != request.user
        ):
            btn = self.__set_btn_dict(href, success, "Sélectionner", "select")
        elif (
                proposition.proposition_status.name == 'Sélectionné' and
                proposition.proposition_taker == request.user
        ):
            btn = self.__set_btn_dict(href, danger, "Annuler", "new")
        elif (
                proposition.proposition_status.name == 'Sélectionné' and
                proposition.proposition_creator == request.user
        ):
            btn = self.__set_btn_dict(href, success, "Confirmer", "inprogress")
        elif (
                proposition.proposition_status.name == 'En cours' and
                proposition.proposition_taker == request.user
        ):
            btn = self.__set_btn_dict(
                href, success, "Terminer", "realized",
                href, danger, "Annuler", "new",
            )
        elif (
                proposition.proposition_status.name == 'Réalisé' and
                proposition.proposition_creator == request.user
        ):
            btn = self.__set_btn_dict(
                href, success, "Valider", "done",
                href, danger, "Rejeter", "rejected",
            )
        elif (
                proposition.proposition_status.name == 'Rejeté' and
                proposition.proposition_taker == request.user
        ):
            btn = self.__set_btn_dict(
                href, success, "Reprendre", "inprogress",
                href, warning, "Forcer terminer", "done",
            )
        elif (
                proposition.proposition_status.name == 'Rejeté' and
                proposition.proposition_creator == request.user
        ):
            btn = self.__set_btn_dict(href, success, "Valider", "done")
        else:
            btn = self.__set_btn_dict()
        return btn
    
    def __set_btn_dict(self, *args):
        btn = {}
        btn['btn1_href'] = self.__check_index(args, 0)
        btn['btn1_class'] = self.__check_index(args, 1)
        btn['btn1_text'] = self.__check_index(args, 2)
        btn['btn1_value'] = self.__check_index(args, 3)
        btn['btn2_href'] = self.__check_index(args, 4)
        btn['btn2_class'] = self.__check_index(args, 5)
        btn['btn2_text'] = self.__check_index(args, 6)
        btn['btn2_value'] = self.__check_index(args, 7)
        return btn

    def __check_index(self, arg, i):
        try:
            return arg[i]
        except IndexError:
            return None

    def __set_offer_btn(self, request, proposition):
        """
        """
        href = (
            "/proposition/update_proposition/{0}/".format(proposition.id)
        )
        success = "text-success btn btn-block btn-light border border-success"
        danger = "text-danger btn btn-block btn-light border border-danger"
        warning = "text-warning btn btn-block btn-light border border-warning"
        if (
                proposition.proposition_status.name == 'Nouveau' and
                proposition.proposition_taker is None and
                proposition.proposition_creator != request.user
        ):
            btn = self.__set_btn_dict(href, success, "Sélectionner", "select")
        elif (
                proposition.proposition_status.name == 'Sélectionné' and
                proposition.proposition_taker == request.user
        ):
            btn = self.__set_btn_dict(href, danger, "Annuler", "new")
        elif (
                proposition.proposition_status.name == 'Sélectionné' and
                proposition.proposition_creator == request.user
        ):
            btn = self.__set_btn_dict(href, success, "Commencer", "inprogress")
        elif (
                proposition.proposition_status.name == 'En cours' and
                proposition.proposition_creator == request.user
        ):
            btn = self.__set_btn_dict(href, success, "Terminer", "realized")
        elif (
                proposition.proposition_status.name == 'Réalisé' and
                proposition.proposition_taker == request.user
        ):
            btn = self.__set_btn_dict(
                href, success, "Valider", "done",
                href, danger, "Rejeter", "rejected",
            )
        elif (
                proposition.proposition_status.name == 'Rejeté' and
                proposition.proposition_taker == request.user
        ):
            btn = self.__set_btn_dict(href, success, "Valider", "done")
        elif (
                proposition.proposition_status.name == 'Rejeté' and
                proposition.proposition_creator == request.user
        ):
            btn = self.__set_btn_dict(
                href, success, "Reprendre", "inprogress",
                href, warning, "Forcer terminer", "done",
            )
        else:
            btn = self.__set_btn_dict()
        return btn
