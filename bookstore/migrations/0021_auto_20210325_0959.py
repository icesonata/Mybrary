# Generated by Django 2.0.3 on 2021-03-25 09:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0020_auto_20210313_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 25, 9, 59, 15, 157861, tzinfo=utc)),
        ),
    ]
