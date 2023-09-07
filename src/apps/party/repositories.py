from django.db.models import Q, F
from rest_framework.exceptions import NotFound

from apps.core.repositories import BaseRepository
from apps.party.models import Party
from apps.authentication.models import User
from apps.question.models import UserPartyQuestionAnswer


class PartyRepository(BaseRepository):
    model = Party

    def list(self, **kwargs):
        party_list = (self.model.objects.filter(userparty__user_id=kwargs.get('user').id)
                      .prefetch_related('userparty').values('id',
                                                            'name',
                                                            'description',
                                                            'image',
                                                            is_confirmed=F('userparty__is_confirmed')))
        return party_list

    def add_user(self, user: User, party: Party, is_owner=False, is_confirmed=False) -> Party:
        party.users.add(
            user,
            through_defaults={
                'is_owner': is_owner,
                'is_confirmed': is_confirmed,
            }
        )
        return party

    def confirm_user(self, user: User, party: Party):
        party_user = party.users.through.objects.get(user=user, party=party)
        party_user.is_confirmed = True
        party_user.save()

    def get_question_answer(self, party: Party, **kwargs):
        receiver = self.get_receiver(party, **kwargs)

        user_question_answers = UserPartyQuestionAnswer.objects.filter(
            Q(user=receiver) &
            Q(party=party)
        ).prefetch_related('question').annotate(
            question_name=F('question__name'),
            question_text=F('question__text')
        ).all().values('answer', 'question_name', 'question_text')

        return user_question_answers

    def get_receiver(self, party: Party, **kwargs):
        try:
            return party.drawresult_set.filter(sender=kwargs.get('user')).first().receiver
        except:
            raise NotFound("Объект не найден")
