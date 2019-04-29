from django.shortcuts import redirect
from django.views import generic
from .forms import FormSearch,FormLidNieuw,FormInschrijving,FormLidInschrijven,FormAdres,FormGroepen,FormLeiding,FormUser,FormMultiLid
from .models import Inschrijving, Lid,InschrijvingLid,Leiding,Groep
from django.contrib.messages.views import SuccessMessageMixin
from inschrijven import tables
from django_tables2 import SingleTableView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages



# Create your views here.
class InschrijvenView(generic.ListView):
    template_name = 'inschrijven.html'
    context_object_name = 'inschrijven_list'
    model = Inschrijving

    def get_queryset(self):
        return Inschrijving.objects.filter(actief=True)

class InschrijvenDetailView(SuccessMessageMixin,generic.DetailView):
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
           #     if not query:
                    #messages.ERROR(self.request,'geen lid gevonden met die naam')
                context['search'] = query
          #  else:
                #messages.ERROR(self.request,'de lengte van voor en achternaam moeten minstens 2 letters lang zijn')
        return context

class InschrijvenLidView(SuccessMessageMixin,generic.CreateView):
    template_name = 'inschrijven/inschrijvinglid_form.html'
    form_class = FormLidInschrijven
    success_url = '/inschrijven'
    success_message = 'Jouw lid is ingeschreven'

    def get_initial(self):
        lid_id = self.kwargs['lid_id']
        inschrijving_id = self.kwargs['inschrijven_id']
        return {
            'inschrijvingid': inschrijving_id,
            'lidid':lid_id,
        }

    def get_context_data(self, **kwargs):
        context = super(InschrijvenLidView, self).get_context_data(**kwargs)
        context['lid'] = Lid.objects.get(uuid__exact=self.kwargs['lid_id'])
        return context

class InschrijvenLidListView(SingleTableView):
    model = InschrijvingLid
    table_class = tables.InschrijvingLidTable
    template_name = 'inschrijvinglid_list.html'

    def get_context_data(self, **kwargs):
        context = super(InschrijvenLidListView,self).get_context_data(**kwargs)
        context['inschrijving'] = Inschrijving.objects.filter(id=self.kwargs.get('pk')).first()
        return context

    def get_queryset(self):
        return InschrijvingLid.objects.filter(inschrijvingid_id=self.kwargs.get('pk'))

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

class InschrijveNieuwView(SuccessMessageMixin,generic.CreateView):
    model = Lid
    form_class = FormMultiLid
    success_url = '/inschrijven/nieuw/'
    success_message = 'Uw lid is succesvol ingeschreven'

    def form_valid(self, form):
        adres = form['adres'].save()
        lid = form['lid'].save(commit=False)
        lid.adresid = adres
        lid.save()
        return redirect(self.get_success_url())

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

class BegeleidingView(generic.ListView):
    model = Leiding
    template_name = 'begeleiding.html'
    context_object_name = 'begeleiding_list'
    ordering = ['groep']

class GroepenView(generic.ListView):
    model = Groep
    template_name = 'groepen.html'
    context_object_name = 'groep_list'

class GroepUpdateView(SuccessMessageMixin,generic.UpdateView):
    model = Groep
    form_class = FormGroepen
    success_url = '/dashboard/groepen'
    template_name = 'groep/groep_form.html'

class GroepListView(SingleTableView):
    model = Groep
    template_name = 'groep/groep_list.html'
    table_class = tables.GroepenTable

class LeidingListView(SingleTableView):
    model = Leiding
    template_name = 'leiding/leiding_list.html'
    table_class = tables.LeidingTable

class LeidingCreateView(SuccessMessageMixin,generic.CreateView):
    model = Leiding
    template_name = 'leiding/leiding_form.html'
    success_url = '/dashboard/leiding'
    success_message = 'leiding is gecreeerd'
    form_class = FormLeiding

class LeidingDeleteView(SuccessMessageMixin,generic.DeleteView):
    model = Leiding
    success_url = '/dashboard/leiding/'
    template_name = 'leiding/leiding_confirm_delete.html'
    success_message = 'leiding is succesvol gedeleted'

class UserCreateView(SuccessMessageMixin,generic.CreateView):
    model = User
    form_class = FormUser
    success_url = '/dashboard/user/'
    template_name = 'leiding/leiding_form.html'
    success_message = 'user is succesvol gecreeerd'

class UserListView(SingleTableView):
    model = Leiding
    template_name = 'leiding/user_list.html'
    table_class = tables.UserTable

class UserDeleteView(SuccessMessageMixin,generic.DeleteView):
    model = Leiding
    success_url = '/dashboard/user/'
    template_name = 'leiding/user_confirm_del.html'
    success_message = 'user is succesvol gedeleted'
