from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    path('', PostListView.as_view(), name='blog'),
    path('new/', PostCreateView.as_view(), name='blog_new'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name="blog_edit"),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name="blog_delete"),

    path('<int:pk>/', PostDetailView.as_view(), name='blog_detail'),
]
