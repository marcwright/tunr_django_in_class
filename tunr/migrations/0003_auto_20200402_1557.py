# Generated by Django 3.0.5 on 2020-04-02 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunr', '0002_song'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='album',
            field=models.CharField(default='No Album', max_length=100),
        ),
        migrations.AddField(
            model_name='song',
            name='preview_url',
            field=models.TextField(default='No Image'),
        ),
        migrations.AddField(
            model_name='song',
            name='title',
            field=models.CharField(default='No Title', max_length=100),
        ),
    ]
