# Generated by Django 4.0 on 2024-03-01 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='visibility',
            field=models.BooleanField(),
        ),
    ]
