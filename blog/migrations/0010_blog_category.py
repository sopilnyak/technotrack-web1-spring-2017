# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 13:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20170327_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ManyToManyField(default=None, to='blog.Category'),
        ),
    ]
