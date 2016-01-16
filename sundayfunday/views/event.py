from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import render

from sundayfunday.forms.event import AddEventForm
from sundayfunday.forms.event import UpdateEventForm
from sundayfunday.models import Event
from sundayfunday.models import AttendEvent
from sundayfunday.models import User
from django.utils import timezone

class EventDetailView(DetailView):
    queryset = Event.objects.all()
    template_name = 'event-detail.html'

    def get_object(self):
        object = super(EventDetailView, self).get_object()
        return object

    def post(self, request, *args, **kwargs):
        print(request.POST)
        object = self.get_object()
        attend_events = AttendEvent.objects. \
            filter(user__id=int(request.POST['user'])).filter(event__id=object.id)
        toggle = request.POST.get('toggle', None)
        if toggle == None:
            return HttpResponse("WRONG REQUEST")
        if toggle == 'true':
            if len(attend_events) == 0:
                user = User.objects.get(id=int(request.POST['user']))
                AttendEvent(user=user, event=object, data=timezone.now()).save()
        if toggle == 'false':
            if len(attend_events) > 0:
                attend_events.delete()
        return HttpResponse("OK")


class AddEventView(CreateView):
    form_class = AddEventForm
    success_url = '/'
    template_name = 'addevent.html'

    def post(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.POST['owner'] = request.user.id
        return super(AddEventView, self).post(request, *args, **kwargs)

class EventEditView(UpdateView):
    form_class = UpdateEventForm
    model = Event
    success_url = '/'
    template_name = 'eventedit.html'

class SeeUpcomingEventsView(View):
    def get(self, request, *args, **kwargs):
        attended_events = AttendEvent.objects.filter(user__id=request.user.id)
        attended_events = map(lambda x: x.event, attended_events)
        return render(request, 'upcoming-events.html',
                context={'events': attended_events})
