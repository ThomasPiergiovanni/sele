from datetime import date

from django.core.paginator import Paginator
from django.utils import timezone

from proposition.models.proposition import Proposition
from proposition.models.status import Status
from proposition.forms.collectivity_propositions_form import (
    CollectivityPropositionsForm
)



class Manager():
    """Manager app class.
    """
    def __init__(self):
        pass

    def set_form_context(self, attribute, order):
        context_form = CollectivityPropositionsForm(
            initial = {'attribute_selector': attribute, 'order_selector': order}
        )
        return context_form

    def set_page_objects_context(self, request, attribute, order):
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

    def set_session_vars(self, request, attribute, order):
        request.session['c_p_v_f_attribute'] = attribute
        request.session['c_p_v_f_order'] = order
    
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
