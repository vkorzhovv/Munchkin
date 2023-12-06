# Generated by Django 4.1.6 on 2023-12-06 07:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("room", "0020_playerpower_creator"),
    ]

    operations = [
        migrations.AddField(
            model_name="playerleavel",
            name="creator",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="created_leavel",
                to=settings.AUTH_USER_MODEL,
                verbose_name="создатель",
            ),
        ),
    ]
