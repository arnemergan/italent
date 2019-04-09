from django.contrib import admin
from .models import Inschrijving,Lid

@admin.register(Inschrijving)
class InschrijvingAdmin(admin.ModelAdmin):
    pass

@admin.register(Lid)
class LidAdmin(admin.ModelAdmin):
    pass
