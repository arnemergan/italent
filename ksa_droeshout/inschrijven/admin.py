from django.contrib import admin
from .models import Inschrijving

@admin.register(Inschrijving)
class InschrijvingAdmin(admin.ModelAdmin):
    pass
