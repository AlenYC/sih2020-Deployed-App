# Generated by Django 3.0.7 on 2020-07-26 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiary', '0037_auto_20200726_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficiary_register',
            name='u_phno',
            field=models.CharField(default=None, max_length=13, null=True),
        ),
    ]
