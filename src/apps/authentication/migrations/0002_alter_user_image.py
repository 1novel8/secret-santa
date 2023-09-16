# Generated by Django 4.2.3 on 2023-08-14 11:43

import apps.core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=apps.core.models.generate_unique_image_name, verbose_name='User Image'),
        ),
    ]