from django.core.paginator import Paginator

from proposition.models.proposition import Proposition
from proposition.forms.collectivity_propositions_form import (
    CollectivityPropositionsForm
)


class Manager():
    """Manager app class.
    """
    def __init__(self):
        pass

    def set_colvity_propositions_form_context(self, attribute, order):
        context_form = CollectivityPropositionsForm(
            initial = {
                'attribute_selector': attribute,
                'order_selector': order
            }
        )
        return context_form

    def set_colvity_propositions_page_obj_context(
        self, request, attribute, order
    ):
        propositions = self.__get_sorted_propositions(request, attribute, order)
        paginator = Paginator(propositions, 3)
        page_number = request.GET.get('page')
        page_objects = paginator.get_page(page_number)
        return page_objects

    def __get_sorted_propositions(self, request, attribute, order):
        if attribute == 'name' and order == 'asc':
            return self.__get_proposition_queryset(request, 'creation_date')
        elif attribute == 'name' and order == 'desc':
            return self.__get_proposition_queryset(request, '-creation_date')
        elif attribute == 'proposition_kind' and order == 'asc':
            return self.__get_proposition_queryset(request, 'proposition_kind')
        elif attribute == 'proposition_kind' and order == 'desc':
            return self.__get_proposition_queryset(request, '-proposition_kind')
        elif attribute == 'proposition_domain' and order == 'asc':
            return self.__get_proposition_queryset(request, 'proposition_domain')
        elif attribute == 'proposition_domain' and order == 'desc':
            return self.__get_proposition_queryset(request, '-proposition_domain')
        elif attribute == 'duration' and order == 'asc':
            return self.__get_proposition_queryset(request, 'duration')
        elif attribute == 'duration' and order == 'desc':
            return self.__get_proposition_queryset(request, '-duration')
        elif attribute == 'proposition_status' and order == 'asc':
            return self.__get_proposition_queryset(request, 'proposition_status')
        elif attribute == 'proposition_status' and order == 'desc':
            return self.__get_proposition_queryset(request, '-proposition_status')
        elif attribute == 'proposition_creator' and order == 'asc':
            return self.__get_proposition_queryset(request, 'proposition_creator')
        elif attribute == 'proposition_creator' and order == 'desc':
            return self.__get_proposition_queryset(request, '-proposition_creator')
        elif attribute == 'proposition_taker' and order == 'asc':
            return self.__get_proposition_queryset(request, 'proposition_taker')
        elif attribute == 'proposition_taker' and order == 'desc':
            return self.__get_proposition_queryset(request, '-proposition_taker')
        elif attribute == 'creation_date' and order == 'asc':
            return self.__get_proposition_queryset(request, 'creation_date')
        elif attribute == 'creation_date' and order == 'desc':
            return self.__get_proposition_queryset(request, '-creation_date')
        else:
            return self.__get_proposition_queryset(request, '-creation_date')   
    
    def __get_proposition_queryset(self, request, parameter):
        return Proposition.objects.filter(
            proposition_creator_id__collectivity_id__exact=
            request.user.collectivity
        ).order_by(parameter)

