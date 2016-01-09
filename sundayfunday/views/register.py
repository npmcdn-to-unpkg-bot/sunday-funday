from django.contrib.auth.forms import PasswordResetForm
from django.shortcuts import render
from django.views.generic import CreateView

from sundayfunday.forms.register import RegisterUserForm

class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    success_url = '/'
    template_name = 'register.html'
