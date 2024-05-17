# Generated by Django 4.2.13 on 2024-05-17 06:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_bm_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loandetails',
            name='last_payment_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 17, 6, 12, 31, 184258), null=True),
        ),
        migrations.AddField(
            model_name='loandetails',
            name='total_interest',
            field=models.FloatField(default=0),
        ),
    ]
