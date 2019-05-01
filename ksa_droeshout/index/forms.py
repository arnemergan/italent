from django import forms

class contact(forms.Form):
    email = forms.EmailField()
    bericht = forms.CharField(max_length=400)