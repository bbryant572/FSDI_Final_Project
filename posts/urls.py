from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import (
    FloraDetailView,
    BeachDetailView,
    ArtDetailView,
    PoetryDetailView,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    FloraDetailView,
)

urlpatterns = [
    path('', PostListView.as_view(), name='content_list'),
    path('flora/', FloraDetailView.as_view(), name='flora_list'),
    path('beach/', BeachDetailView.as_view(), name='beach_list'),
    path('art/', ArtDetailView.as_view(), name='art_list'),
    path('writing/', PoetryDetailView.as_view(), name='poetry_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='content_detail'),
    path('new/', PostCreateView.as_view(), name='content_new'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name="content_edit"),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name="content_delete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
