from django.db import models
from agenda.models import Adres
from inschrijven.models import Leiding

# Create your models here.
class Lokaal(models.Model):
    adresid = models.ForeignKey(Adres,models.CASCADE)

    # verantwoordelijke verhuren lokaal
    userid = models.ForeignKey(Leiding,models.CASCADE)
    beschrijving = models.TextField(max_length=1000)
    prijsperpersoon = models.DecimalField(decimal_places=2,max_digits=5)
    prijs = models.DecimalField(decimal_places=2,max_digits=5)
    waarborg = models.DecimalField(decimal_places=2,max_digits=5)
    contract = models.FileField(upload_to='contract')

    def __str__(self):
        return 'lokaal'

class Lokaalfoto(models.Model):
    lokaalid = models.ForeignKey(Lokaal,models.CASCADE)
    image = models.ImageField(upload_to='images/lokaal')

class Tent(models.Model):
    type = models.CharField(max_length=50)
    afmeting = models.CharField(max_length=20)

    #verantwoordelijke verhuren tenten
    userid = models.ForeignKey(Leiding,models.CASCADE)
    beschrijving = models.TextField(max_length=1000)
    prijswinst = models.DecimalField(decimal_places=2,max_digits=5)
    prijsnwinst = models.DecimalField(decimal_places=2,max_digits=5)
    waarborg = models.DecimalField(decimal_places=2,max_digits=5)
    contract = models.FileField(upload_to='contract')


    def __str__(self):
        return self.type

class TentFoto(models.Model):
    tentid = models.ForeignKey(Tent,models.CASCADE)
    image = models.ImageField(upload_to='images/tent')

class Materiaal(models.Model):
    #verantwoordelijke verhuren materiaal
    userid = models.ForeignKey(Leiding,models.CASCADE)
    beschrijving = models.TextField(max_length=500)

class Weekend(models.Model):
    datumvan = models.DateTimeField()
    datumtot = models.DateTimeField()
    groep = models.CharField(max_length=100)