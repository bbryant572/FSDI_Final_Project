from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
)

urlpatterns = [
    path('', PostListView.as_view(), name='posts_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]
