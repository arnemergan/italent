from django import forms
from .models import AgendaItem
from bootstrap_datepicker_plus import DateTimePickerInput


class FormAgendaItem(forms.ModelForm):
    class Meta:
        model = AgendaItem
        fields = ['datumvan','datumtot','titel','adres','beschrijving']
        widgets = {
            'datumvan': DateTimePickerInput(format='%d-%m-%Y %H:%M'),
            'datumtot': DateTimePickerInput(format='%d-%m-%Y %H:%M'),
        }

    def clean(self):
        start_date = self.cleaned_data.get('datumvan')
        end_date = self.cleaned_data.get('datumtot')
        if end_date < start_date:
            raise forms.ValidationError('Datumvan moet voor datumtot')
