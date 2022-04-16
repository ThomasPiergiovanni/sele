
from django.core.paginator import Paginator
from django.utils import timezone

from authentication.models import CustomUser
from chat.management.engine.manager import Manager as ChatManager
from chat.forms.comment_form import CommentForm
from chat.models.comment import Comment
from chat.models.discussion import Discussion
from chat.models.discussion_type import DiscussionType
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
                ).order_by('-creation_date')|
                Proposition.objects.filter(
                    proposition_creator_id__collectivity_id__exact=
                    request.user.collectivity,
                    proposition_status_id__name__icontains=search_input
                ).order_by('-creation_date')|
                Proposition.objects.filter(
                    proposition_creator_id__collectivity_id__exact=
                    request.user.collectivity,
                    proposition_kind_id__name__icontains=search_input
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
            proposition_discussion=Discussion.objects.all().last()
        )
    
    def create_discussion(self, form, custom_user):
        form.cleaned_data['subject'] = form.cleaned_data['name']
        chat_manager = ChatManager()
        discussion_type = DiscussionType.objects.get(name__exact='Proposition')
        chat_manager.create_discussion(form, custom_user, discussion_type)

    # TOTEST
    def set_read_proposition_view_context(self, request, id_proposition):
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
    # /TOTEST
 
    def __set_demand_btn(self, request, proposition):
        """
        """
        href = (
            "/proposition/update_proposition/{0}/".format(proposition.id)
        )
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

    #TOTEST
    def __get_discussion(self, proposition):
        discussion = None
        try:
            discussion = proposition.proposition_discussion
        except:
            pass
        return discussion

    def __get_comments(self, proposition):
        comments = None
        try:
            comments = Comment.objects.filter(
                comment_discussion_id__exact=proposition
                .proposition_discussion.id
            )
        except:
            pass
        return  comments


    def create_comment(self, form, custom_user, id_proposition):
        discussion = (
            Proposition.objects.get(pk=id_proposition).proposition_discussion
        )
        chat_manager = ChatManager()
        chat_manager.create_comment(form, custom_user, discussion.id)
    #/TOTEST

    def set_proposition_status(self, request, id_proposition):
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
        else:
            pass
        proposition.save()
    
    def __set_status(self, argument):
        return Status.objects.get(name__exact=argument)

