# Generated by Django 4.1.4 on 2023-01-18 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_serviceimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceimage',
            name='name',
            field=models.CharField(default='service', max_length=100),
        ),
    ]