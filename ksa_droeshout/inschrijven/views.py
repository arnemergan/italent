from django.views import generic
from .forms import FormSearch,FormLidNieuw,FormInschrijving,FormLidInschrijven
from .models import Inschrijving, Lid,InschrijvingLid
from django.contrib.messages.views import SuccessMessageMixin
from inschrijven import tables
from django_tables2 import SingleTableView
from django.http import HttpResponseRedirect

# Create your views here.
class InschrijvenView(generic.ListView):
    template_name = 'inschrijven.html'
    context_object_name = 'inschrijven_list'
    model = Inschrijving

    def get_queryset(self):
        return Inschrijving.objects.filter(actief=True)

class InschrijvenDetailView(generic.DetailView):
    template_name = 'inschrijven_info.html'
    model = Inschrijving

    def get_context_data(self, **kwargs):
        context = super(InschrijvenDetailView, self).get_context_data(**kwargs)
        context['form'] = FormSearch
        if ('voornaam' in self.request.GET and 'achternaam' in self.request.GET):
            voornaam = self.request.GET.get('voornaam')
            achternaam = self.request.GET.get('achternaam')
            if (len(voornaam) > 2 and len(achternaam) > 2):
                query = Lid.objects.filter(voornaam__contains=voornaam, achternaam__contains=achternaam)
                context['search'] = query
        return context

    def post(self,request,pk):
        print(self.request.POST['lid_id'])
        print(self.request.POST['inschrijving_id'])
        lid = InschrijvingLid(lidid_id=self.request.POST['lid_id'],inschrijvingid_id=self.request.POST['inschrijving_id'])
        InschrijvingLid.objects.get_or_create(lidid_id=str(lid.lidid),inschrijvingid_id=(str(lid.inschrijvingid)))
        # InschrijvingLid.save(lid)
        return HttpResponseRedirect('/')

class InschrijvenLidView(generic.TemplateView):
    template_name = 'inschrijven_info.html'

    def get_context_data(self, **kwargs):
        context = super(InschrijvenLidView, self).get_context_data(**kwargs)
        context['formSearch'] = FormSearch
        context['inschrijving'] = Inschrijving.objects.get(pk=self.kwargs.get('pk'))

class InschrijvenCreateView(SuccessMessageMixin,generic.CreateView):
    model = Inschrijving
    form_class = FormInschrijving
    success_url = '/inschrijven/list/'
    success_message = 'inschrijving is succesvol gecreëerd'

class InschrijvenUpdateView(SuccessMessageMixin,generic.UpdateView):
    model = Inschrijving
    form_class = FormInschrijving
    success_url = '/inschrijven/list/'
    success_message = 'inschrijving is succesvol geupdated'

class InschrijvenDeleteView(SuccessMessageMixin,generic.DeleteView):
    model = Inschrijving
    success_url = '/inschrijven/list/'
    success_message = 'inschrijving is succesvol gedeleted'


class InschrijvingAllView(SingleTableView):
    template_name = 'inschrijven_list.html'
    model = Inschrijving
    table_class = tables.InschrijvingTable

class InschrijveNieuwView(generic.CreateView):
    model = Lid
    form_class = FormLidNieuw
    success_url = '/inschrijven'

class LedenView(SingleTableView):
    template_name = 'leden/leden_list.html'
    model = Lid
    table_class = tables.LedenTable

class LidView(generic.DetailView):
    model = Lid
    template_name = 'leden/lid_detail.html'

    def get_object(self):
        return Lid.objects.get(pk=self.kwargs['lid_id'])

class LidDeleteView(generic.DeleteView):
    model = Lid
    success_url = '/dashboard'

    def get_object(self):
        return Lid.objects.get(pk=self.kwargs['lid_id'])

