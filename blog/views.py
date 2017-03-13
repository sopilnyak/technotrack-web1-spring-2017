from .models import Blog
from .models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class BlogList(ListView):
    template_name = "blog/blogs.html"
    model = Blog


class BlogDetail(DetailView):
    template_name = "blog/blog_detail.html"
    model = Blog


class PostDetail(DetailView):
    template_name = "blog/post_detail.html"
    model = Post

