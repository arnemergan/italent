from django.contrib import admin
from .models import Inschrijving,Lid,Groep,Leiding,InschrijvingLid,Contact_Geg,Allergie,InschrijvingAllowed

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

@admin.register(Contact_Geg)
class Contact_Geg(admin.ModelAdmin):
    pass

@admin.register(Allergie)
class Allergie(admin.ModelAdmin):
    pass

@admin.register(InschrijvingAllowed)
class InschrijvingAllowed(admin.ModelAdmin):
    pass