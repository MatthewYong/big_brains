# Generated by Django 3.1.5 on 2021-01-20 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_blog_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]