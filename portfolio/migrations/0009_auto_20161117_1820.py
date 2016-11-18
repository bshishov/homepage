# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-17 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_auto_20161115_0309'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='short_description',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='profilecontact',
            name='link',
            field=models.CharField(blank=True, max_length=1024),
        ),
    ]