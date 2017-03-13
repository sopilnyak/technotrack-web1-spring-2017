from .models import Comment
from django.views.generic.list import ListView


class CommentList(ListView):
    template_name = {"blog/post_detail.html", "blog/posts.html"}
    model = Comment
