from django import forms
from .models import Lid,Inschrijving,InschrijvingLid
from bootstrap_datepicker_plus import DateTimePickerInput


class FormSearch(forms.Form):
    voornaam = forms.CharField()
    achternaam = forms.CharField()

class FormLidNieuw(forms.ModelForm):
    class Meta:
        model = Lid
        fields = ['voornaam','achternaam','geboortedatum','geslacht','groep']
        widgets = {
            'geboortedatum': DateTimePickerInput(format='%d-%m-%Y')
        }

class FormInschrijving(forms.ModelForm):
    class Meta:
        model = Inschrijving
        fields = ['agendaitemid','prijs','brief','actief']
        labels = {
            'agendaitemid':'titel'
        }

class FormLidInschrijven(forms.ModelForm):
    class Meta:
        model = InschrijvingLid
        fields = ['inschrijvingid','lidid']





