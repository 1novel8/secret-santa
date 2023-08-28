from django.db import models

from apps.core.models import BaseModel
from apps.party.models import Party, User


class Question(BaseModel):
    name = models.CharField(
        "Question Name",
        max_length=50,
    )
    text = models.CharField(
        "Question Text",
        max_length=200,
    )

    party = models.ForeignKey(
        Party,
        on_delete=models.CASCADE,
        related_name='questions',
    )

    answers = models.ManyToManyField(
        Party,
        through='UserPartyQuestionAnswer',
        related_name='answers',
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "question"
        verbose_name = "Question"
        verbose_name_plural = "Questions"


class UserPartyQuestionAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    answer = models.CharField(
        "User Answer",
        max_length=200,
    )
