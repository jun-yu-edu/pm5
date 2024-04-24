# Generated by Django 4.2 on 2024-04-22 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_author'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bookmarks',
            field=models.ManyToManyField(related_name='bookmark_users', to='articles.article'),
        ),
    ]