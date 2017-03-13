from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^/$', CommentList.as_view(), name="comments"),
]