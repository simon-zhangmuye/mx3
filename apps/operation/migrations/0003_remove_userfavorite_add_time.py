# Generated by Django 2.0.1 on 2018-05-06 00:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0002_auto_20180505_1125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userfavorite',
            name='add_time',
        ),
    ]