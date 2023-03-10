# Generated by Django 4.1.4 on 2023-01-18 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_serviceimage_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='SideNotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sideImage', models.ImageField(upload_to='img/sideNotes')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'SideNotes',
                'verbose_name_plural': 'SideNotes',
            },
        ),
    ]
