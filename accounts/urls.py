from django.urls import path


from .views import SignUpView, RegisterView, profile
from .views import PasswordChangeView, PasswordChangeSuccessView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', profile, name='profile'),
    path('passwordchange/<int:pk>',
         PasswordChangeView.as_view(), name='password_change'),
    path('passwordchange/success/',
         PasswordChangeSuccessView.as_view(), name='password_success'),
]
