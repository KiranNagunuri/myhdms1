# Generated by Django 2.2.4 on 2019-11-19 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HDMS_ADMIN', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empoyee',
            name='Emp_contact',
            field=models.IntegerField(default=True, unique=True),
        ),
    ]
