from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    url(r'^/$', BlogList.as_view(), name="blogs"),
    url(r'^/(?P<pk>[-\w]+)/$', BlogDetail.as_view(), name="blog_detail"),
    url(r'^/posts/(?P<pk>[-\w]+)/$', PostDetail.as_view(), name="post_detail"),
    url(r'^create/$', login_required(CreateBlog.as_view()), name="create_blog"),
    url(r'^/(?P<pk>[-\w]+)/edit/$', login_required(EditBlog.as_view()), name="edit_blog"),
    url(r'^/(?P<pk>[-\w]+)/post/$', login_required(CreatePost.as_view()), name="create_post"),
    url(r'^/posts/(?P<pk>[-\w]+)/edit/$', login_required(EditPost.as_view()), name="edit_post"),
    url(r'^/posts/(?P<pk>[-\w]+)/like/$', like, name='like'),
]
