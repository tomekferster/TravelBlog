# Generated by Django 4.2.3 on 2024-08-10 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_remove_comment_vote_remove_reply_vote_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
