# Generated by Django 3.2.5 on 2021-08-17 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210705_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.FileField(default='pics/default.jpg', upload_to='pics/'),
        ),
    ]
