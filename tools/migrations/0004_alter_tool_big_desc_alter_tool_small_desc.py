# Generated by Django 4.1.4 on 2023-01-25 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0003_tool_features_tool_specification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='big_desc',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='small_desc',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
