# Generated by Django 2.0.2 on 2018-04-07 19:11

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='height_field',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=accounts.models.users_upload_location, width_field='width_field'),
        ),
        migrations.AddField(
            model_name='user',
            name='width_field',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
