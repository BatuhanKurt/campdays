# Generated by Django 2.0.2 on 2018-04-07 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180407_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('female', 'Kadın'), ('male', 'Erkek')], default='male', max_length=10),
            preserve_default=False,
        ),
    ]
