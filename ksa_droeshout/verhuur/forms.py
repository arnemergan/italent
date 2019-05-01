from django import forms
from bootstrap_datepicker_plus import DateTimePickerInput
from verhuur import models

class FormLokaal(forms.ModelForm):
    class Meta:
        model = models.Lokaal
        fields = ['userid','adresid','beschrijving','prijs','prijsperpersoon','waarborg','contract']

class FormTent(forms.ModelForm):
    class Meta:
        model = models.Tent
        fields = ['userid','type','prijsnwinst','prijswinst','beschrijving','afmeting','waarborg','contract']

class FormMateriaal(forms.ModelForm):
    class Meta:
        model = models.Materiaal
        fields = ['userid','beschrijving']

class FormTentFoto(forms.ModelForm):
    class Meta:
        model = models.TentFoto
        fields = ['tentid','image']

class FormLokaalFoto(forms.ModelForm):
    class Meta:
        model = models.Lokaalfoto
        fields = ['lokaalid','image']