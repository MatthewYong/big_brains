# Generated by Django 3.1.5 on 2021-02-14 11:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0003_remove_toyreview_user_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='toyreview',
            name='user_review',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
