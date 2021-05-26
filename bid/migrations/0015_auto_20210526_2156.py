# Generated by Django 3.2.3 on 2021-05-26 15:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bid', '0014_auto_20210526_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bid_amount',
            field=models.DecimalField(decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='bid',
            name='created_at',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2021, 5, 26, 21, 56, 26, 428595)),
        ),
    ]
