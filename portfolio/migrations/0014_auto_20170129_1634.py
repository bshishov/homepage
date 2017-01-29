# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-29 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_auto_20170128_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilecontact',
            name='visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='articles', to='portfolio.Tag'),
        ),
        migrations.AlterField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='projects', to='portfolio.Tag'),
        ),
    ]
