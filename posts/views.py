from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from .models import Content, Image


class BeachListView(ListView):
    template_name = "beaches/list.html"
    model = Content
    image_img = Image.objects.all()
    context_vars = {'image_img': image_img, }
    # context_object_name = 'photography'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(BeachListView.context_vars)
        # context['image_img'] = Image.objects.all()
        return context


class BeachDetailView(DetailView):
    template_name = "beaches/content_detail.html"
    model = Content
    # context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image_img'] = Image.objects.all()
        return context


class BeachCreateView(CreateView):
    template_name = "beaches/new.html"
    model = Content
    fields = ['title', 'text']


class BeachUpdateView(UpdateView):
    template_name = "beaches/edit.html"
    model = Content
    fields = ['title', 'text']


class BeachDeleteView(DeleteView):
    template_name = "beaches/delete.html"
    model = Content
    success_url = reverse_lazy('')


class CocoDetailView(ListView):
    template_name = "beaches/coco.html"
    model = Content
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classification'] = Content.objects.filter(
            title='playas del coco')
        return context


class OcotalDetailView(ListView):
    template_name = "beaches/ocotal.html"
    model = Content
    # context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classification'] = Content.objects.filter(
            title='playa ocotal')
        return context


class HermosaDetailView(ListView):
    template_name = "beaches/hermosa.html"
    model = Content
    # context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classification'] = Content.objects.filter(
            title='playa hermosa')
        return context


class BallenaDetailView(ListView):
    template_name = "beaches/ballena.html"
    model = Content
    # context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classification'] = Content.objects.filter(
            title='marino ballena')
        return context
