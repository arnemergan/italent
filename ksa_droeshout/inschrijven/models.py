from django.contrib.auth.models import User
from django.db import models
from agenda.models import AgendaItem,Adres
import uuid

# Create your models here.
class Groep(models.Model):
    groepen = (('L', 'Leeuwkes'), ('JK', 'Jong Knapen'), ('K', 'Knapen'), ('JH', 'Jong Hernieuwers'), ('H', 'Hernieuwers'),('16', '+16'), ('LE', 'Leiding'))
    naam = models.CharField(max_length=2, choices=groepen)
    beschrijving = models.TextField(max_length=255)
    groepfoto = models.ImageField()

    def __str__(self):
        return self.naam

class Lid(models.Model):
    # unieke id voor lid
    uuid = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)

    # algemene gegevens
    geslachten = (('V', 'v',),('M', 'm',),('X', 'x',))
    voornaam = models.CharField(max_length=50)
    achternaam = models.CharField(max_length=50)
    geboortedatum = models.DateField(null=False)
    geslacht = models.CharField(max_length=1,choices=geslachten)
    adresid = models.ForeignKey(Adres,models.PROTECT)

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
    groep = models.ForeignKey(Groep,models.CASCADE)

    def __str__(self):
        return self.voornaam


class Leiding(models.Model):
    userid = models.OneToOneField(User,on_delete=models.CASCADE)
    groep = models.ForeignKey(Groep,on_delete=models.CASCADE)
    email = models.EmailField(unique=True, max_length=255)
    tel = models.IntegerField()
    foto = models.ImageField()

class Inschrijving(models.Model):
    agendaitemid = models.OneToOneField(AgendaItem,models.CASCADE)
    prijs = models.DecimalField(decimal_places=2,max_digits=4)
    actief = models.BooleanField(default=True)
    brief = models.FileField()

    def __str__(self):
        return self.agendaitemid.titel

class InschrijvingLid(models.Model):
    inschrijvingid = models.ForeignKey(Inschrijving,models.CASCADE)
    lidid = models.ForeignKey(Lid,models.CASCADE)
