from django.contrib import admin
from .models import Inschrijving,Lid,Groep,Leiding,InschrijvingLid

@admin.register(Inschrijving)
class InschrijvingAdmin(admin.ModelAdmin):
    pass

@admin.register(Lid)
class LidAdmin(admin.ModelAdmin):
    pass

@admin.register(Groep)
class GroepAdmin(admin.ModelAdmin):
    pass

@admin.register(Leiding)
class LeidingAdmin(admin.ModelAdmin):
    pass

@admin.register(InschrijvingLid)
class InschrijvingLid(admin.ModelAdmin):
    pass