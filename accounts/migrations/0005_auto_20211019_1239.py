# Generated by Django 3.2.3 on 2021-10-19 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20211019_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='buyer',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='seller',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]