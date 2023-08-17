from rest_framework.generics import get_object_or_404

from apps.core.repositories import BaseRepository

from .models import Question, UserPartyQuestionAnswer
from apps.authentication.models import User
from apps.party.models import Party


class QuestionRepository(BaseRepository):
    model = Question

    def add_user_answer(self, user: User, party: Party, question: Question, answer: str) -> str:
        obj, created = UserPartyQuestionAnswer.objects.update_or_create(
            user=user,
            party=party,
            question=question,
            defaults={'answer': answer}
        )

        if not created:
            obj.answer = answer
            obj.save()

        return answer

    def get_answer(self, user: User, question: Question):
        obj = get_object_or_404(
            UserPartyQuestionAnswer,
            user=user,
            question=question,
        )
        return obj.answer
