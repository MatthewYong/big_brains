# Generated by Django 3.1.5 on 2021-02-08 20:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20210208_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]