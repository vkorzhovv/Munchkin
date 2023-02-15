# Generated by Django 4.1.6 on 2023-02-15 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rulesbook',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rulesBook', to='users.profile', verbose_name='Владелец книги'),
        ),
    ]