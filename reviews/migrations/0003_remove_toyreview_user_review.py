# Generated by Django 3.1.5 on 2021-02-14 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_toyreview_user_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='toyreview',
            name='user_review',
        ),
    ]
