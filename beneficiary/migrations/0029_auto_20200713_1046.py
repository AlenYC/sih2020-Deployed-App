# Generated by Django 3.0.5 on 2020-07-13 05:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiary', '0028_auto_20200712_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='userappointments',
            name='apassign',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='userappointments',
            name='apreceived',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='userbmi',
            name='bmdate',
            field=models.DateField(default=datetime.date(2020, 7, 13)),
        ),
    ]
