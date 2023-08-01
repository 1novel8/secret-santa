from src.apps.core.decorators import attribute_required


class BaseService:
    _repository = None

    def __init__(self, *args, **kwargs):
        if getattr(self, '_repository') is None:
            raise AttributeError(f"attribute _repository should not be None.")

    def create(self, **kwargs):
        return self._repository.create(**kwargs)

    def update_present(self, pk, **kwargs):
        return self._repository.update_present(pk, **kwargs)

    def get_by_id(self, pk):
        return self._repository.get_present_by_id(pk)

    def delete(self, pk):
        obj = self._repository.get_by_id(pk)
        self._repository.delete_present(obj)


s = BaseService()
print(dir(s))

