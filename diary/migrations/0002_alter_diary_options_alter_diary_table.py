# Generated by Django 4.1.2 on 2022-10-18 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='diary',
            options={'verbose_name': '게시글', 'verbose_name_plural': '게시글들'},
        ),
        migrations.AlterModelTable(
            name='diary',
            table='diary',
        ),
    ]
