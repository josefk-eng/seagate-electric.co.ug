# Generated by Django 4.1.4 on 2022-12-27 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=2000)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('rating', models.IntegerField(default=0)),
                ('type', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='img/products')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
