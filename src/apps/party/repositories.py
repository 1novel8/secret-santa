from apps.core.repositories import BaseRepository
from .models import Party, UserParty
from apps.authentication.models import User


class PartyRepository(BaseRepository):
    model = Party

    def create(self, **kwargs) -> Party:
        party = super().create(**kwargs)
        return party

    def add_user(self, user: User, party: Party, is_owner=False) -> Party:
        party.users.add(
            user,
            through_defaults={'is_owner': is_owner}
        )
        return party
