from django.urls import path


from .views import SignUpView, AccountUpdateView, AccountCreateView
from .views import PasswordChangeView, PasswordChangeSuccessView


urlpatterns = [
     path('signup/', SignUpView.as_view(), name='signup'),
     path('passwordchange/<int:pk>',
         PasswordChangeView.as_view(), name='password_change'),
     path('passwordchange/success/',
         PasswordChangeSuccessView.as_view(), name='password_success'),
     path('userprofileupdate/<int:pk>', AccountUpdateView.as_view(), name='user_profile_update'),
     path('userprofile/<int:pk>', AccountCreateView.as_view(), name='user_profile')
]
