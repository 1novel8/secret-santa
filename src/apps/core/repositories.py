from django.db import models
from django.db.models import Model, QuerySet
from rest_framework.exceptions import NotFound


class BaseRepository:
    model = None

    def get_by_id(self, pk: int):
        try:
            return self.model.objects.get(id=pk)
        except:
            raise NotFound("Объект не найден")

    def update_multiple_fields(self, obj: Model, **kwargs):
        fields = []
        for field, value in kwargs.items():
            if not hasattr(obj, field):
                continue
            field_obj = obj._meta.get_field(field)
            if isinstance(field_obj, (models.ManyToManyField, models.ManyToManyRel))\
                    or 'id' in field or field == 'password':
                continue
            fields.append(field)
            setattr(obj, field, value)

        obj.save(update_fields=fields)
        return obj

    def create(self, **kwargs):
        return self.model.objects.create(**kwargs)

    def delete(self, obj: Model) -> None:
        obj.delete()

    def list(self):
        return self.model.objects.all()

