from datetime import date

from django.core.paginator import Paginator
from django.utils import timezone

from vote.forms.collectivity_votings_form import CollectivityVotingsForm
from vote.models.voting import Voting
from vote.models.vote import Vote


class Manager():
    """Manager manager class.
    """
    def __init__(self):
        pass
    
    def create_voting(self, form, custom_user):
        """Method for creating Voting instances into DB
        """
        Voting.objects.create(
            question=form.cleaned_data['question'],
            description=form.cleaned_data['description'],
            creation_date=date.today(),
            opening_date=form.cleaned_data['opening_date'],
            closure_date=form.cleaned_data['closure_date'],
            voting_method=form.cleaned_data['voting_method'],
            voting_custom_user = custom_user
        )
    
    def set_context(self, context, voting , operation):
        votes = Vote.objects.filter(vote_voting_id__exact=voting)
        context['voting'] = voting
        context['voting_operation'] = operation
        context['voting_result'] = self.__get_voting_result(votes)
        context['voting_status'] = self.__get_voting_status(voting)
        return context

    def __get_voting_status(self, voting):
        current_date = date.today()
        if (
            current_date >= voting.opening_date and 
            current_date <= voting.closure_date
        ):
            return 'Ouvert'
        else:
            return 'Fermé'
    
    def __get_voting_result(self, votes):
        counter = 0
        yes_counter = 0
        for vote in votes:
            counter += 1
            if vote.choice:
                yes_counter += 1
        try:
            return yes_counter/counter * 100
        except ZeroDivisionError:
           return None
    
    def set_collectivity_votings_form_context(self, attribute, order):
        context_form = CollectivityVotingsForm(
            initial = {
                'attribute_selector': attribute,
                'order_selector': order
            }
        )
        return context_form
    
    def set_collectivity_votings_page_objects_context(
        self, request, attribute, order
    ):
        votings = self.__get_sorted_votings(request, attribute, order)
        paginator = Paginator(votings, 3)
        page_number = request.GET.get('page')
        page_objects = paginator.get_page(page_number)
        return page_objects
    
    def __get_sorted_votings(self, request, attribute, order):
        if attribute == 'date' and order == 'asc':
            return Voting.objects.filter(
                voting_custom_user_id__collectivity_id__exact=
                request.user.collectivity
            ).order_by('creation_date')
        elif attribute == 'date' and order == 'desc':
            return Voting.objects.filter(
                voting_custom_user_id__collectivity_id__exact=
                request.user.collectivity
            ).order_by('-creation_date')
        elif attribute == 'question' and order == 'asc':
            return Voting.objects.filter(
                voting_custom_user_id__collectivity_id__exact=
                request.user.collectivity
            ).order_by('question')
        else:
            return Voting.objects.filter(
                voting_custom_user_id__collectivity_id__exact=
                request.user.collectivity
            ).order_by('-question')

    def set_session_vars(self, request, attribute, order):
        request.session['c_v_v_f_attribute'] = attribute
        request.session['c_v_v_f_order'] = order


    def create_vote(self, request, id_voting):
        form_vote = request.POST['form_vote']
        choice = False
        if form_vote == 'yes':
            choice = True
        Vote.objects.create(
            choice=choice,
            creation_date=timezone.now(),
            vote_voting_id=id_voting,
            vote_custom_user_id=request.user.id
        )
