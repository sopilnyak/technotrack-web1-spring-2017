from __future__ import unicode_literals

from django.db import models
from application import settings
from blog.models import Post


class Comment(models.Model):
    id = models.IntegerField
    text = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey(Post)
