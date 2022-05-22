# pylint: disable=E1101,R0201
"""Proposition manager module.
"""
from django.core.paginator import Paginator
from django.utils import timezone

from authentication.models import CustomUser
from chat.forms.comment_form import CommentForm
from chat.management.engine.manager import Manager as ChatManager
from chat.models import Comment, Discussion, DiscussionType
from proposition.models import Proposition, Status


class Manager():
    """Proposition manager class.
    """

    def set_page_objects_context(self, request, search_input):
        """Method setting Proposition page objects.
        """
        propositions = self.__get_proposition_queryset(request, search_input)
        paginator = Paginator(propositions, 4)
        page_number = request.GET.get('page')
        page_objects = paginator.get_page(page_number)
        return page_objects

    def __get_proposition_queryset(self, request, search_input):
        """Method getting Propsition queryset.
        """
        queryset = None
        if search_input:
            queryset = (
                Proposition.objects.filter(
                    proposition_creator_id__collectivity_id__exact=request
                    .user.collectivity, name__icontains=search_input
                ).order_by('-creation_date') | Proposition.objects.filter(
                    proposition_creator_id__collectivity_id__exact=request
                    .user.collectivity, id__icontains=search_input
                ).order_by('-creation_date') | Proposition.objects.filter(
                    proposition_creator_id__collectivity_id__exact=request
                    .user.collectivity,
                    proposition_creator_id__email__icontains=search_input
                ).order_by('-creation_date') | Proposition.objects.filter(
                    proposition_creator_id__collectivity_id__exact=request
                    .user.collectivity,
                    proposition_taker_id__email__icontains=search_input
                ).order_by('-creation_date') | Proposition.objects.filter(
                    proposition_creator_id__collectivity_id__exact=request
                    .user.collectivity,
                    proposition_status_id__name__icontains=search_input
                ).order_by('-creation_date') | Proposition.objects.filter(
                    proposition_creator_id__collectivity_id__exact=request
                    .user.collectivity,
                    proposition_kind_id__name__icontains=search_input
                ).order_by('-creation_date')
            )
        else:
            queryset = (
                Proposition.objects.filter(
                    proposition_creator_id__collectivity_id__exact=request
                    .user.collectivity
                ).order_by('-creation_date')
            )
        return queryset

    def set_session_vars(self, request, search_input):
        """Method setting collectivity proposition form search to a session
        variable.
        """
        request.session['c_p_v_f_search_input'] = search_input

    def create_proposition(self, form, custom_user):
        """Method creating Proposition into DB.
        """
        Proposition.objects.create(
            name=form.cleaned_data['name'],
            description=form.cleaned_data['description'],
            creation_date=timezone.now(),
            start_date=form.cleaned_data['start_date'],
            end_date=form.cleaned_data['end_date'],
            duration=form.cleaned_data['duration'],
            proposition_category=form.cleaned_data['proposition_category'],
            proposition_creator=custom_user,
            proposition_creator_type=(
                form.cleaned_data['proposition_creator_type']
            ),
            proposition_domain=form.cleaned_data['proposition_domain'],
            proposition_kind=form.cleaned_data['proposition_kind'],
            proposition_status=Status.objects.get(name__exact="Nouveau"),
            proposition_discussion=Discussion.objects.all().last()
        )

    def proposition_creates_discussion(self, form, custom_user):
        """Method create discussion with proposition.
        """
        form.cleaned_data['subject'] = form.cleaned_data['name']
        chat_manager = ChatManager()
        discussion_type = DiscussionType.objects.get(name__exact='Proposition')
        chat_manager.create_discussion(form, custom_user, discussion_type)

    def set_read_proposition_view_context(self, request, id_proposition):
        """Method setting read proposition view context.
        """
        context = {}
        proposition = Proposition.objects.get(pk=id_proposition)
        if proposition.proposition_kind.name == 'Demande':
            context = self.__set_demand_btn(request, proposition)
        else:
            context = self.__set_offer_btn(request, proposition)
        context['proposition'] = proposition
        context['discussion'] = self.__get_discussion(proposition)
        context['comments'] = self.__get_comments(proposition)
        context['form'] = CommentForm()
        return context

    def __set_demand_btn(self, request, proposition):
        """Method setting demands (proposition kind) button based on
        Proposition status.
        """
        href = f"/proposition/update_proposition/{proposition.id}/"
        success = "btn btn-block btn-success"
        danger = "btn btn-block btn-danger"
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
                href, danger, "Forcer terminer", "done",
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
        """Method setting button keys and values.
        """
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
        """Method checking index arg presence in list.
        """
        try:
            return arg[i]
        except IndexError:
            return None

    def __set_offer_btn(self, request, proposition):
        """Method setting offer (proposition kind) button based on
        Proposition status.
        """
        href = f"/proposition/update_proposition/{proposition.id}/"
        success = "btn btn-block btn-success"
        danger = "btn btn-block btn-danger"
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
                href, danger, "Forcer terminer", "done",
            )
        else:
            btn = self.__set_btn_dict()
        return btn

    def __get_discussion(self, proposition):
        """Method getting Discussion.
        """
        discussion = None
        try:
            discussion = proposition.proposition_discussion
        except AttributeError:
            pass
        return discussion

    def __get_comments(self, proposition):
        """Method getting Comments.
        """
        comments = None
        try:
            comments = Comment.objects.filter(
                comment_discussion_id__exact=proposition
                .proposition_discussion.id
            )
        except AttributeError:
            pass
        return comments

    def create_comment(self, form, custom_user, id_proposition):
        """Method creating Comment.
        """
        discussion = (
            Proposition.objects.get(pk=id_proposition).proposition_discussion
        )
        chat_manager = ChatManager()
        chat_manager.create_comment(form, custom_user, discussion.id)

    def set_proposition_status(self, request, id_proposition):
        """Method setting Proposition status.
        """
        upd_status_btn = request.POST.get('update_status_button')
        proposition = Proposition.objects.get(pk=id_proposition)
        custom_user = CustomUser.objects.get(pk=request.user.id)
        if upd_status_btn == 'select':
            proposition.proposition_status = self.__set_status('Sélectionné')
            proposition.proposition_taker = custom_user
        elif upd_status_btn == 'new':
            proposition.proposition_status = self.__set_status('Nouveau')
            proposition.proposition_taker = None
        elif upd_status_btn == 'inprogress':
            proposition.proposition_status = self.__set_status('En cours')
        elif upd_status_btn == 'realized':
            proposition.proposition_status = self.__set_status('Réalisé')
        elif upd_status_btn == 'rejected':
            proposition.proposition_status = self.__set_status('Rejeté')
        elif upd_status_btn == 'done':
            proposition.proposition_status = self.__set_status('Terminé')
            self.__set_creator_taker_balance(proposition)
        else:
            pass
        proposition.save()

    def __set_status(self, argument):
        """Method setting Status.
        """
        return Status.objects.get(name__exact=argument)

    def __set_creator_taker_balance(self, proposition):
        """Method setting Proposition creator and taker balance.
        """
        if (
                proposition.proposition_kind.name == 'Demande' and
                proposition.proposition_creator_type.name == 'Individuelle'
        ):
            proposition.proposition_creator.balance -= proposition.duration
            proposition.proposition_taker.balance += proposition.duration
            proposition.proposition_creator.save()
        elif (
                proposition.proposition_kind.name == 'Offre'
        ):
            proposition.proposition_creator.balance += proposition.duration
            proposition.proposition_taker.balance -= proposition.duration
            proposition.proposition_creator.save()
        else:
            self.__set_custom_users_balances(proposition)
            proposition.proposition_taker.balance += proposition.duration
        proposition.proposition_taker.save()

    def __set_custom_users_balances(self, proposition):
        custom_users = CustomUser.objects.filter(
            collectivity_id__exact=proposition.proposition_creator
            .collectivity.id
        )
        for custom_user in custom_users:
            custom_user.balance -= proposition.duration/len(custom_users)
            custom_user.save()
