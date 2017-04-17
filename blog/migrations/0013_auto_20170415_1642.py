# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-15 16:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='like',
            name='post',
        ),
        migrations.RemoveField(
            model_name='like',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='post',
            name='rating',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Like'),
        ),
    ]