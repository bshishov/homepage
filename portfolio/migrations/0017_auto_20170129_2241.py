# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-29 19:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0016_auto_20170129_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlecategory',
            name='keywords',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectgroup',
            name='keywords',
            field=models.TextField(blank=True, null=True),
        ),
    ]
