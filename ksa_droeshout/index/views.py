from django.shortcuts import render
from django.views import generic

# Create your views here.
class PrivacyView(generic.TemplateView):
    template_name = 'privacy.html'
