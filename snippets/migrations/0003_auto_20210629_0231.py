# Generated by Django 3.2.4 on 2021-06-29 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_snippet_favorited_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=75, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='snippet',
            name='category',
            field=models.ManyToManyField(related_name='snippets', to='snippets.Category'),
        ),
    ]