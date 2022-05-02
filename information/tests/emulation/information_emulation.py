"""Test chat emulation module.
"""
from information.models.question import Question


class InformationEmulation():
    """Test InformationEmulation class.
    """
    def __init__(self):
        pass

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
            )
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
            )
        )