from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    path('', PostListView.as_view(), name='photography_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='photography_detail'),
    path('new/', PostCreateView.as_view(), name='photography_new'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name="photography_edit"),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name="photography_delete"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
