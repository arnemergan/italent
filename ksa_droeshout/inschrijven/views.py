from django.views import generic
from .forms import FormLid
from .models import Inschrijving,Lid

# Create your views here.
class InschrijvenView(generic.ListView):
    template_name = 'inschrijven.html'
    context_object_name = 'inschrijven_list'

    def get_queryset(self):
        return Inschrijving.objects.filter(actief=True)

class InschrijvenDetailView(generic.DetailView):
    template_name ='inschrijven_info.html'
    model = Inschrijving
    def get_context_data(self, **kwargs):
        context = super(InschrijvenDetailView, self).get_context_data(**kwargs)
        context['form'] = FormLid
        return context

class InschrijvenForm(generic.FormView):
    template_name = 'inschrijven_form.html'
    form_class = FormLid
    success_url = '/inschrijven'
