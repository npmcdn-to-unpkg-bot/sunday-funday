from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from sundayfunday.models import Event

class IndexView(generic.TemplateView):
    template_name = 'index.html'


@method_decorator(login_required, name='dispatch')
class UserHomePageView(generic.View):
    def get(self, request, *args, **kwargs):
        # TODO for now, user gets all events in the database.
        # Later we can filter by preferences.
        relevant_events = Event.objects.all()
        return render(request, 'user-homepage.html',
                      context={'events' : relevant_events})
