from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from agenda.forms import FormAgendaItem
from .models import AgendaItem
from django_tables2 import SingleTableView
from agenda import tables

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'agenda_items_list'
    
    def get_queryset(self):
        return AgendaItem.objects.order_by('datumvan')[:6]

class AgendaItemDetailView(generic.DetailView):
    template_name = 'agenda_item.html'
    model = AgendaItem

class AgendaItemCreateView(SuccessMessageMixin,generic.CreateView):
    model = AgendaItem
    form_class = FormAgendaItem
    success_url = '/agenda/list'
    success_message = 'agenda item succesvol gecreëerd'

class AgendaItemUpdateView(SuccessMessageMixin,generic.UpdateView):
    model = AgendaItem
    form_class = FormAgendaItem
    success_url = '/agenda/list'
    success_message = 'agenda item succesvol geupdated'

class AgendaItemDeleteView(SuccessMessageMixin,generic.DeleteView):
    model = AgendaItem
    success_url = '/agenda/list'
    success_message = 'agenda item succesvol gedeleted'

class AgendaItemView(SingleTableView):
    template_name = 'agenda_list.html'
    model = AgendaItem
    table_class = tables.AgendaItemTable


class AgendaView(generic.ListView):
    template_name = 'agenda.html'
    context_object_name = 'agenda_items_list'

    def get_queryset(self):
        return AgendaItem.objects.order_by('datumvan')