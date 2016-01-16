from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from sundayfunday.models import Event
from sundayfunday.models import AttendEvent
from sundayfunday.models import Preference
from sundayfunday.forms.event import FilterEventForm

class IndexView(generic.TemplateView):
    template_name = 'index.html'


@method_decorator(login_required, name='dispatch')
class UserHomePageView(generic.View):
    def get(self, request, *args, **kwargs):

        preferences = Preference.objects.all()
        pref = request.GET.getlist("preference", None)
        event_name = request.GET.get("event_name", "")
        relevant_events = Event.objects.all().distinct()
        attended_events = AttendEvent.objects.filter(user__id=request.user.id)
        attended_events = map(lambda x: x.event.id, attended_events)
        print attended_events

        if pref:
            relevant_events = relevant_events.filter(preference__name__in=pref).distinct()
        if not event_name == "":
            relevant_events = relevant_events.filter(title__contains=event_name).distinct()

        return render(request, 'user-homepage.html',
                      context={'events' : relevant_events,
                               'preferences' : preferences,
                               'selected_preferences' : pref,
                               'event_name_prefill' : event_name,
                               'attended_events' : attended_events})
