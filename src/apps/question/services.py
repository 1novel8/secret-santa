from rest_framework.exceptions import PermissionDenied, NotFound

from apps.core.services import BaseService
from .models import Question
from .repositories import QuestionRepository
from apps.party.services import PartyService


class QuestionService(BaseService):
    repository = QuestionRepository()

    party_service = PartyService()

    def create(self, **kwargs) -> Question:
        party_pk = kwargs.pop('party_pk')
        user = kwargs.pop('user')
        party = self.party_service.get_by_id(pk=party_pk, user=user)
        if self.party_service.is_owner(party=party, user=user):
            question = super().create(**kwargs, party=party)
            return question
        raise PermissionDenied("only owner can add questions")

    def get_by_id(self, pk: int, **kwargs):
        question = self.repository.get_by_id(pk=pk)
        party = self.party_service.get_by_id(pk=kwargs.get('party_pk'), **kwargs)
        if self.party_service.is_member(user=kwargs.pop('user'), party=party):
            if question.party_id == int(kwargs.pop('party_pk')):
                return question
            raise NotFound('No such question')
        raise PermissionDenied("only member can see questions")

    def list(self, **kwargs):
        party = self.party_service.get_by_id(pk=kwargs.get('party_pk'), **kwargs)
        return party.questions.all()

    def update(self, pk: int, **kwargs) -> Question:
        question = self.get_by_id(pk=pk, **kwargs)
        return self.repository.update_multiple_fields(obj=question, **kwargs)
