from django.db import models
from django.contrib.auth.models import User
from inschrijven.models import Lid


class Groep(models.Model):
    groepen = (
    ('L', 'Leeuwkes'), ('JK', 'Jong Knapen'), ('K', 'Knapen'), ('JH', 'Jong Hernieuwers'), ('H', 'Hernieuwers'),
    ('16', '+16'), ('LE', 'Leiding'))
    groep = models.CharField(max_length=2, choices=groepen)
    beschrijving = models.TextField(max_length=1000)
    groepfoto = models.FileField()


class leiding(models.Model):
    userid = models.OneToOneField(User, on_delete=models.CASCADE)
    lidid = models.OneToOneField(Lid, on_delete=models.CASCADE)
    groepid = models.OneToOneField(Groep, on_delete=models.CASCADE)
    email = models.EmailField(unique=True, max_length=255)
    tel = models.IntegerField()
    foto = models.FileField()
