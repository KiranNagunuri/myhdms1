# Generated by Django 2.2.4 on 2019-11-26 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HDMS_ADMIN', '0006_auto_20191125_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctordevices',
            name='DEVICE_NAME',
            field=models.CharField(default=False, max_length=25),
        ),
        migrations.AddField(
            model_name='doctordevices',
            name='DOCTOR_NAME',
            field=models.CharField(default=False, max_length=30),
        ),
    ]
