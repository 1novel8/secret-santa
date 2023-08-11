from django.db import models

from apps.core.models import BaseModel, generate_unique_image_name
from apps.authentication.models import User


class Party(BaseModel):
    name = models.CharField(
        "Party name",
        max_length=100,
        blank=False,
        null=False,
    )
    description = models.CharField(
        "Party description",
        max_length=500,
        blank=False,
        null=False,
    )
    image = models.ImageField(
        upload_to=generate_unique_image_name,
        blank=True,
        null=True,
        default=None,
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

    class Meta:
        db_table = "party"
        verbose_name = "Party"
        verbose_name_plural = "parties"


class UserParty(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)

    joined_at = models.DateTimeField(auto_now_add=True)
    is_owner = models.BooleanField(default=False)


class DrawResult(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    party = models.ForeignKey(Party, on_delete=models.CASCADE)

