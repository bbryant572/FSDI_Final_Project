from django.urls import path
from .views import HomePageView, AboutPageView, MainPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home_firstpage"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("main/", MainPageView.as_view(), name="home_loggedin"),
]
