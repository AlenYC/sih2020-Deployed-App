# Generated by Django 3.0.7 on 2020-07-12 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiary', '0027_auto_20200712_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userappointments',
            name='apstatus',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
