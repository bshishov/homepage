# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-13 12:33
from __future__ import unicode_literals

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20161113_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectimage',
            name='image',
            field=sorl.thumbnail.fields.ImageField(upload_to='portfolio/images'),
        ),
    ]
