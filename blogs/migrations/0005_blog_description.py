# Generated by Django 3.1.5 on 2021-01-21 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_auto_20210120_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='description',
            field=models.CharField(default=10, max_length=200),
            preserve_default=False,
        ),
    ]