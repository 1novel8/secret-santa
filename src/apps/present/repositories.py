from apps.core.repositories import BaseRepository

from apps.present.models import Present
from apps.authentication.models import User


class PresentRepository(BaseRepository):
    model = Present

    def add_user(self, user: User, present: Present, is_preferred: bool) -> Present:
        present.users.add(
            user,
            through_defaults={'is_preferred': is_preferred}
        )
        return present
