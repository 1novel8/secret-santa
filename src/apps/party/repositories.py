from django.db.models import Model

from apps.core.repositories import BaseRepository
from .models import Party, UserParty


class PartyRepository(BaseRepository):
    model = Party

    def create(self, **kwargs):
        user = kwargs.pop('user')
        party = super().create(**kwargs)
        party.users.add(
            user,
            through_defaults={'is_owner': True}
        )
        return party


class UserPartyRepository(BaseRepository):
    model = UserParty
