from apps.core.repositories import BaseRepository
from .models import Party, UserParty
from apps.authentication.models import User
from ..question.models import Question


class PartyRepository(BaseRepository):
    model = Party

    def add_user(self, user: User, party: Party, is_owner=False) -> Party:
        party.users.add(
            user,
            through_defaults={'is_owner': is_owner}
        )
        return party
