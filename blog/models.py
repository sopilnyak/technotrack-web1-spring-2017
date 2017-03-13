from __future__ import unicode_literals

from django.db import models
from application import settings


class Blog(models.Model):
    id = models.IntegerField
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)


class Post(models.Model):
    id = models.IntegerField
    header = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    text = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    blog = models.ForeignKey(Blog)
