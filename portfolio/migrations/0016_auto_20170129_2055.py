# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-29 17:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0015_articleattachment_visible'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articleattachment',
            old_name='project',
            new_name='article',
        ),
    ]
