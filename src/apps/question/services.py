from rest_framework.exceptions import PermissionDenied

from apps.core.services import BaseService
from apps.question.models import Question
from apps.question.repositories import QuestionRepository
from apps.party.services import PartyService


class QuestionService(BaseService):
    repository = QuestionRepository()

    party_service = PartyService()

    def create(self, **kwargs) -> Question:
        user = kwargs.pop('user')
        party = self.party_service.get_by_id(pk=kwargs.pop('party_id'), user=user)
        if self.party_service.is_owner(party=party[0], user=user):
            question = super().create(**kwargs, party=party[0])
            return question
        raise PermissionDenied("Only owner can add questions to the party")

    def get_by_id(self, pk: int, **kwargs):
        question = self.repository.get_by_id(pk=pk)
        party = question.party
        if self.party_service.is_member(party=party, user=kwargs.get('user')):
            return question
        raise PermissionDenied('Only member can work with party\'s question')

    def update(self, pk: int, **kwargs) -> Question:
        question = self.get_by_id(pk=pk, **kwargs)
        if self.party_service.is_owner(party=question.party, user=kwargs.get('user')):
            return self.repository.update_multiple_fields(obj=question, **kwargs)
        raise PermissionDenied('Only owner can update party\'s question')

    def delete(self, pk: int, **kwargs) -> None:
        question = self.get_by_id(pk=pk, **kwargs)
        if self.party_service.is_owner(party=question.party, user=kwargs.get('user')):
            self.repository.delete(question)
        else:
            raise PermissionDenied('Only member can work with party\'s question')

    def make_answer(self, pk: int, **kwargs):
        user = kwargs.pop('user')
        answer = kwargs.pop('answer')

        question = self.get_by_id(pk=pk, user=user)
        answer = self.repository.add_user_answer(
            question=question,
            party=question.party,
            user=user,
            answer=answer
        )
        return answer

    def get_answer(self, pk, **kwargs):
        user = kwargs.pop('user')

        question = self.get_by_id(pk=pk, user=user)
        answer = self.repository.get_answer(question=question, user=user)
        return answer
