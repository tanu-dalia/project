# Generated by Django 4.0.4 on 2022-06-11 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temp', '0008_resumemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='resumemodel',
            name='address',
            field=models.CharField(default='', max_length=400),
        ),
    ]
