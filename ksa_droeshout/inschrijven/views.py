from django.views import generic
from .forms import FormLid
from .models import Inschrijving, Lid
from inschrijven import tables
from django_tables2 import SingleTableView


# Create your views here.
class InschrijvenView(generic.ListView):
    template_name = 'inschrijven.html'
    context_object_name = 'inschrijven_list'

    def get_queryset(self):
        return Inschrijving.objects.filter(actief=True)


class InschrijvenDetailView(generic.DetailView):
    template_name = 'inschrijven_info.html'
    model = Inschrijving

    def get_context_data(self, **kwargs):
        context = super(InschrijvenDetailView, self).get_context_data(**kwargs)
        context['form'] = FormLid
        return context


class InschrijvenForm(generic.FormView):
    template_name = 'inschrijven_form.html'
    form_class = FormLid
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
