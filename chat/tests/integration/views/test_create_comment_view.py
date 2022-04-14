"""Test create comment view module.
"""
from django.test import TestCase
from django.urls import reverse

from chat.models.comment import Comment
from chat.models.discussion import Discussion
from chat.tests.emulation.chat_emulation import ChatEmulation


class CreateCommentView(TestCase):
    """Test CreateCommentView class.
    """
    def setUp(self):
        self.chat_emulation = ChatEmulation()


    def test_post_with_nominal_scenario(self):
        self.chat_emulation.emulate_discussion()
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        form_data = {'comment':'Alors???'}
        response = self.client.post(
            '/chat/create_comment/1/',
            data=form_data,
            follow=True
        )
        try:
            comment = Comment.objects.get(pk=1)
        except:
            comment = False
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0],
            reverse('chat:read_discussion', args=[1])
        )
        self.assertTrue(comment)
        self.assertTrue(comment.comment)


    
    def test_post_with_alternative_scenario(self):
        self.chat_emulation.emulate_discussion()
        self.client.login(email='user1@email.com', password='xxx_Xxxx')
        form_data = {'comment':''}
        response = self.client.post(
            '/chat/create_comment/1/',
            data=form_data,
            follow=True
        )
        try:
            comment = Comment.objects.get(pk=1)
        except:
            comment = False
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat/read_discussion.html')
        self.assertTrue(response.context['form'].errors)

    def test_post_with_second_alternative_scenario(self):
        form_data = {'comment':''}
        response = self.client.post(
            '/chat/create_comment/1/',
            data=form_data,
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0],reverse('authentication:login')
        )
