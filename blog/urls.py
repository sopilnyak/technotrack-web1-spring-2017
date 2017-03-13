from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^/$', BlogList.as_view(), name="blogs"),
    url(r'^/(?P<pk>[-\w]+)/$', BlogDetail.as_view(), name="blog_detail"),
    url(r'^/posts/(?P<pk>[-\w]+)/$', PostDetail.as_view(), name="post_detail"),
]
