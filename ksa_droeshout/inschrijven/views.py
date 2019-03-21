from django.shortcuts import render
from django.views import generic
from .models import Inschrijving

# Create your views here.
class InschrijvenView(generic.ListView):
    template_name = 'inschrijven.html'
    context_object_name = 'inschrijven_list'

    def get_queryset(self):
        return Inschrijving.objects.all()

class InschrijvenDetailView(generic.DetailView):
    template_name = 'inschrijven_info.html'
    model = Inschrijving