# Generated by Django 4.2.1 on 2023-05-27 20:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 27, 20, 54, 16, 261163, tzinfo=datetime.timezone.utc)),
        ),
    ]
