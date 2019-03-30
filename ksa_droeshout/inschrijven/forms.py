from django import forms
from .models import Lid

class FormLid(forms.ModelForm):
    class Meta:
        model = Lid
        fields = ['voornaam','achternaam','geboortedatum','geslacht']
        widgets = {
            'voornaam': forms.TextInput(attrs={'class': 'form-control'}),
            'achternaam': forms.TextInput(attrs={'class': 'form-control'}),
            'geboortedatum': forms.SelectDateWidget(attrs={'class','form-control'})
        }
