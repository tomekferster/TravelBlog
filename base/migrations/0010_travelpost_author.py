# Generated by Django 4.2.3 on 2023-09-23 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_name_profile_social_instagram'),
        ('base', '0009_alter_comment_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='travelpost',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile'),
        ),
    ]
