from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from .models import Post


class PostListView(ListView):
    template_name = "blog/list.html"
    model = Post


class PostDetailView(DetailView):
    template_name = "blog/detail.html"
    model = Post


class PostCreateView(CreateView):
    template_name = "blog/new.html"
    model = Post
    fields = ['title', 'text']


class PostUpdateView(UpdateView):
    template_name = "blog/edit.html"
    model = Post
    fields = ['title', 'text']


class PostDeleteView(DeleteView):
    template_name = "blog/delete.html"
    model = Post
    success_url = reverse_lazy('')
