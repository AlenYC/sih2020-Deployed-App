# Generated by Django 3.0.5 on 2020-07-04 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiary', '0002_auto_20200704_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficiary_register',
            name='u_verified',
            field=models.CharField(max_length=13, null=True),
        ),
    ]
