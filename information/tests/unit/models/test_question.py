"""Test voting method module.
"""
from datetime import date
from django.db import models
from django.test import TestCase

from authentication.models import CustomUser
from information.models.question import Question


class QuestionTest(TestCase):
    """Test question class.
    """
    def setUp(self):
        self.emulate_question()

    def emulate_question(self):
        """
        """
        Question.objects.create(
            id=1,
            question="Qu'est ce qu une demande de groupe?",
            answer=(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
                " Sed non risus. Suspendisse lectus tortor, dignissim sit"
                " amet, adipiscing nec, ultricies sed, dolor. Cras elementum"
                " ultrices diam. Maecenas ligula massa, varius a, semper"
                " congue, euismod non, mi. Proin porttitor, orci nec nonummy"
                " molestie, enim est eleifend mi, non fermentum diam nisl sit"
                " amet erat. Duis semper. Duis arcu massa, scelerisque vitae,"
                " consequat in, pretium a, enim. Pellentesque congue"
            ),
            user_id=1
        )
        Question.objects.create(
            id=2,
            question="Ou sont hébergée nos données?",
            answer=(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
                " Sed non risus. Suspendisse lectus tortor, dignissim sit"
                " amet, adipiscing nec, ultricies sed, dolor. Cras elementum"
                " ultrices diam. Maecenas ligula massa, varius a, semper"
                " congue, euismod non, mi. Proin porttitor, orci nec nonummy"
                " molestie, enim est eleifend mi, non fermentum diam nisl sit"
                " amet erat. Duis semper. Duis arcu massa, scelerisque vitae,"
                " consequat in, pretium a, enim. Pellentesque congue"
            ),
            user_id=2
        )

    def test_question_with_question_class(self):
        question = Question.objects.get(pk=1)
        self.assertIsInstance(question, Question)

    def test_question_with_attr_question_characteristic(self):
        attribute = Voting._meta.get_field('question')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.CharField()))
        self.assertEqual(attribute.max_length, 256)
        self.assertEqual(attribute.unique, False)

    def test_question_with_attr_answer_characteristic(self):
        attribute = Voting._meta.get_field('answer')
        self.assertTrue(attribute)
        self.assertEqual(type(attribute), type(models.TextField()))
        self.assertEqual(attribute.max_length, 1000)

    def test_voting_with_attr_voting_method_characteristic(self):
        attribute = Voting._meta.get_field('custom_user')
        self.assertTrue(attribute)
        self.assertEqual(
            type(attribute),
            type(models.ForeignKey(CustomUser, models.CASCADE))
        )
    
    def test_status_with_emulated_status_instance(self):
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
