from django.contrib.auth.forms import PasswordResetForm
from django.shortcuts import render
from django.views.generic import CreateView

from sundayfunday.forms.addevent import AddEventForm

class AddEventView(CreateView):
    form_class = AddEventForm
    success_url = '/'
    template_name = 'addevent.html'

    def post(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.POST['owner'] = request.user.id
        return super(AddEventView, self).post(request, *args, **kwargs)

