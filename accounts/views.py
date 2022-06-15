from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy
from .models import Account


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class PasswordChangeView(PasswordChangeView):
    template_name = 'registration/password_change_form.html'


class PasswordChangeSuccessView(PasswordChangeDoneView):
    template_name = 'registration/password_change_done.html'

class AccountUpdateView(UpdateView): 
    template_name = 'registration/user_profile_update.html'
    model = Account
    fields = ['image', 'username', 'name', 'about']

class AccountCreateView(CreateView): 
    template_name = 'registration/user_profile.html'
    model = Account
    fields = ['image', 'username', 'name', 'about']