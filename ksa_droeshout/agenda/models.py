from django.db import models

class AgendaItem(models.Model):
    datumvan = models.DateTimeField()
    datumtot = models.DateTimeField()
    titel = models.CharField(max_length=100)
    locatie = models.CharField(max_length=100)
    beschrijving = models.TextField()