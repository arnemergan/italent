from django.views import generic
from .forms import FormAddUser,FormSearch,FormLidInschrijven,FormGroepen,FormLeiding,FormMultiLid,FormSearchLid,FormInschrijving
from .models import Inschrijving, Lid,InschrijvingLid,Leiding,Groep,Contact_Geg,InschrijvingAllowed,Fiche_Geg
from agenda.models import Adres
from django.contrib.messages.views import SuccessMessageMixin
from inschrijven import tables
from django.db.models import Q
from django_tables2 import SingleTableView
from .resources import LidResource
from django.http import HttpResponse
from django.contrib.auth.mixins import UserPassesTestMixin

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
                context['search'] = query
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

    # def get_form_kwargs(self):
    #     kwargs = super(InschrijvenUpdateView, self).get_form_kwargs()
    #     kwargs.update(instance={
    #         'inschrijving': self.object
    #     })
    #     return kwargs

class InschrijvenDeleteView(UserPassesTestMixin,SuccessMessageMixin,generic.DeleteView):
    model = Inschrijving
    success_url = '/inschrijven/list/'
    success_message = 'inschrijving is succesvol gedeleted'

    def test_func(self):
        return self.request.user.is_superuser

class InschrijvingAllView(SingleTableView):
    template_name = 'inschrijven_list.html'
    model = Inschrijving
    table_class = tables.InschrijvingTable

class InschrijveNieuwView(SuccessMessageMixin,generic.CreateView):
    model = Lid
    form_class = FormMultiLid
    success_url = '/inschrijven/'
    success_message = 'Uw lid is succesvol ingeschreven'

class LedenView(SingleTableView):
    template_name = 'leden/leden_list.html'
    model = Lid
    table_class = tables.LedenTable

    def get_context_data(self, **kwargs):
        context = super(LedenView,self).get_context_data(**kwargs)
        context['search'] = FormSearchLid
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = Lid.objects.filter(Q(voornaam__contains=query) | Q(achternaam__contains=query))
        else:
            object_list = Lid.objects.all()
        return object_list

class LidView(generic.DetailView):
    model = Lid
    template_name = 'leden/lid_detail.html'

    def get_context_data(self, **kwargs):
        context = super(LidView,self).get_context_data(**kwargs)
        context['contact'] = Contact_Geg.objects.filter(lid__uuid__exact=self.kwargs.get('lid_id'))
        context['fiche'] = Fiche_Geg.objects.filter(lid__uuid__exact=self.kwargs.get('lid_id')).first()
        context['adres'] = Adres.objects.filter(lid__uuid__exact=self.kwargs.get('lid_id')).first()
        return context
    def get_object(self):
        return Lid.objects.get(pk=self.kwargs['lid_id'])

class LidDeleteView(UserPassesTestMixin,generic.DeleteView):
    model = Lid
    success_url = '/dashboard'

    def get_object(self):
        return Lid.objects.get(pk=self.kwargs['lid_id'])

    def test_func(self):
        return self.request.user.is_superuser

def export_leden_csv(request):
    leden_resource = LidResource()
    data = leden_resource.export()
    response = HttpResponse(data.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="leden.xls"'
    return response

# def export_inschrijving_csv(request):
#     leden_resource = InschrijvingLidResource()
#     data = leden_resource.export()
#     response = HttpResponse(data.xls, content_type='application/vnd.ms-excel')
#     response['Content-Disposition'] = 'attachment; filename="leden.xls"'
#     return response

class BegeleidingView(generic.ListView):
    model = Leiding
    template_name = 'begeleiding.html'
    context_object_name = 'begeleiding_list'
    ordering = ['groep']

class GroepenView(generic.ListView):
    model = Groep
    template_name = 'groepen.html'
    context_object_name = 'groep_list'

class GroepUpdateView(UserPassesTestMixin,SuccessMessageMixin,generic.UpdateView):
    model = Groep
    form_class = FormGroepen
    success_url = '/dashboard/groepen'
    template_name = 'groep/groep_form.html'

    def test_func(self):
        return self.request.user.is_superuser

class GroepListView(UserPassesTestMixin,SingleTableView):
    model = Groep
    template_name = 'groep/groep_list.html'
    table_class = tables.GroepenTable

    def test_func(self):
        return self.request.user.is_superuser

class LeidingListView(UserPassesTestMixin,SingleTableView):
    model = Leiding
    template_name = 'leiding/leiding_list.html'
    table_class = tables.LeidingTable

    def test_func(self):
        return self.request.user.is_superuser

class LeidingCreateView(UserPassesTestMixin,SuccessMessageMixin,generic.CreateView):
    model = Leiding
    template_name = 'leiding/leiding_form.html'
    success_url = '/dashboard/leiding'
    success_message = 'leiding is gecreeerd'
    form_class = FormAddUser

    def test_func(self):
        return self.request.user.is_superuser

class LeidingUpdateView(UserPassesTestMixin,SuccessMessageMixin,generic.UpdateView):
    model = Leiding
    template_name = 'leiding/leiding_form.html'
    success_url = '/dashboard/leiding'
    success_message = 'leiding is geupdated'
    form_class = FormLeiding

    def test_func(self):
        return self.request.user.is_superuser

class LeidingDeleteView(UserPassesTestMixin,SuccessMessageMixin,generic.DeleteView):
    model = Leiding
    success_url = '/dashboard/leiding/'
    template_name = 'leiding/leiding_confirm_delete.html'
    success_message = 'leiding is succesvol gedeleted'

    def test_func(self):
        return self.request.user.is_superuser

# class UserCreateView(SuccessMessageMixin,generic.CreateView):
#     model = User
#     form_class = FormUser
#     success_url = '/dashboard/user/'
#     template_name = 'leiding/leiding_form.html'
#     success_message = 'user is succesvol gecreeerd'
#
# class UserListView(SingleTableView):
#     model = Leiding
#     template_name = 'leiding/user_list.html'
#     table_class = tables.UserTable
#
# class UserDeleteView(SuccessMessageMixin,generic.DeleteView):
#     model = Leiding
#     success_url = '/dashboard/user/'
#     template_name = 'leiding/user_confirm_del.html'
#     success_message = 'user is succesvol gedeleted'
