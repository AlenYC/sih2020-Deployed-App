# Generated by Django 3.0.5 on 2020-07-09 11:04

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiary', '0019_userbmi_bmuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='userappointments',
            name='apuser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='beneficiary.beneficiary_register'),
        ),
        migrations.AlterField(
            model_name='userbmi',
            name='bmdate',
            field=models.DateField(default=datetime.date(2020, 7, 9)),
        ),
    ]
