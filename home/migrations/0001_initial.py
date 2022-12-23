# Generated by Django 4.1.4 on 2022-12-21 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ClientImages",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("client_image", models.ImageField(upload_to="img/clients")),
            ],
            options={
                "verbose_name": "ClientImages",
                "verbose_name_plural": "ClientImagess",
            },
        ),
        migrations.CreateModel(
            name="PortFolio",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tab_text", models.CharField(max_length=20)),
                ("description", models.CharField(max_length=100)),
            ],
            options={"verbose_name": "PortFolio", "verbose_name_plural": "PortFolios",},
        ),
        migrations.CreateModel(
            name="Slider",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="img/sliders")),
                ("header", models.CharField(max_length=20)),
                ("description", models.CharField(max_length=100)),
                ("button_text", models.CharField(max_length=10)),
                ("button_link", models.CharField(max_length=10)),
            ],
            options={"verbose_name": "Slider", "verbose_name_plural": "Sliders",},
        ),
        migrations.CreateModel(
            name="WelcomingNote",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sideImage", models.ImageField(upload_to="img/abt")),
                ("header", models.CharField(max_length=30)),
                ("subheader", models.CharField(max_length=50)),
                ("descriptive_text", models.CharField(max_length=200)),
                ("bullet_list", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name": "WelcomingNote",
                "verbose_name_plural": "WelcomingNotes",
            },
        ),
        migrations.CreateModel(
            name="WhyChooseUS",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("header", models.CharField(max_length=100)),
                ("subHeader", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=300)),
            ],
            options={
                "verbose_name": "WhyChooseUS",
                "verbose_name_plural": "WhyChooseUSs",
            },
        ),
        migrations.CreateModel(
            name="PortfolioImages",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                ("description", models.CharField(max_length=100)),
                ("link", models.CharField(max_length=50)),
                ("image", models.ImageField(upload_to="img/portfolio")),
                (
                    "portfolio",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="home.portfolio",
                        verbose_name="",
                    ),
                ),
            ],
            options={
                "verbose_name": "PortfolioImages",
                "verbose_name_plural": "PortfolioImagess",
            },
        ),
    ]
