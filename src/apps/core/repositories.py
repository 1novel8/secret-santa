from django.db.models import Model
from django.http import Http404


class BaseRepository:
    model = None

    def get_by_id(self, pk: int) -> Model:
        try:
            return self.model.objects.get(id=pk)
        except:
            raise Http404("Объект не найден")

    def update_multiple_fields(self, obj: Model, **kwargs) -> Model:
        for field, value in kwargs.items():
            if not hasattr(obj, field):
                raise AttributeError(f"Object {obj._meta.db_table} has no field called {field}")
            setattr(obj, field, value)
        obj.save(update_fields=kwargs.keys())
        return obj

    def create(self, **kwargs) -> Model:
        return self.model.objects.create(**kwargs)

    def delete(self, obj: Model) -> None:
        obj.delete()
