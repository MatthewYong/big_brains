# Generated by Django 3.1.5 on 2021-01-31 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='procurement_date',
        ),
        migrations.AddField(
            model_name='order',
            name='order_date',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
