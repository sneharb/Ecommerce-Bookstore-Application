# Generated by Django 3.1.4 on 2020-12-10 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20201210_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='subject',
            field=models.CharField(max_length=50, null=True),
        ),
    ]