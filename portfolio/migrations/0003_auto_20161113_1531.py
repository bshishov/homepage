# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-13 12:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20161113_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectimage',
            name='image',
            field=models.ImageField(upload_to='portfolio/images'),
        ),
    ]