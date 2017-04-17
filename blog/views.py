import json

from django.forms import TextInput, Textarea, SelectMultiple
from django.forms.models import ModelForm
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views import View

from .models import Blog
from .models import Post
from .models import PostLike
from comments.models import Comment
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView
from django.shortcuts import get_object_or_404


class CreateForm(ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'category')
        widgets = {
            'title': TextInput(),
            'category': SelectMultiple(attrs={'class': 'categories'})
        }


class CreateBlog(CreateView):

    template_name = 'blog/create_blog.html'
    model = Blog
    success_url = reverse_lazy('blogs:blogs')
    form_class = CreateForm

    #def get_success_url(self):
    #    return reverse('blogs:blog_detail', (self.object.pk, ))

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateBlog, self).form_valid(form)


class EditBlog(UpdateView):

    template_name = 'blog/edit_blog.html'
    model = Blog
    success_url = '../'
    form_class = CreateForm

    def form_valid(self, form):
        return super(EditBlog, self).form_valid(form)

    def get_queryset(self):
        return super(EditBlog, self).get_queryset().filter(author=self.request.user)


class BlogList(ListView):

    template_name = "blog/blogs.html"
    model = Blog

    def get_context_data(self, **kwargs):
        context = super(BlogList, self).get_context_data(**kwargs)
        context['sort'] = self.request.GET.get('orderby', 'id')
        return context

    def get_queryset(self):
        key = self.request.GET.get('orderby', 'id')
        if key not in ['title', 'id']:
            key = 'id'
        return Blog.objects.order_by(key)


class BlogDetail(DetailView):

    template_name = "blog/blog_detail.html"
    model = Blog


class CreatePost(CreateView):

    template_name = 'blog/create_post.html'
    model = Post
    fields = ('header', 'description', 'text')
    success_url = '../'

    def form_valid(self, form, pk=None):
        form.instance.author = self.request.user
        form.instance.blog = get_object_or_404(Blog, id=self.kwargs['pk'])
        return super(CreatePost, self).form_valid(form)


class EditPost(UpdateView):

    template_name = 'blog/edit_post.html'
    model = Post
    fields = ('header', 'description', 'text')
    success_url = '../'

    def get_queryset(self):
        return super(EditPost, self).get_queryset().filter(author=self.request.user)

    def form_valid(self, form):
        response = super(EditPost, self).form_valid(form)
        return JsonResponse({
            'success': True,
            'text': '...'
        })


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': Textarea(attrs={'rows': '2'}),
        }


class PostDetail(CreateView):

    template_name = 'blog/post_detail.html'
    model = Comment
    success_url = '.'
    form_class = CommentForm

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.postobject = get_object_or_404(Post, id=pk)
        return super(PostDetail, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['post'] = self.postobject
        # get list of comments added to current post
        context['comment_set'] = Comment.objects.filter(post_id=self.kwargs['pk'])
        context['like_number'] = PostLike.objects.filter(post=self.postobject).count()

        if not self.request.user.is_anonymous():
            if not PostLike.objects.filter(post=self.postobject).filter(author=self.request.user).exists():
                context['like_status'] = '+'
            else:
                context['like_status'] = '-'

        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, id=self.kwargs['pk'])
        response = super(PostDetail, self).form_valid(form)
        return JsonResponse({
            'success': 'true',
            'text': form.instance.text
        })


class PostCommentsView(DetailView):
    template_name = 'blog/comments.html'
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PostCommentsView, self).get_context_data(**kwargs)
        # get list of comments added to current post
        context['comment_set'] = Comment.objects.filter(post_id=self.kwargs['pk'])
        return context


class PostContainerView(DetailView):
    template_name = 'blog/post_container.html'
    queryset = Post.objects.all()


class PostLikeAjaxView(View):
    def dispatch(self, request, pk=None, *args, **kwargs):
        self.post_object = get_object_or_404(Post, id=pk)
        return super(PostLikeAjaxView, self).dispatch(request, *args, **kwargs)

    def post(self, data):
        # if user didn't liked it yet
        status = 'null'
        if not self.request.user.is_anonymous():
            if not PostLike.objects.filter(post=self.post_object).filter(author=self.request.user).exists():
                PostLike(author=self.request.user, post=self.post_object).save()
                status = 'set'
            else:  # reset like
                PostLike.objects.filter(post=self.post_object).filter(author=self.request.user).delete()
                status = 'unset'

        return JsonResponse({
            'number': PostLike.objects.filter(post=self.post_object).count(),
            'status': status
        })
