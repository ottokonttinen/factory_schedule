from django.views.generic import TemplateView
from .models import *

class ScheduleView(TemplateView):
    template_name = 'schedule/schedule.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        days = Day.objects.all()
        stations = Station.objects.all()
        schedule = Schedule.objects.all()
        context['days'] = days
        context['stations'] = stations
        context['schedule'] = schedule
        return context
