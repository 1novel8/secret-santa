import base64
import time

from celery import shared_task
from django.core.mail import send_mail


def generate_token(email):
    data = f'{email}:{time.time()}'
    token_bytes = data.encode('utf-8')
    token_base64 = base64.b64encode(token_bytes).decode('utf-8')
    return token_base64

@shared_task
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
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=to_email,
            fail_silently=False)
    except Exception as e:
        raise e
