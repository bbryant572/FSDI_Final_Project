from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from .models import Post, Images


class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image_img'] = Images.objects.all()
        return context


class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image_img'] = Images.objects.all()
        return context


class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ['title', 'text']


class PostUpdateView(UpdateView):
    template_name = "post/edit.html"
    model = Post
    fields = ['title', 'text']


class PostDeleteView(DeleteView):
    template_name = "post/delete.html"
    model = Post
    success_url = reverse_lazy('')
