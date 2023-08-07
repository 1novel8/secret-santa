from rest_framework.exceptions import PermissionDenied

from apps.core.services import BaseService
from .models import Question
from .repositories import QuestionRepository
from apps.party.services import PartyService


class QuestionService(BaseService):
    repository = QuestionRepository()

    party_service = PartyService()

    def create(self, **kwargs) -> Question:
        user = kwargs.pop('user')
        party = self.party_service.get_by_id(pk=kwargs.pop('party_id'), user=user)
        if self.party_service.is_owner(party=party, user=user):
            question = super().create(**kwargs, party=party)
            return question
        raise PermissionDenied("Only owner can add questions to the party")

    def get_by_id(self, pk: int, **kwargs):
        question = self.repository.get_by_id(pk=pk)
        party = question.party
        if self.party_service.is_owner(party=party, user=kwargs.get('user')):
            raise PermissionDenied('Only member can work with party\'s question')
        return question

    def update(self, pk: int, **kwargs) -> Question:
        question = self.get_by_id(pk=pk, **kwargs)
        return self.repository.update_multiple_fields(obj=question, **kwargs)

    def delete(self, pk: int, **kwargs) -> None:
        question = self.get_by_id(pk=pk, **kwargs)
        if self.party_service.is_owner(party=question.party, user=kwargs.get('user')):
            self.repository.delete(question)
        else:
            raise PermissionDenied('Only member can work with party\'s question')

