# Generated by Django 4.1.2 on 2022-10-20 00:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_user_user_user_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='profile',
        ),
    ]