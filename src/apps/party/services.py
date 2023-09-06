from django.db.models import F
from django.utils import timezone

from rest_framework.exceptions import PermissionDenied

from .models import Party
from .repositories import PartyRepository
from apps.core.services import BaseService
from apps.authentication.models import User


class PartyService(BaseService):
    repository = PartyRepository()

    def create(self, **kwargs) -> Party:
        user = kwargs.pop('user')
        party = super().create(**kwargs)
        self.repository.add_user(
            user=user,
            party=party,
            is_owner=True,
            is_confirmed=True,
        )
        return party

    def update(self, pk: int, **kwargs) -> Party:
        obj = self.repository.get_by_id(pk=pk)
        if self.is_owner(user=kwargs.pop('user'), party=obj):
            return self.repository.update_multiple_fields(obj, **kwargs)
        else:
            raise PermissionDenied('Edit party can only owner')

    def get_by_id(self, pk: int, **kwargs):
        obj = self.repository.get_by_id(pk=pk)
        if self.is_member(user=kwargs.get('user'), party=obj):
            return obj
        else:
            raise PermissionDenied('View party can only members')

    def is_owner(self, user: User, party: Party) -> bool:
        return party.userparty_set.filter(user=user, is_owner=True).exists()

    def is_member(self, user: User, party: Party) -> bool:
        return party.userparty_set.filter(user=user).exists()

    def is_finished(self, pk: int, **kwargs) -> bool:
        party = self.get_by_id(pk=pk, **kwargs)
        return party.finish_time <= timezone.now()

    def get_result(self, pk: int, **kwargs) -> tuple:
        party = self.get_by_id(pk=pk, **kwargs)
        receiver = self.repository.get_receiver(party=party, **kwargs)
        user_question_answers = self.repository.get_question_answer(party, **kwargs)

        return receiver, user_question_answers

    def delete(self, pk: int, **kwargs) -> None:
        party = self.get_by_id(pk=pk, **kwargs)
        if self.is_owner(party=party, user=kwargs.get('user')):
            self.repository.delete(party)
        else:
            raise PermissionDenied('Only member can work with party\'s question')

    def list(self, **kwargs) -> list:
        return self.repository.list(**kwargs)

    def invite_user(self, inviter: User, user: User, party: Party):
        if self.is_owner(party=party, user=inviter):
            self.repository.add_user(
                user=user,
                party=party,
                is_owner=False,
            )
        else:
            raise PermissionDenied('Only owner can invite users')

    def confirm_user(self, pk: int, user: User):
        party = self.repository.get_by_id(pk=pk)
        if self.is_member(user=user, party=party):
            self.repository.confirm_user(user=user, party=party)
