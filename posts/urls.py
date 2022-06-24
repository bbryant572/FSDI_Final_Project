from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import (
    CocoDetailView,
    OcotalDetailView,
    HermosaDetailView,
    BallenaDetailView,
    BeachListView,
    BeachDetailView,
    BeachCreateView,
    BeachUpdateView,
    BeachDeleteView,
)

urlpatterns = [
    path('', BeachListView.as_view(), name='content_list'),
    path('coco/', CocoDetailView.as_view(), name='coco_list'),
    path('ocotal/', OcotalDetailView.as_view(), name='ocotal_list'),
    path('hermosa/', HermosaDetailView.as_view(), name='hermosa_list'),
    path('ballena/', BallenaDetailView.as_view(), name='ballena_list'),
    path('<int:pk>/', BeachDetailView.as_view(), name='content_detail'),
    path('new/', BeachCreateView.as_view(), name='content_new'),
    path('<int:pk>/edit/', BeachUpdateView.as_view(), name="content_edit"),
    path('<int:pk>/delete/', BeachDeleteView.as_view(), name="content_delete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
