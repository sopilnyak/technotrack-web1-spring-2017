from __future__ import unicode_literals

from django.db import models
from application import settings


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title


class Blog(models.Model):
    title = models.TextField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    category = models.ManyToManyField(Category, default=None)

    def __unicode__(self):
        return self.title


class Post(models.Model):
    header = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    blog = models.ForeignKey(Blog)

    def __unicode__(self):
        return self.header


class Rating(models.Model):
    value = models.IntegerField(default=0)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey(Post)


class PostLike(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey(Post)

