# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-29 14:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0014_auto_20170129_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='articleattachment',
            name='visible',
            field=models.BooleanField(default=False),
        ),
    ]
