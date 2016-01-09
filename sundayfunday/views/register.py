from django.contrib.auth.forms import PasswordResetForm
from django.shortcuts import render
from django.views.generic import CreateView

from sundayfunday.forms.register import RegisterUserForm
from django.contrib.auth.models import User

class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    model = User
    success_url = '/'
    template_name = 'register.html'
