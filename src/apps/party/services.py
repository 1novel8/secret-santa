from rest_framework.exceptions import PermissionDenied

from .models import Party
from .repositories import PartyRepository
from apps.core.services import BaseService
from apps.authentication.models import User
from apps.question.models import Question


class PartyService(BaseService):
    repository = PartyRepository()

    def create(self, **kwargs) -> Party:
        user = kwargs.pop('user')
        party = super().create(**kwargs)
        self.repository.add_user(
            user=user,
            party=party,
            is_owner=True,
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
