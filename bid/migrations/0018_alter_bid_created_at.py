# Generated by Django 3.2.3 on 2021-05-28 06:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bid', '0017_alter_bid_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='created_at',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2021, 5, 28, 12, 53, 41, 611186)),
        ),
    ]