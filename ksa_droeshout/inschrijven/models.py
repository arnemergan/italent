from django.db import models

# Create your models here.

class Lid(models.Model):
    geslachten = (('V', 'v',),('M', 'm',),('X', 'x',))
    voornaam = models.CharField(max_length=50)
    achternaam = models.CharField(max_length=50)
    geboortedatum = models.DateField()
    geslacht = models.CharField(max_length=1,choices=geslachten)

class Inschrijving(models.Model):
    soorten = (('k','klein kamp'),('K','kamp'),('Y','jaar'),('m','medium kamp'),('d','daguitstap'))
    soort = models.CharField(max_length=20,choices=soorten)
    beschrijving = models.TextField(max_length=200)
    startdatum = models.DateTimeField()
    einddatum = models.DateTimeField()
    prijs = models.DecimalField(decimal_places=2,max_digits=4)
    locatie = models.CharField(max_length=100)

