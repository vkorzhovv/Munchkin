# Generated by Django 4.1.6 on 2023-02-15 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('M', 'Мужской'), ('F', 'Женский'), ('O', 'Не задано')], default='O', max_length=1, verbose_name='Пол'),
        ),
    ]