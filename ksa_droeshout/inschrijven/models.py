from django.contrib.auth.models import User
from django.db import models
from agenda.models import AgendaItem, Adres
import uuid


# Create your models here.
class Groep(models.Model):
    groepen = (('Leeuwkes', 'Leeuwkes'), ('Jong Knapen', 'Jong Knapen'), ('Knapen', 'Knapen'),
               ('Jong Hernieuwers', 'Jong Hernieuwers'), ('Hernieuwers', 'Hernieuwers'), ('+16', '+16'),
               ('Leiding', 'Leiding'))
    naam = models.CharField(max_length=20, choices=groepen)
    beschrijving = models.TextField(max_length=750)
    groepfoto = models.ImageField(upload_to='images/groep')

    def __str__(self):
        return self.naam


class Lid(models.Model):
    # unieke id voor lid
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # algemene gegevens
    geslachten = (('V', 'v',), ('M', 'm',), ('X', 'x',))
    voornaam = models.CharField(max_length=50)
    achternaam = models.CharField(max_length=50)
    geboortedatum = models.DateField(null=False)
    geslacht = models.CharField(max_length=1, choices=geslachten)
    adresid = models.ForeignKey(Adres, models.PROTECT)

    # lid ingeschreven
    timestamp = models.DateTimeField(auto_now_add=True)
    actief = models.BooleanField(default=True)

    # groep waar lid in zit
    groep = models.ForeignKey(Groep, models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.voornaam, self.achternaam)


class Contact_Geg(models.Model):
    contacttypes = (('Ouder', 'Ouder'), ('Extra', 'Extra'), ('Huisarts', 'Huisarts'))
    lid = models.ForeignKey(Lid,models.CASCADE)
    voornaam = models.CharField(max_length=50)
    naam = models.CharField(max_length=75)
    email = models.EmailField(unique=True, max_length=255, blank=True, null=True)
    tel = models.IntegerField()
    type = models.CharField(choices=contacttypes, max_length=25)


class Allergie(models.Model):
    naam = models.CharField(max_length=100)

    def __str__(self):
        return self.naam
#
# class Medicatie(models.Model):
#     aantal = [(i, i) for i in range(10)]
#     naam = models.CharField(max_length=100)
#     aantal_savonds = models.IntegerField(choices=aantal, default=0)
#     hoeveelheid_savonds = models.IntegerField()
#     aantal_smiddags = models.IntegerField(choices=aantal, default=0)
#     hoeveelheid_smiddags = models.IntegerField()
#     aantal_sochtends = models.IntegerField(choices=aantal, default=0)
#     hoeveelheid_sochtends = models.IntegerField()


class Fiche_Geg(models.Model):
    lid = models.OneToOneField(Lid,models.CASCADE)
    allergie = models.ManyToManyField(Allergie)
    # medicatie = models.ManyToManyField(Medicatie)
    timestamp = models.DateTimeField(auto_now_add=True)


class Leiding(models.Model):
    userid = models.OneToOneField(User, on_delete=models.CASCADE)
    lid = models.OneToOneField(Lid, on_delete=models.CASCADE)
    groep = models.ForeignKey(Groep, on_delete=models.CASCADE)
    email = models.EmailField(unique=True, max_length=255)
    tel = models.IntegerField()
    foto = models.ImageField(upload_to='images/leiding')


class Inschrijving(models.Model):
    agendaitemid = models.OneToOneField(AgendaItem, models.CASCADE)
    prijs = models.DecimalField(decimal_places=2, max_digits=4)
    actief = models.BooleanField(default=True)
    brief = models.FileField(upload_to='brieven')

    def __str__(self):
        return self.agendaitemid.titel

class InschrijvingAllowed(models.Model):
    inschrijving = models.OneToOneField(Inschrijving,models.CASCADE)
    groep = models.ManyToManyField(Groep)

class InschrijvingLid(models.Model):
    inschrijvingid = models.OneToOneField(Inschrijving, models.CASCADE)
    lidid = models.OneToOneField(Lid, models.CASCADE)
