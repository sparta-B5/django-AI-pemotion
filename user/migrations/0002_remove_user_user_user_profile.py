# Generated by Django 4.1.2 on 2022-10-19 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='profile',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]