from datetime import datetime
from django.db import models


def now(): return datetime.now()


class BaseModelManager(models.Manager):
    def _get_queryset(self):  # returns ordinary queryset
        return super().get_queryset()

    def get_queryset(self):  # returns filtered deleted_at=None queryset
        queryset = self._get_queryset()
        queryset = queryset.filter(deleted_at__isnull=True)
        return queryset

    def all_fully(self):  # returns ordinary queryset.all()
        return self._get_queryset()

    def all(self):  # returns queryset.filter(deleted_at=None).all()
        return self.get_queryset()

    def delete(self):
        self.update(delete_at=now())


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, null=True)

    objects = BaseModelManager()

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        self.deleted_at = now()
        self.save()
