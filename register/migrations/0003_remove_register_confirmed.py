# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-19 06:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20160118_1204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='confirmed',
        ),
    ]
