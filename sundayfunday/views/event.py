from django.views.generic import CreateView
from django.views.generic import DetailView

from sundayfunday.forms.event import AddEventForm
from sundayfunday.models import Event

class EventDetailView(DetailView):
    queryset = Event.objects.all()
    template_name = 'event-detail.html'

    def get_object(self):
        object = super(EventDetailView, self).get_object()
        return object


class AddEventView(CreateView):
    form_class = AddEventForm
    success_url = '/'
    template_name = 'addevent.html'

    def post(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.POST['owner'] = request.user.id
        return super(AddEventView, self).post(request, *args, **kwargs)
