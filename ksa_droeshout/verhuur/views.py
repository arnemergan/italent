from django.shortcuts import render

# Create your views here.
from django.views import generic
from verhuur import models
from django.contrib.messages.views import SuccessMessageMixin
from verhuur import forms


class VerhuurTemplateView(generic.TemplateView):
    template_name = 'verhuur.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lokaal'] = models.Lokaal.objects.first()
        context['mat'] = models.Materiaal.objects.first()
        context['tenten'] = models.Tent.objects.all()
        context['lokaalfoto'] = models.Lokaalfoto.objects.all()
        context['tentfoto'] = models.TentFoto.objects.all()
        return context

class VerhuurDashTemplateView(generic.TemplateView):
    template_name = 'verhuur_dash.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lokaal'] = models.Lokaal.objects.first()
        context['mat'] = models.Materiaal.objects.first()
        context['tenten'] = models.Tent.objects.all()
        return context

class VerhuurLokaalUpdate(SuccessMessageMixin,generic.UpdateView):
    model = models.Lokaal
    success_url = '/dashboard/verhuur/'
    success_message = 'Lokaal is succesvol geupdated'
    form_class = forms.FormLokaal

class VerhuurTentUpdate(SuccessMessageMixin,generic.UpdateView):
    model = models.Tent
    success_url = '/dashboard/verhuur/'
    success_message = 'Tent is succesvol geupdated'
    form_class = forms.FormTent

class VerhuurMateriaalUpdate(SuccessMessageMixin,generic.UpdateView):
    model = models.Materiaal
    success_url = '/dashboard/verhuur/'
    success_message = 'Materiaal is succesvol geupdated'
    form_class = forms.FormMateriaal

class TentCreateImage(SuccessMessageMixin,generic.CreateView):
    model = models.TentFoto
    template_name = 'verhuur/tent_form.html'
    success_url = '/dashboard/verhuur/'
    success_message = 'Image is succesvol gecreeerd'
    form_class = forms.FormTentFoto

class LokaalCreateImage(SuccessMessageMixin,generic.CreateView):
    model = models.Lokaalfoto
    template_name = 'verhuur/lokaal_form.html'
    success_url = '/dashboard/verhuur/'
    success_message = 'Image is succesvol gecreeerd'
    form_class = forms.FormLokaalFoto

class LokaalDeleteImage(SuccessMessageMixin,generic.DeleteView):
    model = models.Lokaalfoto
    success_url = '/dashboard/verhuur/'
    success_message = 'Image succesvol gedeleted'
    template_name = 'verhuur/verhuur_confirm_delete.html'

class TentDeleteImage(SuccessMessageMixin,generic.DeleteView):
    model = models.TentFoto
    success_url = '/dashboard/verhuur/'
    success_message = 'Image succesvol gedeleted'
    template_name = 'verhuur/verhuur_confirm_delete.html'