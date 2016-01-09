from django.views.generic import DetailView
from sundayfunday.models import Event

class EventDetailView(DetailView):
    queryset = Event.objects.all()
    template_name = 'event-detail.html'

    def get_object(self):
        object = super(EventDetailView, self).get_object()
        return object
