# Generated by Django 4.1.4 on 2023-01-27 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contactmessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmessage',
            name='message',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='contactmessage',
            name='subject',
            field=models.CharField(max_length=100),
        ),
    ]
