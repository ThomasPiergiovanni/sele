"""Test reset vote module.
"""
from django.db import models
from django.test import TestCase

from information.management.commands.reset_information import Command
from information.models.question import Question
from information.tests.emulation.information_emulation import (
    InformationEmulation
)


class ResetInformationTest(TestCase):
    """Test reset information method class.
    """
    def setUp(self):
        """Method that set up data for the entire class
        """
        self.command = Command()
        self.information_emulation = InformationEmulation()
        self.information_emulation.emulate_question()

    def test_drop_question_with_instance_is_none(self):
        question = Question.objects.all()
        self.assertTrue(question)
        self.command._Command__drop_question()
        question = Question.objects.all()
        self.assertFalse(question)
