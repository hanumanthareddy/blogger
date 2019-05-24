from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views import generic


class PostsView(ListView):
    model = Post
    template_name = 'index.html'


class PostDetailedView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostNew(CreateView):
    model = Post
    template_name = 'create_post.html'
    fields = ['title', 'body']


class PostUpdate(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ['title', 'body']


class PostDelete(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('index')
