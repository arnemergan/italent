from django.db import models

class Adres(models.Model):
    straat = models.CharField(max_length=100)
    nr = models.CharField(max_length=10)
    postcode = models.IntegerField()
    stad = models.CharField(max_length=100)

    def __str__(self):
        return "%s %s, %s %s." % (self.straat,self.nr,self.postcode,self.stad)

class AgendaItem(models.Model):
    datumvan = models.DateTimeField()
    datumtot = models.DateTimeField()
    titel = models.CharField(max_length=100)
    adres = models.ForeignKey(Adres,models.PROTECT)
    beschrijving = models.TextField()

    def __str__(self):
        return self.titel