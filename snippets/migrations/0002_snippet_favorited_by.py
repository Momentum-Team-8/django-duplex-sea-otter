# Generated by Django 3.2.4 on 2021-06-28 16:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='favorited_by',
            field=models.ManyToManyField(related_name='fav_snippets', to=settings.AUTH_USER_MODEL),
        ),
    ]
