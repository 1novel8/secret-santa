from django.db import models

from apps.authentication.models import User
from apps.core.models import BaseModel


class Present(BaseModel):
    name = models.CharField(
        "Present Name",
        max_length=50,
    )
    description = models.CharField(
        "Present Description",
        max_length=200,
    )
    image = models.ImageField(
        upload_to='static/img/present/',
        blank=True,
        null=True,
        default=None
    )
    url = models.URLField(
        blank=True,
        null=True,
        default=None
    )

    users = models.ManyToManyField(
        User,
        through='UserPresent',
        related_name='present',
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "present"
        verbose_name = "Present"
        verbose_name_plural = "Presents"


class UserPresent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    present = models.ForeignKey(Present, on_delete=models.CASCADE)
    is_preferred = models.BooleanField(default=True)
