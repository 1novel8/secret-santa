from django.db.models import Model

from apps.core.repositories import BaseRepository


class BaseService:
    repository = BaseRepository()

    def create(self, **kwargs) -> Model:
        return self.repository.create(**kwargs)

    def update(self, pk: int, **kwargs) -> Model:
        obj = self.repository.get_by_id(pk=pk)
        return self.repository.update_multiple_fields(obj, **kwargs)

    def get_by_id(self, pk: int) -> Model:
        return self.repository.get_by_id(pk)

    def delete(self, pk: int) -> None:
        obj = self.repository.get_by_id(pk)
        self.repository.delete(obj)
