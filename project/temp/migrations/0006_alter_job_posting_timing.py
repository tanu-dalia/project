# Generated by Django 4.0.4 on 2022-05-25 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temp', '0005_user_profile_qualification_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_posting',
            name='timing',
            field=models.CharField(max_length=200),
        ),
    ]
