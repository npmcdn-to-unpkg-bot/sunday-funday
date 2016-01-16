"""Login, Register, Change pass. """

import httplib

from django import shortcuts
from django.contrib import auth
from django.views import generic

from sundayfunday.forms.register import UpdateUserForm
from sundayfunday.models import User

class LoginView(generic.TemplateView):
    template_name = 'login.html'

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return shortcuts.redirect('/')
            else:
                return shortcuts.render(
                        request, self.template_name,
                        {'error': 'Inactive User, call Support'},
                        status=httplib.UNAUTHORIZED)
        else:
            return shortcuts.render(
                    request, self.template_name,
                    {'error': 'User Or Password are Invalid'},
                    status=httplib.UNAUTHORIZED)

class LogoutView(generic.View):

    def get(self, request):
        auth.logout(request)
        return shortcuts.redirect('/')

class UserEditView(generic.UpdateView):
    form_class = UpdateUserForm
    model = User
    success_url = '/'
    template_name = 'useredit.html'
