# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-09 17:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_order_is_cancelled'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_returned',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='is_shipped',
            field=models.BooleanField(default=False),
        ),
    ]
