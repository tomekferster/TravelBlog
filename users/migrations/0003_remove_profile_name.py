# Generated by Django 4.2.3 on 2023-09-23 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
    ]
