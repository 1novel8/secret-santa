from random import shuffle
from datetime import timedelta
from django.db.models import Q, Count
from django.utils import timezone
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

from apps.core.utils import generate_token
from apps.party.models import Party, DrawResult


@shared_task()
def invite_user_by_email(email, party_name):
    subject = f'Hi! You was invited to Secret Santa Party named "{party_name}"!'

    register_url = f'{settings.FRONT_URL}?token={generate_token(email)}'

    message = f'If you have no account yet' \
              f'register here: ' \
              f'{register_url}' \

    from_email = 'secret_santa@gmail.com'
    to_email = [email]
    send_mail(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=to_email,
        fail_silently=False
    )


@shared_task()
def remind_users():
    now = timezone.now()
    parties = (Party.objects
               .filter(Q(finish_time__gte=now) & Q(finish_time__lt=now + timedelta(hours=24)))
               .prefetch_related("users").all())
    for party in parties:
        subject = f'Wow it\'s Santa!'
        party_url = f'http://localhost:8000/api/parties/{party.id}/'
        message = f'Your party "{party.name}" will be ended soon! ' \
                  f'You can check it here: {party_url} ' \
                  f'Or you have the last chance to join here: {party_url}/join '
        from_email = 'secret_santa@gmail.com'

        email_list = list()
        for user in party.users.all():
            email_list.append(user.email)
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=email_list,
            fail_silently=False
        )


@shared_task()
def finish_parties():
    now = timezone.now()

    parties = (Party.objects.filter(
        Q(finish_time__lte=now) &
        Q(finish_time__gt=now - timedelta(days=3, minutes=5))
    ).annotate(
        question_count=Count('questions')
    ).prefetch_related(
        "users"
    ).all())

    for party in parties:
        users_list = list()
        for user in party.users.all():
            if user.answers.filter(party=party).count() != party.question_count:
                continue
            users_list.append(user)

        shuffle(users_list)
        for i, sender in enumerate(users_list):
            if i + 1 < len(users_list):
                receiver = users_list[i + 1]
            else:
                receiver = users_list[0]
            DrawResult.objects.create(
                party=party,
                sender=sender,
                receiver=receiver
            )

        send_results.delay(party.id)


@shared_task()
def send_results(party_id: int):
    results = DrawResult.objects.filter(party_id=party_id).all()
    for result in results:
        subject = f'Wow it\'s Santa!'
        result_url = f'http://localhost:8000/api/parties/{result.party.id}/result'
        message = f'Your party "{result.party.name}" FINISHED!!!\n ' \
                  f'And now you became a real SANTA!\n ' \
                  f'You should find a special gift for {result.receiver.username}\n ' \
                  f'There are some tips for you right here: {result_url}'
        from_email = 'secret_santa@gmail.com'
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=[result.sender.email],
            fail_silently=False
        )
