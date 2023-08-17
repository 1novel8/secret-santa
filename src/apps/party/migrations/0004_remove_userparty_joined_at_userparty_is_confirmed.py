# Generated by Django 4.2.3 on 2023-08-09 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0003_remove_party_duration_party_finish_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userparty',
            name='joined_at',
        ),
        migrations.AddField(
            model_name='userparty',
            name='is_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]