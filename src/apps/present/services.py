from apps.core.services import BaseService
from .models import Present

from .repositories import PresentRepository


class PresentService(BaseService):
    repository = PresentRepository()

    def create(self, **kwargs) -> Present:
        user = kwargs.pop('user')
        is_preferred = kwargs.pop('user')
        present = self.repository.create(**kwargs)
        self.repository.add_user(
            user=user,
            present=present,
            is_preferred=is_preferred
        )
        return present
