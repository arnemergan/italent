from django.views import generic
from datetime import datetime, timedelta, date
from django.utils.safestring import mark_safe
from calendar import HTMLCalendar
from calendar import calendar

from .models import AgendaItem

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'agenda_items_list'
    
    def get_queryset(self):
        return AgendaItem.objects.order_by('datumvan')[:6]

class AgendaItemView(generic.DetailView):
    template_name = 'agenda_item.html'
    model = AgendaItem
    
class AgendaView(generic.ListView):
    template_name = 'agenda.html'
    context_object_name = 'agenda_items_list'

    def get_queryset(self):
        return AgendaItem.objects.order_by('datumvan')