import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")

app = Celery("celery")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.timezone = 'Europe/Minsk'
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'send-email-to-remind-users': {
        'task': 'apps.party.tasks.remind_users',
        'schedule': crontab(hour='12', minute='0'),
    },
}
