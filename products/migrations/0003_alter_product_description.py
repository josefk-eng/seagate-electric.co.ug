# Generated by Django 4.1.4 on 2023-01-26 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_features_product_specification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
