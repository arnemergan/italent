from django.db import models
import uuid
from django.urls import reverse

# Create your models here.

class Lid(models.Model):
    # unieke id voor lid
    uuid = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)

    # algemene gegevens
    geslachten = (('V', 'v',),('M', 'm',),('X', 'x',))
    voornaam = models.CharField(max_length=50)
    achternaam = models.CharField(max_length=50)
    geboortedatum = models.DateField(null=False)
    geslacht = models.CharField(max_length=1,choices=geslachten)

    # adres gegevens
    # straat = models.CharField(max_length=200)
    # huisnummer = models.CharField(max_length=10)
    # postcode = models.IntegerField(max_length=4)
    # stad = models.CharField(max_length=50)

    # ouders gegevens
    # tel = models.IntegerField()
    # email = models.CharField(max_length=60)

    # huisarts, extra contact persoon ?

    #medische gegevens

    #wat allemaal bijhouden van medische gegevens?

    # lid ingeschreven
    # timestamp = models.DateTimeField(auto_now_add=True)
    actief = models.BooleanField(default=True)

    #groep waar lid in zit
    #groepid = models.ForeignKey(Groep,models.CASCADE)


class Inschrijving(models.Model):
    soorten = (('klein kamp','k'),('kamp','K'),('jaar','Y'),('medium kamp','m'),('daguitstap','d'))
    soort = models.CharField(max_length=20,choices=soorten)
    beschrijving = models.TextField(max_length=200)
    startdatum = models.DateTimeField()
    einddatum = models.DateTimeField()
    prijs = models.DecimalField(decimal_places=2,max_digits=4)
    locatie = models.CharField(max_length=100)
    actief = models.BooleanField()


