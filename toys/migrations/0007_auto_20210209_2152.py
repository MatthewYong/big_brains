# Generated by Django 3.1.5 on 2021-02-09 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toys', '0006_toyreview_toy_sku'),
    ]

    operations = [
        migrations.RenameField(
            model_name='toyreview',
            old_name='toy_sku',
            new_name='toy_review',
        ),
    ]
