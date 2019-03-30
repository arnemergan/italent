from django.db import models
from django.urls import reverse

# Create your models here.

class Lid(models.Model):
    # unieke id voor lid
    uuid = models.UUIDField()

    # algemene gegevens
    geslachten = (('V', 'v',),('M', 'm',),('X', 'x',))
    voornaam = models.CharField(max_length=50)
    achternaam = models.CharField(max_length=50)
    geboortedatum = models.DateField()
    geslacht = models.CharField(max_length=1,choices=geslachten)

    # adres gegevens
    straat = models.CharField(max_length=200)
    huisnummer = models.CharField(max_length=10)
    postcode = models.IntegerField(max_length=4)
    stad = models.CharField(max_length=50)

    # ouders gegevens
    tel = models.IntegerField(max_length=10)
    email = models.CharField(max_length=60)

    # huisarts, extra contact persoon ?

    #medische gegevens

    #wat allemaal bijhouden van medische gegevens?

    # lid ingeschreven
    code = models.TextField()
    actief = models.BooleanField()

class Inschrijving(models.Model):
    soorten = (('klein kamp','k'),('kamp','K'),('jaar','Y'),('medium kamp','m'),('daguitstap','d'))
    soort = models.CharField(max_length=20,choices=soorten)
    beschrijving = models.TextField(max_length=200)
    startdatum = models.DateTimeField()
    einddatum = models.DateTimeField()
    prijs = models.DecimalField(decimal_places=2,max_digits=4)
    locatie = models.CharField(max_length=100)
    actief = models.BooleanField()


