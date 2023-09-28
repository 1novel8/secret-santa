from apps.core.services import BaseService
from apps.present.models import Present

from apps.present.repositories import PresentRepository


class PresentService(BaseService):
    repository = PresentRepository()

    def create(self, **kwargs) -> Present:
        user = kwargs.pop('user')
        is_preferred = kwargs.pop('is_preferred')

        present = self.repository.create(**kwargs)
        self.repository.add_user(
            user=user,
            present=present,
            is_preferred=is_preferred
        )
        return present

    def list(self, **kwargs) -> list:
        user_id = kwargs.get('user_id')
        if user_id is not None:
            return self.repository.user_list(user_id=user_id)
        else:
            return self.repository.list()
