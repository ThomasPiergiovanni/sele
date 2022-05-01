"""Test voting method module.
"""
from django.db import models
from django.test import TestCase

from authentication.models import CustomUser
from authentication.tests.emulation.authentication_emulation import (
    AuthenticationEmulation
)
from information.tests.emulation.information_emulation import (
    InformationEmulation
)
from information.models.question import Question


class QuestionTest(TestCase):
    """Test question class.
    """
    def setUp(self):
        self.auth_emulation = AuthenticationEmulation()
        self.auth_emulation.emulate_custom_user()
        self.information_emulation = InformationEmulation()
        self.information_emulation.emulate_question()



    def test_question_with_question_class(self):
        question = Question.objects.get(pk=1)
        self.assertIsInstance(question, Question)

    def test_question_with_attr_question_characteristic(self):
        attribute = Question._meta.get_field('question')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.CharField()))
        self.assertEqual(attribute.max_length, 256)
        self.assertEqual(attribute.unique, False)

    def test_question_with_attr_answer_characteristic(self):
        attribute = Question._meta.get_field('answer')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.TextField()))
        self.assertEqual(attribute.max_length, 1000)

    def test_question_with_attr_custom_user_characteristic(self):
        attribute = Question._meta.get_field('custom_user')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),
            type(models.ForeignKey(CustomUser, models.CASCADE))
        )
    
    def test_question_with_emulated_question_instance(self):
        question= Question.objects.get(pk=1)
        self.assertEqual(
            question.question,
            "Qu'est ce qu une demande de groupe?"
        )
        question= Question.objects.get(pk=2)
        self.assertEqual(
            question.question, 
            "Ou sont hébergée nos données?"
        )
