# Generated by Django 4.2 on 2023-04-25 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vessels", "0004_rename_name_vessle_vessel_vessel_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vessel",
            name="cor_expiration",
            field=models.DateField(blank=True, null=True),
        ),
    ]
