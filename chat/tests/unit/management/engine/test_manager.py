# pylint: disable=C0114,C0115,C0116,E1101,R0201,W0212
from datetime import date

from django.contrib.auth import authenticate
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import RequestFactory, TestCase

from authentication.models import CustomUser
from chat.forms.discussion_form import DiscussionForm
from chat.forms.comment_form import CommentForm
from chat.management.engine.manager import Manager
from chat.models import Comment, Discussion, DiscussionType
from chat.tests.emulation.chat_emulation import ChatEmulation


class TestManager(TestCase):

    def setUp(self):
        self.chat_emulation = ChatEmulation()
        self.chat_emulation.emulate_test_setup()
        self.manager = Manager()

    def test_create_discussion_with_voting_instance(self):
        Discussion.objects.all().delete()
        form_data = {
            'subject': 'Le sujet est',
        }
        form = DiscussionForm(data=form_data)
        form.is_valid()
        custom_user = CustomUser.objects.get(pk=1)
        discussion_type = DiscussionType.objects.get(pk=1)
        self.manager.create_discussion(form, custom_user, discussion_type)
        self.assertEqual(
            Discussion.objects.all().last().subject, 'Le sujet est'
        )
        self.assertEqual(
            Discussion.objects.all().last().creation_date,
            date.today()
        )
        self.assertEqual(
            Discussion.objects.all().last().discussion_discussion_type,
            discussion_type
        )

    def test_set_page_objects_context(self):
        request = RequestFactory().get('', data={'page': 1})
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user
        page_objects = (
            self.manager.set_page_objects_context(request, 'HTML')
        )
        self.assertEqual(page_objects[0].id, 1)

    def test_get_discussion_queryset_with_search_input(self):
        request = RequestFactory().get('', data={'page': 1})
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user
        votings = self.manager._Manager__get_discussion_queryset(
            request, 'HTML'
        )
        self.assertEqual(votings[0].id, 1)

    def test_get_discussion_queryset_with_search_input_is_false(self):
        request = RequestFactory().get('', data={'page': 1})
        user = authenticate(email='user1@email.com', password='xxx_Xxxx')
        request.user = user
        votings = self.manager._Manager__get_discussion_queryset(
            request, False
        )
        self.assertEqual(votings[0].id, 3)

    def test_set_session_vars_with_search_input(self):
        request = RequestFactory().post('')
        session_middleware = SessionMiddleware(request)
        session_middleware.process_request(request)
        self.manager.set_session_vars(request, 'JS')
        self.assertEqual(request.session.get(
            'c_d_v_f_search_input'), 'JS'
        )

    def test_create_comment(self):
        Comment.objects.all().delete()
        form_data = {
            'comment': 'Alors???'
        }
        form = CommentForm(data=form_data)
        form.is_valid()
        discussion = Discussion.objects.get(pk=1)
        custom_user = CustomUser.objects.get(pk=1)
        self.manager.create_comment(form, custom_user, discussion.id)
        comment = Comment.objects.last()
        self.assertEqual(comment.comment, 'Alors???')
