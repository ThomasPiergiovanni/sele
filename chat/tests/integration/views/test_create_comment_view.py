# pylint: disable=C0114,C0115,C0116,E1101,R0201, W0702
from django.test import TestCase
from django.urls import reverse

from chat.models.comment import Comment
from chat.tests.emulation.chat_emulation import ChatEmulation


class CreateCommentView(TestCase):

    def setUp(self):
        self.chat_emulation = ChatEmulation()
        self.chat_emulation.emulate_test_setup()

    def test_post_with_nominal_scenario(self):
        Comment.objects.all().delete()
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        form_data = {'comment': 'Alors???'}
        response = self.client.post(
            '/chat/create_comment/1/',
            data=form_data,
            follow=True
        )
        try:
            comment = Comment.objects.get(pk=1)
        except Comment.DoesNotExist:
            comment = False
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0],
            reverse('chat:read_discussion', args=[1])
        )
        self.assertTrue(comment)
        self.assertTrue(comment.comment)

    def test_post_with_alternative_scenario(self):
        Comment.objects.all().delete()
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        form_data = {'comment': ''}
        response = self.client.post(
            '/chat/create_comment/1/',
            data=form_data,
            follow=True
        )
        try:
            comment = Comment.objects.get(pk=1)
        except Comment.DoesNotExist:
            comment = False
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat/read_discussion.html')
        self.assertTrue(response.context['form'].errors)
        self.assertFalse(comment)

    def test_post_with_second_alternative_scenario(self):
        form_data = {'comment': ''}
        response = self.client.post(
            '/chat/create_comment/1/',
            data=form_data,
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0], reverse('authentication:login')
        )
