from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .models import Post


class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post


class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post
