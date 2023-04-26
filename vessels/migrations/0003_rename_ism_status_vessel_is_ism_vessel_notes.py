# Generated by Django 4.2 on 2023-04-25 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vessels", "0002_remove_vessel_beam_remove_vessel_draft_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="vessel",
            old_name="ism_status",
            new_name="is_ism",
        ),
        migrations.AddField(
            model_name="vessel",
            name="notes",
            field=models.TextField(blank=True),
        ),
    ]
