from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_email(email):
    subject = 'Hi! You was invited to Secret Santa Party!'
    message = f'If you want to accept the invite ' \
              f'register with this EMAIL: {email}.'

    from_email = 'secret_santa@gmail.com'
    to_email = [email]  # Replace with your desired email address
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=to_email,
            fail_silently=False)
    except Exception as e:
        raise e
