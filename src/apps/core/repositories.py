from django.db import models
from django.db.models import Model
from django.http import Http404


class BaseRepository:
    model = None

    def get_by_id(self, pk: int):
        try:
            return self.model.objects.get(id=pk)
        except:
            raise Http404("Объект не найден")

    def update_multiple_fields(self, obj: Model, **kwargs):
        fields = []
        for field, value in kwargs.items():
            if not hasattr(obj, field):
                continue
            field_obj = obj._meta.get_field(field)
            if isinstance(field_obj, (models.ManyToManyField, models.ManyToManyRel)) \
                    or field == 'id':
                continue
            fields.append(field)
            setattr(obj, field, value)

        obj.save(update_fields=fields)
        return obj

    def create(self, **kwargs):
        return self.model.objects.create(**kwargs)

    def delete(self, obj: Model) -> None:
        obj.delete()
