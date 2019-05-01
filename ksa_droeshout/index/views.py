from django.shortcuts import render
from django.views import generic
from index import forms
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail


# Create your views here.
class PrivacyView(generic.TemplateView):
    template_name = 'privacy.html'

class OverView(generic.TemplateView):
    template_name = 'overons.html'

class ContactView(generic.FormView,SuccessMessageMixin):
    form_class = forms.contact
    success_url = '/contact'
    success_message = 'Uw bericht is succesvol verzonden'
    template_name = 'contact.html'

    def form_valid(self, form):
        send_mail('Contact formulier - ksa droeshout', form.cleaned_data['bericht'], form.cleaned_data['email'], ['leiding@ksadroeshout.be'])
        return super(ContactView, self).form_valid(form)

