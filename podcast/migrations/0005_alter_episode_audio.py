# Generated by Django 4.0.2 on 2022-02-23 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0004_episode_audio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='audio',
            field=models.FileField(default='audio/default.mp3', upload_to='audio/'),
        ),
    ]
