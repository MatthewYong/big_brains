# Generated by Django 3.1.5 on 2021-01-31 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20210131_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.CharField(max_length=20),
        ),
    ]