# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-17 01:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_auto_20170417_0115'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='value',
            field=models.IntegerField(default=0),
        ),
    ]