# pylint: disable=C0114,C0115,C0116,E1101,R0201,R0903,W0201
from authentication.tests.emulation.authentication_emulation import (
    AuthenticationEmulation
)
from chat.tests.emulation.chat_emulation import ChatEmulation
from collectivity.tests.emulation.collectivity_emulation import (
    CollectivityEmulation
)
from information.models.question import Question
from proposition.tests.emulation.proposition_emulation import (
    PropositionEmulation
)
from vote.tests.emulation.vote_emulation import VoteEmulation


class InformationEmulation():

    def emulate_question(self):
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

    def emulate_test_setup(self):
        self.auth_emulation = AuthenticationEmulation()
        self.auth_emulation.emulate_custom_user()
        self.collectivity_emulation = CollectivityEmulation()
        self.collectivity_emulation.emulate_collectivity()
        self.chat_emulation = ChatEmulation()
        self.chat_emulation.emulate_discussion()
        self.chat_emulation.emulate_comment()
        self.proposition_emulation = PropositionEmulation()
        self.proposition_emulation.emulate_proposition()
        self.vote_emulation = VoteEmulation()
        self.vote_emulation.emulate_voting_method()
        self.vote_emulation.emulate_voting()
        self.vote_emulation.emulate_vote()
