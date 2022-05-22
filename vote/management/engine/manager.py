# pylint: disable=E1101,R0201
"""Vote manager module.
"""
from datetime import date

from django.core.paginator import Paginator
from django.utils import timezone

from vote.models import Vote, Voting


class Manager():
    """Vote manager class.
    """

    def create_voting(self, form, custom_user):
        """Method creating Voting into DB.
        """
        Voting.objects.create(
            question=form.cleaned_data['question'],
            description=form.cleaned_data['description'],
            creation_date=date.today(),
            opening_date=form.cleaned_data['opening_date'],
            closure_date=form.cleaned_data['closure_date'],
            voting_method=form.cleaned_data['voting_method'],
            voting_custom_user=custom_user
        )

    def set_context(self, context, voting, operation):
        """Method setting ReadVotingView context.
        """
        votes = Vote.objects.filter(vote_voting_id__exact=voting)
        context['voting'] = voting
        context['voting_operation'] = operation
        context['voting_result'] = self.__get_voting_result(votes)
        context['voting_status'] = self.__get_voting_status(voting)
        return context

    def __get_voting_status(self, voting):
        """Method getting votings status i.e. if voting is still open
        or not.
        """
        current_date = date.today()
        if voting.opening_date <= current_date <= voting.closure_date:
            return 'Ouvert'
        return 'Fermé'

    def __get_voting_result(self, votes):
        """Method getting votings results.
        """
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

    def set_page_objects_context(self, request, search_input):
        """Method setting Voting page objects.
        """
        votings = self.__get_voting_queryset(request, search_input)
        paginator = Paginator(votings, 3)
        page_number = request.GET.get('page')
        page_objects = paginator.get_page(page_number)
        return page_objects

    def __get_voting_queryset(self, request, search_input):
        """Method getting Voting queryset.
        """
        queryset = None
        if search_input:
            queryset = (
                Voting.objects.filter(
                    voting_custom_user_id__collectivity_id__exact=request
                    .user.collectivity, question__icontains=search_input
                ).order_by('-creation_date') | Voting.objects.filter(
                    voting_custom_user_id__collectivity_id__exact=request
                    .user.collectivity, id__icontains=search_input
                ).order_by('-creation_date')
            )
        else:
            queryset = (
                Voting.objects.filter(
                    voting_custom_user_id__collectivity_id__exact=request
                    .user.collectivity
                ).order_by('-creation_date')
            )
        return queryset

    def set_session_vars(self, request, search_input):
        """Method setting collectivity voting form search to a session
        variable.
        """
        request.session['c_v_v_f_search_input'] = search_input

    def create_vote(self, request, id_voting):
        """Method creating Vote into DB.
        """
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
