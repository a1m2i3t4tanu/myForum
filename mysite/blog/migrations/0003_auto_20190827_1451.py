# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-08-27 09:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190827_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 27, 9, 21, 32, 327472, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 27, 9, 21, 32, 327472, tzinfo=utc)),
        ),
    ]
