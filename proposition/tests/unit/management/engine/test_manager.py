# pylint: disable=C0114,C0115,C0116,E1101,R0904,W0212
from django.contrib.auth import authenticate
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import RequestFactory, TestCase

from authentication.models import CustomUser
from chat.forms.comment_form import CommentForm
from chat.models import Comment, Discussion
from proposition.forms.proposition_form import PropositionForm
from proposition.management.engine.manager import Manager
from proposition.models import (
    Category, CreatorType, Domain, Kind, Proposition, Status
)
from proposition.tests.emulation.proposition_emulation import (
    PropositionEmulation
)


class TestManager(TestCase):

    def setUp(self):
        self.proposition_emulation = PropositionEmulation()
        self.proposition_emulation.emulate_test_setup()
        self.manager = Manager()

    def test_set_page_objects_context(self):
        request = RequestFactory().get('', data={'page': 1})
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user
        page_objects = (
            self.manager.set_page_objects_context(request, 'DCours1')
        )
        self.assertEqual(page_objects[0].id, 1)

    def test_get_proposition_queryset_with_search_input(self):
        request = RequestFactory().get('', data={'page': 1})
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user
        propositions = self.manager._Manager__get_proposition_queryset(
            request, 'DCours1'
        )
        self.assertEqual(propositions[0].id, 1)

    def test_get_proposition_queryset_with_search_input_is_false(self):
        request = RequestFactory().get('', data={'page': 1})
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user
        propositions = self.manager._Manager__get_proposition_queryset(
            request, False
        )
        self.assertEqual(propositions[0].id, 17)

    def test_set_session_vars_with_search_input(self):
        request = RequestFactory().post('')
        session_middleware = SessionMiddleware(request)
        session_middleware.process_request(request)
        self.manager.set_session_vars(request, 'Python')
        self.assertEqual(
            request.session.get('c_p_v_f_search_input'), 'Python'
        )

    def test_create_proposition_with_proposition_instance(self):
        Proposition.objects.all().delete()
        form_data = {
            'name': 'Cours de Python',
            'description': 'dsdss',
            'proposition_kind': Kind.objects.get(pk=1).id,
            'proposition_category': Category.objects.get(pk=1).id,
            'proposition_domain': Domain.objects.get(pk=1).id,
            'start_date': "2022-01-25",
            'end_date': "2022-01-30",
            'duration': 45,
            'proposition_creator_type': CreatorType.objects.get(pk=1).id
        }
        form = PropositionForm(data=form_data)
        form.is_valid()
        custom_user = CustomUser.objects.get(pk=1)
        self.manager.create_proposition(form, custom_user)
        self.assertEqual(
            Proposition.objects.all().last().name, 'Cours de Python'
        )
        self.assertEqual(
            Proposition.objects.all().last()
            .proposition_discussion.discussion_discussion_type.name,
            'Proposition'
        )

    def test_set_proposition_creates_discussion_args_with_discussion(self):
        Discussion.objects.all().delete()
        form_data = {
            'name': 'Cours de Python',
            'description': 'dsdss',
            'proposition_kind': Kind.objects.get(pk=1).id,
            'proposition_category': Category.objects.get(pk=1).id,
            'proposition_domain': Domain.objects.get(pk=1).id,
            'start_date': "2022-01-25",
            'end_date': "2022-01-30",
            'duration': 45,
            'proposition_creator_type': CreatorType.objects.get(pk=1).id
        }
        form = PropositionForm(data=form_data)
        form.is_valid()
        custom_user = CustomUser.objects.get(pk=1)
        self.manager.proposition_creates_discussion(form, custom_user)
        self.assertEqual(
            Discussion.objects.all().last().subject, 'Cours de Python'
        )

    def test_set_read_prop_view_context_with_demand_nouveau_tak_none(self):
        proposition = Proposition.objects.get(pk=3)
        request = RequestFactory().get('')
        user = authenticate(email='user3@email.com', password='xxx_Xxxx')
        request.user = user
        context = self.manager.set_read_proposition_view_context(
            request, proposition.id
        )
        self.assertEqual(
            context['btn1_href'], "/proposition/update_proposition/3/"
        )
        self.assertEqual(context['btn1_class'], "btn btn-block btn-success")
        self.assertEqual(context['btn1_text'], "Sélectionner")
        self.assertEqual(context['btn1_value'], "select")
        self.assertEqual(context['proposition'], proposition)
        self.assertEqual(
            context['discussion'],
            proposition.proposition_discussion
        )
        self.assertEqual(
            context['comments'][0], Comment.objects.get(pk=1)
        )
        self.assertIsInstance(context['form'], CommentForm)

    def test_set_read_prop_view_context_with_offer_selectionne_creator(self):
        proposition = Proposition.objects.get(pk=16)
        request = RequestFactory().get('')
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user
        context = self.manager.set_read_proposition_view_context(
            request, proposition.id
        )
        self.assertEqual(
            context['btn1_href'], "/proposition/update_proposition/16/"
        )
        self.assertEqual(context['btn1_class'], "btn btn-block btn-success")
        self.assertEqual(context['btn1_text'], "Commencer")
        self.assertEqual(context['btn1_value'], "inprogress")

    def test_set_demand_button_with_sta_nouveau_tak_none_cre_not_user(self):
        proposition = Proposition.objects.get(pk=3)
        request = RequestFactory().get('')
        user = authenticate(email='user3@email.com', password='xxx_Xxxx')
        request.user = user
        btn = self.manager._Manager__set_demand_btn(request, proposition)
        self.assertEqual(
            btn['btn1_href'], "/proposition/update_proposition/3/"
        )
        self.assertEqual(btn['btn1_class'], "btn btn-block btn-success")
        self.assertEqual(btn['btn1_text'], "Sélectionner")
        self.assertEqual(btn['btn1_value'], "select")

    def test_set_demand_button_with_sta_selectionne_tak_user(self):
        proposition = Proposition.objects.get(pk=6)
        request = RequestFactory().get('')
        user = authenticate(email='user3@email.com', password='xxx_Xxxx')
        request.user = user
        btn = self.manager._Manager__set_demand_btn(request, proposition)
        self.assertEqual(
            btn['btn1_href'], "/proposition/update_proposition/6/"
        )
        self.assertEqual(btn['btn1_class'], "btn btn-block btn-danger")
        self.assertEqual(btn['btn1_text'], "Annuler")
        self.assertEqual(btn['btn1_value'], "new")

    def test_set_demand_button_with_sta_selectionne_cre_user(self):
        proposition = Proposition.objects.get(pk=6)
        request = RequestFactory().get('')
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user
        btn = self.manager._Manager__set_demand_btn(request, proposition)
        self.assertEqual(
            btn['btn1_href'], "/proposition/update_proposition/6/"
        )
        self.assertEqual(btn['btn1_class'], "btn btn-block btn-success")
        self.assertEqual(btn['btn1_text'], "Confirmer")
        self.assertEqual(btn['btn1_value'], "inprogress")

    def test_set_demand_button_with_sta_en_cours_tak_user(self):
        proposition = Proposition.objects.get(pk=2)
        request = RequestFactory().get('')
        user = authenticate(email='user3@email.com', password='xxx_Xxxx')
        request.user = user
        btn = self.manager._Manager__set_demand_btn(request, proposition)
        self.assertEqual(
            btn['btn1_href'], "/proposition/update_proposition/2/"
        )
        self.assertEqual(btn['btn1_class'], "btn btn-block btn-success")
        self.assertEqual(btn['btn1_text'], "Terminer")
        self.assertEqual(btn['btn1_value'], "realized")
        self.assertEqual(
            btn['btn2_href'], "/proposition/update_proposition/2/"
        )
        self.assertEqual(btn['btn2_class'], "btn btn-block btn-danger")
        self.assertEqual(btn['btn2_text'], "Annuler")
        self.assertEqual(btn['btn2_value'], "new")

    def test_set_demand_button_with_sta_realized_cre_user(self):
        proposition = Proposition.objects.get(pk=4)
        request = RequestFactory().get('')
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user
        btn = self.manager._Manager__set_demand_btn(request, proposition)
        self.assertEqual(
            btn['btn1_href'], "/proposition/update_proposition/4/"
        )
        self.assertEqual(btn['btn1_class'], "btn btn-block btn-success")
        self.assertEqual(btn['btn1_text'], "Valider")
        self.assertEqual(btn['btn1_value'], "done")
        self.assertEqual(
            btn['btn2_href'], "/proposition/update_proposition/4/"
        )
        self.assertEqual(btn['btn2_class'], "btn btn-block btn-danger")
        self.assertEqual(btn['btn2_text'], "Rejeter")
        self.assertEqual(btn['btn2_value'], "rejected")

    def test_set_demand_button_with_sta_rejected_tak_user(self):
        proposition = Proposition.objects.get(pk=5)
        request = RequestFactory().get('')
        user = authenticate(email='user3@email.com', password='xxx_Xxxx')
        request.user = user
        btn = self.manager._Manager__set_demand_btn(request, proposition)
        self.assertEqual(
            btn['btn1_href'], "/proposition/update_proposition/5/"
        )
        self.assertEqual(btn['btn1_class'], "btn btn-block btn-success")
        self.assertEqual(btn['btn1_text'], "Reprendre")
        self.assertEqual(btn['btn1_value'], "inprogress")
        self.assertEqual(
            btn['btn2_href'], "/proposition/update_proposition/5/"
        )
        self.assertEqual(btn['btn2_class'], "btn btn-block btn-danger")
        self.assertEqual(btn['btn2_text'], "Forcer terminer")
        self.assertEqual(btn['btn2_value'], "done")

    def test_set_demand_button_with_sta_rejected_cre_user(self):
        proposition = Proposition.objects.get(pk=5)
        request = RequestFactory().get('')
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user
        btn = self.manager._Manager__set_demand_btn(request, proposition)
        self.assertEqual(
            btn['btn1_href'], "/proposition/update_proposition/5/"
        )
        self.assertEqual(btn['btn1_class'], "btn btn-block btn-success")
        self.assertEqual(btn['btn1_text'], "Valider")
        self.assertEqual(btn['btn1_value'], "done")

    def test_set_demand_button_with_sta_annule_cre_user(self):
        proposition = Proposition.objects.get(pk=1)
        request = RequestFactory().get('')
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user
        btn = self.manager._Manager__set_demand_btn(request, proposition)
        self.assertIsNone(btn['btn1_href'])
        self.assertIsNone(btn['btn1_class'])
        self.assertIsNone(btn['btn1_text'])
        self.assertIsNone(btn['btn1_value'])

    def test_set_btn_dict_with_argument(self):
        btn = self.manager._Manager__set_btn_dict('un', 'deux', 'trois')
        self.assertEqual(btn['btn1_href'], 'un')
        self.assertIsNone(btn['btn1_value'])

    def test_set_check_index_with_list(self):
        items = ['item1', 'item2', 'item3']
        item1 = self.manager._Manager__check_index(items, 0)
        item4 = self.manager._Manager__check_index(items, 3)
        self.assertIsNotNone(item1)
        self.assertIsNone(item4)

    def test_set_offer_btn_with_sta_nouveau_tak_none_cre_not_user(self):
        proposition = Proposition.objects.get(pk=13)
        request = RequestFactory().get('')
        user = authenticate(email='user3@email.com', password='xxx_Xxxx')
        request.user = user
        btn = self.manager._Manager__set_offer_btn(request, proposition)
        self.assertEqual(
            btn['btn1_href'], "/proposition/update_proposition/13/"
        )
        self.assertEqual(btn['btn1_class'], "btn btn-block btn-success")
        self.assertEqual(btn['btn1_text'], "Sélectionner")
        self.assertEqual(btn['btn1_value'], "select")

    def test_set_offer_btn_with_sta_selectionne_tak_user(self):
        proposition = Proposition.objects.get(pk=16)
        request = RequestFactory().get('')
        user = authenticate(email='user3@email.com', password='xxx_Xxxx')
        request.user = user
        btn = self.manager._Manager__set_offer_btn(request, proposition)
        self.assertEqual(
            btn['btn1_href'], "/proposition/update_proposition/16/"
        )
        self.assertEqual(btn['btn1_class'], "btn btn-block btn-danger")
        self.assertEqual(btn['btn1_text'], "Annuler")
        self.assertEqual(btn['btn1_value'], "new")

    def test_set_offer_btn_with_sta_selectionne_cre_user(self):
        proposition = Proposition.objects.get(pk=16)
        request = RequestFactory().get('')
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user
        btn = self.manager._Manager__set_offer_btn(request, proposition)
        self.assertEqual(
            btn['btn1_href'], "/proposition/update_proposition/16/"
        )
        self.assertEqual(btn['btn1_class'], "btn btn-block btn-success")
        self.assertEqual(btn['btn1_text'], "Commencer")
        self.assertEqual(btn['btn1_value'], "inprogress")

    def test_set_offer_bun_with_sta_en_cours_cre_user(self):
        proposition = Proposition.objects.get(pk=12)
        request = RequestFactory().get('')
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user
        btn = self.manager._Manager__set_offer_btn(request, proposition)
        self.assertEqual(
            btn['btn1_href'], "/proposition/update_proposition/12/"
        )
        self.assertEqual(btn['btn1_class'], "btn btn-block btn-success")
        self.assertEqual(btn['btn1_text'], "Terminer")
        self.assertEqual(btn['btn1_value'], "realized")

    def test_set_offer_btn_with_sta_realized_tak_user(self):
        proposition = Proposition.objects.get(pk=14)
        request = RequestFactory().get('')
        user = authenticate(email='user3@email.com', password='xxx_Xxxx')
        request.user = user
        btn = self.manager._Manager__set_offer_btn(request, proposition)
        self.assertEqual(
            btn['btn1_href'], "/proposition/update_proposition/14/"
        )
        self.assertEqual(btn['btn1_class'], "btn btn-block btn-success")
        self.assertEqual(btn['btn1_text'], "Valider")
        self.assertEqual(btn['btn1_value'], "done")
        self.assertEqual(
            btn['btn2_href'], "/proposition/update_proposition/14/"
        )
        self.assertEqual(btn['btn2_class'], "btn btn-block btn-danger")
        self.assertEqual(btn['btn2_text'], "Rejeter")
        self.assertEqual(btn['btn2_value'], "rejected")

    def test_set_offer_btn_with_sta_rejected_tak_user(self):
        proposition = Proposition.objects.get(pk=15)
        request = RequestFactory().get('')
        user = authenticate(email='user3@email.com', password='xxx_Xxxx')
        request.user = user
        btn = self.manager._Manager__set_offer_btn(request, proposition)
        self.assertEqual(
            btn['btn1_href'], "/proposition/update_proposition/15/"
        )
        self.assertEqual(btn['btn1_class'], "btn btn-block btn-success")
        self.assertEqual(btn['btn1_text'], "Valider")
        self.assertEqual(btn['btn1_value'], "done")

    def test_set_offer_btn_with_sta_rejected_cre_user(self):
        proposition = Proposition.objects.get(pk=15)
        request = RequestFactory().get('')
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user
        btn = self.manager._Manager__set_offer_btn(request, proposition)
        self.assertEqual(
            btn['btn1_href'], "/proposition/update_proposition/15/"
        )
        self.assertEqual(btn['btn1_class'], "btn btn-block btn-success")
        self.assertEqual(btn['btn1_text'], "Reprendre")
        self.assertEqual(btn['btn1_value'], "inprogress")
        self.assertEqual(
            btn['btn2_href'], "/proposition/update_proposition/15/"
        )
        self.assertEqual(btn['btn2_class'], "btn btn-block btn-danger")
        self.assertEqual(btn['btn2_text'], "Forcer terminer")
        self.assertEqual(btn['btn2_value'], "done")

    def test_set_proposition_status_with_select_taker(self):
        request = RequestFactory().post(
            '', data={'update_status_button': 'select'}
        )
        user = authenticate(email='user3@email.com', password='xxx_Xxxx')
        request.user = user
        self.manager.set_proposition_status(request, 3)
        proposition = Proposition.objects.get(pk=3)
        self.assertEqual(proposition.proposition_status.id, 6)
        self.assertEqual(
            proposition.proposition_taker.email, 'user3@email.com'
        )

    def test_set_proposition_status_with_new_taker(self):
        request = RequestFactory().post(
            '', data={'update_status_button': 'new'}
        )
        user = authenticate(email='user3@email.com', password='xxx_Xxxx')
        request.user = user
        self.manager.set_proposition_status(request, 1)
        proposition = Proposition.objects.get(pk=1)
        self.assertEqual(proposition.proposition_status.id, 3)
        self.assertIsNone(proposition.proposition_taker)

    def test_set_proposition_status_with_inprogress(self):
        request = RequestFactory().post(
            '', data={'update_status_button': 'inprogress'}
        )
        user = authenticate(email='user3@email.com', password='xxx_Xxxx')
        request.user = user
        self.manager.set_proposition_status(request, 6)
        proposition = Proposition.objects.get(pk=6)
        self.assertEqual(proposition.proposition_status.id, 2)

    def test_set_proposition_status_with_realized(self):
        request = RequestFactory().post(
            '', data={'update_status_button': 'realized'}
        )
        user = authenticate(email='user3@email.com', password='xxx_Xxxx')
        request.user = user
        self.manager.set_proposition_status(request, 2)
        proposition = Proposition.objects.get(pk=2)
        self.assertEqual(proposition.proposition_status.id, 4)

    def test_set_proposition_status_with_rejected(self):
        request = RequestFactory().post(
            '', data={'update_status_button': 'rejected'}
        )
        user = authenticate(email='user3@email.com', password='xxx_Xxxx')
        request.user = user
        self.manager.set_proposition_status(request, 4)
        proposition = Proposition.objects.get(pk=4)
        self.assertEqual(proposition.proposition_status.id, 5)

    def test_set_proposition_status_with_done(self):
        request = RequestFactory().post(
            '', data={'update_status_button': 'done'}
        )
        user = authenticate(email='user3@email.com', password='xxx_Xxxx')
        request.user = user
        self.manager.set_proposition_status(request, 4)
        proposition = Proposition.objects.get(pk=4)
        self.assertEqual(proposition.proposition_status.id, 7)
        self.assertEqual(proposition.proposition_creator.balance, 940)
        self.assertEqual(proposition.proposition_taker.balance, 3060)

    def test_set_proposition_status_with_selectione(self):
        status = self.manager._Manager__set_status('Sélectionné')
        self.assertEqual(
            Status.objects.get(name__exact='Sélectionné').name,
            status.name
        )

    def test_set_creator_taker_balance_with_demande_individuelle(self):
        proposition = Proposition.objects.get(pk=18)
        self.manager._Manager__set_creator_taker_balance(proposition)
        proposition = Proposition.objects.get(pk=18)
        self.assertEqual(proposition.proposition_creator.balance, 880)
        self.assertEqual(proposition.proposition_taker.balance, 3120)

    def test_set_creator_taker_balance_with_demande_collective(self):
        proposition = Proposition.objects.get(pk=4)
        self.manager._Manager__set_creator_taker_balance(proposition)
        proposition = Proposition.objects.get(pk=4)
        self.assertEqual(proposition.proposition_creator.balance, 940)
        self.assertEqual(proposition.proposition_taker.balance, 3060)

    def test_set_custom_users_balances_with_demande_collective(self):
        proposition = Proposition.objects.get(pk=4)
        self.manager._Manager__set_custom_users_balances(proposition)
        proposition = Proposition.objects.get(pk=4)
        self.assertEqual(proposition.proposition_creator.balance, 940)
        self.assertEqual(proposition.proposition_taker.balance, 2940)

    def test_get_discussion_with_proposition_instance(self):
        proposition = Proposition.objects.get(pk=1)
        discussion = self.manager._Manager__get_discussion(proposition)
        self.assertEqual(discussion, Discussion.objects.get(pk=1))

    def test_get_discussion_with_none(self):
        proposition = None
        discussion = self.manager._Manager__get_discussion(proposition)
        self.assertIsNone(discussion)

    def test_get_comments_with_proposition_instance(self):
        proposition = Proposition.objects.get(pk=1)
        comments = self.manager._Manager__get_comments(proposition)
        self.assertEqual(comments[0], Comment.objects.get(pk=1))

    def test_get_comments_with_none(self):
        proposition = None
        comments = self.manager._Manager__get_comments(proposition)
        self.assertIsNone(comments)

    def test_create_comment(self):
        Comment.objects.all().delete()
        form = CommentForm(data={'comment': 'Alors???'})
        form.is_valid()
        custom_user = CustomUser.objects.get(pk=1)
        id_proposition = Proposition.objects.get(pk=1).id
        self.manager.create_comment(form, custom_user, id_proposition)
        self.assertEqual(
            Comment.objects.all().last().comment, 'Alors???'
        )
