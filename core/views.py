from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
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


class UserForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2')


class CreateUser(CreateView):

    template_name = 'registration/registration_form.html'
    model = get_user_model()
    form_class = UserForm
    success_url = reverse_lazy('home')
