from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from .models import Content, Image


class PostListView(ListView):
    template_name = "photography/list.html"
    model = Content
    image_img = Image.objects.all()
    context_vars = {'image_img': image_img, }
    # context_object_name = 'photography'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(PostListView.context_vars)
        # context['image_img'] = Image.objects.all()
        return context


class PostDetailView(DetailView):
    template_name = "photography/content_detail.html"
    model = Content
    # context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image_img'] = Image.objects.all()
        return context


class FloraDetailView(ListView):
    template_name = "photography/flora.html"
    model = Content
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classification'] = Content.objects.filter(title='flora')
        return context


class BeachDetailView(ListView):
    template_name = "photography/beach.html"
    model = Content
    # context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classification'] = Content.objects.filter(title='beach')
        return context


class ArtDetailView(ListView):
    template_name = "photography/art.html"
    model = Content
    # context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classification'] = Content.objects.filter(title='art')
        return context


class PoetryDetailView(ListView):
    template_name = "photography/writings.html"
    model = Content
    # context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classification'] = Content.objects.filter(title='poetry')
        return context


class PostCreateView(CreateView):
    template_name = "photography/new.html"
    model = Content
    fields = ['title', 'text']


class PostUpdateView(UpdateView):
    template_name = "photography/edit.html"
    model = Content
    fields = ['title', 'text']


class PostDeleteView(DeleteView):
    template_name = "photography/delete.html"
    model = Content
    success_url = reverse_lazy('')
