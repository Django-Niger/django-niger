# Generated by Django 5.0.6 on 2024-05-23 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("event", "0002_rename_category_category_evenement"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="external_link",
            field=models.URLField(blank=True, null=True),
        ),
    ]
