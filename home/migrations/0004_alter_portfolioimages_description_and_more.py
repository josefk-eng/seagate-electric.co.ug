# Generated by Django 4.1.4 on 2023-01-16 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_alter_portfolio_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="portfolioimages",
            name="description",
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name="portfolioimages",
            name="link",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
