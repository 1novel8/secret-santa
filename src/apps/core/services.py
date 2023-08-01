

class BaseService:
    repository = None

    def __init__(self):
        if getattr(self, '_repository') is None:
            raise AttributeError(f"attribute _repository should not be None.")

    def create(self, **kwargs):
        return self.repository.create(**kwargs)

    def update_present(self, pk, **kwargs):
        return self.repository.update_present(pk, **kwargs)

    def get_by_id(self, pk):
        return self.repository.get_present_by_id(pk)

    def delete(self, pk):
        obj = self.repository.get_by_id(pk)
        self.repository.delete_present(obj)


s = BaseService()
print(dir(s))

