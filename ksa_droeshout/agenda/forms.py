from django import forms
from .models import AgendaItem
from datetimewidget.widgets import DateTimeWidget
from django.contrib.admin import widgets
import datetime

class FormAgendaItem(forms.ModelForm):
    class Meta:
        model = AgendaItem
        fields = ['datumvan','datumtot','titel','locatie','beschrijving']
        widgets = {
            'datumvan': forms.DateInput(),
            'datumtot': forms.DateInput(),
        }