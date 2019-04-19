from django.db import models
from agenda.models import Adres
from django.contrib.auth.models import User

# Create your models here.
class Lokaal(models.Model):
    adresid = models.ForeignKey(Adres,models.CASCADE)

    # verantwoordelijke verhuren lokaal
    userid = models.ForeignKey(User,models.CASCADE)
    beschrijving = models.TextField(max_length=500)
    prijsperpersoon = models.DecimalField(decimal_places=2)
    prijs = models.DecimalField(decimal_places=2)

class Lokaalfoto(models.Model):
    lokaalid = models.ForeignKey(Lokaal,models.CASCADE)
    image = models.ImageField()

class Tent(models.Model):
    type = models.CharField(max_length=50)
    afmeting = models.CharField(max_length=20)

    #verantwoordelijke verhuren tenten
    userid = models.ForeignKey(User,models.CASCADE)
    beschrijving = models.TextField(max_length=500)
    prijsperstuk = models.DecimalField(decimal_places=2)

class TentFoto(models.Model):
    tentid = models.ForeignKey(Tent,models.CASCADE)
    image = models.ImageField()

class Materiaal(models.Model):
    #verantwoordelijke verhuren materiaal
    userid = models.ForeignKey(User,models.CASCADE)
    beschrijving = models.TextField(max_length=500)

class weekend(models.Model):
    datumvan = models.DateTimeField()
    datumtot = models.DateTimeField()
    groep = models.CharField(max_length=100)