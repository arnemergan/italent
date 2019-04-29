from django import forms
from .models import Lid,Inschrijving,InschrijvingLid,Adres,Groep,Leiding
from bootstrap_datepicker_plus import DateTimePickerInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from betterforms.multiform import MultiModelForm

class FormSearch(forms.Form):
    voornaam = forms.CharField()
    achternaam = forms.CharField()

class FormLidNieuw(forms.ModelForm):
    class Meta:
        model = Lid
        fields = ['voornaam','achternaam','geboortedatum','geslacht','groep','adresid']
        widgets = {
            'geboortedatum': DateTimePickerInput(format='%d-%m-%Y'),
        }

class FormAdres(forms.ModelForm):
    class Meta:
        model = Adres
        fields = ['straat','nr','postcode','stad']

class FormMultiLid(MultiModelForm):
    form_classes = {
        'lid':FormLidNieuw,
        'adres': FormAdres,
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
        widgets={
            'inschrijvingid':forms.TextInput(attrs={'readonly':'readonly'}),
            'lidid':forms.TextInput(attrs={'readonly':'readonly'})
        }

class FormGroepen(forms.ModelForm):
    class Meta:
        model = Groep
        fields = ['beschrijving','groepfoto','naam']

class FormLeiding(forms.ModelForm):
    class Meta:
        model = Leiding
        fields = ['userid','lid','groep','email','tel','foto']

    def __init__(self, *args, **kwargs):
        super(FormLeiding, self).__init__(*args, **kwargs)
        self.fields['lid'].queryset = Lid.objects.filter(groep__naam__exact='Leiding')
        self.fields['groep'].queryset = Groep.objects.filter(~Q(naam = 'Leiding'))

class FormUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']



