from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from .models import Blog


class PostListView(ListView):
    template_name = "blog/list.html"
    model = Blog


class PostDetailView(DetailView):
    template_name = "blog/detail.html"
    model = Blog


class PostCreateView(CreateView):
    template_name = "blog/new.html"
    model = Blog
    fields = ['title', 'text']


class PostUpdateView(UpdateView):
    template_name = "blog/edit.html"
    model = Blog
    fields = ['title', 'text']


class PostDeleteView(DeleteView):
    template_name = "blog/delete.html"
    model = Blog
    success_url = reverse_lazy('')
