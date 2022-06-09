from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from .models import Photography, Image


class PostListView(ListView):
    template_name = "photography/list.html"
    model = Image
    context_object_name = 'photography'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image_img'] = Image.objects.all()
        return context


class PostDetailView(DetailView):
    template_name = "photography/detail.html"
    model = Photography
    # context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image_img'] = Image.objects.all()
        return context


class PostCreateView(CreateView):
    template_name = "photography/new.html"
    model = Photography
    fields = ['title', 'text']


class PostUpdateView(UpdateView):
    template_name = "photography/edit.html"
    model = Photography
    fields = ['title', 'text']


class PostDeleteView(DeleteView):
    template_name = "photography/delete.html"
    model = Photography
    success_url = reverse_lazy('')
