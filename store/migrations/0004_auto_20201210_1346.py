# Generated by Django 3.1.4 on 2020-12-10 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20201210_1337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='phone',
        ),
    ]