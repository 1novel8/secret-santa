from apps.core.repositories import BaseRepository
from .models import Party, UserParty
from apps.authentication.models import User
from ..question.models import Question


class PartyRepository(BaseRepository):
    model = Party

    def add_user(self, user: User, party: Party, is_owner=False, is_confirmed=False) -> Party:
        party.users.add(
            user,
            through_defaults={
                'is_owner': is_owner,
                'is_confirmed': is_confirmed,
            }
        )
        return party

    def confirm_user(self, user: User, party: Party):
        party_user = party.users.through.objects.get(user=user, party=party)
        party_user.is_confirmed = True
        party_user.save()
