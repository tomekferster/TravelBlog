# Generated by Django 4.2.3 on 2023-08-20 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_travelpost_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelpost',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='travelpost',
            name='text',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]
