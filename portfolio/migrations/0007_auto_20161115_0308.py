# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-15 00:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20161115_0252'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profilecontact',
            options={'ordering': ('order',)},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ('order',)},
        ),
        migrations.AlterModelOptions(
            name='projectgroup',
            options={'ordering': ('order',)},
        ),
        migrations.AlterModelOptions(
            name='projectimage',
            options={},
        ),
        migrations.RemoveField(
            model_name='projectimage',
            name='order',
        ),
        migrations.AlterField(
            model_name='profilecontact',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='project',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='projectgroup',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
