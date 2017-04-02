from django.forms import TextInput, Textarea
from django.forms.models import ModelForm
from django.urls import reverse_lazy

from .models import Blog
from .models import Post
from comments.models import Comment
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView
from django.shortcuts import get_object_or_404, render
from django import forms


class CreateForm(ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'category')
        widgets = {
            'title': TextInput(),
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
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, id=self.kwargs['pk'])
        return super(PostDetail, self).form_valid(form)


class LikeForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('rating', )


def like(request, pk=None):

    post = get_object_or_404(Post, id=pk)

    if request.method == 'GET':
        form = LikeForm()
    else:
        form = LikeForm(request.POST, instance=post)
        post.rating = post.rating + 1
        post.save()
    return render(request, 'blog/blog_detail.html', {'form': form})
