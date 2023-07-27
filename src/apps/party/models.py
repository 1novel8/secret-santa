from django.db import models

from apps.core.models import BaseModel
from apps.authentication.models import User


class Party(BaseModel):
    name = models.CharField(
        "Party name",
        max_length=100,
    )
    description = models.CharField(
        "Party description",
        max_length=500,
    )
    image = models.ImageField(
        upload_to='static/img/parties',
        blank=True,
    )
    users = models.ManyToManyField(
        User,
        through='UserParty',
        related_name='parties',
    )
    draw_results = models.ManyToManyField(
        User,
        through='DrawResult',
        through_fields=('party', 'sender'),
        related_name='draw_results',
    )

    # questions - M2M
    # answers - M2M

    def __str__(self):
        return self.name

    class Meta:
        db_table = "party"
        verbose_name = "Party"
        verbose_name_plural = "parties"


class UserParty(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)

    joined_at = models.DateTimeField(auto_now_add=True)


class DrawResult(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
