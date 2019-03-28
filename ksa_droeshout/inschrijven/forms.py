from django import forms
from .models import Lid

class FormLid(forms.ModelForm):
    class Meta:
        model = Lid
        fields = ['voornaam','achternaam','geboortedatum','geslacht']
