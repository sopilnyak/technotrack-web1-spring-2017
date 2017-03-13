from django.views.generic.base import TemplateView

from blog.models import Blog
from blog.models import Post
from comments.models import Comment


class HomePageView(TemplateView):

    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['latest_blogs'] = Blog.objects.all()[:5]
        context['blogs_number'] = Blog.objects.all().count()
        context['posts_number'] = Post.objects.all().count()
        context['comments_number'] = Comment.objects.all().count()
        return context
