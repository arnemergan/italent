from django import forms
from .models import Lid,Inschrijving,InschrijvingLid,Adres,Groep,Leiding,Contact_Geg,Fiche_Geg,Allergie
from bootstrap_datepicker_plus import DateTimePickerInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from betterforms.multiform import MultiModelForm
from django.http import HttpResponseRedirect,HttpResponse
from django.core.exceptions import ValidationError
from django.contrib import messages
from django_select2.forms import Select2MultipleWidget
from rolepermissions.roles import assign_role


class FormSearchLid(forms.Form):
    q = forms.CharField()

class FormSearch(forms.Form):
    voornaam = forms.CharField()
    achternaam = forms.CharField()

class FormLidNieuw(forms.ModelForm):
    class Meta:
        model = Lid
        fields = ['voornaam','achternaam','geboortedatum','geslacht','groep']
        widgets = {
            'geboortedatum': DateTimePickerInput(format='%d-%m-%Y'),
        }
        labels = {
            'voornaam':'voornaam lid',
            'achternaam':'achternaam lid'
        }



class FormAdres(forms.ModelForm):
    class Meta:
        model = Adres
        fields = ['straat','nr','postcode','stad']

class FormContactGegOuder(forms.ModelForm):
    class Meta:
        model = Contact_Geg
        fields = ['voornaam','naam','email','tel']
        labels = {
            'voornaam':'voornaam ouder',
            'naam':'achternaam ouder'
        }

class FormContactGegArts(forms.ModelForm):
    class Meta:
        model = Contact_Geg
        fields = ['voornaam','naam','tel']
        labels = {
            'voornaam':'voornaam huisarts',
            'naam':'achternaam huisarts'
        }

class FormContactGegExtra(forms.ModelForm):
    class Meta:
        model = Contact_Geg
        fields = ['voornaam','naam','tel']
        labels = {
            'voornaam':'voornaam',
            'naam':'achternaam'
        }

class FormFicheGeg(forms.ModelForm):
    class Meta:
        model = Fiche_Geg
        fields = ['allergie']
        widgets = {
            'allergie':Select2MultipleWidget
        }


class FormMultiLid(MultiModelForm):
    form_classes = {
        'lid':FormLidNieuw,
        'adres': FormAdres,
        'ouder':FormContactGegOuder,
        'arts':FormContactGegArts,
        'extra':FormContactGegExtra,
        'med':FormFicheGeg,
    }

    def save(self, commit=True):
        objects = super(FormMultiLid, self).save(commit=False)
        if commit:
            adres = objects['adres']
            obj,created = Adres.objects.get_or_create(straat=adres.straat,nr=adres.nr,postcode=adres.postcode,stad=adres.stad)
            lid = objects['lid']
            lid.adresid = obj
            lid_obj = Lid.objects.filter(voornaam=lid.voornaam,achternaam=lid.achternaam,geboortedatum=lid.geboortedatum,adresid=lid.adresid)
            if lid_obj is None:
                lid.save()
                ouder = objects['ouder']
                arts = objects['arts']
                extra = objects['extra']
                extra.lid = lid
                extra.type = 'Extra'
                extra.save()
                arts.lid = lid
                arts.type = 'Huisarts'
                arts.save()
                ouder.lid = lid
                ouder.type = 'Ouder'
                ouder.save()
                med = objects['med']
                med.lid = lid
                med.save()
            else:
                raise ValidationError('lid bestaat al')
        return objects

class FormInschrijving(forms.ModelForm):
    class Meta:
        model = Inschrijving
        fields = ['agendaitemid','prijs','brief','actief']
        labels = {
            'agendaitemid':'titel'
        }

# class FormAllowGroep(forms.ModelForm):
#     class Meta:
#         model = InschrijvingAllowed
#         fields = ['groep']
#         widgets = {
#             'groep':forms.CheckboxSelectMultiple
#         }
#         labels = {
#             'groep':'groepen die mogen inschrijven'
#         }
#

# class FormInschrijvingAllow(MultiModelForm):
#     form_classes = {
#         'inschrijving':FormInschrijving,
#         'allow':FormAllowGroep,
#     }
#
#     def save(self, commit=True):
#         objects = super(FormInschrijvingAllow, self).save(commit=False)
#         if commit:
#             inschrijving = objects['inschrijving']
#             allow = objects['allow']
#             inschrijving.save()
#             allow.inschrijving = inschrijving
#             allow.save()
#             print(allow.groep.all())
#         return objects

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
        fields = ['lid','groep','email','tel','foto']

    def __init__(self, *args, **kwargs):
        super(FormLeiding, self).__init__(*args, **kwargs)
        self.fields['lid'].queryset = Lid.objects.filter(groep__naam__exact='Leiding')
        self.fields['groep'].queryset = Groep.objects.filter(~Q(naam = 'Leiding'))

class FormUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']

class FormAddUser(MultiModelForm):
    form_classes = {
        'user':FormUser,
        'leiding':FormLeiding
    }

    def save(self, commit=True):
        objects = super(FormAddUser, self).save(commit=False)
        if commit:
            user = objects['user']
            leiding = objects['leiding']
            user.save()
            leiding.userid = user
            leiding.save()
        return objects



