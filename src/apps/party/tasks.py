import base64

from datetime import timedelta
from django.db.models import Q
from django.utils import timezone

from celery import shared_task
from django.core.mail import send_mail
from apps.party.models import Party


def generate_token(email):
    data = f'{email}:{timezone.now()}'
    token_bytes = data.encode('utf-8')
    token_base64 = base64.b64encode(token_bytes).decode('utf-8')
    return token_base64


@shared_task()
def invite_user_by_email(email, party_id, party_name):
    subject = f'Hi! You was invited to Secret Santa Party named "{party_name}"!'

    register_url = f'http://localhost:8000/api/users/?token={generate_token(email)} '
    join_url = f'http://localhost:8000/api/parties/{party_id}/join/'

    message = f'If you have no account yet' \
              f'register here: ' \
              f'{register_url}' \
              f'To join go here: ' \
              f'{join_url}'

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
    print(parties)
    for party in parties:
        subject = f'Wow it\'s Santa!'
        party_url = f'http://localhost:8000/api/parties/{party.id}/'
        message = f'Your party "{party.name}" will be ended soon! ' \
                  f'You can check it here: {party_url} ' \
                  f'Or you have last chance to join here: {party_url}/join '
        from_email = 'secret_santa@gmail.com'

        email_list = list()
        for user in party.users.all():
            email_list.append(user.email)
        print(email_list)
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=email_list,
            fail_silently=False
        )
