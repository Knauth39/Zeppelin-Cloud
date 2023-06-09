# Generated by Django 4.2 on 2023-04-24 14:25

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Vessel",
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
                (
                    "thumbnail",
                    models.ImageField(default="yacht_image.jpg", upload_to="images/"),
                ),
                (
                    "vessel_type",
                    models.CharField(
                        choices=[
                            ("M/Y", "M/Y"),
                            ("M/V", "M/V"),
                            ("S/Y", "S/Y"),
                            ("S/V", "S/V"),
                            ("T/T", "T/T"),
                        ],
                        default="M/Y",
                        max_length=20,
                    ),
                ),
                ("name_vessle", models.CharField(max_length=200)),
                ("builder", models.CharField(max_length=200)),
                ("build_country", django_countries.fields.CountryField(max_length=200)),
                ("year_built", models.IntegerField(blank=True, null=True)),
                ("flag_country", django_countries.fields.CountryField(max_length=200)),
                ("home_port", models.CharField(max_length=200)),
                ("owner_name", models.CharField(max_length=200)),
                ("owner_country", django_countries.fields.CountryField(max_length=200)),
                ("cor_number", models.CharField(max_length=200)),
                ("cor_expiration", models.DateField()),
                ("imo_number", models.IntegerField(blank=True, null=True)),
                ("call_sign", models.CharField(max_length=200)),
                ("mmsi_number", models.IntegerField(blank=True, null=True)),
                ("length", models.IntegerField(blank=True, null=True)),
                ("beam", models.IntegerField(blank=True, null=True)),
                ("draft", models.IntegerField(blank=True, null=True)),
                ("gross_tonnage", models.IntegerField(blank=True, null=True)),
                ("net_tonnage", models.IntegerField(blank=True, null=True)),
                ("cbp_decal", models.IntegerField(blank=True, null=True)),
                ("crusing_permit", models.IntegerField(blank=True, null=True)),
                ("cruising_permit_exp", models.DateField()),
                ("class_society", models.CharField(max_length=200)),
                ("engine_make", models.CharField(max_length=200)),
                ("engine_hp", models.IntegerField(blank=True, null=True)),
                ("cofr_number", models.IntegerField(blank=True, null=True)),
                ("cofr_exp", models.DateField(blank=True, null=True)),
                ("ntvrp_number", models.IntegerField(blank=True, null=True)),
                ("ism_status", models.BooleanField(default=False)),
                ("for_charter", models.BooleanField(default=False)),
            ],
        ),
    ]
